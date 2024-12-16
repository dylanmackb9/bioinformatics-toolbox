from scripts.utils import read_fasta
import os
import pandas as pd

data_path = os.path.expanduser("~/Development/gitreps/bioinformatics-toolbox/data/rosalind_cons.txt")

## Ingest data
string_data = read_fasta(data_path)

## Turning dict into dataframe matrix
mydf = []
for i, j in string_data.items():
    mydf.append([j])

df = pd.DataFrame(mydf)
df = df[0].apply(lambda x: pd.Series(list(x)))


def build_profile(df):

    ## Create frame

    N = df.shape[-1]
    profile_df = pd.DataFrame(0, index=['A', 'C', 'G', 'T'], columns=[i for i in range(N)])  # f'col_{i+1}'

    ## Count occurence and sum
    a_df = df.map(lambda x: 1 if x == "A" else 0).sum()
    c_df = df.map(lambda x: 1 if x == "C" else 0).sum()
    g_df = df.map(lambda x: 1 if x == "G" else 0).sum()
    t_df = df.map(lambda x: 1 if x == "T" else 0).sum()

    profile_df.loc["A"] = a_df
    profile_df.loc["C"] = c_df
    profile_df.loc["G"] = g_df
    profile_df.loc["T"] = t_df

    consensus = "".join(list(profile_df.idxmax()))

    print(consensus)
    return consensus, profile_df


con, prof = build_profile(df)



# Prepare the output format
output = []
for idx, row in prof.iterrows():
    # Format the row: index (as letter) followed by space-separated values
    formatted_row = f"{idx[0]}: " + " ".join(map(str, row))
    output.append(formatted_row)

# Write the formatted output to a file
with open('output.txt', 'w') as f:
    f.write(con)
    f.write("\n")
    f.write("\n".join(output))
