class Task(object):

    """
        :param name: The name of the task
            :type name: str
        :param taskid: The id of the task
            :type taskid: str

    """
    def __init__(self, name, taskid):
        self._name = name
        self._taskid = taskid

    @property
    def name(self):
        return self._name

    @property
    def id(self):
        return self._taskid
