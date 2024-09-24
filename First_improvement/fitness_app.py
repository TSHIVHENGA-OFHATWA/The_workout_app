#!/usr/bin/python3
"""
This module defines the FitnessApp class for the Get Fit App.
"""


import hashlib
from user import User
from workout import Workout


class FitnessApp:
    """
    Manages user registration, authentication, and workout logging for the Get Fit App.
    """

    def __init__(self):
        """Initializes a new FitnessApp instance."""
        self.users = []

    def hash_password(self, password):
        """
        Hashes a password using SHA-256 for secure storage.

        Args:
            password (str): The user's password in plaintext.

        Returns:
            str: The hashed password.
        """
        return hashlib.sha256(password.encode()).hexdigest()

    def register_user(self, username, email, password):
        """
        Registers a new user with a hashed password.

        Args:
            username (str): The user's username.
            email (str): The user's email address.
            password (str): The user's password.

        Returns:
            User: The newly registered user.
        """
        hashed_password = self.hash_password(password)
        new_user = User(username, email, hashed_password)
        self.users.append(new_user)
        return new_user

    def authenticate_user(self, username, password):
        """
        Authenticates a user by checking the hashed password.

        Args:
            username (str): The user's username.
            password (str): The user's password.

        Returns:
            User: The authenticated user or None if authentication fails.
        """
        hashed_password = self.hash_password(password)
        user = next((u for u in self.users if u.username == username and u.password == hashed_password), None)
        return user

    def log_workout(self, user, date, duration, exercises):
        """
        Logs a workout for the specified user.

        Args:
            user (User): The user logging the workout.
            date (str): The workout date.
            duration (int): The workout duration in minutes.
            exercises (list): A list of exercises performed.

        Returns:
            Workout: The logged workout.
        """
        new_workout = Workout(date, duration, exercises)
        user.workouts.append(new_workout)
        return new_workout

    def view_workout_history(self, user):
        """
        Displays the workout history for the specified user.

        Args:
            user (User): The user whose workout history is displayed.

        Returns:
            list: A list of the user's workouts.
        """
        if not user.workouts:
            print("No workouts logged.")
            return []

        print(f"Workout History for {user.username}:")
        for workout in user.workouts:
            print(f"Date: {workout.date}, Duration: {workout.duration} min, Exercises: {', '.join(workout.exercises)}")

        return user.workouts

    def track_goal_progress(self, user):
        """
        Tracks the user's progress toward their weekly workout goal.

        Args:
            user (User): The user whose progress is being tracked.

        Returns:
            int: The number of workouts completed this week.
        """
        from datetime import datetime, timedelta
        current_week = datetime.now().isocalendar()[1]
        workouts_this_week = [
            w for w in user.workouts
            if datetime.strptime(w.date, "%Y-%m-%d").isocalendar()[1] == current_week
        ]
        num_workouts = len(workouts_this_week)

        if user.goal is not None:
            print(f"Workouts this week: {num_workouts}/{user.goal}")
        else:
            print(f"Workouts this week: {num_workouts}")

        return num_workouts
