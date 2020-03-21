import mock
import pytest

import query_a_build

from jenkinsapi.jenkinsbase import JenkinsBase
from jenkinsapi.jenkins import Jenkins
from jenkinsapi.view import View
from jenkinsapi.job import Job
from jenkinsapi.build import Build
from datetime import datetime
from datetime import timezone

JENKINS_DATA = {
  "_class" : "hudson.model.Hudson",
  "assignedLabels" : [
    {
      "name" : "master"
    }
  ],
  "mode" : "EXCLUSIVE",
  "nodeDescription" : "Jenkins Master-Knoten",
  "nodeName" : "",
  "numExecutors" : 0,
  "description" : None,
  "jobs" : [
    {
      "_class" : "org.jenkinsci.plugins.workflow.job.WorkflowJob",
      "name" : "0_ModularizedControlRelease",
      "url" : "http://localhost:800/job/0_ModularizedControlRelease/",
      "color" : "red"
    },
    {
      "_class" : "org.jenkinsci.plugins.workflow.job.WorkflowJob",
      "name" : "1_ReleasePipelineModular",
      "url" : "http://localhost:800/job/1_ReleasePipelineModular/",
      "color" : "blue"
    },
    {
      "_class" : "org.jenkinsci.plugins.workflow.job.WorkflowJob",
      "name" : "1Upstream",
      "url" : "http://localhost:800/job/1Upstream/",
      "color" : "blue"
    },
    {
      "_class" : "org.jenkinsci.plugins.workflow.job.WorkflowJob",
      "name" : "2_IncreaseVersions",
      "url" : "http://localhost:800/job/2_IncreaseVersions/",
      "color" : "blue"
    },
    {
      "_class" : "org.jenkinsci.plugins.workflow.job.WorkflowJob",
      "name" : "2Downstream",
      "url" : "http://localhost:800/job/2Downstream/",
      "color" : "red"
    },
    {
      "_class" : "org.jenkinsci.plugins.workflow.job.WorkflowJob",
      "name" : "Akzeptanztests",
      "url" : "http://localhost:800/job/Akzeptanztests/",
      "color" : "yellow"
    },
    {
      "_class" : "org.jenkinsci.plugins.workflow.job.WorkflowJob",
      "name" : "Akzeptanztests-Feature-Branch",
      "url" : "http://localhost:800/job/Akzeptanztests-Feature-Branch/",
      "color" : "yellow"
    },
    {
      "_class" : "org.jenkinsci.plugins.workflow.job.WorkflowJob",
      "name" : "Analyse_Whitesource-Audit",
      "url" : "http://localhost:800/job/Analyse_Whitesource-Audit/",
      "color" : "blue"
    },
    {
      "_class" : "org.jenkinsci.plugins.workflow.job.WorkflowJob",
      "name" : "Bridge-fis-neu",
      "url" : "http://localhost:800/job/Bridge-fis-neu/",
      "color" : "blue"
    },
    {
      "_class" : "org.jenkinsci.plugins.workflow.job.WorkflowJob",
      "name" : "Bridge-fis-neu-Feature-Branch",
      "url" : "http://localhost:800/job/Bridge-fis-neu-Feature-Branch/",
      "color" : "red"
    },
    {
      "_class" : "org.jenkinsci.plugins.workflow.job.WorkflowJob",
      "name" : "Build Documentation",
      "url" : "http://localhost:800/job/Build%20Documentation/",
      "color" : "blue"
    },
    {
      "_class" : "org.jenkinsci.plugins.workflow.job.WorkflowJob",
      "name" : "commons-Feature-Branch",
      "url" : "http://localhost:800/job/commons-Feature-Branch/",
      "color" : "blue"
    },
    {
      "_class" : "org.jenkinsci.plugins.workflow.job.WorkflowJob",
      "name" : "DEPLOY ALL",
      "url" : "http://localhost:800/job/DEPLOY%20ALL/",
      "color" : "blue"
    },
    {
      "_class" : "org.jenkinsci.plugins.workflow.job.WorkflowJob",
      "name" : "DEPLOY ALL-Feature Tomcat9",
      "url" : "http://localhost:800/job/DEPLOY%20ALL-Feature%20Tomcat9/",
      "color" : "blue"
    },
    {
      "_class" : "org.jenkinsci.plugins.workflow.job.WorkflowJob",
      "name" : "DEPLOY Fahrzeug-Server",
      "url" : "http://localhost:800/job/DEPLOY%20Fahrzeug-Server/",
      "color" : "disabled"
    },
    {
      "_class" : "org.jenkinsci.plugins.workflow.job.WorkflowJob",
      "name" : "DEPLOY Fahrzeug-Server-Feature",
      "url" : "http://localhost:800/job/DEPLOY%20Fahrzeug-Server-Feature/",
      "color" : "disabled"
    },
    {
      "_class" : "org.jenkinsci.plugins.workflow.job.WorkflowJob",
      "name" : "DEPLOY mgw-sender",
      "url" : "http://localhost:800/job/DEPLOY%20mgw-sender/",
      "color" : "disabled"
    },
    {
      "_class" : "org.jenkinsci.plugins.workflow.job.WorkflowJob",
      "name" : "DEPLOY Service-Einbuchung",
      "url" : "http://localhost:800/job/DEPLOY%20Service-Einbuchung/",
      "color" : "disabled"
    },
    {
      "_class" : "org.jenkinsci.plugins.workflow.job.WorkflowJob",
      "name" : "DEPLOY Service-Einbuchung-Feature",
      "url" : "http://localhost:800/job/DEPLOY%20Service-Einbuchung-Feature/",
      "color" : "disabled"
    },
    {
      "_class" : "org.jenkinsci.plugins.workflow.job.WorkflowJob",
      "name" : "Deploy_To_Server",
      "url" : "http://localhost:800/job/Deploy_To_Server/",
      "color" : "blue"
    },
    {
      "_class" : "org.jenkinsci.plugins.workflow.job.WorkflowJob",
      "name" : "docker_test",
      "url" : "http://localhost:800/job/docker_test/",
      "color" : "blue"
    },
    {
      "_class" : "org.jenkinsci.plugins.workflow.job.WorkflowJob",
      "name" : "Experimentation",
      "url" : "http://localhost:800/job/Experimentation/",
      "color" : "red"
    },
    {
      "_class" : "org.jenkinsci.plugins.workflow.job.WorkflowJob",
      "name" : "Fahrzeug-Server",
      "url" : "http://localhost:800/job/Fahrzeug-Server/",
      "color" : "yellow"
    },
    {
      "_class" : "org.jenkinsci.plugins.workflow.job.WorkflowJob",
      "name" : "Fahrzeug-Server-Feature-Branch",
      "url" : "http://localhost:800/job/Fahrzeug-Server-Feature-Branch/",
      "color" : "yellow"
    },
    {
      "_class" : "org.jenkinsci.plugins.workflow.job.WorkflowJob",
      "name" : "Fahrzeug-Server-Templates",
      "url" : "http://localhost:800/job/Fahrzeug-Server-Templates/",
      "color" : "blue"
    },
    {
      "_class" : "org.jenkinsci.plugins.workflow.job.WorkflowJob",
      "name" : "Fahrzeug-Server-Templates-ConfigBranch",
      "url" : "http://localhost:800/job/Fahrzeug-Server-Templates-ConfigBranch/",
      "color" : "blue"
    },
    {
      "_class" : "org.jenkinsci.plugins.workflow.job.WorkflowJob",
      "name" : "Fahrzeug-Server-Templates-FeatureBranch",
      "url" : "http://localhost:800/job/Fahrzeug-Server-Templates-FeatureBranch/",
      "color" : "blue"
    },
    {
      "_class" : "org.jenkinsci.plugins.workflow.job.WorkflowJob",
      "name" : "Fahrzeug-Server-Templates-Production",
      "url" : "http://localhost:800/job/Fahrzeug-Server-Templates-Production/",
      "color" : "blue"
    },
    {
      "_class" : "hudson.model.FreeStyleProject",
      "name" : "FIS-DV-Branch-Build",
      "url" : "http://localhost:800/job/FIS-DV-Branch-Build/",
      "color" : "disabled"
    },
    {
      "_class" : "hudson.model.FreeStyleProject",
      "name" : "FIS-DV-Install-Deployment",
      "url" : "http://localhost:800/job/FIS-DV-Install-Deployment/",
      "color" : "disabled"
    },
    {
      "_class" : "hudson.model.FreeStyleProject",
      "name" : "FIS-DV-Release",
      "url" : "http://localhost:800/job/FIS-DV-Release/",
      "color" : "disabled"
    },
    {
      "_class" : "hudson.model.FreeStyleProject",
      "name" : "FIS-DV-SonarQubePZ",
      "url" : "http://localhost:800/job/FIS-DV-SonarQubePZ/",
      "color" : "disabled"
    },
    {
      "_class" : "hudson.model.FreeStyleProject",
      "name" : "FIS-DV-Testsuite",
      "url" : "http://localhost:800/job/FIS-DV-Testsuite/",
      "color" : "disabled"
    },
    {
      "_class" : "hudson.model.FreeStyleProject",
      "name" : "FIS-DV-WhiteSource",
      "url" : "http://localhost:800/job/FIS-DV-WhiteSource/",
      "color" : "disabled"
    },
    {
      "_class" : "org.jenkinsci.plugins.workflow.job.WorkflowJob",
      "name" : "ParallelTestExecution(SEB)",
      "url" : "http://localhost:800/job/ParallelTestExecution(SEB)/",
      "color" : "yellow"
    },
    {
      "_class" : "hudson.model.FreeStyleProject",
      "name" : "Periodical Jenkins WS Cleanup",
      "url" : "http://localhost:800/job/Periodical%20Jenkins%20WS%20Cleanup/",
      "color" : "blue"
    },
    {
      "_class" : "org.jenkinsci.plugins.workflow.job.WorkflowJob",
      "name" : "Release-Feature-Branch",
      "url" : "http://localhost:800/job/Release-Feature-Branch/",
      "color" : "blue"
    },
    {
      "_class" : "org.jenkinsci.plugins.workflow.job.WorkflowJob",
      "name" : "ReleaseAndPublishArtifacts",
      "url" : "http://localhost:800/job/ReleaseAndPublishArtifacts/",
      "color" : "disabled"
    },
    {
      "_class" : "org.jenkinsci.plugins.workflow.job.WorkflowJob",
      "name" : "ReleasePipeline_Standalone",
      "url" : "http://localhost:800/job/ReleasePipeline_Standalone/",
      "color" : "blue"
    },
    {
      "_class" : "org.jenkinsci.plugins.workflow.multibranch.WorkflowMultiBranchProject",
      "name" : "RIBOF Fahrzeugserver Multibranch",
      "url" : "http://localhost:800/job/RIBOF%20Fahrzeugserver%20Multibranch/"
    },
    {
      "_class" : "org.jenkinsci.plugins.workflow.job.WorkflowJob",
      "name" : "Run-All-Feature-Branches-(Cloud-Projects)",
      "url" : "http://localhost:800/job/Run-All-Feature-Branches-(Cloud-Projects)/",
      "color" : "blue"
    },
    {
      "_class" : "org.jenkinsci.plugins.workflow.job.WorkflowJob",
      "name" : "Run-All-Feature-Branches-(OnPremise-Projects)",
      "url" : "http://localhost:800/job/Run-All-Feature-Branches-(OnPremise-Projects)/",
      "color" : "blue"
    },
    {
      "_class" : "org.jenkinsci.plugins.workflow.job.WorkflowJob",
      "name" : "Service-Einbuchung",
      "url" : "http://localhost:800/job/Service-Einbuchung/",
      "color" : "blue"
    },
    {
      "_class" : "org.jenkinsci.plugins.workflow.job.WorkflowJob",
      "name" : "Service-Einbuchung-Feature-Branch",
      "url" : "http://localhost:800/job/Service-Einbuchung-Feature-Branch/",
      "color" : "blue"
    },
    {
      "_class" : "org.jenkinsci.plugins.workflow.job.WorkflowJob",
      "name" : "Service-Einbuchung-Migrationstest",
      "url" : "http://localhost:800/job/Service-Einbuchung-Migrationstest/",
      "color" : "red"
    },
    {
      "_class" : "org.jenkinsci.plugins.workflow.job.WorkflowJob",
      "name" : "Service-Fahrplan",
      "url" : "http://localhost:800/job/Service-Fahrplan/",
      "color" : "red"
    },
    {
      "_class" : "org.jenkinsci.plugins.workflow.job.WorkflowJob",
      "name" : "Service-Fahrtverlauf",
      "url" : "http://localhost:800/job/Service-Fahrtverlauf/",
      "color" : "blue"
    },
    {
      "_class" : "hudson.model.FreeStyleProject",
      "name" : "Service-Fahrtverlauf Deployment",
      "url" : "http://localhost:800/job/Service-Fahrtverlauf%20Deployment/",
      "color" : "blue"
    },
    {
      "_class" : "org.jenkinsci.plugins.workflow.job.WorkflowJob",
      "name" : "Service-Fahrtverlauf-Feature-Branch",
      "url" : "http://localhost:800/job/Service-Fahrtverlauf-Feature-Branch/",
      "color" : "blue"
    },
    {
      "_class" : "org.jenkinsci.plugins.workflow.job.WorkflowJob",
      "name" : "Service-FisDv",
      "url" : "http://localhost:800/job/Service-FisDv/",
      "color" : "blue"
    },
    {
      "_class" : "hudson.model.FreeStyleProject",
      "name" : "Service-FisDv Deployment",
      "url" : "http://localhost:800/job/Service-FisDv%20Deployment/",
      "color" : "blue"
    },
    {
      "_class" : "org.jenkinsci.plugins.workflow.job.WorkflowJob",
      "name" : "Service-FisDv-Feature-Branch",
      "url" : "http://localhost:800/job/Service-FisDv-Feature-Branch/",
      "color" : "blue"
    },
    {
      "_class" : "org.jenkinsci.plugins.workflow.job.WorkflowJob",
      "name" : "Service-MGW",
      "url" : "http://localhost:800/job/Service-MGW/",
      "color" : "blue"
    },
    {
      "_class" : "hudson.model.FreeStyleProject",
      "name" : "Service-MGW Deployment",
      "url" : "http://localhost:800/job/Service-MGW%20Deployment/",
      "color" : "blue"
    },
    {
      "_class" : "org.jenkinsci.plugins.workflow.job.WorkflowJob",
      "name" : "Service-MGW-Feature-Branch",
      "url" : "http://localhost:800/job/Service-MGW-Feature-Branch/",
      "color" : "blue"
    },
    {
      "_class" : "org.jenkinsci.plugins.workflow.job.WorkflowJob",
      "name" : "Service-Reisendeninformation",
      "url" : "http://localhost:800/job/Service-Reisendeninformation/",
      "color" : "blue"
    },
    {
      "_class" : "org.jenkinsci.plugins.workflow.job.WorkflowJob",
      "name" : "SharedGlobalLibTest",
      "url" : "http://localhost:800/job/SharedGlobalLibTest/",
      "color" : "blue"
    },
    {
      "_class" : "hudson.model.FreeStyleProject",
      "name" : "ShellPlayground",
      "url" : "http://localhost:800/job/ShellPlayground/",
      "color" : "blue"
    },
    {
      "_class" : "hudson.model.FreeStyleProject",
      "name" : "Smoketest EU Instanz3",
      "url" : "http://localhost:800/job/Smoketest%20EU%20Instanz3/",
      "color" : "disabled"
    },
    {
      "_class" : "org.jenkinsci.plugins.workflow.job.WorkflowJob",
      "name" : "Smoketest(Pipeline) EU Instanz3",
      "url" : "http://localhost:800/job/Smoketest(Pipeline)%20EU%20Instanz3/",
      "color" : "disabled"
    },
    {
      "_class" : "org.jenkinsci.plugins.workflow.job.WorkflowJob",
      "name" : "Sonderzuege",
      "url" : "http://localhost:800/job/Sonderzuege/",
      "color" : "yellow"
    },
    {
      "_class" : "org.jenkinsci.plugins.workflow.job.WorkflowJob",
      "name" : "temp",
      "url" : "http://localhost:800/job/temp/",
      "color" : "disabled"
    },
    {
      "_class" : "hudson.model.FreeStyleProject",
      "name" : "WhiteSource Test",
      "url" : "http://localhost:800/job/WhiteSource%20Test/",
      "color" : "notbuilt"
    },
    {
      "_class" : "org.jenkinsci.plugins.workflow.job.WorkflowJob",
      "name" : "Zug-Simulator",
      "url" : "http://localhost:800/job/Zug-Simulator/",
      "color" : "blue"
    },
    {
      "_class" : "org.jenkinsci.plugins.workflow.job.WorkflowJob",
      "name" : "Zug-Template-Tests",
      "url" : "http://localhost:800/job/Zug-Template-Tests/",
      "color" : "blue"
    },
    {
      "_class" : "org.jenkinsci.plugins.workflow.job.WorkflowJob",
      "name" : "Zug-Template-Tests-Feature-Branch",
      "url" : "http://localhost:800/job/Zug-Template-Tests-Feature-Branch/",
      "color" : "blue"
    },
    {
      "_class" : "org.jenkinsci.plugins.workflow.job.WorkflowJob",
      "name" : "Zug-Template-Tests-Feature-Branch_Single",
      "url" : "http://localhost:800/job/Zug-Template-Tests-Feature-Branch_Single/",
      "color" : "blue"
    },
    {
      "_class" : "org.jenkinsci.plugins.workflow.job.WorkflowJob",
      "name" : "Zug-Templates",
      "url" : "http://localhost:800/job/Zug-Templates/",
      "color" : "blue"
    },
    {
      "_class" : "org.jenkinsci.plugins.workflow.job.WorkflowJob",
      "name" : "Zug-Templates-Developer-Build-4ZSIM",
      "url" : "http://localhost:800/job/Zug-Templates-Developer-Build-4ZSIM/",
      "color" : "blue"
    },
    {
      "_class" : "org.jenkinsci.plugins.workflow.job.WorkflowJob",
      "name" : "Zug-Templates-Feature-Branch",
      "url" : "http://localhost:800/job/Zug-Templates-Feature-Branch/",
      "color" : "blue"
    },
    {
      "_class" : "org.jenkinsci.plugins.workflow.job.WorkflowJob",
      "name" : "Zug-Templates-Release",
      "url" : "http://localhost:800/job/Zug-Templates-Release/",
      "color" : "red"
    }
  ],
  "overallLoad" : {
    
  },
  "primaryView" : {
    "_class" : "hudson.model.AllView",
    "name" : "all",
    "url" : "http://localhost:800/"
  },
  "quietingDown" : False,
  "slaveAgentPort" : 50000,
  "unlabeledLoad" : {
    "_class" : "jenkins.model.UnlabeledLoadStatistics"
  },
  "useCrumbs" : True,
  "useSecurity" : True,
  "views" : [
    {
      "_class" : "hudson.model.ListView",
      "name" : "Buildampel",
      "url" : "http://localhost:800/view/Buildampel/"
    },
    {
      "_class" : "hudson.model.ListView",
      "name" : "Cloud",
      "url" : "http://localhost:800/view/Cloud/"
    },
    {
      "_class" : "hudson.plugins.view.dashboard.Dashboard",
      "name" : "Dashboard",
      "url" : "http://localhost:800/view/Dashboard/"
    },
    {
      "_class" : "hudson.plugins.view.dashboard.Dashboard",
      "name" : "FIS-DV",
      "url" : "http://localhost:800/view/FIS-DV/"
    },
    {
      "_class" : "hudson.plugins.view.dashboard.Dashboard",
      "name" : "FIS-DV-Dashboard",
      "url" : "http://localhost:800/view/FIS-DV-Dashboard/"
    },
    {
      "_class" : "hudson.model.ListView",
      "name" : "Fahrzeug-Server",
      "url" : "http://localhost:800/view/Fahrzeug-Server/"
    },
    {
      "_class" : "se.diabol.jenkins.workflow.WorkflowPipelineView",
      "name" : "Pipelines",
      "url" : "http://localhost:800/view/Pipelines/"
    },
    {
      "_class" : "hudson.model.ListView",
      "name" : "Release",
      "url" : "http://localhost:800/view/Release/"
    },
    {
      "_class" : "hudson.model.ListView",
      "name" : "Service-EB",
      "url" : "http://localhost:800/view/Service-EB/"
    },
    {
      "_class" : "hudson.model.ListView",
      "name" : "Templates",
      "url" : "http://localhost:800/view/Templates/"
    },
    {
      "_class" : "hudson.model.ListView",
      "name" : "Test",
      "url" : "http://localhost:800/view/Test/"
    },
    {
      "_class" : "hudson.model.AllView",
      "name" : "all",
      "url" : "http://localhost:800/"
    }
  ]
}

VIEW_DATA = {
  "_class" : "hudson.model.ListView",
  "description" : None,
  "jobs" : [
    {
      "_class" : "org.jenkinsci.plugins.workflow.job.WorkflowJob",
      "name" : "Bridge-fis-neu",
      "url" : "http://localhost:800/job/Bridge-fis-neu/",
      "color" : "blue"
    },
    {
      "_class" : "org.jenkinsci.plugins.workflow.job.WorkflowJob",
      "name" : "Fahrzeug-Server",
      "url" : "http://localhost:800/job/Fahrzeug-Server/",
      "color" : "yellow"
    },
    {
      "_class" : "org.jenkinsci.plugins.workflow.job.WorkflowJob",
      "name" : "Fahrzeug-Server-Templates",
      "url" : "http://localhost:800/job/Fahrzeug-Server-Templates/",
      "color" : "blue"
    },
    {
      "_class" : "org.jenkinsci.plugins.workflow.job.WorkflowJob",
      "name" : "Service-Einbuchung",
      "url" : "http://localhost:800/job/Service-Einbuchung/",
      "color" : "blue"
    },
    {
      "_class" : "org.jenkinsci.plugins.workflow.job.WorkflowJob",
      "name" : "Service-Fahrtverlauf",
      "url" : "http://localhost:800/job/Service-Fahrtverlauf/",
      "color" : "blue"
    },
    {
      "_class" : "org.jenkinsci.plugins.workflow.job.WorkflowJob",
      "name" : "Service-FisDv",
      "url" : "http://localhost:800/job/Service-FisDv/",
      "color" : "blue"
    },
    {
      "_class" : "org.jenkinsci.plugins.workflow.job.WorkflowJob",
      "name" : "Service-MGW",
      "url" : "http://localhost:800/job/Service-MGW/",
      "color" : "blue"
    },
    {
      "_class" : "org.jenkinsci.plugins.workflow.job.WorkflowJob",
      "name" : "Service-Reisendeninformation",
      "url" : "http://localhost:800/job/Service-Reisendeninformation/",
      "color" : "blue"
    },
    {
      "_class" : "org.jenkinsci.plugins.workflow.job.WorkflowJob",
      "name" : "Zug-Template-Tests",
      "url" : "http://localhost:800/job/Zug-Template-Tests/",
      "color" : "blue"
    },
    {
      "_class" : "org.jenkinsci.plugins.workflow.job.WorkflowJob",
      "name" : "Zug-Templates",
      "url" : "http://localhost:800/job/Zug-Templates/",
      "color" : "blue"
    }
  ],
  "name" : "Buildampel",
  "property" : [
    
  ],
  "url" : "http://localhost:800/view/Buildampel/"
}

JOB_DATA = {
  "_class" : "org.jenkinsci.plugins.workflow.job.WorkflowJob",
  "actions" : [
    {
      
    },
    {
      
    },
    {
      
    },
    {
      
    },
    {
      
    },
    {
      
    },
    {
      
    },
    {
      
    },
    {
      
    },
    {
      
    },
    {
      
    },
    {
      
    },
    {
      
    },
    {
      
    },
    {
      "_class" : "org.jenkinsci.plugins.testresultsanalyzer.TestResultsAnalyzerAction"
    },
    {
      
    },
    {
      "_class" : "com.cloudbees.plugins.credentials.ViewCredentialsAction"
    }
  ],
  "description" : "",
  "displayName" : "Fahrzeug-Server",
  "displayNameOrNull" : None,
  "fullDisplayName" : "Fahrzeug-Server",
  "fullName" : "Fahrzeug-Server",
  "name" : "Fahrzeug-Server",
  "url" : "http://localhost:800/view/Buildampel/job/Fahrzeug-Server/",
  "buildable" : True,
  "builds" : [
    {
      "_class" : "org.jenkinsci.plugins.workflow.job.WorkflowRun",
      "number" : 3123,
      "url" : "http://localhost:800/view/Buildampel/job/Fahrzeug-Server/3123/"
    },
    {
      "_class" : "org.jenkinsci.plugins.workflow.job.WorkflowRun",
      "number" : 3122,
      "url" : "http://localhost:800/view/Buildampel/job/Fahrzeug-Server/3122/"
    },
    {
      "_class" : "org.jenkinsci.plugins.workflow.job.WorkflowRun",
      "number" : 3121,
      "url" : "http://localhost:800/view/Buildampel/job/Fahrzeug-Server/3121/"
    },
    {
      "_class" : "org.jenkinsci.plugins.workflow.job.WorkflowRun",
      "number" : 3120,
      "url" : "http://localhost:800/view/Buildampel/job/Fahrzeug-Server/3120/"
    },
    {
      "_class" : "org.jenkinsci.plugins.workflow.job.WorkflowRun",
      "number" : 3119,
      "url" : "http://localhost:800/view/Buildampel/job/Fahrzeug-Server/3119/"
    },
    {
      "_class" : "org.jenkinsci.plugins.workflow.job.WorkflowRun",
      "number" : 3112,
      "url" : "http://localhost:800/view/Buildampel/job/Fahrzeug-Server/3112/"
    }
  ],
  "color" : "yellow",
  "firstBuild" : {
    "_class" : "org.jenkinsci.plugins.workflow.job.WorkflowRun",
    "number" : 3112,
    "url" : "http://localhost:800/view/Buildampel/job/Fahrzeug-Server/3112/"
  },
  "healthReport" : [
    {
      "description" : "Testergebnis: 9 Tests von 1,040 Tests fehlgeschlagen.",
      "iconClassName" : "icon-health-80plus",
      "iconUrl" : "health-80plus.png",
      "score" : 99
    },
    {
      "description" : "Testabdeckung: Alle Testabdeckungsziele wurden erreicht.    ",
      "iconClassName" : "icon-health-80plus",
      "iconUrl" : "health-80plus.png",
      "score" : 100
    },
    {
      "description" : "Build-Stabilität: In letzter Zeit schlug kein Build fehl.",
      "iconClassName" : "icon-health-80plus",
      "iconUrl" : "health-80plus.png",
      "score" : 100
    }
  ],
  "inQueue" : False,
  "keepDependencies" : False,
  "lastBuild" : {
    "_class" : "org.jenkinsci.plugins.workflow.job.WorkflowRun",
    "number" : 3123,
    "url" : "http://localhost:800/view/Buildampel/job/Fahrzeug-Server/3123/"
  },
  "lastCompletedBuild" : {
    "_class" : "org.jenkinsci.plugins.workflow.job.WorkflowRun",
    "number" : 3123,
    "url" : "http://localhost:800/view/Buildampel/job/Fahrzeug-Server/3123/"
  },
  "lastFailedBuild" : None,
  "lastStableBuild" : {
    "_class" : "org.jenkinsci.plugins.workflow.job.WorkflowRun",
    "number" : 3112,
    "url" : "http://localhost:800/view/Buildampel/job/Fahrzeug-Server/3112/"
  },
  "lastSuccessfulBuild" : {
    "_class" : "org.jenkinsci.plugins.workflow.job.WorkflowRun",
    "number" : 3123,
    "url" : "http://localhost:800/view/Buildampel/job/Fahrzeug-Server/3123/"
  },
  "lastUnstableBuild" : {
    "_class" : "org.jenkinsci.plugins.workflow.job.WorkflowRun",
    "number" : 3123,
    "url" : "http://localhost:800/view/Buildampel/job/Fahrzeug-Server/3123/"
  },
  "lastUnsuccessfulBuild" : {
    "_class" : "org.jenkinsci.plugins.workflow.job.WorkflowRun",
    "number" : 3123,
    "url" : "http://localhost:800/view/Buildampel/job/Fahrzeug-Server/3123/"
  },
  "nextBuildNumber" : 3124,
  "property" : [
    {
      "_class" : "org.jenkinsci.plugins.workflow.job.properties.PipelineTriggersJobProperty"
    },
    {
      "_class" : "hudson.model.ParametersDefinitionProperty",
      "parameterDefinitions" : [
        {
          "_class" : "hudson.model.BooleanParameterDefinition",
          "defaultParameterValue" : {
            "_class" : "hudson.model.BooleanParameterValue",
            "name" : "performSmokeTests",
            "value" : False
          },
          "description" : "true=execute smoke tests (no tests yet)",
          "name" : "performSmokeTests",
          "type" : "BooleanParameterDefinition"
        },
        {
          "_class" : "hudson.model.BooleanParameterDefinition",
          "defaultParameterValue" : {
            "_class" : "hudson.model.BooleanParameterValue",
            "name" : "performSystemTests",
            "value" : False
          },
          "description" : "true=execute system tests (no tests yet)",
          "name" : "performSystemTests",
          "type" : "BooleanParameterDefinition"
        }
      ]
    },
    {
      "_class" : "jenkins.model.BuildDiscarderProperty"
    },
    {
      "_class" : "org.jenkinsci.plugins.workflow.job.properties.DisableConcurrentBuildsJobProperty"
    },
    {
      "_class" : "com.dabsquared.gitlabjenkins.connection.GitLabConnectionProperty"
    },
    {
      "_class" : "hudson.plugins.copyartifact.CopyArtifactPermissionProperty"
    },
    {
      "_class" : "hudson.plugins.jira.JiraProjectProperty"
    }
  ],
  "queueItem" : None,
  "concurrentBuild" : False,
  "resumeBlocked" : False
}

BUILD_DATA_FAIL = {
  "_class" : "org.jenkinsci.plugins.workflow.job.WorkflowRun",
  "actions" : [
    {
      "_class" : "hudson.model.ParametersAction",
      "parameters" : [
        {
          "_class" : "hudson.model.BooleanParameterValue",
          "name" : "performSmokeTests",
          "value" : False
        },
        {
          "_class" : "hudson.model.BooleanParameterValue",
          "name" : "performSystemTests",
          "value" : False
        }
      ]
    },
    {
      "_class" : "hudson.model.CauseAction",
      "causes" : [
        {
          "_class" : "hudson.model.Cause$UserIdCause",
          "shortDescription" : "Gestartet durch Benutzer Oliver Schwab",
          "userId" : "oschwab",
          "userName" : "Oliver Schwab"
        }
      ]
    },
    {
      
    },
    {
      "_class" : "hudson.plugins.git.util.BuildData",
      "buildsByBranchName" : {
        "master" : {
          "_class" : "hudson.plugins.git.util.Build",
          "buildNumber" : 3119,
          "buildResult" : None,
          "marked" : {
            "SHA1" : "d979e55feeaac991c635630709d83d9c60a23c68",
            "branch" : [
              {
                "SHA1" : "d979e55feeaac991c635630709d83d9c60a23c68",
                "name" : "master"
              }
            ]
          },
          "revision" : {
            "SHA1" : "d979e55feeaac991c635630709d83d9c60a23c68",
            "branch" : [
              {
                "SHA1" : "d979e55feeaac991c635630709d83d9c60a23c68",
                "name" : "master"
              }
            ]
          }
        }
      },
      "lastBuiltRevision" : {
        "SHA1" : "d979e55feeaac991c635630709d83d9c60a23c68",
        "branch" : [
          {
            "SHA1" : "d979e55feeaac991c635630709d83d9c60a23c68",
            "name" : "master"
          }
        ]
      },
      "remoteUrls" : [
        "git@ssh.git.tech.rz.db.de:PZ-RIS/ribof/ops/jenkins-shared.git"
      ],
      "scmName" : ""
    },
    {
      "_class" : "hudson.plugins.git.GitTagAction"
    },
    {
      
    },
    {
      
    },
    {
      
    },
    {
      "_class" : "hudson.plugins.git.util.BuildData",
      "buildsByBranchName" : {
        "refs/remotes/origin/develop" : {
          "_class" : "hudson.plugins.git.util.Build",
          "buildNumber" : 3119,
          "buildResult" : None,
          "marked" : {
            "SHA1" : "cd2021b6ea88a2392904cebb23c0951bbf0fe617",
            "branch" : [
              {
                "SHA1" : "cd2021b6ea88a2392904cebb23c0951bbf0fe617",
                "name" : "refs/remotes/origin/develop"
              }
            ]
          },
          "revision" : {
            "SHA1" : "cd2021b6ea88a2392904cebb23c0951bbf0fe617",
            "branch" : [
              {
                "SHA1" : "cd2021b6ea88a2392904cebb23c0951bbf0fe617",
                "name" : "refs/remotes/origin/develop"
              }
            ]
          }
        }
      },
      "lastBuiltRevision" : {
        "SHA1" : "cd2021b6ea88a2392904cebb23c0951bbf0fe617",
        "branch" : [
          {
            "SHA1" : "cd2021b6ea88a2392904cebb23c0951bbf0fe617",
            "name" : "refs/remotes/origin/develop"
          }
        ]
      },
      "remoteUrls" : [
        "git@ssh.git.tech.rz.db.de:PZ-RIS/ribof/core/backoffice_fahrzeug.git"
      ],
      "scmName" : ""
    },
    {
      
    },
    {
      
    },
    {
      
    },
    {
      
    },
    {
      "_class" : "hudson.plugins.sonar.action.SonarAnalysisAction",
      "ceTaskId" : "AXCvxgIvy1IfXWk8tfx8",
      "credentialsId" : None,
      "installationName" : "Sonar Team Fahrzeug",
      "new" : True,
      "serverUrl" : "https://sonar.reisendeninfo.aws.db.de",
      "skipped" : False,
      "sonarqubeDashboardUrl" : "https://sonar.reisendeninfo.aws.db.de/dashboard?id=tfz-ribof-fahrzeug"
    },
    {
      "_class" : "hudson.tasks.junit.TestResultAction",
      "failCount" : 9,
      "skipCount" : 0,
      "totalCount" : 1040,
      "urlName" : "testReport"
    },
    {
      "_class" : "hudson.plugins.jacoco.JacocoBuildAction"
    },
    {
      
    },
    {
      
    },
    {
      
    },
    {
      
    },
    {
      "_class" : "hudson.plugins.sonar.action.SonarBuildBadgeAction",
      "url" : "https://sonar.reisendeninfo.aws.db.de/dashboard?id=tfz-ribof-fahrzeug"
    },
    {
      
    },
    {
      
    },
    {
      
    },
    {
      "_class" : "org.jenkinsci.plugins.pipeline.modeldefinition.actions.RestartDeclarativePipelineAction"
    },
    {
      
    },
    {
      "_class" : "org.jenkinsci.plugins.workflow.job.views.FlowGraphAction"
    },
    {
      
    },
    {
      
    },
    {
      
    }
  ],
  "artifacts" : [
    
  ],
  "building" : False,
  "description" : None,
  "displayName" : "#3119",
  "duration" : 1208714,
  "estimatedDuration" : 749457,
  "executor" : None,
  "fullDisplayName" : "Fahrzeug-Server #3119",
  "id" : "3119",
  "keepLog" : False,
  "number" : 3119,
  "queueId" : 52737,
  "result" : "UNSTABLE",
  "timestamp" : 1583495750710,
  "url" : "http://localhost:800/view/Buildampel/job/Fahrzeug-Server/3119/",
  "changeSets" : [
    
  ],
  "culprits" : [
    
  ],
  "nextBuild" : {
    "number" : 3120,
    "url" : "http://localhost:800/view/Buildampel/job/Fahrzeug-Server/3120/"
  },
  "previousBuild" : {
    "number" : 3112,
    "url" : "http://localhost:800/view/Buildampel/job/Fahrzeug-Server/3112/"
  }
}

BUILD_DATA_SUCCESS = {
  "_class" : "org.jenkinsci.plugins.workflow.job.WorkflowRun",
  "actions" : [
    {
      "_class" : "hudson.model.CauseAction",
      "causes" : [
        {
          "_class" : "hudson.triggers.SCMTrigger$SCMTriggerCause",
          "shortDescription" : "Build wurde durch eine SCM-Änderung ausgelöst."
        }
      ]
    },
    {
      
    },
    {
      "_class" : "hudson.model.ParametersAction",
      "parameters" : [
        {
          "_class" : "hudson.model.BooleanParameterValue",
          "name" : "performSmokeTests",
          "value" : False
        },
        {
          "_class" : "hudson.model.BooleanParameterValue",
          "name" : "performSystemTests",
          "value" : False
        }
      ]
    },
    {
      
    },
    {
      "_class" : "hudson.plugins.git.util.BuildData",
      "buildsByBranchName" : {
        "master" : {
          "_class" : "hudson.plugins.git.util.Build",
          "buildNumber" : 3112,
          "buildResult" : None,
          "marked" : {
            "SHA1" : "d979e55feeaac991c635630709d83d9c60a23c68",
            "branch" : [
              {
                "SHA1" : "d979e55feeaac991c635630709d83d9c60a23c68",
                "name" : "master"
              }
            ]
          },
          "revision" : {
            "SHA1" : "d979e55feeaac991c635630709d83d9c60a23c68",
            "branch" : [
              {
                "SHA1" : "d979e55feeaac991c635630709d83d9c60a23c68",
                "name" : "master"
              }
            ]
          }
        }
      },
      "lastBuiltRevision" : {
        "SHA1" : "d979e55feeaac991c635630709d83d9c60a23c68",
        "branch" : [
          {
            "SHA1" : "d979e55feeaac991c635630709d83d9c60a23c68",
            "name" : "master"
          }
        ]
      },
      "remoteUrls" : [
        "git@ssh.git.tech.rz.db.de:PZ-RIS/ribof/ops/jenkins-shared.git"
      ],
      "scmName" : ""
    },
    {
      "_class" : "hudson.plugins.git.GitTagAction"
    },
    {
      
    },
    {
      
    },
    {
      
    },
    {
      "_class" : "hudson.plugins.git.util.BuildData",
      "buildsByBranchName" : {
        "refs/remotes/origin/develop" : {
          "_class" : "hudson.plugins.git.util.Build",
          "buildNumber" : 3112,
          "buildResult" : None,
          "marked" : {
            "SHA1" : "5dac1aa0c6e6cec71bd06ef7b37b11c271a57b82",
            "branch" : [
              {
                "SHA1" : "5dac1aa0c6e6cec71bd06ef7b37b11c271a57b82",
                "name" : "refs/remotes/origin/develop"
              }
            ]
          },
          "revision" : {
            "SHA1" : "5dac1aa0c6e6cec71bd06ef7b37b11c271a57b82",
            "branch" : [
              {
                "SHA1" : "5dac1aa0c6e6cec71bd06ef7b37b11c271a57b82",
                "name" : "refs/remotes/origin/develop"
              }
            ]
          }
        }
      },
      "lastBuiltRevision" : {
        "SHA1" : "5dac1aa0c6e6cec71bd06ef7b37b11c271a57b82",
        "branch" : [
          {
            "SHA1" : "5dac1aa0c6e6cec71bd06ef7b37b11c271a57b82",
            "name" : "refs/remotes/origin/develop"
          }
        ]
      },
      "remoteUrls" : [
        "git@ssh.git.tech.rz.db.de:PZ-RIS/ribof/core/backoffice_fahrzeug.git"
      ],
      "scmName" : ""
    },
    {
      
    },
    {
      
    },
    {
      
    },
    {
      
    },
    {
      "_class" : "hudson.plugins.sonar.action.SonarAnalysisAction",
      "ceTaskId" : "AXCq8rKhy1IfXWk8tfuO",
      "credentialsId" : None,
      "installationName" : "Sonar Team Fahrzeug",
      "new" : True,
      "serverUrl" : "https://sonar.reisendeninfo.aws.db.de",
      "skipped" : False,
      "sonarqubeDashboardUrl" : "https://sonar.reisendeninfo.aws.db.de/dashboard?id=tfz-ribof-fahrzeug"
    },
    {
      "_class" : "hudson.tasks.junit.TestResultAction",
      "failCount" : 0,
      "skipCount" : 0,
      "totalCount" : 1040,
      "urlName" : "testReport"
    },
    {
      "_class" : "hudson.plugins.jacoco.JacocoBuildAction"
    },
    {
      
    },
    {
      
    },
    {
      
    },
    {
      "_class" : "hudson.plugins.sonar.action.SonarBuildBadgeAction",
      "url" : "https://sonar.reisendeninfo.aws.db.de/dashboard?id=tfz-ribof-fahrzeug"
    },
    {
      
    },
    {
      
    },
    {
      
    },
    {
      "_class" : "org.jenkinsci.plugins.pipeline.modeldefinition.actions.RestartDeclarativePipelineAction"
    },
    {
      
    },
    {
      "_class" : "org.jenkinsci.plugins.workflow.job.views.FlowGraphAction"
    },
    {
      
    },
    {
      
    },
    {
      
    }
  ],
  "artifacts" : [
    {
      "displayPath" : "ris-backoffice-fahrzeug-7.8.0.0.zip",
      "fileName" : "ris-backoffice-fahrzeug-7.8.0.0.zip",
      "relativePath" : "ris-bo-fzg/fahrzeug/build/distributions/ris-backoffice-fahrzeug-7.8.0.0.zip"
    },
    {
      "displayPath" : "Tomcat-RIS-BO-Fahrzeug-7.8.0.0.tar.gz",
      "fileName" : "Tomcat-RIS-BO-Fahrzeug-7.8.0.0.tar.gz",
      "relativePath" : "ris-bo-fzg/fahrzeug/build/distributions/Tomcat-RIS-BO-Fahrzeug-7.8.0.0.tar.gz"
    },
    {
      "displayPath" : "Tomcat-RIS-BO-Fahrzeug-7.8.0.0.zip",
      "fileName" : "Tomcat-RIS-BO-Fahrzeug-7.8.0.0.zip",
      "relativePath" : "ris-bo-fzg/fahrzeug/build/distributions/Tomcat-RIS-BO-Fahrzeug-7.8.0.0.zip"
    },
    {
      "displayPath" : "Tomcat-RIS-BO-Fahrzeug-latest.tar.gz",
      "fileName" : "Tomcat-RIS-BO-Fahrzeug-latest.tar.gz",
      "relativePath" : "Tomcat-RIS-BO-Fahrzeug-latest.tar.gz"
    }
  ],
  "building" : False,
  "description" : None,
  "displayName" : "#3112",
  "duration" : 748959,
  "estimatedDuration" : 749457,
  "executor" : None,
  "fullDisplayName" : "Fahrzeug-Server #3112",
  "id" : "3112",
  "keepLog" : False,
  "number" : 3112,
  "queueId" : 52633,
  "result" : "SUCCESS",
  "timestamp" : 1583415254093,
  "url" : "http://localhost:800/view/Buildampel/job/Fahrzeug-Server/3112/",
  "changeSets" : [
    {
      "_class" : "hudson.plugins.git.GitChangeSetList",
      "items" : [
        {
          "_class" : "hudson.plugins.git.GitChangeSet",
          "affectedPaths" : [
            "fahrzeug-server-templates/build.xml"
          ],
          "commitId" : "c4b395c417cd069ca71bea36e87bdb3cc3e5752c",
          "timestamp" : 1582199884000,
          "author" : {
            "absoluteUrl" : "http://localhost:800/user/nkipper",
            "fullName" : "Nicolas Kipper"
          },
          "authorEmail" : "nicolas.kipper@deutschebahn.com",
          "comment" : "build.xml - Versionsnummer auf 7.7.0.7 erhöht\n",
          "date" : "2020-02-20 12:58:04 +0100",
          "id" : "c4b395c417cd069ca71bea36e87bdb3cc3e5752c",
          "msg" : "build.xml - Versionsnummer auf 7.7.0.7 erhöht",
          "paths" : [
            {
              "editType" : "edit",
              "file" : "fahrzeug-server-templates/build.xml"
            }
          ]
        },
        {
          "_class" : "hudson.plugins.git.GitChangeSet",
          "affectedPaths" : [
            "fahrzeug-server-templates/config/einbuchung/inventar(2)-NETZBBMVNS.vm"
          ],
          "commitId" : "5a35dc8170b174a736a8bf6f4ad7ce5d33e4ebbe",
          "timestamp" : 1582721695000,
          "author" : {
            "absoluteUrl" : "http://localhost:800/user/sschellhaas",
            "fullName" : "Steven Schellhaas"
          },
          "authorEmail" : "steven.schellhaas@deutschebahn.com",
          "comment" : "configBranch: TFZ-3898 FIS-neu: Baustelle NO NNS - RE5 - 09.03.–26.03.2020\n",
          "date" : "2020-02-26 12:54:55 +0000",
          "id" : "5a35dc8170b174a736a8bf6f4ad7ce5d33e4ebbe",
          "msg" : "configBranch: TFZ-3898 FIS-neu: Baustelle NO NNS - RE5 - 09.03.–26.03.2020",
          "paths" : [
            {
              "editType" : "edit",
              "file" : "fahrzeug-server-templates/config/einbuchung/inventar(2)-NETZBBMVNS.vm"
            }
          ]
        },
        {
          "_class" : "hudson.plugins.git.GitChangeSet",
          "affectedPaths" : [
            "fahrzeug-server-templates/config/einbuchung/inventar(2)-NETZBW3GM.vm"
          ],
          "commitId" : "a207f71840f0ae61c2289de98760b7a82450635a",
          "timestamp" : 1582809090000,
          "author" : {
            "absoluteUrl" : "http://localhost:800/user/sschellhaas",
            "fullName" : "Steven Schellhaas"
          },
          "authorEmail" : "steven.schellhaas@deutschebahn.com",
          "comment" : "configBranch: TFZ-3901 FIS-neu: Baustelle BW Teilnetz 3b (Gäu-Murr)19.03.2020 – 24.03.2020\n",
          "date" : "2020-02-27 13:11:30 +0000",
          "id" : "a207f71840f0ae61c2289de98760b7a82450635a",
          "msg" : "configBranch: TFZ-3901 FIS-neu: Baustelle BW Teilnetz 3b (Gäu-Murr)19.03.2020 – 24.03.2020",
          "paths" : [
            {
              "editType" : "edit",
              "file" : "fahrzeug-server-templates/config/einbuchung/inventar(2)-NETZBW3GM.vm"
            }
          ]
        },
        {
          "_class" : "hudson.plugins.git.GitChangeSet",
          "affectedPaths" : [
            "fahrzeug-server-templates/config/einbuchung/inventar(2)-NETZBW3GM.vm"
          ],
          "commitId" : "78e45111d7ac53e3132fef727a8df178e2ef92a9",
          "timestamp" : 1582813347000,
          "author" : {
            "absoluteUrl" : "http://localhost:800/user/sschellhaas",
            "fullName" : "Steven Schellhaas"
          },
          "authorEmail" : "steven.schellhaas@deutschebahn.com",
          "comment" : "configBranch: NETZBW3GM altes Template entfernt\n",
          "date" : "2020-02-27 14:22:27 +0000",
          "id" : "78e45111d7ac53e3132fef727a8df178e2ef92a9",
          "msg" : "configBranch: NETZBW3GM altes Template entfernt",
          "paths" : [
            {
              "editType" : "edit",
              "file" : "fahrzeug-server-templates/config/einbuchung/inventar(2)-NETZBW3GM.vm"
            }
          ]
        },
        {
          "_class" : "hudson.plugins.git.GitChangeSet",
          "affectedPaths" : [
            "fahrzeug-server-templates/config/einbuchung/inventar(1)-NETZEEN.vm"
          ],
          "commitId" : "67399bdd715eba87abd23b49486971a4899a382e",
          "timestamp" : 1583241613000,
          "author" : {
            "absoluteUrl" : "http://localhost:800/user/stefan.wegener",
            "fullName" : "Stefan.Wegener"
          },
          "authorEmail" : "Stefan.Wegener@deutschebahn.com",
          "comment" : "configBranch: TFZ-3926 FIS-neu: Baustelle NO EEN - RE15 - 09.03.–16.03.2020\n",
          "date" : "2020-03-03 14:20:13 +0100",
          "id" : "67399bdd715eba87abd23b49486971a4899a382e",
          "msg" : "configBranch: TFZ-3926 FIS-neu: Baustelle NO EEN - RE15 - 09.03.–16.03.2020",
          "paths" : [
            {
              "editType" : "edit",
              "file" : "fahrzeug-server-templates/config/einbuchung/inventar(1)-NETZEEN.vm"
            }
          ]
        },
        {
          "_class" : "hudson.plugins.git.GitChangeSet",
          "affectedPaths" : [
            "fahrzeug-server-templates/config/einbuchung/inventar(2)-NETZBW3GM.vm"
          ],
          "commitId" : "c04873193e64bbe206bc65995f16d02e87e8861c",
          "timestamp" : 1583250298000,
          "author" : {
            "absoluteUrl" : "http://localhost:800/user/sschellhaas",
            "fullName" : "Steven Schellhaas"
          },
          "authorEmail" : "steven.schellhaas@deutschebahn.com",
          "comment" : "configBranch: TFZ-3901 FIS-neu: Baustelle BW Teilnetz 3b (Gäu-Murr)19.03.2020 – 24.03.2020 - Korrektur\n",
          "date" : "2020-03-03 15:44:58 +0000",
          "id" : "c04873193e64bbe206bc65995f16d02e87e8861c",
          "msg" : "configBranch: TFZ-3901 FIS-neu: Baustelle BW Teilnetz 3b (Gäu-Murr)19.03.2020 – 24.03.2020 - Korrektur",
          "paths" : [
            {
              "editType" : "edit",
              "file" : "fahrzeug-server-templates/config/einbuchung/inventar(2)-NETZBW3GM.vm"
            }
          ]
        },
        {
          "_class" : "hudson.plugins.git.GitChangeSet",
          "affectedPaths" : [
            "fahrzeug-server-templates/config/einbuchung/inventar(2)-NETZBW3GM.vm"
          ],
          "commitId" : "b0707011404d7023dd680bc5334d17916c0218fa",
          "timestamp" : 1583251224000,
          "author" : {
            "absoluteUrl" : "http://localhost:800/user/sschellhaas",
            "fullName" : "Steven Schellhaas"
          },
          "authorEmail" : "steven.schellhaas@deutschebahn.com",
          "comment" : "configBranch: TFZ-3901 FIS-neu: Baustelle BW Teilnetz 3b (Gäu-Murr)19.03.2020 – 24.03.2020 - Korrektur 2\n",
          "date" : "2020-03-03 16:00:24 +0000",
          "id" : "b0707011404d7023dd680bc5334d17916c0218fa",
          "msg" : "configBranch: TFZ-3901 FIS-neu: Baustelle BW Teilnetz 3b (Gäu-Murr)19.03.2020 – 24.03.2020 - Korrektur 2",
          "paths" : [
            {
              "editType" : "edit",
              "file" : "fahrzeug-server-templates/config/einbuchung/inventar(2)-NETZBW3GM.vm"
            }
          ]
        },
        {
          "_class" : "hudson.plugins.git.GitChangeSet",
          "affectedPaths" : [
            "fahrzeug-server-templates/config/einbuchung/inventar(2)-NETZBW3GM.vm"
          ],
          "commitId" : "55291b59050e48cfec10bb591333c1b0dcffffbe",
          "timestamp" : 1583253779000,
          "author" : {
            "absoluteUrl" : "http://localhost:800/user/sschellhaas",
            "fullName" : "Steven Schellhaas"
          },
          "authorEmail" : "steven.schellhaas@deutschebahn.com",
          "comment" : "configBranch: TFZ-3901 FIS-neu: Baustelle BW Teilnetz 3b (Gäu-Murr)19.03.2020 – 24.03.2020 - Korrektur 3\n",
          "date" : "2020-03-03 16:42:59 +0000",
          "id" : "55291b59050e48cfec10bb591333c1b0dcffffbe",
          "msg" : "configBranch: TFZ-3901 FIS-neu: Baustelle BW Teilnetz 3b (Gäu-Murr)19.03.2020 – 24.03.2020 - Korrektur 3",
          "paths" : [
            {
              "editType" : "edit",
              "file" : "fahrzeug-server-templates/config/einbuchung/inventar(2)-NETZBW3GM.vm"
            }
          ]
        },
        {
          "_class" : "hudson.plugins.git.GitChangeSet",
          "affectedPaths" : [
            "fahrzeug-server-templates/config/einbuchung/inventar(1)-NETZDNOWMV.vm",
            "fahrzeug-server-templates/config/einbuchung/inventar(2)-NETZBBMVNS.vm",
            "fahrzeug-server-templates/config/einbuchung/inventar(1)-NETZEEN.vm"
          ],
          "commitId" : "5a9c40960d798f87588775415c7206cf22ade438",
          "timestamp" : 1583330679000,
          "author" : {
            "absoluteUrl" : "http://localhost:800/user/nkipper",
            "fullName" : "Nicolas Kipper"
          },
          "authorEmail" : "nicolas.kipper@deutschebahn.com",
          "comment" : "TFZ-3948 FIS-neu: Baustelle NO NNS - RE5 - sofort–05.04.2020\nTFZ-3949 FIS-neu: Baustelle NO DNOW - RE4 - sofort–23.04.2020\nTFZ-3926 FIS-neu: Baustelle NO EEN - RE15 - 09.03.–16.03.2020\n",
          "date" : "2020-03-04 15:04:39 +0100",
          "id" : "5a9c40960d798f87588775415c7206cf22ade438",
          "msg" : "TFZ-3948 FIS-neu: Baustelle NO NNS - RE5 - sofort–05.04.2020",
          "paths" : [
            {
              "editType" : "edit",
              "file" : "fahrzeug-server-templates/config/einbuchung/inventar(1)-NETZEEN.vm"
            },
            {
              "editType" : "edit",
              "file" : "fahrzeug-server-templates/config/einbuchung/inventar(2)-NETZBBMVNS.vm"
            },
            {
              "editType" : "edit",
              "file" : "fahrzeug-server-templates/config/einbuchung/inventar(1)-NETZDNOWMV.vm"
            }
          ]
        },
        {
          "_class" : "hudson.plugins.git.GitChangeSet",
          "affectedPaths" : [
            "fahrzeug-server-templates/build.xml"
          ],
          "commitId" : "92c922b5b0e0dbc34bc8c3e704db165b7ad60d65",
          "timestamp" : 1583410489000,
          "author" : {
            "absoluteUrl" : "http://localhost:800/user/nkipper",
            "fullName" : "Nicolas Kipper"
          },
          "authorEmail" : "nicolas.kipper@deutschebahn.com",
          "comment" : "build.xml - Versionsnummer auf 7.8.0.3 erhöht\n",
          "date" : "2020-03-05 13:14:49 +0100",
          "id" : "92c922b5b0e0dbc34bc8c3e704db165b7ad60d65",
          "msg" : "build.xml - Versionsnummer auf 7.8.0.3 erhöht",
          "paths" : [
            {
              "editType" : "edit",
              "file" : "fahrzeug-server-templates/build.xml"
            }
          ]
        }
      ],
      "kind" : "git"
    }
  ],
  "culprits" : [
    {
      "absoluteUrl" : "http://localhost:800/user/stefan.wegener",
      "fullName" : "Stefan.Wegener"
    },
    {
      "absoluteUrl" : "http://localhost:800/user/nkipper",
      "fullName" : "Nicolas Kipper"
    },
    {
      "absoluteUrl" : "http://localhost:800/user/sschellhaas",
      "fullName" : "Steven Schellhaas"
    }
  ],
  "nextBuild" : {
    "number" : 3119,
    "url" : "http://localhost:800/view/Buildampel/job/Fahrzeug-Server/3119/"
  },
  "previousBuild" : None
}

@pytest.fixture
def jenkins(monkeypatch):
    def fake_get_jenkins_poll(cls, tree=None):  # pylint: disable=unused-argument
        return JENKINS_DATA
    def fake_job_data(cls, url, params=None, tree=None):  # pylint: disable=unused-argument
        return BUILD_DATA_FAIL           


    monkeypatch.setattr(JenkinsBase, 'get_data', fake_job_data)    
    monkeypatch.setattr(Jenkins, '_poll', fake_get_jenkins_poll)
    return Jenkins('http://localhost:800/')

@pytest.fixture
def job(jenkins, monkeypatch):
    def fake_get_data(cls, url, tree=None):  # pylint: disable=unused-argument
        return JOB_DATA

    monkeypatch.setattr(JenkinsBase, 'get_data', fake_get_data)

    return Job('http://localhost:800/view/Buildampel/job/Fahrzeug-Server/', 'Fahrzeug-Server', jenkins)    

@pytest.fixture
def build(jenkins, job, monkeypatch):
    def fake_get_data(cls, url, params=None, tree=None):  # pylint: disable=unused-argument
        return BUILD_DATA_FAIL

    monkeypatch.setattr(JenkinsBase, 'get_data', fake_get_data)

    return Build('http://localhost:800/view/Buildampel/job/Fahrzeug-Server/3119/', 3119, job)    



def test_returns_build_info(jenkins, job, monkeypatch, build):
    jenkins.get_job  = mock.MagicMock(return_value=job)
    job.get_build    = mock.MagicMock(return_value=build)
    timestamp = 1583495750
    result = "UNSTABLE"

    build = query_a_build.getBuildJobInfo(3119, "Fahrzeug-Server", jenkins)

    dt_object = datetime.fromtimestamp(timestamp, timezone.utc)
    assert dt_object == build.get_timestamp()
    assert result == build.get_status()

