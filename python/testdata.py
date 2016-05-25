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
# splitLinearSeqids()
#

global example_linear_seqids
global expected_split_linear_seqids

example_linear_seqids = [
'sample1',
'sample2',
'sample3>sample3429',
'sample4>sample3s>__45-dfs_d34|df3',
'sample5>sdf>32off>dfsu0sd$',
'sample6>r32n@'
]

expected_split_linear_seqids = [
'sample1',
'sample2',
'sample3',
'sample3429',
'sample4',
'sample3s',
'__45-dfs_d34|df3',
'sample5',
'sdf',
'32off',
'dfsu0sd$',
'sample6',
'r32n@'
]

#
# reduceNames()
#

global example_search_seqids
global example_db_seqids
global example_db_seqs
global expected_reduced_data

example_search_seqids = [
'sample1',
'sample2',
'sample7',
'sample4',
'sample5',
'sample8'
]

example_db_seqids = [
'sample1',
'sample2',
'sample3',
'sample4',
'sample5',
'sample6',
'sample7',
'sample8'
]

example_db_seqs = [
'FJKDHGSKJGHLSKULSDUHRGLSIHUG',
'CIVAWUHEFLIAUSBECLIASUEFHLAKEUFHLASIEUFGAKLSEFULAEWK',
'KSLADJFHALKSUDHFALKSDUHFALKS',
'SDJKFHALSKDUFHASLKFHASLKJFHASDLKJH',
'SKDJFHALKSDJFHFJKGHSLDKFGJHDSKLFJGHSLDKF',
'DSSDHJFBAGKJDHFKSDGHK',
'SDKJFHALKSDFBASLKJFBASLDKDSAKLJDS',
'DFLKJSDFDJKGHSLKDHGSKDJHGKSDJHFGSLKDJHFGG'
]

expected_reduced_data = {
'output_seq_ids':[
'sample1',
'sample2',
'sample4',
'sample5',
'sample7',
'sample8'],
'output_seqs':[
'FJKDHGSKJGHLSKULSDUHRGLSIHUG',
'CIVAWUHEFLIAUSBECLIASUEFHLAKEUFHLASIEUFGAKLSEFULAEWK',
'SDJKFHALSKDUFHASLKFHASLKJFHASDLKJH',
'SKDJFHALKSDJFHFJKGHSLDKFGJHDSKLFJGHSLDKF',
'SDKJFHALKSDFBASLKJFBASLDKDSAKLJDS',
'DFLKJSDFDJKGHSLKDHGSKDJHGKSDJHFGSLKDJHFGG'
]
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
