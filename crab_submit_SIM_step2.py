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

#pset                                   = 'aNTGC_ZNuNuG_200_UMN_step2_Run2_2016_HIPM_SIM.py'
mainOutputDir                          = '/store/user/mwadud/aNTGC/crab/'

#jobName                                = "aNTGC_ZNuNuGamma_200_2016PreVFP_SIM"
#inputDataset                           = '/aNTGC_ZNuNuGamma_200_2016PreVFP_GEN/mwadud-crab_aNTGC_ZNuNuGamma_200_2016PreVFP_GEN-b6fbda0a3edec0e4a3772270fe87c558/USER'

# jobName                                = "aNTGC_ZNuNuGamma_600_2016PreVFP_SIM"
# inputDataset                           = '/aNTGC_ZNuNuGamma_600_2016PreVFP_GEN/mwadud-crab_aNTGC_ZNuNuGamma_600_2016PreVFP_GEN-4c0ee162004ed96d057ea427281a2926/USER'



# workarea                               = '/afs/hep.wisc.edu/user/wadud/private/signal_production/CMSSW_10_6_29/src/GeneratorInterface/LHEInterface/aNTGCcrabsubmit/'
# pset                                   = 'aNTGC_ZNuNuG_200_UMN_step2_Run2_2016_SIM.py'
# mainOutputDir                          = '/store/user/mwadud/aNTGC/crab/'

# jobName                                = "aNTGC_ZNuNuGamma_200_2016PostVFP_SIM"
# inputDataset                           = '/aNTGC_ZNuNuGamma_200_2016PostVFP_GEN/mwadud-crab_aNTGC_ZNuNuGamma_200_2016PostVFP_GEN-b6fbda0a3edec0e4a3772270fe87c558/USER'

# jobName                                = "aNTGC_ZNuNuGamma_600_2016PostVFP_SIM"
# inputDataset                           = '/aNTGC_ZNuNuGamma_600_2016PostVFP_GEN/mwadud-crab_aNTGC_ZNuNuGamma_600_2016PostVFP_GEN-cd2888dd697eb953b4238b515057d25f/USER'



# workarea                               = '/afs/hep.wisc.edu/user/wadud/private/signal_production/CMSSW_10_6_29/src/GeneratorInterface/LHEInterface/aNTGCcrabsubmit/'
#pset                                   = 'aNTGC_ZNuNuG_200_UMN_step2_Run2_2017_SIM.py'
#jobName                                = "aNTGC_ZNuNuGamma_200_2017_SIM"
#inputDataset                           = '/aNTGC_ZNuNuGamma_200_2017_GEN/mwadud-crab_aNTGC_ZNuNuGamma_200_2017_GEN-3c6575d3269427736df33edce2a13735/USER'

# jobName                                = "aNTGC_ZNuNuGamma_600_2017_SIM"
# inputDataset                           = '/aNTGC_ZNuNuGamma_600_2017/mwadud-crab_aNTGC_ZNuNuGamma_600_2017-2e7aa344f669f222ecd552081b525815/USER'



# workarea                               = '/afs/hep.wisc.edu/user/wadud/private/signal_production/CMSSW_10_6_29/src/GeneratorInterface/LHEInterface/aNTGCcrabsubmit/'
pset                                   = 'aNTGC_ZNuNuG_200_UMN_step2_Run2_2018_SIM.py'
jobName                                = "aNTGC_ZNuNuGamma_200_2018_SIM"
inputDataset                           = '/aNTGC_ZNuNuGamma_200_2018_GEN/mwadud-crab_aNTGC_ZNuNuGamma_200_2018_GEN-ed4cec5c2fd2f6c0df9afec09e735afd/USER'

# jobName                                = "aNTGC_ZNuNuGamma_600_2018_SIM"
# inputDataset                           = '/aNTGC_ZNuNuGamma_600_2018_GEN/mwadud-crab_aNTGC_ZNuNuGamma_600_2018_GEN-b0c9806a67e462cfc76117a0c1785b6e/USER'


config                                 = config()

config.General.requestName             = jobName
config.General.workArea                = workarea
config.General.transferLogs            = True
config.General.instance                = 'prod'

config.JobType.pluginName              = 'Analysis'
config.JobType.psetName                = pset
config.JobType.maxMemoryMB             = 4000
config.JobType.maxJobRuntimeMin        = 5760
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
