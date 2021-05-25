import unittest


class SampleTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.x = 1

    @classmethod
    def tearDownClass(cls):
        print("tearDownClass")

    def setUp(self):
        self.y = None

    def tearDown(self):
        print("tearDown")

    def test_test1(self):
        self.assertEqual(1, self.x)

    def test_test2(self):
        self.assertIsNone(self.y)
