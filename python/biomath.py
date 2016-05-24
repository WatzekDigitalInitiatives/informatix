# -*- coding: utf-8 -*-
"""
Created on Mon May 23 14:06:52 2016

@author: rishijavia
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

def reduceNames(seqid, data):
    import sys
    output = {}
    total = float(len(data))
    for i in range(0, len(data), 2):
        id = data[i][1:]
        if id in seqid:
            progress = str(round(((i/total)*100),2)) + " % processed " + id
            sys.stdout.write("\r")
            sys.stdout.write(progress)
            sys.stdout.flush()
            output[data[i]] = data[i+1]
    return output

def findMissingSeqs(names_list, data_list):
    output = []
    for val in names_list:
        if val in data_list:
            continue
        else:
            output.append(val)
    return output
