import unittest
from rock_app.data_point import DataPoint

class TestFileReader(unittest.TestCase):
    def test_1(self):
        self.assertTrue(file_reader() == 5)

if __name__ == "__main__":
    unittest.main()
