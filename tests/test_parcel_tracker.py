
"""Tests for the parcel tracking application."""

import unittest

import parcel_tracker


class TestParcelTracker(unittest.TestCase):
    """Test parcel booking, tracking, and shipping costs."""

    def setUp(self):
        """Reset parcel state before each test."""
        parcel_tracker.parcels.clear()

    def test_book_parcel(self):
        """Booking a parcel returns a tracking ID."""
        tracking_id = parcel_tracker.book_parcel(
            "Sender", "Receiver", 2.0
        )
        self.assertIn(tracking_id, parcel_tracker.parcels)

    def test_invalid_weight(self):
        """Non-positive parcel weight is rejected."""
        with self.assertRaises(ValueError):
            parcel_tracker.book_parcel("Sender", "Receiver", 0)

    def test_shipping_cost(self):
        """Shipping cost follows the defined pricing rules."""
        self.assertEqual(parcel_tracker.shipping_cost(1), 50.0)
        self.assertEqual(parcel_tracker.shipping_cost(2), 80.0)

    def test_unknown_tracking_id(self):
        """Unknown parcel IDs return a helpful message."""
        self.assertIn(
            "Unknown tracking ID",
            parcel_tracker.track_parcel("INVALID"),
        )

    def test_advance_status(self):
        """Parcel status advances from Booked to Picked Up."""
        tracking_id = parcel_tracker.book_parcel(
            "Sender", "Receiver", 1.0
        )
        self.assertEqual(
            parcel_tracker.advance_status(tracking_id),
            "Picked Up",
        )

    def test_history_lists_are_independent(self):
        """Separate calls can use separate history lists."""
        first_history = []
        second_history = []

        parcel_tracker.book_parcel(
            "A", "B", 1.0, first_history
        )
        parcel_tracker.book_parcel(
            "C", "D", 1.0, second_history
        )

        self.assertEqual(len(first_history), 1)
        self.assertEqual(len(second_history), 1)


if __name__ == "__main__":
    unittest.main()
