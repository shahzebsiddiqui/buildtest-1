#!/bin/sh
./buildtest.py -s GCC/5.4.0-2.27 
./buildtest.py -s GCC/6.2.0-2.27 
./buildtest.py -s intel/2017.01
./buildtest.py -s CMake/3.7.1 -t GCCcore/.5.4.0
./buildtest.py -s Java/1.8.0_92
./buildtest.py -s git/2.10.2 -t GCCcore/.5.4.0
./buildtest.py -s Python/2.7.12 -t foss/.2016.03
./buildtest.py -s hwloc/1.11.3 -t GCC/5.4.0-2.27
./buildtest.py -s numactl/2.0.11 -t GCC/5.4.0-2.27
./buildtest.py -s CUDA/8.0.44 -t GCC/5.4.0-2.27
./buildtest.py -s OpenMPI/2.0.0 -t GCC/5.4.0-2.27
./buildtest.py -s OpenMPI/2.0.1 -t GCC/6.2.0-2.27
./buildtest.py -s OpenMPI/2.0.2 -t intel/2017.01
./buildtest.py -s Bowtie2/2.2.9 -t GCCcore/.5.4.0

