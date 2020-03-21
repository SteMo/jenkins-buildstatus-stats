from __future__ import print_function

from job_dto import JobDto
from build_dto import BuildDto

from jenkinsapi.jenkins import Jenkins
from jenkinsapi.view import View
from jenkinsapi.job import Job
from jenkinsapi.build import Build
import sys



def connect_to_jenkins(url):
    return Jenkins

def get_job_by_name(jenkins, jobname):
    return jenkins.get_job(jobname)    

def get_builds_from_build_ids(job:Job, build_id_list):
    build_dto_list = []    
    for build_id in build_id_list:
        print("Build id " + str(build_id))
        build = job.get_build(build_id)  
        build_dto = BuildDto(build.get_number(), build.get_status(), build.get_timestamp())
        build_dto_list.append(build_dto)
    return JobDto(job.name, build_dto_list)


# executed if you run the file, not when you import the file.
if __name__ == '__main__':
    connect_to_jenkins("")
    arguments = len(sys.argv) - 1
    print("Called Script with " + str(arguments) + " Parameters. First: " + sys.argv[1])