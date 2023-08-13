import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand

class TestConsoleShowCommand(unittest.TestCase):

    def setUp(self):
        self.console = HBNBCommand()

    def tearDown(self):
        self.console = None

    @patch('sys.stdout', new_callable=StringIO)
    def test_show_valid(self, mock_stdout):
        # Create an instance to be shown
        self.console.onecmd("create User")
        obj_id = mock_stdout.getvalue().strip()

        # Reset mock_stdout for next capture
        mock_stdout.truncate(0)

        # Test 'show' command
        self.console.onecmd("show User {}".format(obj_id))
        expected_output = "[User] ({}) {}".format(obj_id, str(self.console.classlist['User'](id=obj_id)))
        self.assertEqual(mock_stdout.getvalue().strip(), expected_output)

    @patch('sys.stdout', new_callable=StringIO)
    def test_show_invalid_class(self, mock_stdout):
        # Test 'show' with invalid class name
        self.console.onecmd("show InvalidClass 123")
        expected_output = "** class doesn't exist **"
        self.assertEqual(mock_stdout.getvalue().strip(), expected_output)

    @patch('sys.stdout', new_callable=StringIO)
    def test_show_invalid_id(self, mock_stdout):
        # Test 'show' with invalid object ID
        self.console.onecmd("show User InvalidID")
        expected_output = "** no instance found **"
        self.assertEqual(mock_stdout.getvalue().strip(), expected_output)

if __name__ == "__main__":
    unittest.main()

