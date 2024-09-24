#!/usr/bin/python3
"""
This module defines the User class for the Get Fit App.
"""


class User:
    """
    Represents a user of the Get Fit App.

    Attributes:
        username (str): The username of the user.
        email (str): The email of the user.
        password (str): The password of the user.
        workouts (list): A list to store the user's workouts.
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
        
    def set_goal(self, goal):
        """
        Sets the user's fitness goal.

        Args:
            goal (int): The number of workouts the user wants to complete per week.
        """
        self.goal = goal
        print(f"Goal set to {goal} workouts per week.")
