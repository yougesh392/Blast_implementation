#!/usr/bin/python
# -*- coding: utf-8 -*-
from Bio import SeqIO
for i in range(3, 8):

    # getting the fasta file provided by user

    myfile = SeqIO.parse('sequence.fasta', 'fasta')
    seq_id = 0
    d = {}
    for record in myfile:
        sequence = record.seq
        seq_len = len(sequence)
        count = 0

        # kmer length

        kmer = i
        seq_id += 1
        d[(seq_id, count)] = record.id
        for seq in list(range(seq_len - (kmer - 1))):
            count = count + 1
            my_kmer = sequence[seq:seq + kmer]
            d[(seq_id, count)] = my_kmer

    fo = open('Database/file%s.txt' % i, 'w')

    for (k, v) in d.items():

        # creating Database File

        fo.write(str(k[0]) + ' ' + str(k[1]) + ' ' + str(v) + '\n')

    fo.close()

			