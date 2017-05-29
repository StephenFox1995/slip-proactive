import unittest
from slip_proactive.worker import Worker
from slip_proactive.task import Task
from slip_proactive.exceptions import WorkerTaskLimitException

class TestTask(unittest.TestCase):

    def setUp(self):
        self._name = "StephenFox"
        self._taskid = "W123"
        self._tasklimit = 2

    def tearDown(self):
        pass

    def test_init(self):
        worker = Worker(self._name, self._taskid, self._tasklimit)
        self.assertEqual(self._name, worker.name)
        self.assertEqual(self._taskid, worker.workerid)

    def test_task_assignment_length(self):
        worker = Worker(self._name, self._taskid, self._tasklimit)
        worker.assign_task(self._task_create())
        self.assertEqual(len(worker.assigned_tasks), 1)
        worker.assign_task(self._task_create())
        self.assertEqual(len(worker.assigned_tasks), 2)

    def test_task_assignment_exception(self):
        worker = Worker(self._name, self._taskid, self._tasklimit)
        worker.assign_task(self._task_create())
        worker.assign_task(self._task_create())
        with self.assertRaises(WorkerTaskLimitException):
            worker.assign_task(self._task_create())

    def _task_create(self):
        return Task("TestTask", "SomeRandomID")
