# -*- coding: utf-8 -*-
"""
Created on Mon May 23 14:06:52 2016

@author: rishijavia
"""

python sys.path.append(os.path.dirname(sys.path[o]),'lib')
python sys.path.append(os.path.dirname(sys.path[o]),'test')
import sys, os, biomath, bioio, unittest
from testdata import *


class TestBioMath(unittest.TestCase):

    def test_findLongestSeq(self):
        self.assertEqual(biomath.findLongestSeq(example_rows),expected_longest_rows)

    def test_reduceNames(self):
        reduced_data = biomath.reduceNames(example_search_seqids,example_db_seqids,example_db_seqs)
        self.assertEqual(reduced_data['output_seq_ids'],expected_reduced_data['output_seq_ids'])
        self.assertEqual(reduced_data['output_seqs'],expected_reduced_data['output_seqs'])

    def test_findMissingSeqs(self):
        self.assertEqual(biomath.findMissingSeqs(example_names_list,example_data_list),expected_missing_seqs)

class TestBioIO(unittest.TestCase):

    def test_readCSV(self):
        self.assertDictEqual(bioio.readCSV(example_csv_files),example_csv_input)
        with self.assertRaises(SystemExit):
            bioio.readCSV(['sample1.csv','path/sample2.csv'])
        with self.assertRaises(SystemExit):
            bioio.readCSV(['sample1.csv','sample2.txt'])

    def test_readTXT(self):
        self.assertDictEqual(bioio.readTXT(example_txt_files),example_txt_input)
        with self.assertRaises(SystemExit):
            bioio.readTXT(['sample1.txt','path/sample2.txt'])
        with self.assertRaises(SystemExit):
            bioio.readTXT(['sample1.csv','sample2.txt'])

    def test_readFASTA(self):
        self.assertDictEqual(bioio.readFASTA(example_fasta_files),example_fasta_input)
        with self.assertRaises(SystemExit):
            bioio.readFASTA(['sample1.fasta','path/sample2.fasta'])
        with self.assertRaises(SystemExit):
            bioio.readFASTA(['sample1.fasta','sample2.txt'])

    def test_splitLinearSeqids(self):
        self.assertEqual(bioio.splitLinearSeqids(example_linear_seqids),expected_split_linear_seqids)

if __name__ == '__main__':
    mathsuite = unittest.TestLoader().loadTestsFromTestCase(TestBioMath)
    iosuite = unittest.TestLoader().loadTestsFromTestCase(TestBioIO)
    unittest.TextTestRunner(verbosity=2).run(mathsuite)
    unittest.TextTestRunner(verbosity=2).run(iosuite)
