class Workout:

    def __init__(self, exercise, repetitions, sets, rest_time, comments, id=None):
        self.exercise = exercise
        self.repetitions = repetitions
        self.sets = sets
        self.rest_time = rest_time
        self.comments = comments
        self.id = id
