import unittest
from slip_proactive import timeutil
from datetime import datetime, timedelta


class TestTimeutil(unittest.TestCase):
    def test_processing_time(self):
        now = datetime(
            year=2017,
            month=1,
            day=5,
            hour=0,
            minute=0,
            second=0,
            microsecond=0
        )
        processing = timeutil.processing_time(
            days=0,
            hours=1,
            minutes=2,
            seconds=30
        )
        expected = datetime(
            year=2017,
            month=1,
            day=5,
            hour=1,
            minute=2,
            second=30,
            microsecond=0
        )
        actual = now + processing
        self.assertEqual(expected, actual)

    def test_release_time(self):

        in_5_minutes = datetime.now() + timedelta(minutes=5)
        processing = timeutil.processing_time(
            days=0,
            hours=0,
            minutes=2,
            seconds=30
        )
        expected = in_5_minutes - processing
        release = timeutil.release_time(in_5_minutes, processing)
        self.assertEqual(expected, release)
