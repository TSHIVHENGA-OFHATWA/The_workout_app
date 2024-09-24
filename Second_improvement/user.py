#!/usr/bin/python3
"""
This module defines the User class for the Get Fit App, with support for workout goals.
"""


class User:
    """
    Represents a user of the Get Fit App.

    Attributes:
        username (str): The username of the user.
        email (str): The email of the user.
        password (str): The password of the user.
        workouts (list): A list to store the user's workouts.
        weekly_goal (int): The number of workouts the user aims to complete per week.
    """

    def __init__(self, username, email, password):
        """
        Initializes a new User instance.

        Args:
            username (str): The user's username.
            email (str): The user's email address.
            password (str): The user's password.
        """
        self.username = username
        self.email = email
        self.password = password
        self.workouts = []
        self.weekly_goal = 0
