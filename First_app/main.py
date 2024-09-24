#!/usr/bin/python3
"""
This module runs main interactive command-line interface for the Get Fit App.
"""

from fitness_app import FitnessApp


def print_separator():
    """Prints a separator line of 40 equals signs."""
    print("=" * 40)


def main():
    """Runs the main command-line interface for the Get Fit App."""
    fitness_app = FitnessApp()

    while True:
        print_separator()
        print("Welcome to Get Fit App")
        print_separator()
        print("1. Register\n2. Log Workout\n3. Exit")

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
            user = next((u for u in fitness_app.users if u.username == username
                         ), None)

            if user:
                date = input("Enter workout date (YYYY-MM-DD): ")
                duration = int(input("Enter workout duration (minutes): "))
                exercises = input("Enter exercises (comma-separated): "
                                  ).split(',')
                fitness_app.log_workout(user, date, duration, exercises)
                print_separator()
                print(f"Workout logged successfully on {date}")
            else:
                print_separator()
                print("User not found. Please register first.")

        elif choice == "3":
            print_separator()
            print("Exiting the Get Fit App. Goodbye!")
            break
        else:
            print_separator()
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
