# db.py
import unittest
from unittest.mock import patch
from db import process_data_from_db


class TestProcessDataFromDB(unittest.TestCase):
    @patch("db.fetch_data_from_db")  # Patch the correct function
    def test_process_data_from_db(self, mock_fetch_data):
        mock_fetch_data.return_value = 5
        result = process_data_from_db()  # Call the correct function
        self.assertEqual(result, 10)


if __name__ == "__main__":
    unittest.main()
