# -*- coding: utf-8 -*-
"""
Created on Mon May 23 14:06:52 2016

@author: rishijavia and thatbudakguy
"""

def findLongestSeq(rows):
    data = rows[0]
    output_data = []
    for i in range(1,len(rows)):
        col1 = rows[i][0]
        if (col1 == data[0]):
            len_data = len(data[1])
            len_test = len(rows[i][1])
            if(len_test > len_data):
                data = rows[i]
        else:
            output_data.append(data)
            data = rows[i]
    output_data.append(data)
    return output_data

def reduceNames(search_seq_ids, db_seq_ids, db_seqs):
    import sys
    output_seq_ids = []
    output_seqs = []
    total = float(len(db_seq_ids))
    for i in range(0,len(db_seq_ids)):
        progress = str(round(((i/total)*100),2)) + " % processed "
        sys.stdout.write("\r")
        sys.stdout.write(progress)
        if db_seq_ids[i] in search_seq_ids:
            sys.stdout.write(db_seq_ids[i])
            output_seq_ids.append(db_seq_ids[i])
            output_seqs.append(db_seqs[i])
        sys.stdout.flush()
    return {'output_seq_ids':output_seq_ids,'output_seqs':output_seqs}

def findMissingSeqs(names_list, data_list):
    output = []
    for val in names_list:
        if val in data_list:
            continue
        else:
            output.append(val)
    return output
