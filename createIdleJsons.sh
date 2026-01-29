#!/bin/bash


# for iGenDir in $(find . -maxdepth 1 -mindepth 1 -type d -name "*GEN" | sort); do

	iGenDir=crab_aNTGC_ZNuNuGamma_600_2017

	genDir=$(basename $iGenDir)
	simDir=${genDir%GEN}_SIM

	genJSON=${genDir}/results/outputDatasetsLumis.json

	genLumi=$(cat ${genJSON} | sed 's/^[^:]*://g')
	genLumi=${genLumi::-1}

	tmpGenJson=${genDir}/results/tmp.json

	echo ${genLumi} > ${tmpGenJson}

	simJSON=${simDir}/results/processedLumis.json

	resubmitJSON=$(basename ${genDir%GEN})SIM_unProcessedLumis.json

	compareJSON.py --sub ${tmpGenJson} ${simJSON} ${resubmitJSON}
# done
