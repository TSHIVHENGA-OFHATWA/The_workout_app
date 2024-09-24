#!/usr/bin/python3
"""
This module runs main interactive command-line interface for the Get Fit App.
"""

from fitness_app import FitnessApp

def main():
    """Runs the main command-line interface for the Get Fit App."""
    fitness_app = FitnessApp()
    current_user = None

    def print_separator():
        print("=" * 40)

    while True:
        print_separator()
        print("Welcome to Get Fit App")
        print_separator()
        print("1. Register\n2. Login\n3. Log Workout\n4. View Workout History\n5. Set Fitness Goal\n6. Track Goal Progress\n7. Exit")

        choice = input("Choose an option: ")

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
            user = fitness_app.authenticate_user(username, password)

            if user:
                current_user = user
                print_separator()
                print(f"Welcome back, {username}!")
            else:
                print_separator()
                print("Authentication failed. Please check your credentials.")

        elif choice == "3":
            if current_user:
                date = input("Enter workout date (YYYY-MM-DD): ")
                duration = int(input("Enter workout duration (minutes): "))
                exercises = input("Enter exercises (comma-separated): ").split(',')
                fitness_app.log_workout(current_user, date, duration, exercises)
                print_separator()
                print(f"Workout logged successfully on {date}")
            else:
                print_separator()
                print("Please login first.")

        elif choice == "4":
            if current_user:
                fitness_app.view_workout_history(current_user)
            else:
                print_separator()
                print("Please login first.")

        elif choice == "5":
            if current_user:
                goal = int(input("Enter your weekly workout goal: "))
                current_user.set_goal(goal)
            else:
                print_separator()
                print("Please login first.")

        elif choice == "6":
            if current_user:
                fitness_app.track_goal_progress(current_user)
            else:
                print_separator()
                print("Please login first.")

        elif choice == "7":
            print_separator()
            print("Exiting the Get Fit App. Goodbye!")
            break

        else:
            print_separator()
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
