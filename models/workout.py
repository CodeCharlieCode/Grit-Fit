class Workout:

    def __init__(self, exercise, sets,repetitions, rest_time, comments, id=None):
        self.exercise = exercise
        self.sets = sets
        self.repetitions = repetitions
        self.rest_time = rest_time
        self.comments = comments
        self.id = id
