class WorkerTaskLimitException(Exception):
    """ Indicates too many tasks have been assigned to a worker."""
    pass


class WorkerUnassignableTasktypeException(Exception):
    """Indicates that the worker cannot be assigned
    tasks of a specific type"""
    pass


class WorkerTaskPreviouslyAssignedException(Exception):
    """Indicates that a worker is current assigned a task with
    the same task id"""
    pass
