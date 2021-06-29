from models.user import User
from db.run_sql import run_sql

def save(user):
    sql="INSERT INTO users( first_name, last_name, gender, age, weight, height ) VALUES (%s, %s, %s, %s, %s, %s) RETURNING id"
    values = [user.first_name, user.last_name, user.gender, user.age, user.weight, user.height]
    results = run_sql(sql, values)
    user.id = results[0]['id']
    return user