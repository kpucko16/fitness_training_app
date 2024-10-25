class Progress:
    def __init__(self, user):
        self.user = user
        self.workout_history = []
        self.weight_history = []

    def log_workout(self, workout):
        """Logs a workout."""
        self.workout_history.append(workout)

    def log_weight(self, weight):
        """Logs the user's weight over time."""
        self.weight_history.append(weight)

    def display_progress(self):
        """Displays the logged progress."""
        print(f"Progress for {self.user.name}:")
        print("\nWorkout History:")
        for workout in self.workout_history:
            print(f"- {workout}")

        print("\nWeight History:")
        for weight in self.weight_history:
            print(f"- {weight} kg")
