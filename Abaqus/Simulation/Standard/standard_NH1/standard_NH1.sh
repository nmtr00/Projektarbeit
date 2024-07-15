#!/usr/bin/zsh

### Start of Slurm SBATCH definitions
### Maximum runtime
#SBATCH --time=7:00:00

### Ask for --ntask cpus (tasks in Slurm terms) across nodes
#SBATCH --ntasks=2
#SBATCH --nodes=1

#ask for 1GB within each node (1)
#SBATCH --mem-per-cpu=512M

### Name the job
#SBATCH --job-name=pa_standard_NH1

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
JOBNAME=standard_NH1
RENAME=rename_1_parameter

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
cp odb_data_extract.py results
cp $JOBNAME.log results/abaqus_reports
cp $RENAME.py results_renamed/abaqus_reports
cd results
python odb_data_extract.py
cd abaqus_reports
python $RENAME.py