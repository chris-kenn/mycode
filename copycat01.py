#!/usr/bin/env python3

import shutil
import os

# Change dir
os.chdir('/home/student/mycode/')

# Copy file to new file
shutil.copy('5g_research/sdn_network.txt', '5g_research/sdn_network.txt.copy')
# copy directory and all files in the directory
shutil.copytree('5g_research/', '5g_research_backup/')

