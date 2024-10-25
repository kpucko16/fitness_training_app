class Exercise:
    def __init__(self, name: str, description: str, difficulty: str):
        self.name = name
        self.description = description
        self.difficulty = difficulty

    def __repr__(self):
        return f"{self.name} ({self.difficulty}): {self.description}"


workout_types = {
    'Push': [
        Exercise('Barbell bench press', 'Targets chest and triceps', 'Intermediate'),
        Exercise('Barbell overhead press', 'Targets shoulders and triceps', 'Intermediate'),
        Exercise('Standing barbell push press', 'Targets shoulders and triceps', 'Intermediate'),
        Exercise('Dumbbell shoulder press', 'Targets shoulders and triceps', 'Intermediate'),
        Exercise('Dumbbell overhead triceps extension', 'Targets triceps', 'Intermediate'),
        Exercise('Dips', 'Targets chest and triceps', 'Intermediate'),
        Exercise('Push-ups', 'Targets chest and triceps', 'Intermediate'),
        Exercise('Pec deck', 'Targets chest and triceps', 'Intermediate'),
    ],
    'Pull': [
        Exercise("Deadlift", "Targets back and legs", "Advanced"),
        Exercise("Pull-Up", "Targets upper back and biceps", "Intermediate"),
        Exercise("Single-Arm Dumbbell Bent-Over Rows", "Targets back muscles", "Intermediate"),
        Exercise("Lat Pulldowns", "Targets back muscles", "Intermediate"),
        Exercise("Barbell Row", "Targets back muscles", "Intermediate"),
        Exercise("Rope Face Pulls", "Targets back muscles", "Intermediate"),
        Exercise("Dumbbell Shrugs", "Targets back muscles", "Intermediate"),
        Exercise("Barbell Biceps Curls", "Targets biceps", "Intermediate"),
        Exercise("Hammer Curls", "Targets biceps", "Intermediate"),
        Exercise("TRX Rows", "Targets back muscles", "Intermediate"),
    ],
    'Legs': [
        Exercise("Back Squat", "Targets legs and glutes", "Advanced"),
        Exercise("Front Squat", "Targets quads and core", "Intermediate"),
        Exercise("Bulgarian Split Squat", "Targets quads and glutes", "Intermediate"),
        Exercise("Leg Press", "Targets quads, hamstrings, and glutes", "Intermediate"),
        Exercise("Romanian Deadlift", "Targets hamstrings and glutes", "Intermediate"),
        Exercise("Leg Extension", "Targets quads", "Intermediate"),
        Exercise("Glute Bridge", "Targets glutes and hamstrings", "Intermediate"),
        Exercise("Walking Lunge", "Targets legs and glutes", "Intermediate"),
    ]
}

for exercise in workout_types['Pull']:
    print(exercise)