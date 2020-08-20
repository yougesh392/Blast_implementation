#!/usr/bin/python
# -*- coding: utf-8 -*-
from Bio import SeqIO

print('Enter Number of kmers')
num = input()
my_dict = {}
with open('Database/file%s.txt' % num, 'r+') as f:
    for line in f:
        kmer = line.split(' ')
        my_dict[str(kmer[0]), str(kmer[1])] = str(kmer[2])

# query sequence provided by user

myfile = SeqIO.parse('user.fasta', 'fasta')
seq_id = 0
count = 0
user_dict = {}
for record in myfile:
    sequence = record.seq
    seq_len = len(sequence)

    # kmer length

    kmer = int(num)
    seq_id += 1
    user_dict[(seq_id, count)] = record.id
    for seq in list(range(seq_len - (kmer - 1))):
        count = count + 1
        user_kmer = sequence[seq:seq + kmer]
        user_dict[(seq_id, count)] = user_kmer
print('Query sequence id')
print(user_dict[1, 0])


			