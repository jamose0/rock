import unittest
import rock_app.file_reader as fr
#from rock_app.data_point import DataPoint

class TestFileReader(unittest.TestCase):
    def test_1(self):
        self.assertTrue(fr.file_to_data() == 5)

if __name__ == "__main__":
    unittest.main()
