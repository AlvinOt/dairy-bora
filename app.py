from flask import Flask, request, jsonify
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from scripts.database.models import Animal, MilkProductionRecord, User
import bcrypt

app = Flask(__name__)

# Database connection setup
engine = create_engine('mysql+mysqlconnector://farmanager:manage123@localhost/farmgt')
Session = sessionmaker(bind=engine)

@app.route('/')
def welcome():
    return "Welcome to the Dairy Farm Management System\n"

@app.route('/add_animal', methods=['POST'])
def add_animal():
    try:
        data = request.json
        session = Session()

        new_animal = Animal(name=data['name'], breed=data['breed'], birth_date=data['birth_date'], gender=data['gender'])
        session.add(new_animal)
        session.commit()
        session.close()

        return jsonify({"message": "Animal added successfully."}), 201

    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/record_milk_production', methods=['POST'])
def record_milk_production():
    try:
        data = request.json
        session = Session()

        animal = session.query(Animal).get(data['animal_id'])
        if animal is None:
            return jsonify({"error": "Animal not found."}), 404

        new_milk_record = MilkProductionRecord(cow_id=animal.id, date_of_production=data['date_of_production'],
                                              amount_produced=data['amount_produced'], notes=data['notes'])
        session.add(new_milk_record)
        session.commit()
        session.close()

        return jsonify({"message": "Milk production recorded successfully."}), 201

    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/add_users', methods=['POST'])
def create_user():
    # Create a session
    session = Session()

    try:
        # Parse the JSON data from the request
        user_data = request.get_json()

        # Hash the provided password
        hashed_password = bcrypt.hashpw(user_data['password_hashed'].encode('utf-8'), bcrypt.gensalt())

        # Create a new User object with the hashed password
        new_user = User(
            username=user_data['username'],
            password_hashed=hashed_password,
            role=user_data['role'],
            contact_information=user_data['contact_information']
        )

        # Add the new user to the session and commit to the database
        session.add(new_user)
        session.commit()

        # Close the session
        session.close()

        # Return a success message
        return jsonify({'message': 'User created successfully'}), 201

    except Exception as e:
        # Handle exceptions (e.g., validation errors or database errors)
        session.rollback()
        session.close()
        return jsonify({'error': str(e)}), 500


@app.route('/animals', methods=['GET'])
def get_animals():
    try:
        session = Session()
        animals = session.query(Animal).all()
        session.close()
        
        animal_list = [{"id": animal.id, "name": animal.name, "breed": animal.breed, "birth_date": animal.birth_date} for animal in animals]
        
        return jsonify(animal_list), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/milk_records/<int:animal_id>', methods=['GET'])
def get_milk_records(animal_id):
    try:
        session = Session()
        animal = session.query(Animal).get(animal_id)

        if animal is None:
            return jsonify({"error": "Animal not found."}), 404

        milk_records = [{"date_of_production": record.date_of_production,
                         "amount_produced": record.amount_produced,
                         "notes": record.notes} for record in animal.milk_production_records]

        session.close()

        return jsonify(milk_records), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/all_milk_records', methods=['GET'])
def get_all_milk_records():
    try:
        session = Session()
        animals = session.query(Animal).all()

        all_milk_records = []

        for animal in animals:
            records = [{"date_of_production": record.date_of_production,
                        "amount_produced": record.amount_produced,
                        "notes": record.notes} for record in animal.milk_production_records]

            all_milk_records.append({"animal_id": animal.id,
                                     "animal_name": animal.name,
                                     "milk_records": records})

        session.close()

        return jsonify(all_milk_records), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Define the /users endpoint
@app.route('/users', methods=['GET'])
def get_users_with_passwords():
    # Create a session
    session = Session()

    try:
        # Query all users from the database
        users = session.query(User).all()

        # Convert users to a list of dictionaries
        user_list = []
        for user in users:
            user_dict = {
                'id': user.id,
                'username': user.username,
                'role': user.role,
                'contact_information': user.contact_information,
                'password_hashed': user.password_hashed  # Include the password (for educational purposes only)
            }
            user_list.append(user_dict)

        # Close the session
        session.close()

        # Return the list of users as JSON
        return jsonify(user_list)

    except Exception as e:
        # Handle exceptions (e.g., database errors)
        session.close()
        return jsonify({'error': str(e)}), 500

@app.route('/update_animal/<int:animal_id>', methods=['PUT'])
def update_animal(animal_id):
    try:
        data = request.json
        session = Session()

        animal = session.query(Animal).get(animal_id)
        if animal is None:
            return jsonify({"error": "Animal not found."}), 404

        # Update fields based on data
        if 'name' in data:
            animal.name = data['name']
        if 'breed' in data:
            animal.breed = data['breed']

        session.commit()
        session.close()

        return jsonify({"message": "Animal updated successfully."}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/change_password', methods=['POST'])
def change_password():
    # Get user data from the request
    data = request.json

    # Extract user information
    username = data['username']
    current_password = data['current_password']
    new_password = data['new_password']

    # Create a session
    session = Session()

    try:
        # Query the user by username
        user = session.query(User).filter_by(username=username).first()

        if user is None:
            return jsonify({"error": "User not found."}), 404

        # Check if the current password is correct
        if bcrypt.checkpw(current_password.encode('utf-8'), user.password_hashed.encode('utf-8')):
            # Hash the new password
            hashed_password = bcrypt.hashpw(new_password.encode('utf-8'), bcrypt.gensalt())

            # Update the user's password
            user.password_hashed = hashed_password

            # Commit the changes to the database
            session.commit()
            session.close()

            return jsonify({"message": "Password changed successfully."}), 200
        else:
            session.close()
            return jsonify({"error": "Incorrect current password."}), 401

    except Exception as e:
        # Handle exceptions (e.g., database errors)
        session.rollback()
        session.close()
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
