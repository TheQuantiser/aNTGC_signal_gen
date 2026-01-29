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


# v1 already submitted by Mohammad - 1M events
#version         = 'v1'
#inputDataset    = '/GJets_FlatPtHat_200_2021_05_12_v1_GEN/mwadud-GJets_FlatPtHat_200_2021_05_16_v1_PREMIX-c6365a72a74a01e5fcc8553d79679929/USER'

# For Roger - 5M events
version       = 'v2'
inputDataset  = '/GJets_FlatPtHat_200_2021_05_13_v2_GEN/rusack-GJets_FlatPtHat_200_2021_05_17_v2_PREMIX-c6365a72a74a01e5fcc8553d79679929/USER'

# For Mohammad - 3M events
# version       = 'v3'
# inputDataset  = ''

# For Mohammad - 3M events
#version       = 'v4'
#inputDataset  = '/GJets_FlatPtHat_200_2021_05_13_v4_GEN/rusack-GJets_FlatPtHat_200_2021_05_16_v4_PREMIX-c6365a72a74a01e5fcc8553d79679929/USER'

step            = 'HLT'
pset            = 'aNTGC_GJets_HLT_step4.py'

# Mohammad
#workarea        = '/afs/hep.wisc.edu/user/wadud/private/CMSSW_9_4_14_UL_patch1/src/Configuration/GenProduction/test/GJetsGen/crab/'
#mainOutputDir   = str('/store/user/mwadud/aNTGC/crab/')

# Roger
workarea      = '/afs/hep.wisc.edu/home/rusack/private/CMSSW_9_4_14_UL_patch1/src/Configuration/GenProduction/test/GJetsGen/crab/'
mainOutputDir = str('/store/user/rusack/aNTGC/crab/')


jobName         = str('GJets_FlatPtHat_200_') + date.today().strftime("%Y_%m_%d") + str("_") + version + str('_') + step


###################### CRAB config ######################
config.General.requestName 	           = jobName
config.General.workArea                = workarea
config.General.transferLogs            = True
config.General.instance                = 'prod'

config.JobType.pluginName              = 'Analysis'
config.JobType.psetName                = pset
config.JobType.maxMemoryMB             = 3200
config.JobType.maxJobRuntimeMin        = 1200
config.JobType.numCores	               = 1
config.JobType.sendExternalFolder      = True
config.JobType.sendPythonFolder        = True
config.JobType.allowUndistributedCMSSW = True

config.Data.inputDataset               = inputDataset
config.Data.allowNonValidInputDataset  = True
config.Data.outputDatasetTag           = jobName
config.Data.inputDBS                   = 'phys03'
config.Data.splitting                  = 'EventAwareLumiBased'
config.Data.unitsPerJob                = 2000
config.Data.totalUnits                 = 1000000000
config.Data.publication                = True
config.Data.outLFNDirBase              = mainOutputDir
config.Data.ignoreLocality             = True

config.Site.storageSite                = 'T2_US_Wisconsin'
config.Site.blacklist                  = ["T2_US_Purdue"]
config.Site.whitelist                  = ['T3_US_UCR','T3_US_FNALLPC','T3_US_Rice','T3_US_Rutgers','T3_US_FIT','T3_US_PSC','T3_US_OSU','T3_US_TAMU','T3_US_UMD','T3_US_VC3_NotreDame','T3_US_SDSC','T3_US_Colorado','T3_US_OSG','T3_US_Princeton_ICSE','T3_US_NERSC','T3_US_Baylor','T2_US_Nebraska','T2_US_UCSD','T2_US_Wisconsin','T2_US_MIT','T3_US_TACC','T3_US_UMiss','T2_US_Caltech', 'T2_US_Florida','T2_US_Vanderbilt']

submit(config)
