from __future__ import print_function

import sys

class TimeInterval:
    def __init__(self, start_datetime, end_datetime=None):
        self.start_datetime = start_datetime
        self.end_datetime = end_datetime

    def get_start(self):
        return self.start_datetime

    def get_end(self):
        return self.end_datetime

    def set_end(self, end_datetime):
        self.end_datetime = end_datetime