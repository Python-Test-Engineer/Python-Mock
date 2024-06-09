# test_db.py
import unittest
from unittest.mock import patch
from db import double_data


class TestProcessDataFromDB(unittest.TestCase):
    @patch("db.fetch_data_from_db")  # Patch the correct function
    def test_process_data_from_db(self, mock_fetch_data):
        # intercept fetch_data_from_db() and use 5 as the return value
        mock_fetch_data.return_value = 5
        # When we call process_data_from_db() it should return 10 as it double fetch_data_from_db() return value
        result = double_data()
        self.assertEqual(result, 10)


if __name__ == "__main__":
    unittest.main()
