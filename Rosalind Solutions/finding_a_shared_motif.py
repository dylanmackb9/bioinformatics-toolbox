from scripts.utils import read_fasta
import os
import pandas as pd

data_path = os.path.expanduser("~/Development/gitreps/bioinformatics-toolbox/data/rosalind_grph.txt")

## Ingest data
string_data = read_fasta(data_path)

def findsuffixes(string):
    """
    Returns suffix of length len of given string
    """
    suffixes = []
    for i in range(len(string)):
        suffixes.append((string[i:], i))

    suffixes.sort()  # Sort lexicographically 
    suffix_array = [index for suf, index in suffixes]

    return suffix_array


def is_common_substring(substring, strings):
    """
    Check if a substring exists in all strings
    """
    for string in strings:
        if substring not in string:
            return False
    return True


def check_substrings(smallest_string, suffix_array, strings, length):
    """
    Check if any substring of the given length is common across all strings
    """
    
    seen_substrings = set()
    for start in suffix_array:
        # Get the substring of the given length
        if start + length <= len(smallest_string):
            substring = smallest_string[start:start + length]
            seen_substrings.add(substring)

    # Check if any of these substrings exist in all strings
    for substring in seen_substrings:
        if is_common_substring(substring, strings):
            return substring
    return None


def answer(data):

    strings = list(data.values())
    strings_sorted = sorted(strings, key=len)
    smallest_suf_array = findsuffixes(strings_sorted[0])
    smallest_string = strings_sorted[0]

    low = 0
    high = len(strings_sorted[0])
    while low <= high:
        mid = (low + high) // 2  # Length to address
        common_sub = check_substrings(smallest_string, smallest_suf_array, strings_sorted, mid)

        if common_sub:
                # Found a common substring of this length, try for longer ones
                result = common_sub
                low = mid + 1
        else:
            # No common substring of this length, try shorter ones
            high = mid - 1

    return result
 
