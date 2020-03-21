from __future__ import print_function

from time_interval import TimeInterval
from datetime import datetime
import sys



def filter_builds_by_time_range(build_dto_list, startDate, endDate):
    return []

def get_list_of_fail_times_from_builds(build_dto_list):
    fail_time_list = []
    previous_build_successfull = True
    for build_dto in build_dto_list:
        if build_dto.get_status() != "SUCCESS":
            if previous_build_successfull:
                time_interval = TimeInterval(build_dto.get_datetime())
                fail_time_list.append(time_interval)
                previous_build_successfull = False
        else:
            previous_build_successfull = True
            fail_time_list_length = len(fail_time_list)
            if fail_time_list_length > 0:
                last_unstable_entry = fail_time_list[fail_time_list_length-1]
                last_unstable_entry.set_end(build_dto.get_datetime())
    
    _end_last_interval_if_unset(fail_time_list)
    return fail_time_list

def _end_last_interval_if_unset(fail_time_list):
    fail_time_list_length = len(fail_time_list)
    if fail_time_list_length > 0 and fail_time_list[fail_time_list_length-1].get_end() == None:
        last_unstable_entry = fail_time_list[fail_time_list_length-1]
        last_unstable_entry.set_end(get_datetime_today())

def get_datetime_today():
    return datetime.now()