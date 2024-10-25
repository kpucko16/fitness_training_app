import random
from user import User
from exercise import Exercise, workout_types


class Workout:
    def __init__(self, user: str = 'conditional'):
        if not isinstance(user, User):
            raise ValueError("Expected user to be an instance of User class.")
        self.user = user
        self.exercise = []

    def generate_workout(self):
        # Choose exercises based on user goals
        if self.user.goal == 'lose weight':
            self.exercises = self.select_exercises(weight_loss=True)
        elif self.user.goal == 'build muscle':
            self.exercises = self.select_exercises(build_muscle=True)
        elif self.user.goal == 'increase endurance':
            self.exercises = self.select_exercises(increase_endurance=True)

    def select_exercises(self, weight_loss=False, build_muscle=False, increase_endurance=False):
        selected_exercises = []

        # Example selection logic
        if weight_loss:
            # Select exercises from all types (Push, Pull, Legs) that are moderate intensity
            for workout_type, exercises in workout_types.items():
                for exercise in exercises:
                    if exercise.difficulty in ['Beginner', 'Intermediate']:
                        selected_exercises.append(exercise)

        if build_muscle:
            # Select exercises that are more advanced
            for workout_type, exercises in workout_types.items():
                for exercise in exercises:
                    if exercise.difficulty == 'Advanced':
                        selected_exercises.append(exercise)

        if increase_endurance:
            # Example: Add high-rep exercises
            for workout_type, exercises in workout_types.items():
                for exercise in exercises:
                    if exercise.difficulty in ['Beginner', 'Intermediate']:
                        selected_exercises.append(exercise)

        # Shuffle and return a sample of exercises
        random.shuffle(selected_exercises)
        return selected_exercises[:5]  # Return up to 5 exercises

    def display_workout(self):
        print(f"Workout for {self.user.name}:")
        for exercise in self.exercises:
            print(exercise)

