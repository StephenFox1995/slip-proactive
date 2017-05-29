import unittest
from slip_proactive.task import Task


class TestTask(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_init(self):
        name = "TestTask"
        taskid = "T123"
        task = Task(name, taskid)

        self.assertEqual(name, task.name)
        self.assertEqual(taskid, task.id)
