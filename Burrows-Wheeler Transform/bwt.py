def bwt(seq):
    if '$' not in seq:
        raise ValueError("Input sequence must end with a unique sentinel character like '$'")

    table = [seq[i:] + seq[:i] for i in range(len(seq))]
    table_sorted = sorted(table)
    last_column = [row[-1] for row in table_sorted]
    return ''.join(last_column)
