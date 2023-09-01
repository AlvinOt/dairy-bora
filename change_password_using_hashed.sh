curl -X POST -H "Content-Type: application/json" -d '{
  "username": "jontedoe",
  "current_password_hashed": "$2b$12$tGpgWnoJe2xjPJlNc0OLwemVs0j7nbJUhObBDtD9A3CkAQF6Qv1.a",
  "new_password_plain": "omg123abc"
}' http://127.0.0.1:5000/change_password_using_hashed
