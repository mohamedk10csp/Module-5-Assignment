
import unittest
import contact_manager


class TestContactManager(unittest.TestCase):
    """Test the contact manager functions."""

    def setUp(self):
        """Start each test with an empty contact list."""
        contact_manager.contacts.clear()

    def test_add_contact(self):
        """Test adding a new contact."""
        contact_manager.add_contact("Alice", "555-1234")
        self.assertEqual(
            contact_manager.contacts["Alice"], "555-1234"
        )

    def test_find_existing_contact(self):
        """Test finding an existing contact."""
        contact_manager.add_contact("Alice", "555-1234")
        result = contact_manager.find_contact("Alice")
        self.assertEqual(result, "555-1234")

    def test_find_missing_contact(self):
        """Test finding a contact that does not exist."""
        result = contact_manager.find_contact("Bob")
        self.assertIsNone(result)

    def test_delete_existing_contact(self):
        """Test deleting an existing contact."""
        contact_manager.add_contact("Alice", "555-1234")
        contact_manager.delete_contact("Alice")
        self.assertNotIn("Alice", contact_manager.contacts)

    def test_delete_missing_contact(self):
        """Test deleting a contact that does not exist."""
        contact_manager.delete_contact("Bob")
        self.assertNotIn("Bob", contact_manager.contacts)

    def test_duplicate_contact(self):
        """Test adding a contact that already exists."""
        contact_manager.add_contact("Alice", "555-1234")
        self.assertRaises(
            contact_manager.DuplicateContactError,
            contact_manager.add_contact,
            "Alice",
            "555-5678"
        )


if __name__ == "__main__":
    unittest.main()