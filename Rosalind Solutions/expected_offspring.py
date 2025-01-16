from scripts.utils import read_fasta
import os
import pandas as pd


def overlap_graphs(couples, k):
    expected_vals = [1, 1, 1, 0.75, 0.5, 0]
    j = 0  # numbered couple
    E = 0  # Expected value
    for couple in couples:

        ## Expeceted value calc - iterate over number of options
        for i in range(1, couple+1):
            E += 1 * expected_vals[j] * 2
        j += 1

    return E
