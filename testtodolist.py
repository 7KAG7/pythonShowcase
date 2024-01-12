import unittest
from todolist import TodoList  # Make sure to use the correct module name

class TestTodoList(unittest.TestCase):
    def setUp(self):
        # Create a new TodoList instance before each test
        self.todo_list = TodoList()

    def test_add_task(self):
        self.todo_list.add_task("Buy groceries")
        self.assertEqual(self.todo_list.tasks, ["Buy groceries"])

    def test_display_tasks_empty(self):
        result = self.todo_list.display_tasks()
        self.assertEqual(result, "No tasks in the to-do list.")

    def test_display_tasks_non_empty(self):
        self.todo_list.add_task("Buy groceries")
        self.todo_list.add_task("Complete Python project")
        result = self.todo_list.display_tasks()
        expected_result = "1. Buy groceries\n2. Complete Python project"
        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()
