from models.exercise import Exercise
from db.run_sql import run_sql

def save(exercise):
    sql = "INSERT INTO exercises (exercise_type, name_of_exercise, rep_max, personal_best) VALUES (%s, %s, %s, %s) RETURNING id"
    values = [exercise.exercise_type, exercise.name_of_exercise, exercise.rep_max, exercise.personal_best]
    results = run_sql(sql, values)
    exercise.id = results[0]['id']
    return exercise

def select_all():
    exercises = []

    sql = "SELECT * FROM exercises"
    results = run_sql(sql)

    for result in results:
        exercise = Exercise(result['exercise_type'], result["name_of_exercise"], result["rep_max"], result["personal_best"], result["id"])
        exercises.append(exercise)
    return exercises


def select(id):
    exercise = None
    sql = "SELECT * FROM exercises WHERE id =%s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        exericse = Exercise(result['exercise_type'], result["name_of_exercise"], result["rep_max"], result["personal_best"], result["id"])
    return exercise 

