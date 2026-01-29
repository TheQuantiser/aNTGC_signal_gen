from CRABClient.UserUtilities import config
from CRABAPI.RawCommand import crabCommand
from CRABClient.ClientExceptions import ClientException
from httplib import HTTPException

from datetime import date

def submit(config):
    try:
        crabCommand('submit', config = config)
    except HTTPException as hte:
        print "Failed submitting task: %s" % (hte.headers)
    except ClientException as cle:
        print "Failed submitting task: %s" % (cle)

config                                = config()

version                               = 'v4'
step                                  = 'GEN'
workarea                              = '/afs/hep.wisc.edu/user/wadud/private/CMSSW_10_6_24/src/Configuration/GenProduction/test/GJetsGen/crab/'
jobName                               = str('GJets_FlatPtHat_200_') + date.today().strftime("%Y_%m_%d") + str("_") + version + str('_') + step
mainOutputDir                         = str('/store/user/mwadud/aNTGC/crab/')

config.General.requestName            = jobName
config.General.workArea               = workarea
config.General.transferLogs           = True
config.General.instance               = 'prod'

config.JobType.pluginName             = 'PrivateMC'
config.JobType.psetName               = 'aNTGC_GJets_GEN_step1.py'
config.JobType.maxMemoryMB            = 4000
config.JobType.eventsPerLumi          = 1000
config.JobType.maxJobRuntimeMin       = 5760
config.JobType.numCores	              = 4
config.JobType.sendExternalFolder     = True
config.JobType.sendPythonFolder       = True

config.Data.allowNonValidInputDataset = True
config.Data.inputDBS                  = 'global'
config.Data.outputPrimaryDataset      = jobName
config.Data.splitting                 = 'EventBased'
config.Data.unitsPerJob               = 50000
config.Data.totalUnits                = 3000000
config.Data.publication               = True
config.Data.outLFNDirBase             = mainOutputDir
#config.Data.outputDatasetTag         = jobName
config.Data.ignoreLocality            = True

config.Site.storageSite               = 'T2_US_Wisconsin'
config.Site.whitelist                 = ["T2_US*"]

submit(config)
