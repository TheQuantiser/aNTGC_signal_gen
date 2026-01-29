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


workarea                               = '/afs/hep.wisc.edu/user/wadud/private/signal_production/CMSSW_10_6_29/src/GeneratorInterface/LHEInterface/aNTGCcrabsubmit/'
mainOutputDir                          = '/store/user/mwadud/aNTGC/crab/'

pset                                   = 'aNTGC_ZNuNuG_200_UMN_step3_Run2_2018_PREMIX.py'
jobName                                = "aNTGC_ZNuNuGamma_600_2018_PREMIX"
inputDataset                           = '/aNTGC_ZNuNuGamma_600_2018_GEN/rusack-aNTGC_ZNuNuGamma_600_2018_SIM-2d8e34e0c1e3d17f8e40513f6736c9b9/USER'
puList                                 = 'pileupUL2018.txt'


# pset                                   = 'aNTGC_ZNuNuG_200_UMN_step3_Run2_2017_PREMIX.py'
# jobName                                = "aNTGC_ZNuNuGamma_600_2017_PREMIX"
# inputDataset                           = '/aNTGC_ZNuNuGamma_600_2017/rusack-aNTGC_ZNuNuGamma_600_2017_SIM-12a3494d6ece49e1c421dcb16daa1c2a/USER'
# puList                                 = 'pileupUL2017.txt'


# pset                                   = 'aNTGC_ZNuNuG_200_UMN_step3_Run2_2016_HIPM_PREMIX.py'
# jobName                                = "aNTGC_ZNuNuGamma_600_2016PreVFP_PREMIX"
# inputDataset                           = '/aNTGC_ZNuNuGamma_600_2016PreVFP_GEN/rusack-aNTGC_ZNuNuGamma_600_2016PreVFP_SIM-19d19da0f020dc316eba549f0bbd0175/USER'
# puList                                 = 'pileupUL2016.txt'


# pset                                   = 'aNTGC_ZNuNuG_200_UMN_step3_Run2_2016_PREMIX.py'
# jobName                                = "aNTGC_ZNuNuGamma_200_2016PostVFP_PREMIX"
# inputDataset                           = '/aNTGC_ZNuNuGamma_200_2016PostVFP_GEN/rusack-aNTGC_ZNuNuGamma_200_2016PostVFP_SIM-db636700c929be67ae76051bdedc1e95/USER'
# jobName                                = "aNTGC_ZNuNuGamma_600_2016PostVFP_PREMIX"
# inputDataset                           = '/aNTGC_ZNuNuGamma_600_2016PostVFP_GEN/rusack-aNTGC_ZNuNuGamma_600_2016PostVFP_SIM-db636700c929be67ae76051bdedc1e95/USER'
# puList                                 = 'pileupUL2016.txt'


config                                 = config()

config.General.requestName             = jobName
config.General.workArea                = workarea
config.General.transferLogs            = True
config.General.instance                = 'prod'

config.JobType.pluginName              = 'Analysis'
config.JobType.psetName                = pset
config.JobType.maxMemoryMB             = 4000
config.JobType.maxJobRuntimeMin        = 1200
config.JobType.numCores                = 4
config.JobType.sendExternalFolder      = True
config.JobType.sendPythonFolder        = True
config.JobType.allowUndistributedCMSSW = True
config.JobType.inputFiles              = [puList]

config.Data.inputDataset               = inputDataset
config.Data.allowNonValidInputDataset  = True
config.Data.outputDatasetTag           = jobName
config.Data.inputDBS                   = 'phys03'
config.Data.splitting                  = 'FileBased'
config.Data.unitsPerJob                = 1
config.Data.totalUnits                 = 1000000000
config.Data.publication                = True
config.Data.outLFNDirBase              = mainOutputDir
config.Data.ignoreLocality             = True

config.Site.storageSite                = 'T2_US_Wisconsin'
config.Site.whitelist                  = ['T3_US*']

submit(config)
