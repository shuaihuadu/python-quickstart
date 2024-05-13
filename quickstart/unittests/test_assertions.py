import unittest


class TestAssertions(unittest.TestCase):

    def test_equals(self):
        self.assertEqual("one something", "other something")


if __name__ == "__main__":
    unittest.main()
