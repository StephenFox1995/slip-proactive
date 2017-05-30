import unittest
from slip_proactive.task import Task
from slip_proactive import timeutil
from datetime import datetime, timedelta


class TestTask(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_init(self):
        name = "TestTask"
        taskid = "T123"
        created_at = datetime.now()
        deadline = datetime.now() + timedelta(minutes=5, seconds=10)
        processing = timeutil.processing_time(
            days=0,
            hours=0,
            minutes=1,
            seconds=0
        )
        task = Task(name, taskid, created_at, processing, deadline)

        self.assertEqual(name, task.name)
        self.assertEqual(taskid, task.taskid)
        self.assertEqual(created_at, task.created_at)
        self.assertEqual(deadline, deadline)
        self.assertEqual(processing, task.processing)
        release = timeutil.release_time(deadline, processing)
        self.assertEqual(release, task.release)
