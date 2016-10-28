# -*- coding: utf-8 -*-
"""
Created on Mon May 23 14:06:52 2016

@author: rishijavia and thatbudakguy
"""

import bioio
import re

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

def removeDuplicateSequences(rows):
    output_data = []
    for i in range(1,len(rows)):
        col2 = rows[i][1]
        if (col2 in output_data):
            continue
        else:
            output_data.append(col2)
    return output_data

def reduceNames(search_seq_ids, db_seq_ids, db_seqs, venom_switch = None):
    import sys
    output_seq_ids = []
    output_seqs = []
    seqs_dict = {}
    for i in range(len(db_seq_ids)):
        seqs_dict[db_seq_ids[i]] = db_seqs[i]
    print "\n"
    if venom_switch == 1:
        total = float(len(search_seq_ids))
        for i in range(0, len(search_seq_ids)):
            progress = str(round(((i/total)*100),2)) + " % processed "
            sys.stdout.write("\r")
            sys.stdout.write(progress)
            if search_seq_ids[i][:-4] in db_seq_ids:
                sys.stdout.write(search_seq_ids[i])
                output_seq_ids.append(search_seq_ids[i])
                output_seqs.append(seqs_dict[search_seq_ids[i][:-4]])
            sys.stdout.flush()
    else:
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

    print "\n"
    return {'output_seq_ids':output_seq_ids,'output_seqs':output_seqs}

def findMissingSeqs(names_list, data_list):
    output = []
    for val in names_list:
        if val in data_list:
            continue
        else:
            output.append(val)
    print("Found " + str(len(output)) + " missing sequences.")
    return output

def findMatchingSeqs(names_list, data_list):
    output = []
    for val in names_list:
        if val in data_list:
            output.append(val)
        else:
            continue
    print("Found " + str(len(output)) + " matching sequences.")
    return output

def trimShortSeqs(fasta_data, length):
    output = {}
    for seq_id, seq in fasta_data.iteritems():
        if len(seq) >= length:
            output[seq_id] = seq
        else:
            continue
    output_seq_ids = output.keys()
    output_seqs = output.values()
    print("Got back " + str(len(output)) + " sequences.")
    return {'output_seq_ids':output_seq_ids, 'output_seqs':output_seqs}

def reduceIsoforms(fasta_data):
    output = {}
    for seq_id, seq in fasta_data.iteritems():
        if re.match('\w*i1\W\w\W\w*', seq_id):
            output[seq_id] = seq

    for seq_id, seq in fasta_data.iteritems():
        string = seq_id.split('_i')
        flag = 0
        for sid, s in output.iteritems():
            if string[0] in sid:
                flag = 1
                break
        if flag == 1:
            continue
        else:
            output[seq_id] = seq

    output_seq_ids = output.keys()
    output_seqs = output.values()
    return {'output_seq_ids':output_seq_ids,'output_seqs':output_seqs}

def findMissingFromDB(db_dict, blast_dict):
    db_dict_remove = []
    for i in range(len(db_dict)):
        if db_dict.keys()[i] in blast_dict:
            db_dict_remove.append(db_dict.keys()[i])
        else:
            continue
    for key in db_dict_remove:
        del db_dict[key]
    return db_dict
