from __future__ import print_function

import sys

class JobDto:
    def __init__(self, name, build_list):
        self.name = name
        self.build_list = build_list

    def get_name(self):
        return self.name

    def get_build_list(self):
        return self.build_list
