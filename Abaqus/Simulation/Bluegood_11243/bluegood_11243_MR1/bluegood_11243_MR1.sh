#!/usr/bin/zsh

### Start of Slurm SBATCH definitions
### Maximum runtime
#SBATCH --time=40:00:00

### Ask for --ntask cpus (tasks in Slurm terms) across nodes
#SBATCH --ntasks=2
#SBATCH --nodes=1

#ask for 1GB within each node (1)
#SBATCH --mem-per-cpu=512M

### Name the job
#SBATCH --job-name=pa_bluegood_MR1

### Declare an output STDOUT/STDERR file
#SBATCH --output=output.%J.txt

### Choose Partition
#SBATCH -p c23ms_low


######################################################
### Load required modules
module load ABAQUS/2022
module load Python

### Set the amount of memory to be passed to Abaqus as a command line argument
### Beware: This HAS to be lower than the total memory you requested.
### A good starting point is 80%.
export ABAQUS_MEM_ARG="3584 mb"


### name your job HERE, name it DIFFERENT from your input file!
JOBNAME=bluegood_11243_NH1
RENAME=rename_2_parameters

### Execute your application
### Please remember, to adjust the memory, it must be less than the total requested memory
abaqus script=$JOBNAME.psf > $JOBNAME.log
mkdir -p results
mv *.odb results/
mkdir -p results
mkdir -p data
mv *.odb results/
mv *.msg data/
mv *.par data/
mv *.pes data/
mv *.dat data/
mv *.com data/
mv *.pmg data/
mv *.prt data/
mv *.sta data/
cp -r results results_renamed
cp odb_data_extract.py results_renamed
python ./results_renamed/odb_data_extract.py
cp $JOBNAME.log results_renamed/abaqus_reports
cp $RENAME.py results_renamed/abaqus_reports
python ./results_renamed/abaqus_reports/$RENAME.py