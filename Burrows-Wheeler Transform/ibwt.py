def ibwt(bwt):
    counts = {}
    for char in bwt:
        counts[char] = counts.get(char, 0) + 1

    total = 0
    starts = {}
    for char, count in sorted(counts.items()):
        starts[char] = total
        total += count

    table = [0] * len(bwt)
    occ_count = {char: 0 for char in counts}
    for i, char in enumerate(bwt):
        table[i] = starts[char] + occ_count[char]
        occ_count[char] += 1

    for idx, val in enumerate(table):
        if idx == val:
            raise ValueError(f"Self-mapping detected at index {idx}")

    j = bwt.index('$')
    normal_seq = [''] * len(bwt)
    for i in range(len(bwt) - 1, -1, -1):
        normal_seq[i] = bwt[j]
        j = table[j]

    return ''.join(normal_seq)

