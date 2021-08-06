from flask import Flask, render_template

from controllers.exercise_controller import exercise_blueprint

app = Flask(__name__)

app.register_blueprint(exercise_blueprint)

@app.route("/")
def main():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)