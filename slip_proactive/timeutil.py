from datetime import timedelta


def processing_time(days=None, hours=None, minutes=None, seconds=None):
    return timedelta(days=days, hours=hours, minutes=minutes, seconds=seconds)


def release_time(deadline=None, processing=None):
    return deadline - processing
