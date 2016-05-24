# -*- coding: utf-8 -*-
"""
Created on Tues May 24 09:24:52 2016

@author: thatbudakguy
"""

# setup test data

#
# findLongestSeq()
#

global example_rows
global expected_longest_rows

example_rows = [
['sample1','FJKDHGSKJGHLSKULSDUHRGLSIHUG'],
['sample1','KLSURHGLFIAUHRFLAIWUEHFLAIWUEHFALWEI'],
['sample2','CIVAWUHEFLIAUSBECLIASUEFHLAKEUFHLASIEUFGAKLSEFULAEWK'],
['sample2','CIVAWUHEFLAKLSEFULAEWK'],
['sample3','KSLADJFHALKSUDHFALKSDUHFALKS'],
['sample3','DSLKFAJLSFJ'],
['sample4','SDJKFHALSKDUFHASLKFHASLKJFHASDLKJH'],
['sample5','SKDJFHALKSDJFHFJKGHSLDKFGJHDSKLFJGHSLDKF'],
['sample6','DSSDHJFBAGKJDHFKSDGHK']
]

expected_longest_rows = [
['sample1','KLSURHGLFIAUHRFLAIWUEHFLAIWUEHFALWEI'],
['sample2','CIVAWUHEFLIAUSBECLIASUEFHLAKEUFHLASIEUFGAKLSEFULAEWK'],
['sample3','KSLADJFHALKSUDHFALKSDUHFALKS'],
['sample4','SDJKFHALSKDUFHASLKFHASLKJFHASDLKJH'],
['sample5','SKDJFHALKSDJFHFJKGHSLDKFGJHDSKLFJGHSLDKF'],
['sample6','DSSDHJFBAGKJDHFKSDGHK']
]

#
# reduceNames()
#

global example_seqid
global example_data
global expected_reduced_names

example_seqid = [
'sample1',
'sample2',
'sample3',
'sample4',
'sample5',
'sample6'
]

example_data = [
'>sample1',
'FJKDHGSKJGHLSKULSDUHRGLSIHUG',
'>sample2',
'CIVAWUHEFLIAUSBECLIASUEFHLAKEUFHLASIEUFGAKLSEFULAEWK',
'>sample3',
'KSLADJFHALKSUDHFALKSDUHFALKS',
'>sample4',
'SDJKFHALSKDUFHASLKFHASLKJFHASDLKJH',
'>sample5',
'SKDJFHALKSDJFHFJKGHSLDKFGJHDSKLFJGHSLDKF',
'>sample6',
'DSSDHJFBAGKJDHFKSDGHK',
'>sample7',
'SDKJFHALKSDFBASLKJFBASLDKDSAKLJDS'
]

expected_reduced_names = {
'>sample1':'FJKDHGSKJGHLSKULSDUHRGLSIHUG',
'>sample2':'CIVAWUHEFLIAUSBECLIASUEFHLAKEUFHLASIEUFGAKLSEFULAEWK',
'>sample3':'KSLADJFHALKSUDHFALKSDUHFALKS',
'>sample4':'SDJKFHALSKDUFHASLKFHASLKJFHASDLKJH',
'>sample5':'SKDJFHALKSDJFHFJKGHSLDKFGJHDSKLFJGHSLDKF',
'>sample6':'DSSDHJFBAGKJDHFKSDGHK'
}

#
# findMissingSeqs()
#

global example_names_list
global example_data_list
global expected_missing_seqs

example_names_list = [
'sample1',
'sample2',
'sample3',
'sample3.5',
'sample4',
'sample5',
'sample6',
'sample7',
'sample8',
'sample9'
]

example_data_list = [
'sample1',
'sample2',
'sample3',
'sample4',
'sample5',
'sample6'
]

expected_missing_seqs = [
'sample3.5','sample7','sample8','sample9'
]
