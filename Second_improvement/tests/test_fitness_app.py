#!/usr/bin/python3
"""
Unittests for the Get Fit App.
"""

import unittest
from fitness_app import FitnessApp
import unittest
from fitness_app import FitnessApp
from user import User
from datetime import datetime, timedelta


class TestFitnessAppEnhanced(unittest.TestCase):
    def setUp(self):
        """Set up the test environment before each test."""
        self.app = FitnessApp()
        self.user = self.app.register_user("testuser", "testuser@example.com", "password123")
        self.app.authenticate_user("testuser", "password123")
    
    def test_hash_password(self):
        """Test if password hashing works correctly."""
        hashed = self.app.hash_password("password123")
        self.assertEqual(len(hashed), 64)  # SHA-256 hash length

    def test_log_workout(self):
        """Test logging a workout for a user."""
        workout = self.app.log_workout(self.user, "2024-09-24", 60, ["Squats", "Push-ups"])
        self.assertEqual(len(self.user.workouts), 1)
        self.assertEqual(workout.date, "2024-09-24")

    def test_view_workout_history(self):
        """Test viewing a user's workout history."""
        self.app.log_workout(self.user, "2024-09-24", 60, ["Squats", "Push-ups"])
        workouts = self.app.view_workout_history(self.user)
        self.assertEqual(len(workouts), 1)

    def test_goal_setting(self):
        """Test setting a fitness goal for a user."""
        self.user.set_goal(5)
        self.assertEqual(self.user.goal, 5)

    def test_goal_progress_tracking(self):
        """Test tracking a user's progress toward their weekly workout goal."""
        self.user.set_goal(3)
        
        # Log a workout for this week
        date_today = datetime.now().strftime("%Y-%m-%d")
        self.app.log_workout(self.user, date_today, 30, ["Jumping Jacks", "Burpees"])

        # Log a workout for a different week
        past_date = (datetime.now() - timedelta(weeks=2)).strftime("%Y-%m-%d")
        self.app.log_workout(self.user, past_date, 30, ["Lunges", "Sit-ups"])

        # Track workouts for this week
        workouts_this_week = self.app.track_goal_progress(self.user)
        self.assertEqual(workouts_this_week, 1)

    def test_authenticate_user(self):
        """Test if the user can be authenticated correctly."""
        authenticated_user = self.app.authenticate_user("testuser", "password123")
        self.assertIsNotNone(authenticated_user)
        self.assertEqual(authenticated_user.username, "testuser")

    def test_failed_authentication(self):
        """Test if authentication fails with the wrong password."""
        authenticated_user = self.app.authenticate_user("testuser", "wrongpassword")
        self.assertIsNone(authenticated_user)


if __name__ == "__main__":
    unittest.main()

