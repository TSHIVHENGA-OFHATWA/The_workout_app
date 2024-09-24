#!/usr/bin/python3
"""
Unittests for the Get Fit App.
"""


import unittest
from fitness_app import FitnessApp
from user import User


class TestFitnessApp(unittest.TestCase):
    def setUp(self):
        """Set up the test environment before each test."""
        self.app = FitnessApp()
        self.user = self.app.register_user("testuser", "testuser@example.com", "password123")

    def test_register_user(self):
        """Test if a new user can be registered."""
        self.assertEqual(self.user.username, "testuser")
        self.assertEqual(self.user.email, "testuser@example.com")
        self.assertEqual(len(self.app.users), 1)

    def test_log_workout(self):
        """Test if a workout can be logged for a user."""
        workout = self.app.log_workout(self.user, "2024-09-24", 60, ["Squats", "Push-ups"])
        self.assertEqual(len(self.user.workouts), 1)
        self.assertEqual(workout.duration, 60)
        self.assertEqual(workout.exercises, ["Squats", "Push-ups"])

    def test_view_workout_history(self):
        """Test if workout history can be viewed."""
        self.app.log_workout(self.user, "2024-09-24", 60, ["Squats", "Push-ups"])
        workouts = self.app.view_workout_history(self.user)
        self.assertEqual(len(workouts), 1)
        self.assertEqual(workouts[0].date, "2024-09-24")

    def test_authenticate_user_success(self):
        """Test successful user authentication."""
        authenticated_user = self.app.authenticate_user("testuser", "password123")
        self.assertIsNotNone(authenticated_user)
        self.assertEqual(authenticated_user.username, "testuser")

    def test_authenticate_user_failure(self):
        """Test user authentication failure with wrong password."""
        authenticated_user = self.app.authenticate_user("testuser", "wrongpassword")
        self.assertIsNone(authenticated_user)


if __name__ == "__main__":
    unittest.main()
