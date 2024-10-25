class User:
    def __init__(self, name: str, gender: str, age: int, weight: float, height: float, goal: str, activity_level: str = 'moderate'):
        self.name = name
        self.gender = gender
        self.age = age
        self.weight = weight
        self.height = height
        self.goal = goal
        self.activity_level = activity_level
        self.workout_history = []

    def calculate_bmi(self):
        # BMI formula: weight (kg) / height (m)^2
        return round(self.weight / (self.height / 100) ** 2, 2)

    def calculate_calories(self):
        # Simple caloric needs calculation based on user data
        if self.activity_level == "low":
            multiplier = 1.2
        elif self.activity_level == "moderate":
            multiplier = 1.55
        elif self.activity_level == "high":
            multiplier = 1.75
        else:
            # This would be the default for unknown levels
            multiplier = 1.2
        if self.gender == 'Male':
            base_calories = 66.47 + (13.75 * self.weight) + (5.003 * self.height) - (6.755 * self.age)
        elif self.gender == 'Female':
            base_calories = 655.1 + (9.563 * self.weight) + (1.85 * self.height) - (4.676 * self.age)
        else:
            base_calories = 10 * self.weight + 6.25 * self.height - 5 * self.age
        if self.goal.lower() == "lose weight":
            return base_calories * multiplier - 500
        elif self.goal.lower() == "gain muscle":
            return base_calories * multiplier + 500
        else:
            return base_calories * multiplier

    def add_workout(self, workout):
        self.workout_history.append(workout)

    def __repr__(self):
        workout_history = "\n".join(f"- {workout}" for workout in self.workout_history)
        return (
            f"User: {self.name}\n"
            f"Gender: {self.gender}, Age: {self.age}\n"
            f"Height: {self.height} cm, Weight: {self.weight} kg\n"
            f"Goal: {self.goal}, Activity Level: {self.activity_level}\n"
            f"BMI: {self.calculate_bmi()}\n"
            f"Recommended Calorie Intake: {self.calculate_calories()} calories/day\n"
            "Workout History:\n"
            f"{workout_history}"
        )


user1 = User('Kris', 'Male', 31, 103, 183, 'lose weight', 'moderate')
print(user1)