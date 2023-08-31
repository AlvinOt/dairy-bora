from flask import Flask, request, jsonify
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from scripts.database.models import Animal, MilkProductionRecord  # Make sure to import your models

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

@app.route('/update_animal/<int:animal_id>', methods=['PUT'])
def update_animal(animal_id):
    try:
        data = request.json
        session = Session()

        animal = session.query(Animal).get(animal_id)
        if animal is None:
            return jsonify({"error": "Animal not found."}), 404

        animal.name = data['name']
        animal.breed = data['breed']

        session.commit()
        session.close()

        return jsonify({"message": "Animal updated successfully."}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
