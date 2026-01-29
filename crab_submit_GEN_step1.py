from CRABClient.UserUtilities import config
from CRABAPI.RawCommand import crabCommand
from CRABClient.ClientExceptions import ClientException
from httplib import HTTPException

from datetime import date

def submit(config):
    try:
        crabCommand("submit", config = config)
    except HTTPException as hte:
        print "Failed submitting task: %s" % (hte.headers)
    except ClientException as cle:
        print "Failed submitting task: %s" % (cle)

workarea                              = "/afs/hep.wisc.edu/user/wadud/private/signal_production/CMSSW_10_6_29/src/GeneratorInterface/LHEInterface/aNTGCcrabsubmit/"
jobName                               = "aNTGC_ZNuNuGamma_200_2017_GEN"
mainOutputDir                         = "/store/user/mwadud/aNTGC/crab/"

config                                = config()

config.General.requestName            = jobName
config.General.workArea               = workarea
config.General.transferLogs           = True
config.General.instance               = "prod"

config.JobType.pluginName             = "PrivateMC"
config.JobType.psetName               = "aNTGC_ZNuNuG_200_UMN_step1_Run2_2017_GEN.py"
config.JobType.maxMemoryMB            = 4000
config.JobType.eventsPerLumi          = 5000
config.JobType.maxJobRuntimeMin       = 1000
config.JobType.numCores	              = 4
config.JobType.sendExternalFolder     = True
config.JobType.sendPythonFolder       = True

config.Data.allowNonValidInputDataset = True
config.Data.inputDBS                  = "global"
config.Data.outputPrimaryDataset      = jobName
config.Data.splitting                 = "EventBased"
config.Data.unitsPerJob               = 10000
config.Data.totalUnits                = 3000000
config.Data.publication               = True
config.Data.outLFNDirBase             = mainOutputDir
config.Data.ignoreLocality            = True
#config.Data.outputDatasetTag         = jobName

config.Site.storageSite               = "T2_US_Wisconsin"
config.Site.whitelist                 = ["T2_US*"]
# config.Site.whitelist                 = ["T2_US_Wisconsin"]


submit(config)
