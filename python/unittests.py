# -*- coding: utf-8 -*-
"""
Created on Mon May 23 14:06:52 2016

@author: rishijavia
"""

import biomath
import unittest
from testdata import *


class TestBioMath(unittest.TestCase):

    def test_findLongestSeq(self):
        self.assertEqual(biomath.findLongestSeq(example_rows),expected_longest_rows)

    def test_reduceNames(self):
        self.assertEqual(biomath.reduceNames(example_seqid,example_data),expected_reduced_names)

    def test_findMissingSeqs(self):
        self.assertEqual(biomath.findMissingSeqs(example_names_list,example_data_list),expected_missing_seqs)

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestBioMath)
    unittest.TextTestRunner(verbosity=2).run(suite)
