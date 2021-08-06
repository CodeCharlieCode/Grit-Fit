from flask import Blueprint, render_template

from models.exercise import Exercise
import repositories.exercise_repository as exercise_repository 

exercise_blueprint = Blueprint("exercises",__name__)

@exercise_blueprint.route("/exercises")
def exercsies():
    exercises = exercise_repository.select_all()
    return render_template("exercises/index.html", exercises = exercises)