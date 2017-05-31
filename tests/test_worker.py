import unittest
from slip_proactive.worker import Worker
from slip_proactive.task import Task
from slip_proactive.exceptions import (
    WorkerTaskLimitException,
    WorkerUnassignableTasktypeException,
    WorkerTaskPreviouslyAssignedException
)


class TestTask(unittest.TestCase):

    def test_init(self):
        worker = Worker("Stephen", "1", 2, [])
        self.assertEqual("Stephen", worker.name)
        self.assertEqual("1", worker.workerid)

    def test_task_assign_length(self):
        task1 = Task("task1", "1", 0, 0, 0)
        task2 = Task("task2", "2", 0, 0, 0)
        worker = Worker("Stephen", "1", 2, [])
        worker.assign_task(task1)
        self.assertEqual(len(worker.assigned_tasks), 1)
        worker.assign_task(task2)
        self.assertEqual(len(worker.assigned_tasks), 2)

    def test_task_assign_type_set_for_worker_and_task(self):
        task = Task("task1", "1", 0, 0, 0, tasktype="fooditem")
        # test adding task with same task type as worker
        worker = Worker("Stephen", "1", 2, ["fooditem"])
        worker.assign_task(task)
        self.assertEqual(len(worker.assigned_tasks), 1)

    def test_task_assign_type_not_set_for_worker_and_task(self):
        # test with tasktype not set for worker
        worker = Worker("Stephen", "1", 2, [])
        task = Task("Task", "test_id1", 0, 0, 0)
        worker.assign_task(task)

    def test_task_assign_raise_exceptions(self):
        task1 = Task("task1", "1", 0, 0, 0)
        task2 = Task("task2", "2", 0, 0, 0)
        task3 = Task("task3", "3", 0, 0, 0)
        # check task limit exception
        worker1 = Worker("Stephen", "1", 2, [])
        worker1.assign_task(task1)
        worker1.assign_task(task2)
        with self.assertRaises(WorkerTaskLimitException):
            worker1.assign_task(task3)

        # check task type exception with wrong task type
        worker2 = Worker("Stephen", "1", 2, ["sushiitems"])
        task4 = Task("Task", "test_id1", 0, 0, 0, tasktype="drinkitem")
        with self.assertRaises(WorkerUnassignableTasktypeException):
            worker2.assign_task(task4)

        # check that task with same task id cannot be assigned again to worker
        worker3 = Worker("Stephen", "1", 2, [])
        task5 = Task("Task", "test_id1", 0, 0, 0)
        worker3.assign_task(task5)
        with self.assertRaises(WorkerTaskPreviouslyAssignedException):
            worker3.assign_task(task5)

    def test_task_unassign_correct_taskid(self):
        worker = Worker("Stephen", "1", 2, [])
        task = Task("Task", "test_id", 0, 0, 0)
        worker.assign_task(task)
        self.assertEqual(task, worker.unassign_task("test_id"))
        self.assertEqual(len(worker.assigned_tasks), 0)

    def test_task_unassign_incorrect_taskid(self):
        worker = Worker("Stephen", "1", 2, [])
        task = Task("Task", "test_id", 0, 0, 0)
        worker.assign_task(task)
        self.assertEqual(len(worker.assigned_tasks), 1)
        should_be_none = worker.unassign_task("incorrect_id")
        self.assertEqual(None, should_be_none)

