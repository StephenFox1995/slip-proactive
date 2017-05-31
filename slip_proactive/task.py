from . import timeutil


class Task(object):
    def __init__(self,
                 name,
                 taskid,
                 created_at,
                 processing,
                 deadline,
                 tasktype=None):
        """
        :param name: The name of the task
        :type name: str
        :param taskid: The id of the task
        :type taskid: str
        :param: created_at: The time at which the task was created at.
        :type: created_at: :class: `datetime.datetime`
        :param processing: The processing time of the task in seconds.
        :type processing: :class: `datetime.timedelta`
        :param deadline: The deadline time of the task.
        :type: deadline: :class: `datetime.datetime`
        :param tasktype: Some predefined type of task associated
            for each business, this could be, for example, fooditem, drink etc.
        :type tasktype: str
        """
        self._name = name
        self._taskid = taskid
        self._created_at = created_at
        self._processing = processing
        self._deadline = deadline
        self._release = timeutil.release_time(deadline=self._deadline,
                                              processing=self._processing)
        self._tasktype = tasktype

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

    @property
    def tasktype(self):
        return self._tasktype
