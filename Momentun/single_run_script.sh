#!/bin/bash
RUNNAME="tau_case1_100"

mkdir -p output/$RUNNAME

# Compile KiD
make COMPILER=gfortran


# Run case
./bin_gfortran_/KiD_1D.exe namelists/warm1.nml

mv output/*.nc output/$RUNNAME/ 2>/dev/null
mv output/*.nml output/$RUNNAME/ 2>/dev/null

echo "Output saved in output/$RUNNAME"
