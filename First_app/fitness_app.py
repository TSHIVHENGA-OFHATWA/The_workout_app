#!/usr/bin/python3
"""
This module defines the FitnessApp class for the Get Fit App.
"""

from user import User
from workout import Workout


class FitnessApp:
    """
    Manages user registration and workout logging for the Get Fit App.

    Attributes:
        users (list): A list of registered users.
    """

    def __init__(self):
        """Initializes a new FitnessApp instance."""
        self.users = []

    def register_user(self, username, email, password):
        """
        Registers a new user.

        Args:
            username (str): The user's username.
            email (str): The user's email address.
            password (str): The user's password.

        Returns:
            User: The newly registered user.
        """
        new_user = User(username, email, password)
        self.users.append(new_user)
        return new_user

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
