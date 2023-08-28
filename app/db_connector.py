#!/usr/bin/env python3

import mysql.connector
from config import db_config

# Create a connection
connection = mysql.connector.connect(**db_config)

# Create a cursor to execute SQL queries
cursor = connection.cursor()

# Close the connection when done
cursor.close()
connection.close()

