import random
from user import User
from workout import Workout
from exercise import Exercise, workout_types


def create_account():
    name = input("Please input user data:\nName: ")
    if User.user_exists(name):
        print(f"User '{name}' already exists. Please log in.")
        return
    gender = input("Gender: ")
    age = int(input("Age: "))
    weight = float(input("Weight (kg): "))
    height = float(input("Height (cm): "))
    goal = input("Is your goal to lose weight or gain muscle?\nGoal: ")
    activity_level = input('Available activity levels are: "low", "moderate", "high"\nActivity level: ')
    current_user = User(name, gender, age, weight, height, goal, activity_level)
    print("Account created successfully!")
    return current_user


def view_profile():
    current_user_name = input("Please input the user which profile you want to view: ")
    user = next((u for u in User.users if u.name == current_user_name), None)  # Find the user object
    if user:
        print(user)
    else:
        print("No user found with that name.")


def edit_profile():
    current_user_name = input('Please enter the user that you would like to edit: ')
    user = next((u for u in User.users if u.name == current_user_name), None)

    if not user:
        print("No user found with that name. Please create an account or log in.")
        return

    print('Please select the attribute that you would like to adjust: 1.Name\n'
          '2.Gender\n'
          '3.Age\n'
          '4.Weight\n'
          '5.Height\n'
          '6.Enter new goal (lose weight/gain muscle)\n'
          '7.Enter new activity level (low/moderate/high')
    selected_change = int(input('Please select your option:'))
    if selected_change == 1:
        new_name = input('Please input the desired name: ')
        user.name = new_name

    elif selected_change == 3:
        new_name = input('Please input the desired name: ')
        user.name = new_name

    elif selected_change == 2:
        new_age = int(input('Please input the new age: '))
        user.age = new_age

    new_goal = input("Enter new goal (lose weight/gain muscle) or press Enter to keep current: ")
    if new_goal:
        user.goal = new_goal
    print("Profile updated successfully!")


def view_exercises():
    print("\n--- Available Exercises ---")
    for workout_type, exercises in workout_types.items():
        print(f"\n{workout_type} Exercises:")
        for exercise in exercises:
            print(exercise)


def generate_workout(current_user):
    if not current_user:
        print("No user is currently logged in. Please create an account or log in.")
        return

    workout_choice = input("Choose a workout type (Push, Pull, Legs): ").capitalize()

    if workout_choice not in workout_types:
        print("Invalid workout type selected.")
        return

    selected_exercises = random.sample(workout_types[workout_choice], k=6)  # Choose 3 random exercises
    print(f"\n--- Your {workout_choice} Workout ---")
    for exercise in selected_exercises:
        print(exercise)

    current_user.add_workout(f"{workout_choice} Workout: {[ex.name for ex in selected_exercises]}")


def track_progress(current_user):
    if not current_user:
        print("No user is currently logged in. Please create an account or log in.")
        return

    print("\n--- Your Workout Progress ---")
    if current_user.workout_history:
        for workout in current_user.workout_history:
            print(workout)
    else:
        print("No workout history found. Start working out to track your progress!")


def display_menu():
    while True:
        print("\n--- Training Program ---")
        print("1. Create Account")
        print("2. View Profile")
        print("3. Edit Profile")
        print("4. View Exercises")
        print("5. Generate Workout")
        print("0. Exit")

        choice = input("Please select an option: ")

        if choice == '1':
            create_account()
        elif choice == '2':
            view_profile()
        elif choice == '3':
            edit_profile()
        elif choice == '4':
            view_exercises()
        elif choice == '5':
            generate_workout()
        elif choice == '0':
            print("Exiting the application. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    display_menu()
