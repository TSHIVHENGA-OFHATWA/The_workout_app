#!/usr/bin/python3
"""
This module defines the FitnessApp class with enhanced functionality
for the Get Fit App, including user login, workout history, and workout goals.
"""

from user import User
from workout import Workout
import datetime


class FitnessApp:
    """
    Manages user registration, login, workout logging, workout history, and goals.

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

    def login_user(self, username, password):
        """
        Logs in a user by checking the username and password.

        Args:
            username (str): The user's username.
            password (str): The user's password.

        Returns:
            User: The logged-in user, or None if login fails.
        """
        user = next((u for u in self.users if u.username == username and u.password == password), None)
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
        Returns the workout history for the specified user.

        Args:
            user (User): The user whose workout history to view.

        Returns:
            list: A list of the user's past workouts.
        """
        return user.workouts

    def set_workout_goal(self, user, weekly_goal):
        """
        Sets a weekly workout goal for the user.

        Args:
            user (User): The user setting the goal.
            weekly_goal (int): The number of workouts the user aims to complete per week.
        """
        user.weekly_goal = weekly_goal

    def track_goal_progress(self, user):
        """
        Tracks the user's progress toward their weekly workout goal.

        Args:
            user (User): The user whose goal progress to track.

        Returns:
            int: The number of workouts completed in the current week.
            int: The user's weekly goal.
        """
        current_week = datetime.date.today().isocalendar()[1]
        workouts_this_week = [w for w in user.workouts if datetime.datetime.strptime(w.date, '%Y-%m-%d').isocalendar()[1] == current_week]
        return len(workouts_this_week), user.weekly_goal
