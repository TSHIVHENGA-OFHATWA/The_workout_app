#!/usr/bin/python3
"""
This module runs the main interactive command-line interface for the Get Fit App, including login, workout history, and goals.
"""

from fitness_app import FitnessApp


def print_separator():
    """Prints a separator line of 40 equals signs."""
    print("=" * 40)


def main():
    """Runs the main command-line interface for the Get Fit App."""
    fitness_app = FitnessApp()
    
    logged_in_user = None

    while True:
        print_separator()
        print("Welcome to Get Fit App")
        print_separator()

        if logged_in_user:
            print(f"Hello, {logged_in_user.username}!")
            print("1. Log Workout\n2. View Workout History\n3. Set Weekly Workout Goal\n4. Track Goal Progress\n5. Logout\n6. Exit")
        else:
            print("1. Register\n2. Login\n3. Exit")

        choice = input("Choose an option: ")

        if not logged_in_user:
            if choice == "1":
                username = input("Enter username: ")
                email = input("Enter email: ")
                password = input("Enter password: ")
                fitness_app.register_user(username, email, password)
                print_separator()
                print("User registered successfully!")

            elif choice == "2":
                username = input("Enter username: ")
                password = input("Enter password: ")
                user = fitness_app.login_user(username, password)
                if user:
                    logged_in_user = user
                    print_separator()
                    print(f"Logged in successfully as {logged_in_user.username}")
                else:
                    print_separator()
                    print("Invalid username or password. Try again.")

            elif choice == "3":
                print_separator()
                print("Exiting the Get Fit App. Goodbye!")
                break
            else:
                print_separator()
                print("Invalid choice. Please try again.")
        else:
            if choice == "1":
                date = input("Enter workout date (YYYY-MM-DD): ")
                duration = int(input("Enter workout duration (minutes): "))
                exercises = input("Enter exercises (comma-separated): ").split(',')
                fitness_app.log_workout(logged_in_user, date, duration, exercises)
                print_separator()
                print(f"Workout logged successfully on {date}")

            elif choice == "2":
                history = fitness_app.view_workout_history(logged_in_user)
                print_separator()
                if history:
                    for workout in history:
                        print(f"Date: {workout.date}, Duration: {workout.duration} min, Exercises: {', '.join(workout.exercises)}")
                else:
                    print("No workout history available.")

            elif choice == "3":
                goal = int(input("Set your weekly workout goal (e.g., 3 workouts/week): "))
                fitness_app.set_workout_goal(logged_in_user, goal)
                print_separator()
                print(f"Your weekly goal of {goal} workouts has been set.")

            elif choice == "4":
                workouts_completed, goal = fitness_app.track_goal_progress(logged_in_user)
                print_separator()
                print(f"You have completed {workouts_completed}/{goal} workouts this week.")

            elif choice == "5":
                print_separator()
                print(f"Logging out {logged_in_user.username}...")
                logged_in_user = None

            elif choice == "6":
                print_separator()
                print("Exiting the Get Fit App. Goodbye!")
                break
            else:
                print_separator()
                print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
