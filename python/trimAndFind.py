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

#seperate out csv columns and strip venom code from first column
column1 = []
column2 = []
for row in input_csv_data:
    if len(row) == 2:
        column1.append(row[0])
        column2.append(row[1])
    else:
        column1.append(row[0])

column1_stripped = bioio.trimVenomCodes(column1)

#find if the sequence exists in column1 w/o venom code exists in column2
output = []
for i in range(len(column1)):
    if column1_stripped[i] in column2:
        output.append(column1[i])

# write the resulting data to files
output_txt_name = input_csv_name+"_matches.txt"
bioio.writeTXT(output_txt_name,output)