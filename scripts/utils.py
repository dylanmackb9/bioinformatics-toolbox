

def read_fasta(filename):
    """
    Method that reads FASTA formatted DNA strings.

    """
    f = open(filename, 'r')

    data_dict = {}
    buf = f.readline().rstrip()
    while buf:
        seq_name, seq = buf[1:], ''
        buf = f.readline().rstrip()
        while not buf.startswith('>') and buf:
            seq = seq + buf
            buf = f.readline().rstrip()
        data_dict[seq_name] = seq

    f.close()

    return data_dict