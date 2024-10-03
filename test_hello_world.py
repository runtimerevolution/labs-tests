import unittest
import subprocess


class TestHelloWorld(unittest.TestCase):
    def test_output(self):
        result = subprocess.run(['python3', 'hello_world.py'], capture_output=True, text=True)
        self.assertEqual(result.stdout.strip(), 'Hello, World!')


if __name__ == "__main__":
    unittest.main()
