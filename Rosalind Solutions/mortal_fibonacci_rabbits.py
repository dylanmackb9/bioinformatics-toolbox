from scripts.utils import read_fasta
import os
import pandas as pd

data_path = os.path.expanduser("~/Development/gitreps/bioinformatics-toolbox/data/rosalind_cons.txt")

## Ingest data
string_data = read_fasta(data_path)

def rabbit_population(n, M):
    # Initialize the DP array for age groups
    dp = [0] * M
    dp[0] = 1  # At month 1, there is 1 pair of baby rabbits
    
    # Iterate through months
    for month in range(2, n + 1):
        # Compute new babies
        new_babies = sum(dp[1:])  # All non-baby rabbits reproduce
        
        # Age the rabbits
        for i in range(M-1, 0, -1):
            dp[i] = dp[i-1]
        
        # Update newborns
        dp[0] = new_babies
    
    # Total population is the sum of all age groups
    return sum(dp)
