# -*- coding: utf-8 -*-
"""
Created on Mon May 23 14:06:52 2016

@author: rishijavia and thatbudakguy
"""
import sys, os, unittest
sys.path.append(os.path.join(os.path.dirname(sys.path[0]),'lib'))
sys.path.append(os.path.join(os.path.dirname(sys.path[0]),'test'))
import biomath, bioio
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
        self.assertDictEqual(bioio.readCSV(example_csv_files),expected_csv_input)
        with self.assertRaises(SystemExit):
            bioio.readCSV(['sample1.csv','path/sample2.csv'])
        with self.assertRaises(SystemExit):
            bioio.readCSV(['sample1.csv','sample2.txt'])

    def test_readTXT(self):
        self.assertDictEqual(bioio.readTXT(example_txt_files),expected_txt_input)
        with self.assertRaises(SystemExit):
            bioio.readTXT(['sample1.txt','path/sample2.txt'])
        with self.assertRaises(SystemExit):
            bioio.readTXT(['sample1.csv','sample2.txt'])

    def test_readFASTA(self):
        self.assertDictEqual(bioio.readFASTA(example_fasta_files),expected_fasta_input)
        with self.assertRaises(SystemExit):
            bioio.readFASTA(['sample1.fasta','path/sample2.fasta'])
        with self.assertRaises(SystemExit):
            bioio.readFASTA(['sample1.fasta','sample2.txt'])

    def test_splitCSV(self):
        example_input_csv = bioio.readCSV(['sample1.csv'])
        example_input_csv = bioio.splitCSV(example_input_csv['sample1'])
        self.assertDictEqual(example_input_csv,expected_split_data)

    def test_splitFASTA(self):
        example_input_fasta = bioio.readFASTA(['sample1.fasta'])
        example_input_fasta = bioio.splitFASTA(example_input_fasta['sample1'])
        self.assertDictEqual(example_input_fasta,expected_split_data)

    def test_splitLinearSeqids(self):
        self.assertEqual(bioio.splitLinearSeqids(example_linear_seqids),expected_split_linear_seqids)

    def test_addVenomCodes(self):
        self.assertEqual(bioio.addVenomCodes(no_venomcodes, "TST"),has_venomcodes)
        with self.assertRaises(SystemExit):
            bioio.addVenomCodes(no_venomcodes, "TEST")

    def test_trimVenomCodes(self):
        self.assertEqual(bioio.trimVenomCodes(has_venomcodes),no_venomcodes)

    def test_addGreaterThans(self):
        self.assertEqual(bioio.addGreaterThans(some_greaterthans),all_greaterthans)
        self.assertEqual(bioio.addGreaterThans(no_greaterthans),all_greaterthans)

    def test_trimGreaterThans(self):
        self.assertEqual(bioio.trimGreaterThans(some_greaterthans),no_greaterthans)
        self.assertEqual(bioio.trimGreaterThans(all_greaterthans),no_greaterthans)

    def test_replaceSCodes(self):
        self.maxDiff = None
        self.assertEqual(bioio.replaceSCodes(no_scodes), has_scodes)

    def test_writeCSV(self):
        read_csv_data = bioio.readCSV(['sample1.csv'])['sample1']
        bioio.writeCSV('rewritten_sample1.csv',read_csv_data)
        self.assertEqual(bioio.readCSV(['rewritten_sample1.csv'])['rewritten_sample1'],read_csv_data)
        os.remove('rewritten_sample1.csv')

    def test_writeTXT(self):
        read_txt_data = bioio.readTXT(['sample1.txt'])['sample1']
        bioio.writeTXT('rewritten_sample1.txt',read_txt_data)
        self.assertEqual(bioio.readTXT(['rewritten_sample1.txt'])['rewritten_sample1'],read_txt_data)
        os.remove('rewritten_sample1.txt')

    def test_writeFASTA(self):
        read_fasta_data = bioio.readFASTA(['sample1.fasta'])['sample1']
        read_fasta_data_seqids = bioio.splitFASTA(read_fasta_data)['output_seq_ids']
        read_fasta_data_seqs = bioio.splitFASTA(read_fasta_data)['output_seqs']
        bioio.writeFASTA('rewritten_sample1.fasta',read_fasta_data_seqids,read_fasta_data_seqs)
        self.assertEqual(bioio.readFASTA(['rewritten_sample1.fasta'])['rewritten_sample1'],read_fasta_data)
        os.remove('rewritten_sample1.fasta')

if __name__ == '__main__':
    mathsuite = unittest.TestLoader().loadTestsFromTestCase(TestBioMath)
    iosuite = unittest.TestLoader().loadTestsFromTestCase(TestBioIO)
    unittest.TextTestRunner(verbosity=2).run(mathsuite)
    unittest.TextTestRunner(verbosity=2).run(iosuite)
