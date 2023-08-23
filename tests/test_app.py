import unittest

class TestMulti(unittest.TestCase):

    def test_multi(self):
        self.assertEqual(multiaplicacion(2, 3), 6)

if __name__ == '__main__':
    unittest.main()