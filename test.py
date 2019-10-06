import unittest
from hello_world import hello, hello_world


class MyTestCase(unittest.TestCase):
    def test_hello_world(self):
        value = hello_world()

        self.assertEqual(value, 'Hello World!')

    def test_hello(self):
        value = hello()

        self.assertEqual(value, 'Hello!!!')


if __name__ == '__main__':
    unittest.main()
