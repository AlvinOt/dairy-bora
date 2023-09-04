#!/bin/bash

curl -X POST -H "Content-Type: application/json" -d '{
    "animal_id": 2,
    "date_of_production": "2023-06-15",
    "amount_produced": 15.5,
    "notes": "Recorded milk production for testing"
}' http://127.0.0.1:5000/record_milk_production
