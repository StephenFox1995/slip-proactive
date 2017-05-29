from .exceptions import WorkerTaskLimitException


class Worker(object):

    def __init__(self, name, workerid, task_limit):

        self._name = name
        self._workerid = workerid
        self._tasklimit = task_limit
        self._tasks = []

    def assign_task(self, task):
        """
        Assigns a task to a worker.
        :param task: A task to assign to a worker.
        """
        if len(self._tasks) < self._tasklimit:
            self._tasks.append(task)
        else:
            raise WorkerTaskLimitException

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
