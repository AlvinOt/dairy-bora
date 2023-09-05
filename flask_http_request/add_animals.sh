#!/bin/bash

curl -X POST -H "Content-Type: application/json" -d '{
    "name": "Salome",
    "breed": "Holstein",
    "birth_date": "2019-01-01",
    "gender": "Female"
}' http://127.0.0.1:5000/add_animal
