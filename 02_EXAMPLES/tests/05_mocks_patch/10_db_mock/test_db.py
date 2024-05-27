# test.py
import unittest
from unittest.mock import patch
import base  # Import the correct module


class TestProcessDataFromDB(unittest.TestCase):
    @patch("test.fetch_data_from_db")  # Patch the correct function
    def process_data_from_db(self, mock_fetch_data):
        mock_fetch_data.return_value = 5
        result = test.process_data_from_db()  # Call the correct function
        self.assertEqual(result, 10)


if __name__ == "__main__":
    unittest.main()
