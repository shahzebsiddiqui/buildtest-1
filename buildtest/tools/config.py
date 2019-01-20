############################################################################
#
#  Copyright 2017-2018
#
#   https://github.com/HPC-buildtest/buildtest-framework
#
#  This file is part of buildtest.
#
#    buildtest is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    buildtest is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with buildtest.  If not, see <http://www.gnu.org/licenses/>.
#############################################################################

"""
Checks buildtest configuration and reports any errors. Also display buildtest
configuration using buildtest --show

:author: Shahzeb Siddiqui (shahzebmsiddiqui@gmail.com)
"""
import os
import sys
import time
import logging
import subprocess
import yaml

# read the BUILDTEST env vars from the shell environment that is sourced by setup.sh
BUILDTEST_VERSION="0.6.3"
BUILDTEST_ROOT = os.getenv("BUILDTEST_ROOT")

BUILDTEST_JOB_EXTENSION = [".lsf", ".slurm", ".pbs"]
BUILDTEST_SHELLTYPES = ["sh", "bash", "csh"]

PYTHON_APPS = ["python","anaconda2", "anaconda3"]
MPI_APPS = ["openmpi", "mpich","mvapich2", "intel", "impi"]

#BUILDTEST_DEFAULT_CONFIG=os.path.join(BUILDTEST_ROOT,"config.yaml")
#print BUILDTEST_DEFAULT_CONFIG
#fd = open(BUILDTEST_DEFAULT_CONFIG,'r')
BUILDTEST_CONFIG_FILE = os.path.join(os.getenv("HOME"),".local","buildtest","config.yaml")
#if not os.path.exists(BUILDTEST_CONFIG_FILE):
#    print (f"FILE: {BUILDTEST_CONFIG_FILE} not found")
try:
    fd = open(BUILDTEST_CONFIG_FILE,'r')
    config_opts = yaml.load(fd)
    config_opts['BUILDTEST_CONFIGS_REPO_SYSTEM']=""
    config_opts['BUILDTEST_CONFIGS_REPO_SOFTWARE']=""
    config_opts['BUILDTEST_VERSION'] = BUILDTEST_VERSION

except FileNotFoundError as err_msg:
    print(f"{err_msg}")
    raise

#global logID
logID = "buildtest"

FILES_config = ["BUILDTEST_JOB_TEMPLATE"]
DIR_config = ["BUILDTEST_CONFIGS_REPO","BUILDTEST_RUBY_REPO","BUILDTEST_R_REPO","BUILDTEST_PYTHON_REPO","BUILDTEST_LOGDIR","BUILDTEST_TESTDIR","BUILDTEST_RUN_DIR"]
config_yaml_keys = {
    'BUILDTEST_MODULE_NAMING_SCHEME': type("str"),
    'BUILDTEST_EASYBUILD': type(True),
    'BUILDTEST_CLEAN_BUILD': type(True),
    'BUILDTEST_ENABLE_JOB': type(True),
    'BUILDTEST_OHPC': type(True),
    'BUILDTEST_SHELL': type("str"),
    'BUILDTEST_JOB_TEMPLATE': type("file"),
    'BUILDTEST_SUCCESS_THRESHOLD': type(1.0),
    'BUILDTEST_MODULE_ROOT': type([]),
    'BUILDTEST_CONFIGS_REPO': type("str"),
    'BUILDTEST_RUBY_REPO': type("str"),
    'BUILDTEST_R_REPO': type("str"),
    'BUILDTEST_PYTHON_REPO': type("str"),
    'BUILDTEST_LOGDIR': type("str"),
    'BUILDTEST_TESTDIR': type("str"),
    'BUILDTEST_RUN_DIR': type("str"),
    'BUILDTEST_EMAIL': type(True),
}
values_BUILDTEST_MODULE_NAMING_SCHEME = ["HMNS", "FNS"]

def check_configuration():
    """
    Reports buildtest configuration and checks each BUILDTEST environment variable and check
    for module environment
    """

    #print "Checking buildtest environment variables ..."

    ec = 0
    print ("Check Configuration")

    keylist = config_yaml_keys.keys()
    valuelist = config_yaml_keys.values()

    # check if any key is not found in config.yaml file
    for key in keylist:
        if key not in config_opts:
            print ("Unable to find key: " + key + " in your configuration file: " + BUILDTEST_CONFIG_FILE)
            ec = 1


    for key,value in zip(keylist,valuelist):

        if value is not type(config_opts[key]):
            print ("Invalid Type for key:" + key + " expecting type: " + str(value) + " current type: " + str(type(config_opts[key])))
            ec = 1

        # check if BUILDTEST_MODULE_NAMING_SCHEME is either "FNS" or "HMNS"
        if key == "BUILDTEST_MODULE_NAMING_SCHEME" and config_opts[key] not in values_BUILDTEST_MODULE_NAMING_SCHEME:
            print (key + " expects value " + str(values_BUILDTEST_MODULE_NAMING_SCHEME) + " current value is " + str(config_opts[key]))
            ec = 1

        if key == "BUILDTEST_SHELL" and config_opts[key] not in BUILDTEST_SHELLTYPES:
            print (key + " expects value " + str(BUILDTEST_SHELLTYPES) + " current value is " + str(config_opts[key]))
            ec = 1

        # check if BUILDTEST_SUCCESS_THRESHOLD is between 0.0 and 1.0
        if key == "BUILDTEST_SUCCESS_THRESHOLD" and (config_opts[key] < 0.0 or  config_opts[key] > 1.0):
            print (key + " must be between [0.0-1.0]" + " current value is " + str(config_opts[key]))
            ec = 1

        if key == "BUILDTEST_JOB_TEMPLATE" and os.path.splitext(config_opts[key])[1] not in BUILDTEST_JOB_EXTENSION:
            #print (f"Invalid file extension: {config_opts[key])[1]} must be one of the following extension {BUILDTEST_JOB_EXTENSION}")
            print ("Invalid File extension " + str(os.path.splitext(config_opts[key])[1]) + " must be one of the following extension" + str(BUILDTEST_JOB_EXTENSION))
            ec = 1


        # if yaml key is of type FILE, check if file exists
        if key in FILES_config:
            if not os.path.exists(config_opts[key]):
                print (config_opts[key] + " is an invalid file path please check your file")
                ec = 1

        # if yaml key is of type FILE, check if file exists
        if value in DIR_config:
            if not os.path.isdir(config_opts[key]):
                print (config_opts[key] + " has an invalid directory path please check your path")
                ec = 1
    if (ec):
        sys.exit(0)

    cmd = "module --version"
    ret = subprocess.Popen(cmd,shell=True,stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    (outputmsg,errormsg) = ret.communicate()
    ec = ret.returncode

    if ec != 0:
        print ("module commmand not found in system")
        print (outputmsg)
        print (errormsg)
        sys.exit(1)


    # if BUILDTEST_PREPEND_MODULES not defined then declare as empty list in dictionary
    if "BUILDTEST_PREPEND_MODULES" not in  list(config_opts.keys()):
        config_opts["BUILDTEST_PREPEND_MODULES"] = []



def show_configuration():
    """ show buildtest configuration """
    exclude_list = ["BUILDTEST_CONFIGS_REPO_SOFTWARE", "BUILDTEST_CONFIGS_REPO_SYSTEM", "BUILDTEST_PERL_TESTDIR", "BUILDTEST_PYTHON_TESTDIR", "BUILDTEST_RUBY_TESTDIR", "BUILDTEST_R_TESTDIR", "BUILDTEST_VERSION"]
    print
    print ("\t buildtest configuration summary")
    print ("\t (C): Configuration File,  (E): Environment Variable")
    print
    

    for key in sorted(config_opts):
        if key in exclude_list:
            continue
        if os.getenv(key):
            type = "(E)"
        else:
            type = "(C)"

        if key == "BUILDTEST_MODULE_ROOT":
            tree = ""
            for mod_tree in config_opts[key]:
                tree += mod_tree + ":"

            # remove last colon
            tree = tree[:-1]
            print ((key + "\t " + type + " =").expandtabs(50), tree)
        else:
            print ((key + "\t " + type + " =").expandtabs(50), config_opts[key])

    sys.exit(0)
