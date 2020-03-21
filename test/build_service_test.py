import mock
import pytest
import build_service
from job_dto import JobDto
from build_dto import BuildDto
from time_interval import TimeInterval

from datetime import date, datetime, timedelta

STATUS_SUCCESS = "SUCCESS"
STATUS_UNSTABLE = "UNSTABLE"
STATUS_FAILURE = "FAILURE"

def test_single_successfull_build_zero_fail_times():
    build_dto = BuildDto(123, STATUS_SUCCESS, datetime(2020, 1, 1, 0, 30))
    
    result = build_service.get_list_of_fail_times_from_builds([build_dto])
    
    assert result != None
    assert len(result) == 0

def test_single_unstable_build():    
    datetime_of_build = datetime(2020, 1, 1, 0, 30)    
    next_day = datetime.combine(datetime_of_build.date() + timedelta(days=1), datetime.min.time())
    build_service.get_datetime_today  = mock.MagicMock(return_value=next_day)
    expected_fail_time = TimeInterval(datetime_of_build, next_day)
    build_dto = BuildDto(123, STATUS_UNSTABLE, datetime_of_build)
    
    result = build_service.get_list_of_fail_times_from_builds([build_dto])
    
    assert result != None
    assert len(result) == 1
    assert expected_fail_time.get_start() == result[0].get_start()
    assert expected_fail_time.get_end() == result[0].get_end()

def test_single_unstable_and_successfull_build(): 
    datetime_of_unstable_build = datetime(2020, 1, 1, 0, 30)    
    datetime_of_successfull_build = datetime(2020, 1, 1, 14, 30)    
    build_dto_unsuccessfull = BuildDto(123, STATUS_UNSTABLE, datetime_of_unstable_build)
    build_dto_successfull = BuildDto(124, STATUS_SUCCESS, datetime_of_successfull_build)
    expected_fail_time = TimeInterval(datetime_of_unstable_build, datetime_of_successfull_build)
    
    result = build_service.get_list_of_fail_times_from_builds([build_dto_unsuccessfull, build_dto_successfull])
    
    assert result != None
    assert len(result) == 1
    assert expected_fail_time.get_start() == result[0].get_start()
    assert expected_fail_time.get_end() == result[0].get_end()

def test_two_unstable_in_row_and_successfull_builds(): 
    datetime_of_unstable_build1 = datetime(2020, 1, 1, 0, 30)
    datetime_of_unstable_build2 = datetime(2020, 1, 1, 4, 30)
    datetime_of_successfull_build = datetime(2020, 1, 1, 14, 30)    
    build_dto_unsuccessfull1 = BuildDto(123, STATUS_UNSTABLE, datetime_of_unstable_build1)
    build_dto_unsuccessfull2 = BuildDto(124, STATUS_UNSTABLE, datetime_of_unstable_build2)
    build_dto_successfull = BuildDto(125, STATUS_SUCCESS, datetime_of_successfull_build)
    expected_fail_time = TimeInterval(datetime_of_unstable_build1, datetime_of_successfull_build)
    
    result = build_service.get_list_of_fail_times_from_builds([build_dto_unsuccessfull1, build_dto_unsuccessfull2, build_dto_successfull])
    
    assert result != None
    assert len(result) == 1
    assert expected_fail_time.get_start() == result[0].get_start()
    assert expected_fail_time.get_end() == result[0].get_end()

def test_two_unstable_and_successfull_alternating_builds(): 
    datetime_of_unstable_build1 = datetime(2020, 1, 1, 0, 30)
    datetime_of_successfull_build = datetime(2020, 1, 1, 14, 30)    
    datetime_of_unstable_build2 = datetime(2020, 1, 1, 15, 00)
    next_day = datetime.combine(datetime_of_unstable_build1.date() + timedelta(days=1), datetime.min.time())
    build_service.get_datetime_today  = mock.MagicMock(return_value=next_day)    
    build_dto_unsuccessfull1 = BuildDto(123, STATUS_UNSTABLE, datetime_of_unstable_build1)
    build_dto_successfull = BuildDto(124, STATUS_SUCCESS, datetime_of_successfull_build)
    build_dto_unsuccessfull2 = BuildDto(125, STATUS_UNSTABLE, datetime_of_unstable_build2)
        
    result = build_service.get_list_of_fail_times_from_builds([build_dto_unsuccessfull1, build_dto_successfull, build_dto_unsuccessfull2])
    
    expected_fail_time1 = TimeInterval(datetime_of_unstable_build1, datetime_of_successfull_build)
    expected_fail_time2 = TimeInterval(datetime_of_unstable_build2, next_day)
    assert result != None
    assert len(result) == 2
    assert expected_fail_time1.get_start() == result[0].get_start()
    assert expected_fail_time1.get_end() == result[0].get_end()    
    assert expected_fail_time2.get_start() == result[1].get_start()
    assert expected_fail_time2.get_end() == result[1].get_end()      

def test_unstable_failure_and_successfull_alternating_builds(): 
    datetime_of_unstable_build = datetime(2020, 1, 1, 0, 30)
    datetime_of_successfull_build = datetime(2020, 1, 1, 14, 30)    
    datetime_of_failed_build = datetime(2020, 1, 1, 15, 00)
    next_day = datetime.combine(datetime_of_unstable_build.date() + timedelta(days=1), datetime.min.time())
    build_service.get_datetime_today  = mock.MagicMock(return_value=next_day)    
    build_dto_unsuccessfull1 = BuildDto(123, STATUS_UNSTABLE, datetime_of_unstable_build)
    build_dto_successfull = BuildDto(124, STATUS_SUCCESS, datetime_of_successfull_build)
    build_dto_unsuccessfull2 = BuildDto(125, STATUS_FAILURE, datetime_of_failed_build)
        
    result = build_service.get_list_of_fail_times_from_builds([build_dto_unsuccessfull1, build_dto_successfull, build_dto_unsuccessfull2])
    
    expected_fail_time1 = TimeInterval(datetime_of_unstable_build, datetime_of_successfull_build)
    expected_fail_time2 = TimeInterval(datetime_of_failed_build, next_day)
    assert result != None
    assert len(result) == 2
    assert expected_fail_time1.get_start() == result[0].get_start()
    assert expected_fail_time1.get_end() == result[0].get_end()    
    assert expected_fail_time2.get_start() == result[1].get_start()
    assert expected_fail_time2.get_end() == result[1].get_end()      