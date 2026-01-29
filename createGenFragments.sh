#!/bin/bash

current_date_time="`date +%Y-%m-%d-%H:%M:%S`";
echo $current_date_time

source /cvmfs/cms.cern.ch/cmsset_default.sh;
eval `scramv1 runtime -sh`

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"

#resources
#https://twiki.cern.ch/twiki/bin/view/CMS/PdmV2017Analysis?rev=209
#https://twiki.cern.ch/twiki/bin/view/CMSPublic/SWGuideCmsDriver?rev=11

# GENFRAGMENT=gen_fragment_aNTGC.py
# baseName=aNTGC_ZNuNuG

# GENFRAGMENT=gen_fragment_aNTGC_600_UMN.py
# baseName=aNTGC_ZNuNuG_600_UMN

GENFRAGMENT=gen_fragment_aNTGC_200_UMN.py
baseName=aNTGC_ZNuNuG_200_UMN

# cp ${SCRIPT_DIR}/${GENFRAGMENT} ${CMSSW_BASE}/src/Configuration/GenProduction/
# cp ${SCRIPT_DIR}/${GENFRAGMENT} ${CMSSW_BASE}/python/Configuration/GenProduction/

cd ${CMSSW_BASE}/src/
scram b -j$(nproc)

cd $SCRIPT_DIR

nThreads1=4
nThreads2=4


nEvents=100
pileupDataset=puFile

### 2017
# GT1=106X_mc2017_realistic_v8
# GT2=106X_mc2017_realistic_v6
# GT_HLT=94X_mc2017_realistic_v15
# beamspotConditions=Realistic25ns13TeVEarly2017Collision
# era=Run2_2017
# pileupDataset="dbs:/Neutrino_E-10_gun/RunIISummer20ULPrePremix-UL17_106X_mc2017_realistic_v6-v3/PREMIX"


### 2018
# GT1=106X_upgrade2018_realistic_v15_L1v1
# GT2=106X_upgrade2018_realistic_v15_L1v1
# GT_HLT=102X_upgrade2018_realistic_v15
# beamspotConditions=Realistic25ns13TeVEarly2018Collision
# era=Run2_2018
# dbs:/Neutrino_E-10_gun/RunIISummer20ULPrePremix-UL18_106X_upgrade2018_realistic_v11_L1v1-v2/PREMIX


# ### 2016preVFP
# GT1=106X_mcRun2_asymptotic_preVFP_v9
# GT2=106X_mcRun2_asymptotic_preVFP_v9
# GT_HLT=80X_mcRun2_asymptotic_2016_TrancheIV_v6
# beamspotConditions=Realistic25ns13TeV2016Collision
# era=Run2_2016_HIPM
# dbs:/Neutrino_E-10_gun/RunIISummer20ULPrePremix-UL16_106X_mcRun2_asymptotic_v13-v1/PREMIX

### 2016postVFP
GT1=106X_mcRun2_asymptotic_v13
GT2=106X_mcRun2_asymptotic_v13
GT_HLT=80X_mcRun2_asymptotic_2016_TrancheIV_v6
beamspotConditions=Realistic25ns13TeV2016Collision
era=Run2_2016
# dbs:/Neutrino_E-10_gun/RunIISummer20ULPrePremix-UL16_106X_mcRun2_asymptotic_v13-v1/PREMIX

### CMS steps
# ## https://cms-pdmv.cern.ch/mcm/public/restapi/requests/get_setup/SUS-RunIISummer20UL17wmLHEGEN-00032
# cmsDriver.py  Configuration/GenProduction/${GENFRAGMENT} --nThreads ${nThreads1} --fileout file:${baseName}_GEN.root --mc --eventcontent RAWSIM --datatier GEN  --conditions ${GT1} --beamspot ${beamspotConditions} --mc --step LHE,GEN --geometry DB:Extended --era ${era} -n ${nEvents} --python_filename ${baseName}_step1_${era}_GEN.py --customise Configuration/DataProcessing/Utils.addMonitoring  --no_exec

# # ### https://cms-pdmv.cern.ch/mcm/public/restapi/requests/get_setup/SUS-RunIISummer20UL17SIM-00020
# cmsDriver.py --nThreads ${nThreads1} --fileout file:${baseName}_SIM.root --filein file:${baseName}_GEN.root --mc --eventcontent RAWSIM --datatier GEN-SIM  --conditions ${GT1} --beamspot ${beamspotConditions} --mc --step SIM --geometry DB:Extended --era ${era} -n ${nEvents} --python_filename ${baseName}_step2_${era}_SIM.py --customise Configuration/DataProcessing/Utils.addMonitoring --runUnscheduled --no_exec

# # ### https://cms-pdmv.cern.ch/mcm/public/restapi/requests/get_setup/SUS-RunIISummer20UL17DIGIPremix-00020
# cmsDriver.py --nThreads ${nThreads1} --fileout file:${baseName}_PREMIX.root --filein file:${baseName}_SIM.root --mc --eventcontent PREMIXRAW --datatier GEN-SIM-DIGI  --conditions ${GT2} --beamspot ${beamspotConditions} --mc --step DIGI,DATAMIX,L1,DIGI2RAW --procModifiers premix_stage2 --geometry DB:Extended --era ${era} -n ${nEvents}  --python_filename ${baseName}_step3_${era}_PREMIX.py --customise Configuration/DataProcessing/Utils.addMonitoring --pileup_input ${pileupDataset} --datamix PreMix  --runUnscheduled  --no_exec

# with open('pileupList.txt') as puListFile:
#     pileupPremixList = puListFile.read().splitlines()

# process.mixData.input.fileNames = cms.untracked.vstring(['puFile'])
# import random
# process.mixData.input.fileNames = cms.untracked.vstring(random.sample(pileupPremixList, 500))
# del pileupPremixList

# https://cms-pdmv.cern.ch/mcm/public/restapi/requests/get_setup/SUS-RunIISummer20UL17HLT-00020
# run HLT step in CMSSW_9_4_14_UL_patch1!
# HLT:2e34v40
# cmsDriver.py --nThreads ${nThreads2} --fileout file:${baseName}_HLT.root --filein file:${baseName}_PREMIX.root --mc --eventcontent RAWSIM --datatier GEN-SIM-RAW --conditions ${GT_HLT} --mc --step HLT:2e34v40 --geometry DB:Extended --era ${era} -n ${nEvents} --python_filename ${baseName}_HLT_step4.py --customise Configuration/DataProcessing/Utils.addMonitoring --customise_commands 'process.source.bypassVersionCheck = cms.untracked.bool(True)' --no_exec


cmsDriver.py --nThreads ${nThreads2} --fileout file:${baseName}_MINIAODSIM.root --filein file:${baseName}_HLT.root --mc --eventcontent AODSIM,MINIAODSIM --datatier AODSIM,MINIAODSIM --conditions ${GT2} --step RAW2DIGI,L1Reco,RECO,RECOSIM,EI,PAT --geometry DB:Extended --era ${era} -n ${nEvents} --python_filename ${baseName}_step5_${era}_MINIAODSIM.py --customise Configuration/DataProcessing/Utils.addMonitoring --procModifiers run2_miniAOD_UL --runUnscheduled --no_exec

