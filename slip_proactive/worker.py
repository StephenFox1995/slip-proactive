from .exceptions import (
    WorkerTaskLimitException,
    WorkerUnassignableTasktypeException,
    WorkerTaskPreviouslyAssignedException
)


class Worker(object):
    def __init__(self, name, workerid, task_limit, tasktypes):
        """
        Initialize a Worker object.
        :param name: The name of a worker
        :type name: str
        :param workerid: The id of the worker
        :type workerid: str
        :param task_limit: The maximum amount of tasks that can be assigned
            to the worker.
        :type task_limit: int
        :param tasktypes: A list of task types that
            can be assigned to the worker.
        :type tasktypes: list
        """
        self._name = name
        self._workerid = workerid
        self._tasklimit = task_limit
        self._tasks = []
        self._assignable_tasktypes = tasktypes

    def _contains_task_by_taskid(self, taskid):
        for task in self._tasks:
            if task.taskid == taskid:
                return True
        return False

    def _assign_task(self, task):
        # check task limit.
        if len(self._tasks) >= self._tasklimit:
            raise WorkerTaskLimitException
        # cehck task is not already assigned
        elif self._contains_task_by_taskid(task.taskid):
            raise WorkerTaskPreviouslyAssignedException
        # check task type.
        elif (task.tasktype is not None) and \
             (task.tasktype not in self._assignable_tasktypes):
            raise WorkerUnassignableTasktypeException
        else:
            self._tasks.append(task)

    def assign_task(self, task):
        """
        Assigns a task to a worker.
        :param task: A task to assign to a worker.
        """
        self._assign_task(task)

    def unassign_task(self, taskid):
        """
        Unassigns a task from worker and returns it.
        :param taskid: The id of the task
        :type taskid: str
        """
        for task in self._tasks:
            if task.taskid == taskid:
                return self._tasks.pop(self._tasks.index(task))

    @property
    def name(self):
        return self._name

    @property
    def workerid(self):
        return self._workerid

    @property
    def tasklimit(self):
        return self._tasklimit

    @property
    def assigned_tasks(self):
        return self._tasks
