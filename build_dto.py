from __future__ import print_function

import sys

class BuildDto:
    def __init__(self, id, status, build_datetime):
        self.id = id
        self.status = status
        self.build_datetime = build_datetime

    def get_build_id(self):
        return self.id

    def get_status(self):
        return self.status

    def get_datetime(self):
        return self.build_datetime