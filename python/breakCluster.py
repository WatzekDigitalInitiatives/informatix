# -*- coding: utf-8 -*-
"""
@author: rishijavia
"""

import sys
import os
sys.path.append(os.path.join(sys.path[0],'lib'))
sys.path.append(os.path.join(sys.path[0],'test'))
import bioio
import biomath

# strip file extension and read file
read_csv = bioio.readCSV([sys.argv[-1]])
input_csv_name = sys.argv[-1][:-4]
input_csv_data = read_csv[input_csv_name]

# break the clusters
output_data = bioio.breakClusters(input_csv_data)

# write the resulting data to files
output_txt_name = input_csv_name+"_brokenCluster.txt"
bioio.writeTXT(output_txt_name,output_data)