from . import timeutil


class Task(object):
    def __init__(self, name, taskid, created_at, processing, deadline):
        """
        :param name: The name of the task
        :type name: str
        :param taskid: The id of the task
        :type taskid: str
        :param: created_at: The time at which the task was created at.
        :type: created_at: str - ISO 8601 format.
        :param processing: The processing time of the task in seconds.
        :type processing: float
        :param deadline: The deadline time of the task.
        :type: deadline: str - ISO 8601 format.
        """
        self._name = name
        self._taskid = taskid
        self._created_at = created_at
        self._processing = processing
        self._deadline = deadline
        self._release = timeutil.release_time(self._deadline, self._processing)

    @property
    def name(self):
        return self._name

    @property
    def taskid(self):
        return self._taskid

    @property
    def created_at(self):
        return self._created_at

    @property
    def processing(self):
        return self._processing

    @property
    def deadline(self):
        return self._deadline

    @property
    def release(self):
        return self._release
