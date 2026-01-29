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
# version                             = 'v1'
# inputDataset                        = '/GJets_FlatPtHat_200_2021_05_12_v1_GEN/mwadud-crab_GJets_FlatPtHat_200_2021_05_12_v1_GEN-6e8f5986544e75580c2fe106c519a9c0/USER'

# For Roger - 5M events
# version                             = 'v2'
# inputDataset                        = '/GJets_FlatPtHat_200_2021_05_13_v2_GEN/mwadud-crab_GJets_FlatPtHat_200_2021_05_13_v2_GEN-6e8f5986544e75580c2fe106c519a9c0/USER'

# For Mohammad - 3M events
version                               = 'v3'
inputDataset                          = '/GJets_FlatPtHat_200_2021_05_13_v3_GEN/mwadud-crab_GJets_FlatPtHat_200_2021_05_13_v3_GEN-6e8f5986544e75580c2fe106c519a9c0/USER'

# For Mohammad - 3M events
# version                             = 'v4'
# inputDataset                        = '/GJets_FlatPtHat_200_2021_05_13_v4_GEN/mwadud-crab_GJets_FlatPtHat_200_2021_05_13_v4_GEN-6e8f5986544e75580c2fe106c519a9c0/USER'

step                                  = 'SIM'
pset                                  = 'aNTGC_GJets_SIM_step2.py'

# Mohammad
workarea                            = '/afs/hep.wisc.edu/user/wadud/private/CMSSW_10_6_24/src/Configuration/GenProduction/test/GJetsGen/crab/'
mainOutputDir                       = str('/store/user/mwadud/aNTGC/crab/')

# Roger
# workarea                            = '/afs/hep.wisc.edu/home/rusack/private/CMSSW_10_6_24/src/Configuration/GenProduction/test/GJetsGen/crab/'
# mainOutputDir                       = str('/store/user/rusack/aNTGC/crab/')

# Mohammad
# workarea                              = '/afs/hep.wisc.edu/home/shilpi/forMohammad/CMSSW_10_6_24/src/Configuration/GenProduction/test/GJetsGen/crab/'
# mainOutputDir                         = '/store/user/shilpi/forMohammad/crab/'

jobName                               = str('GJets_FlatPtHat_200_') + date.today().strftime("%Y_%m_%d") + str("_") + version + str('_') + step


###################### CRAB config ######################
config.General.requestName 	          = jobName
config.General.workArea               = workarea
config.General.transferLogs           = True
config.General.instance               = 'prod'

config.JobType.pluginName             = 'Analysis'
config.JobType.psetName               = pset
config.JobType.maxMemoryMB            = 4000
config.JobType.maxJobRuntimeMin       = 900
config.JobType.numCores	              = 4
config.JobType.sendExternalFolder     = True
config.JobType.sendPythonFolder       = True
config.JobType.allowUndistributedCMSSW = True

config.Data.inputDataset              = inputDataset
config.Data.allowNonValidInputDataset = True
config.Data.outputDatasetTag          = jobName
config.Data.inputDBS                  = 'phys03'
config.Data.splitting                 = 'EventAwareLumiBased'
config.Data.unitsPerJob               = 1000
config.Data.totalUnits                = 1000000000
config.Data.publication               = True
config.Data.outLFNDirBase             = mainOutputDir
config.Data.ignoreLocality            = True

config.Site.storageSite               = 'T2_US_Wisconsin'
config.Site.blacklist                 = ["T2_US_Purdue"]
config.Site.whitelist                 = ['T3_US_UCR','T3_US_FNALLPC','T3_US_Rice','T3_US_Rutgers','T3_US_FIT','T3_US_PSC','T3_US_OSU','T3_US_TAMU','T3_US_UMD','T3_US_VC3_NotreDame','T3_US_SDSC','T3_US_Colorado','T3_US_OSG','T3_US_Princeton_ICSE','T3_US_NERSC','T3_US_Baylor','T2_US_Nebraska','T2_US_UCSD','T2_US_Wisconsin','T2_US_MIT','T3_US_TACC','T3_US_UMiss','T2_US_Caltech', 'T2_US_Florida','T2_US_Vanderbilt']

submit(config)
