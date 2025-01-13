from scripts.utils import read_fasta
import os
import pandas as pd

data_path = os.path.expanduser("~/Development/gitreps/bioinformatics-toolbox/data/rosalind_grph.txt")

## Ingest data
string_data = read_fasta(data_path)

def overlap_graphs(data, k):
    adjacency_list = []
    data = {v: k for k, v in data.items()}  # inverting
    
    for strand in data.keys():
        connections = [st for st in data.keys() if (st != strand) and (st[0:3] == strand[-3:])]
        [adjacency_list.append((data[strand], data[i])) for i in connections]

    return adjacency_list
