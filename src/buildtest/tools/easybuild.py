############################################################################
#
#  Copyright 2017-2019
#
#  https://github.com/HPC-buildtest/buildtest-framework
#
#  This file is part of buildtest.
#
#  buildtest is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  buildtest is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with buildtest.  If not, see <http://www.gnu.org/licenses/>.
#############################################################################

"""
This module checks for easyconfig files in a module tree by searching module
files and the installation directory for .eb files.
"""

import os

from buildtest.tools.config import config_opts
from buildtest.tools.file import string_in_file, walk_tree
from buildtest.tools.modules import module_obj

def find_easyconfigs_from_modulelist(modulelist):
    """This method returns a list of easyconfig from a list of module files."""

    # list to store easyconfigs
    ec_list = []

    # list to store if no easyconfigs found
    no_ec_list = []

    # look for variable root in modulefile
    search_str = "local root ="

    for module in  modulelist:
        # if variable root found in module file then read file and find value
        # assigned to root to get root of software
        if string_in_file(search_str, module):
            content = open(module).readlines()
            for line in content:
                # if line starts with string "local root = <path>" then get PATH
                if line.startswith(search_str):
                    root_path = line.split()[-1]
                    root_path = root_path.replace('"', '')

                    # trying to find directory easybuild inside the root of the
                    # installation directory of an application
                    easybuild_path = os.path.join(root_path, "easybuild")
                    # if directory exist then run the find command
                    if os.path.isdir(easybuild_path):
                        eb_file = walk_tree(easybuild_path, ".eb")

                        # only add to list ec_list if there is an easyconfig file
                        if len(eb_file) > 0:
                            ec_list += eb_file
                        else:
                            no_ec_list.append(f"Reading File: {module}. "
                                              f"Unable to find any .eb file "
                                              f"in {easybuild_path} ")

                    break
                else:
                    continue
        else:
            no_ec_list.append(f"Reading File: {module} "
                              + "Unable to find variable root in module file. "
                              + "This module is not generated by easybuild")


    return ec_list,no_ec_list

def find_easyconfigs():
    """ This method prints the easyconfig lists in a table format and it
        implements buildtest list --easyconfigs. """

    modulelist = module_obj.get_modulefile_path()

    ec_list,no_ec_list = find_easyconfigs_from_modulelist(modulelist)

    # if one or more easyconfigs found then display the path to easyconfigs
    if len(ec_list) > 0:
        print ("List of easyconfigs found in MODULETREES: %s"
               % (config_opts['BUILDTEST_MODULEPATH']))
        print
        print ("ID   |  easyconfig path")
        print("{:_<4} | {:_<80}".format ("", ""))
        count = 1
        for ec in ec_list:
            print ("{:4} | {:15}".format(count, ec))
            count = count + 1
    else:
        print ("No easyconfigs found!")

    if len(no_ec_list) > 0:
        fname = "/tmp/easyconfigs.txt"
        print ("\n")
        print ("buildtest was unable to find easyconfigs for particular modules")
        print (f"Check file: {fname} for more details")
        fd = open(fname,"w")
        print("\n")
        fd.write("Unable to find easyconfigs for the following, please "
               + "investigate this issue! \n")

        for no_ec in  no_ec_list:
            fd.write(no_ec+"\n")

        fd.close()
    print (f"Total easyconfigs found: {len(ec_list)}")
    print (f"Total module files searched: {len(modulelist)}")

