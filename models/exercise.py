class Exercise:

    def __init__(self, exercise_type, name_of_exercise, rep_max, personal_best, id=None):
        self.exercise_type = exercise_type
        self.name_of_exercise = name_of_exercise
        self.rep_max = rep_max
        self.personal_best = personal_best
        self.id = id

#Rep Max - also known as "1rm" or "1 rep max": https://en.wikipedia.org/wiki/One-repetition_maximum

#Personal Best - should be the highest number in this exercise the user has ever achived in the hisotry of recording/logging with the app

