from models.exercise import Exercise
from db.run_sql import run_sql

def save(exercise):
    sql = "INSERT INTO merchants (exercise_type, name_of_exercise, rep_max, personal_best) VALUES (%s, %s, %s, %s) RETURNING id"
    values = [exercise.exercise_type, exercise.name_of_exercise, exercise.rep_max, exercise.personal_best]
    results = run_sql(sql, values)
    exercise.id = results[0]['id']
    return exercise