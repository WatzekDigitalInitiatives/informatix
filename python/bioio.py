# -*- coding: utf-8 -*-
"""
@author: thatbudakguy
"""

"""
 READ
"""

# takes CSV file and returns list of rows
def readCSV(input_file):
    import csv
    with open(input_file, 'r') as f:
        reader = csv.reader(f, delimiter=',')
        next(reader)
        input_data = [r for r in reader]
    return input_data

# takes TXT file and returns list of lines, strips '>'
def readTXT(input_file):
    with open(input_file, 'r') as f:
        input_data = f.read().splitlines()
    input_data = trimGreaterThans(input_data)
    return input_data

# takes FASTA file and returns list of lines, strips '>'
def readFASTA(input_file):
    with open(input_file, 'r') as f:
        input_data = f.read().splitlines()
    input_data = trimGreaterThans(input_data)
    return input_data

# takes multiple FASTA files and returns one single list with all seqids combined
def combineFASTA(files):
    output_data = []
    for file in files:
        input_txt_data = readTXT(file)
        for line in input_txt_data:
            output_data.append(line)
    return output_data

"""
 MANIPULATE
"""

# takes list of rows and returns dictionary with list of sequence ids and list of sequences
def splitCSV(input_data):
    output_seq_ids = []
    output_seqs = []
    for data in input_data:
        output_seq_ids.append(data[0])
        output_seqs.append(data[1])
    return {'output_seq_ids':output_seq_ids,'output_seqs':output_seqs}

# takes list of lines and returns dictionary with list of sequence ids and list of sequences
def splitFASTA(input_data):
    output_seq_ids = []
    output_seqs = []
    for i in range(0, len(input_data), 2):
        output_seq_ids.append(input_data[i])
    for i in range(1, len(input_data), 2):
        output_seqs.append(input_data[i])
    return {'output_seq_ids':output_seq_ids,'output_seqs':output_seqs}

# takes list of lines and makes sure all sequence ids are on a new line, using remaining '>'
def splitLinearSeqids(rows):
    output_data = []
    for row in rows:
        row = row + ">"
        string = ""
        for c in row:
            if c == ">":
                output_data.append(string)
                string = ""
            else:
                string = string + c
    return output_data

# takes list of lines and appends 3-letter venom code based on filename
def addVenomCode(rows,code):
    output_data = []
    for row in rows:
        output_data.append(row + "_" + code)
    return output_data

# takes list of lines and trims 3-letter venom code
def trimVenomCodes(input_data):
    output_data = []
    for data in input_data:
        output_data.append(input_data[:-4])
    return output_data

# adds a > character to the beginning of every line if one is not present
def addGreaterThans(rows):
    output_data = []
    for row in rows:
        if row[0] != ">":
            output_data.append(">" + row)
        else:
            output_data.append(row)
    return output_data

# trims a > character at the beginning of every line if one is present
def trimGreaterThans(rows):
    output_data = []
    for row in rows:
        if row[0] == ">":
            output_data.append(row[1:])
        else:
            output_data.append(row)
    return output_data

# replaces s??? codes with sample info codes
def replaceSCodes(rows):
    scodes = {
    's001':'Dry_VG_s001',
    's002':'LAz1_VG_s002',
    's003':'LAz2_VG_s003',
    's004':'LAz3_VG_s004',
    's005':'Sic1_VG_s005',
    's006':'Sic2_VG_s006',
    's007':'Sic3_VG_s007',
    's008':'PerM1_VG_s008',
    's009':'PerM2_VG_s009',
    's010':'PerM3_VG_s010',
    's011':'PerM1_WB_s011',
    's012':'PerH_VG_s012',
    's013':'Phol_VG_s013',
    's014':'Plec_VG_s014',
    's015':'Lrec_VG_s015',
    's016':'Arch_VG_s016',
    's017':'Arch_WB_s017',
    's018':'Scy_VG_s018',
    's019':'Lrf_VG_s019',
    's020':'Lsp_VG_s020',
    's021':'PerM2_WB_s021',
    's022':'PerM3_WB_s022'
    }
    output_data = []
    switch = 0
    for row in rows:
        for key, value in scodes.iteritems():
            switch = 0
            if key in row:
                output_data.append(row.replace(key,value))
                switch = 1
                break
        if switch == 0:
            output_data.append(row)
    return output_data


"""
WRITE
"""

# takes a list of rows output_csv and writes a CSV file with name output_csv_name
def writeCSV(output_csv_name,output_csv):
    import csv
    with open(output_csv_name, "w") as file:
        writer = csv.writer(file, lineterminator='\n')
        writer.writerows(output_csv)
    print "\nWrote " + output_csv_name + "\n"

# takes a list of lines output_txt and writes a TXT file with name output_txt_name
def writeTXT(output_txt_name,output_txt):
    output_txt = addGreaterThans(output_txt)
    with open(output_txt_name, "w") as file:
        for line in output_txt:
            file.write(line+"\n")
    print "\nWrote " + output_txt_name + "\n"

# takes a list of sequence ids output_seq_ids and a list of sequences output_seqs and writes a FASTA file with name output_fasta_name
def writeFASTA(output_fasta_name,output_seq_ids,output_seqs):
    output_seq_ids = addGreaterThans(output_seq_ids)
    with open(output_fasta_name, "w") as file:
        for i in range(len(output_seqs)):
            file.write(output_seq_ids[i]+"\n")
            file.write(output_seqs[i]+"\n")
    print "\nWrote " + output_fasta_name + "\n"
