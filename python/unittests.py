# -*- coding: utf-8 -*-
"""
Created on Mon May 23 14:06:52 2016

@author: rishijavia
"""

import biomath
import unittest

class testBioMath(unittest.TestCase):

    def test_findLongestSeq(self):

        # setup test data
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

        self.assertEqual(biomath.findLongestSeq(example_rows),expected_longest_rows)

    def test_reduceNames(self):

        # setup test data
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

        self.assertEqual(biomath.reduceNames(example_seqid,example_data),expected_reduced_names)

    def test_findMissingSeqs(self):

        # findMissingSeqs
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

        self.assertEqual(biomath.findMissingSeqs(example_names_list,example_data_list),expected_missing_seqs)

if __name__ == '__main__':
    unittest.main()
