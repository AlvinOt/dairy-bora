#!/usr/bin/env python3

import mysql.connector
from config.database_config import db_config

# Create a connection
connection = mysql.connector.connect(**db_config)

# Create a cursor to execute SQL queries
cursor = connection.cursor()

# Close the cursor and connection when done
cursor.close()
connection.close()
