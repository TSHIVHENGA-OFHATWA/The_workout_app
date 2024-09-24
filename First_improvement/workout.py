#!/usr/bin/python3
"""
This module defines the Workout class for the Get Fit App.
"""


class Workout:
    """
    Represents a workout logged by a user.

    Attributes:
        date (str): The date of the workout.
        duration (int): The duration of the workout in minutes.
        exercises (list): The exercises performed during the workout.
    """

    def __init__(self, date, duration, exercises):
        """
        Initializes a new Workout instance.

        Args:
            date (str): The workout date.
            duration (int): The workout duration in minutes.
            exercises (list): A list of exercises performed.
        """
        self.date = date
        self.duration = duration
        self.exercises = exercises
