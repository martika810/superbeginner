import unittest
from thread.status import ShareStatus

class ShareStatusTest(unittest.TestCase):

    def test_case01(self):
        status = ShareStatus()
        count = status.read_count()
        thread1_status = status.read_thread1_status()
        thread2_status = status.read_thread2_status()

        self.assertEqual(count,0)
        self.assertFalse(thread1_status)
        self.assertFalse(thread2_status)

