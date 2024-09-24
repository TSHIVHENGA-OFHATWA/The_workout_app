#!/usr/bin/python3
"""
Unittests for the Get Fit App.
"""

import unittest
from fitness_app import FitnessApp


class TestFitnessApp(unittest.TestCase):
    """Tests the functionality of the FitnessApp class."""

    def setUp(self):
        """Set up a new FitnessApp instance before each test."""
        self.app = FitnessApp()

    def test_register_user(self):
        """Test that a user can be registered."""
        user = self.app.register_user("testuser", "test@example.com", "password123")
        self.assertEqual(user.username, "testuser")
        self.assertEqual(user.email, "test@example.com")
        self.assertIn(user, self.app.users)

    def test_log_workout(self):
        """Test that a workout can be logged for a user."""
        user = self.app.register_user("testuser", "test@example.com", "password123")
        workout = self.app.log_workout(user, "2024-09-24", 45, ["push-ups", "squats"])
        self.assertEqual(workout.date, "2024-09-24")
        self.assertEqual(workout.duration, 45)
        self.assertEqual(workout.exercises, ["push-ups", "squats"])
        self.assertIn(workout, user.workouts)


if __name__ == "__main__":
    unittest.main()

