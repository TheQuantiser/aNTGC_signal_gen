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


workarea                               = '/afs/hep.wisc.edu/user/wadud/private/signal_production/CMSSW_10_6_20/src/GeneratorInterface/LHEInterface/aNTGCcrabsubmit'
mainOutputDir                          = '/store/user/mwadud/aNTGC/crab/'

#pset                                   = 'aNTGC_ZNuNuG_200_UMN_step6_Run2_2016_MINIAODSIM.py'
# jobName                                = "aNTGC_ZNuNuGamma_200_2016PostVFP_MINIAODSIM"
# inputDataset                           = '/aNTGC_ZNuNuGamma_200_2016PostVFP_GEN/mwadud-aNTGC_ZNuNuGamma_200_2016PostVFP_AODSIM-a98090b55fee69090c8ccbacb23b46ae/USER'
#jobName                                = "aNTGC_ZNuNuGamma_600_2016PostVFP_MINIAODSIM"
#inputDataset                           = '/aNTGC_ZNuNuGamma_600_2016PostVFP_GEN/mwadud-aNTGC_ZNuNuGamma_600_2016PostVFP_AODSIM-a98090b55fee69090c8ccbacb23b46ae/USER'


# pset                                   = 'aNTGC_ZNuNuG_200_UMN_step6_Run2_2016_HIPM_MINIAODSIM.py'
# jobName                                = "aNTGC_ZNuNuGamma_600_2016PreVFP_MINIAODSIM"
# inputDataset                           = '/aNTGC_ZNuNuGamma_600_2016PreVFP_GEN/mwadud-aNTGC_ZNuNuGamma_600_2016PreVFP_AODSIM-c2fcb581f11a5b818c25cb8f3909ebdf/USER'


pset                                   	= 'aNTGC_ZNuNuG_200_UMN_step6_Run2_2017_MINIAODSIM.py'
# jobName                                = "aNTGC_ZNuNuGamma_600_2017_MINIAODSIM"
# inputDataset                           = '/aNTGC_ZNuNuGamma_600_2017/mwadud-aNTGC_ZNuNuGamma_600_2017_AODSIM-a122d338a02cc87e10d3c6b5a2c3d5fe/USER'

# pset                                   = 'aNTGC_ZNuNuG_200_UMN_step6_Run2_2018_MINIAODSIM.py'
# jobName                                = "aNTGC_ZNuNuGamma_600_2018_MINIAODSIM"
# inputDataset                           = '/aNTGC_ZNuNuGamma_600_2018_GEN/mwadud-aNTGC_ZNuNuGamma_600_2018_AODSIM-1a58fb8b5b36f21bf532e7d34eb23cf7/USER'


config                                 = config()

config.General.requestName             = jobName
config.General.workArea                = workarea
config.General.transferLogs            = True
config.General.instance                = 'prod'

config.JobType.pluginName              = 'Analysis'
config.JobType.psetName                = pset
config.JobType.maxMemoryMB             = 4000
config.JobType.maxJobRuntimeMin        = 600
config.JobType.numCores                = 4
config.JobType.sendExternalFolder      = True
config.JobType.sendPythonFolder        = True
config.JobType.allowUndistributedCMSSW = True

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
