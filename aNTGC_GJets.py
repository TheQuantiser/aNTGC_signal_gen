import FWCore.ParameterSet.Config as cms
from Configuration.Generator.Pythia8CommonSettings_cfi import *
from Configuration.Generator.MCTunes2017.PythiaCP5Settings_cfi import *

# inspirations from:
# https://cms-pdmv.cern.ch/mcm/public/restapi/requests/get_fragment/JME-RunIIFall17GS-00003
# https://cms-pdmv.cern.ch/mcm/public/restapi/requests/get_fragment/EGM-RunIISummer17GS-00014
# https://raw.githubusercontent.com/cms-sw/genproductions/a10c4661b08ff764b90a8b1947689c52c5c992fb/python/ThirteenTeV/Hadronizer/Hadronizer_TuneCP5_13TeV_MLM_5f_max4j_qCut19_LHE_pythia8_cff.py
# https://cms-pdmv.cern.ch/mcm/public/restapi/requests/get_fragment/EXO-RunIIFall17wmLHEGS-00003

# https://monte-carlo-production-tools.gitbook.io

# https://github.com/cms-sw/cmssw/blob/master/GeneratorInterface/Pythia8Interface/plugins/Pythia8Hadronizer.cc
# https://twiki.cern.ch/twiki/bin/view/CMSPublic/SWGuideAboutPythonConfigFile
# https://github.com/cms-sw/cmssw/blob/CMSSW_9_4_X/GeneratorInterface/Pythia8Interface/src/Py8InterfaceBase.cc

# https://twiki.cern.ch/twiki/bin/view/Main/ExoMCInstructions#Multi_year_requests
# https://twiki.cern.ch/twiki/bin/view/CMSPublic/WorkBookChapter6#RndmSeeds
# https://twiki.cern.ch/twiki/bin/view/CMSPublic/SWGuideCmsDriver
# https://twiki.cern.ch/twiki/bin/view/CMSPublic/SWGuideSimulation#Rerun_a_job_with_the_same_random
# https://twiki.cern.ch/twiki/bin/view/CMSPublic/MCproduction
# https://twiki.cern.ch/twiki/bin/view/CMSPublic/WorkBookGeneration#RndmSeeds

generator = cms.EDFilter('Pythia8GeneratorFilter',
	comEnergy=cms.double(13000.0),
	crossSection=cms.untracked.double(1.0),
	filterEfficiency=cms.untracked.double(1.0),
	maxEventsToPrint=cms.untracked.int32(0),
	pythiaHepMCVerbosity=cms.untracked.bool(True),
	pythiaPylistVerbosity=cms.untracked.int32(True),
	PythiaParameters=cms.PSet(
		pythia8CommonSettingsBlock,
		pythia8CP5SettingsBlock,
		processParameters=cms.vstring(
			## http://home.thep.lu.se/~torbjorn/pythia82html/ElectroweakProcesses.htmls
			'PromptPhoton:qg2qgamma = on       	! prompt photon production',
			'PromptPhoton:qqbar2ggamma = on    	! prompt photon production',
			'PromptPhoton:gg2ggamma = on       	! prompt photon production',
			## http://home.thep.lu.se/~torbjorn/pythia82html/PhaseSpaceCuts.html
			'PhaseSpace:pTHatMin = 200.      	! minimum pt hat for hard interactions',
			'PhaseSpace:pTHatMax = 13000       	! maximum pt hat for hard interactions',
			'PhaseSpace:bias2Selection = on',
			'PhaseSpace:bias2SelectionPow = 4.5',
			'PhaseSpace:bias2SelectionRef = 200.',  
			),
		parameterSets=cms.vstring('pythia8CommonSettings',
			'pythia8CP5Settings',
			'processParameters')
		)
	)

pho_filter = cms.EDFilter("PythiaFilter",
	ParticleID=cms.untracked.int32(22),
	Status=cms.untracked.int32(23),
	MaxEta=cms.untracked.double(3.),
	MinEta=cms.untracked.double(-3.),
	MinPt=cms.untracked.double(200.),
	MaxPt=cms.untracked.double(13000.))

ProductionFilterSequence = cms.Sequence(generator*pho_filter)