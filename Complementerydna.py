# 7 kyu / Complementary DNA
# Details
#   https://www.codewars.com/kata/complementary-dna

pairs = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}


def dna_strand(dna):
    return ''.join([pairs[x] for x in dna])
