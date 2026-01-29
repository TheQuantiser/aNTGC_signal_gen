# aNTGC signal generation configs

This repository collects configuration files and helper scripts for producing aNTGC Z(→νν)γ Monte Carlo samples through the standard CMS Run 2 production chain. It focuses on the essentials for generating, simulating, and processing samples, while leaving year-specific details to the configs themselves.

## What’s included

- **Generator fragments** defining the physics process, gridpack location, and Pythia8 settings.
- **Step-wise CMSSW configs** for the standard production stages:
  - **GEN** (LHE + hadronization)
  - **SIM** (detector simulation)
  - **PREMIX** (pileup premixing)
  - **HLT** (trigger emulation)
  - **AODSIM** (reconstruction)
  - **MINIAODSIM** (analysis-ready format)
- **CRAB submission configs** for each step in the chain.
- **Pileup file lists** used for premixing.
- **Utility scripts** to regenerate CMSSW configs and build resubmission JSONs.

## Typical workflow (high level)

1. **GEN**: produce LHE and hadronize with Pythia8 using the provided gridpack.
2. **SIM**: run detector simulation to create GEN-SIM output.
3. **PREMIX**: add pileup using premix_stage2 and a random subset of pileup files.
4. **HLT**: run the trigger menu on premixed data.
5. **AODSIM**: perform reconstruction.
6. **MINIAODSIM**: produce analysis-ready MiniAOD.

Each step has a corresponding CMSSW configuration and (optionally) a CRAB submission script.

## Key files and directories

- `gen_fragment_*.py`: generator fragments and Pythia8 tuning.
- `aNTGC_ZNuNuG_*_step*.py`: CMSSW step configs for the full production chain.
- `crab_submit_*_step*.py`: CRAB submission templates per step.
- `pileupUL*.txt`: premix input file lists.
- `createGenFragments.sh`: helper to regenerate CMSSW configs via `cmsDriver.py`.
- `createIdleJsons.sh`: helper to derive unprocessed lumis for resubmission.

## Usage notes

- The configs are intended to be run inside a CMSSW environment with appropriate releases for each step.
- CRAB configs assume a user-specific work area and output location; adjust these before submission.
- Premixing chooses a random subset of pileup files per job; ensure the pileup list files are available locally.

## Conventions

- File names encode the step number and output tier (e.g., `step1` for GEN, `step6` for MINIAODSIM).
- “HIPM” denotes pre-VFP conditions for 2016.

## License

No license is provided in this repository; use according to your collaboration or project guidelines.
