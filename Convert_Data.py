"""
Translation and End-to-End Learning with a Sequence to Sequence Network and Attention
*************************************************************
**Author**: `Amir Shirian <https://github.com/>`_
In this Code we will be converting a Translation database into End-to-End Learning database.
"""

import numpy as np
import re
import unicodedata


filename='deu.txt'


def normalizeString(s):
    s = unicodeToAscii(s.lower().strip())
    s = re.sub(r"([.!?])", r" \1", s)
    s = re.sub(r"[^a-zA-Z.!?]+", r" ", s)
    return s
def unicodeToAscii(s):
    return ''.join(
        c for c in unicodedata.normalize('NFD', s)
        if unicodedata.category(c) != 'Mn'
    )
lines = open(filename, encoding='utf-8').\
        read().strip().split('\n')
pairs = [[normalizeString(s) for s in l.split('\t')] for l in lines]
out = []
for pair in pairs:
    pair[1]=pair[0]   
    out.append(pair)

outname = 'eng-eng.txt'
np.savetxt(outname, out, fmt='%s', delimiter='\t', newline='\n')