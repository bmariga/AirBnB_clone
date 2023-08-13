import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand


class TestConsoleCommands(unittest.TestCase):

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
    def test_update_valid(self, mock_stdout):
        # Create an instance to be updated
        self.console.onecmd("create User")
        obj_id = mock_stdout.getvalue().strip()

        # Reset mock_stdout for next capture
        mock_stdout.truncate(0)

        # Test 'update' command
        self.console.onecmd(f"update User {obj_id} name John")
        updated_instance = self.console.classlist['User'](id=obj_id, name="John")
        expected_output = "[User] ({}) {}".format(obj_id, str(updated_instance))
        self.assertEqual(mock_stdout.getvalue().strip(), expected_output)


if __name__ == "__main__":
    unittest.main()

