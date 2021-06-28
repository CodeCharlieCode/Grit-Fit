DROP TABLE IF EXISTS workouts;
DROP TABLE IF EXISTS exercises;
DROP TABLE IF EXISTS users;

CREATE TABLE exercises (
    id SERIAL PRIMARY KEY,
    exercise_type VARCHAR(255),
    name_of_exercise VARCHAR(255),
    rep_max FLOAT,
    personal_best FLOAT

);

CREATE TABLE workouts(
    id SERIAL PRIMARY KEY,
    exercise_id INT REFERENCES exercises(id) ON DELETE CASCADE, 
    weight FLOAT,
    sets INT,
    repetitions INT,
    rest_time TIME
);

CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    gender VARCHAR(255),
    age INT,
    weight FLOAT,
    height FLOAT
);