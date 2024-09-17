
import unittest

from hello_world import HelloWorld

class TestHelloWorld(unittest.TestCase):
    def setUp(self):
        self.hw = HelloWorld()

    def test_print_message(self):
        self.assertEqual(self.hw.print_message(), "Hello World")

if __name__ == "__main__":
    unittest.main()