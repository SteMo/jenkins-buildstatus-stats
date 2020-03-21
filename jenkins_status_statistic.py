"""
How to get build from job and query that build
"""
from __future__ import print_function
from jenkinsapi.jenkins import Jenkins
import sys



def connect_to_jenkins(url):
    print("Script start")
    
    jenkins = Jenkins('http://localhost:8080', sys.argv[1], sys.argv[2])
    # Print all jobs in Jenkins
    
    view = jenkins.get_view_by_url(url)

    for job in view.keys():
        print("Job: " + job)
        buildNumberList = getBuildNumbersToJob("Fahrzeug-Server", jenkins)
        for buildNumber in buildNumberList:
            print("Buildnumber: " + str(buildNumber))
            buildjob = getBuildJobInfo(buildNumber, "Fahrzeug-Server", jenkins)

    print("Script end")
    return view

    """ 
        TODO Tabelle aufbauen: Jobname | Buildnummer | Timestamp | Result
        Diese Tabelle dann durchgehen und die Stunden abrufen
     """

def getBuildNumbersToJob(job, jenkins):
    job = jenkins.get_job(job)
    return job.get_build_ids()
#viewJobs = view.get_job_dict()

def getBuildJobInfo(buildNumber, job, jenkins):
    job = jenkins.get_job(job)   
    build = job.get_build(buildNumber) 
    return build
""" 
def getUnstableHoursForJobAtDate(job, testDate):
    job = jenkins.get_job(job)
    buildNumberList = getBuildNumbersToJob("Fahrzeug-Server", jenkins)
    for buildNumber in buildNumberList:
        build = job.get_build(buildNumber) 
        dateFromTimestamp = getDatetimeFromTimestamp(build.get_timestamp()/1000)
        testDatetime = datetime.combine(testDate+1, datetime.min.time())
        if dateFromTimestamp.date() == testDate and build.get_status() == "UNSTABLE":
            return testDatetime - testDatedateFromTimestamp                            
    return 0 

def getDatetimeFromTimestamp():
    return datetime.fromtimestamp(1000/1000)
"""

# executed if you run the file, not when you import the file.
if __name__ == '__main__':
    connect_to_jenkins("")
    arguments = len(sys.argv) - 1
    print("Called Script with " + str(arguments) + " Parameters. First: " + sys.argv[1])