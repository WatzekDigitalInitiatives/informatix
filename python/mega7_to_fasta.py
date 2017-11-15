#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: thatbudakguy
"""
import sys
import csv

def read_csv(filename):
    """Read the csv file into a list of lines."""
    with open(filename, 'rU') as file_data:
        reader = csv.reader(file_data, delimiter=',')
        return [r for r in reader]

def get_block_size(lines):
    """Get the 'block size' of the interleaved csv."""
    for index, line in enumerate(lines):
        if line == []:
            block_size = index
            break
    return block_size

def get_taxa(lines, block_size):
    """Read the first block and extract taxa."""
    return [line[0] for line in lines[1:block_size]]

def traverse_blocks(lines, pointer, block_size, taxa, output):
    """Recursively iterate over the blocks and process them."""
    pointer = 0 if pointer is None else pointer
    output = {taxon : '' for taxon in taxa} if output is None else output
    if lines[pointer] != []:
        for ctr, index in enumerate(range(pointer + 1, pointer + block_size)):
            output[taxa[ctr]] += ''.join(lines[index][1:])
        if pointer < (len(lines) - block_size):
            pointer += block_size + 1
            traverse_blocks(lines, pointer, block_size, taxa, output)
    return output

def write_fasta(sequences, taxa, filename):
    """Write a dict of sequences and ids to a .fasta file."""
    with open(filename, "w") as fasta:
        for taxon in taxa:
            fasta.write(">"+taxon+"\n")
            fasta.write(sequences[taxon]+"\n")

if __name__ == "__main__":
    LINES = read_csv(sys.argv[-1])
    BLOCK_SIZE = get_block_size(LINES)
    TAXA = get_taxa(LINES, BLOCK_SIZE)
    SEQUENCES = traverse_blocks(LINES, None, BLOCK_SIZE, TAXA, None)
    write_fasta(SEQUENCES, TAXA, sys.argv[-1][:-4] + '.fasta')
