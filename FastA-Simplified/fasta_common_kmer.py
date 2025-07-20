import itertools
import re

# A function that reads fasta files and stores every sequence and its name into tuples and stores them into a list.
def loadfile(file_path):
    sequences = []
    with open(file_path, 'r') as file:
        current_seq_name = ""
        current_seq = []
        for line in file:
            if line.startswith('>'):
                if current_seq_name:
                    sequences.append((current_seq_name, ''.join(current_seq)))
                current_seq_name = line[1:].strip()  # for extracting the sequence name without '>'
                current_seq = []
            else:
                current_seq.append(line.strip())
        if current_seq_name:
            sequences.append((current_seq_name, ''.join(current_seq)))
    return sequences

# A function that generates k-mers from a sequence and stores their positions.
def indexKmers(sequence, k):
    positions = {}
    for i in range(len(sequence) - k + 1):
        kmer = sequence[i:i+k]
        if kmer not in positions:
            positions[kmer] = []
        positions[kmer].append(i)
    return positions

# A function to get the most common k-mers in a sequence without using defaultdict.
def get_most_common_kmers(sequence, k, top_n=100):
    kmer_freq = {}
    for i in range(len(sequence) - k + 1):
        kmer = sequence[i:i+k]
        if kmer not in kmer_freq:
            kmer_freq[kmer] = 0
        kmer_freq[kmer] += 1
    most_common_kmers = sorted(kmer_freq, key=kmer_freq.get, reverse=True)[:top_n]  # sort k-mers by frequency and get the top_n most common k-mers
    return most_common_kmers

# A function that calculates the alignment scores between a query sequence and a database sequence.
def calculate_S(query_kmers, database_kmers, k, l, query_len):
    S = [0] * (query_len + l - 1)  # create an S array to store alignment scores
    for kmer in query_kmers:
        if kmer in database_kmers:
            for q_pos in query_kmers[kmer]:
                for d_pos in database_kmers[kmer]:
                    d = (q_pos - d_pos) + (l - 1)  # calculate the position in the S array
                    S[d] += 1
    return S

# A function that filters the indices in the S array to keep only those with scores greater than m.
def filter_S(S, m):
    return [i for i, score in enumerate(S) if score >= m]

# A function that joins close regions based on a gap threshold and calculates the total score for these regions.
def join_regions(filtered_indices, S, g):
    total_score = 0
    current_score = 0
    for i in range(1, len(filtered_indices)):
        if abs(filtered_indices[i] - filtered_indices[i-1]) <= g:  # check if the current index is within the maximum gap size
            current_score += S[filtered_indices[i]]
        else:
            total_score += current_score
            current_score = S[filtered_indices[i]]
    total_score += current_score
    return total_score

# A function that processes each gene sequence to find matches with the query sequence.
def matching(query_sequence, gene_sequences, k, m, g, score_threshold, top_n):
    query_len = len(query_sequence)
    results = []

    query_kmers = indexKmers(query_sequence, k)  # index k-mers for the query sequence
    most_common_query_kmers = get_most_common_kmers(query_sequence, k, top_n)

    for gene_name, gene_sequence in gene_sequences:
        database_kmers = indexKmers(gene_sequence, k)  # index k-mers for the database sequence
        S = calculate_S(query_kmers, database_kmers, k, len(gene_sequence), query_len)  # calculate alignment scores
        filtered_indices = filter_S(S, m)  # filter regions with scores larger than the minimum size criterion (m)
        total_score = join_regions(filtered_indices, S, g)

        if total_score >= score_threshold:
            results.append((gene_name, total_score))

    return results

def main(filepath1, filepath2, k, top_n):
    query_sequence_data = loadfile(filepath1)
    gene_sequences_data = loadfile(filepath2)

    query_sequence = query_sequence_data[0][1]  # because we know there is only one sequence in query file
    gene_sequences = gene_sequences_data

    # define parameters for the alignment process
    m = 20  # minimum size of matched diagonals (S[i])
    g = 3  # maximum gap size before joining regions
    score_threshold = 0.5 * len(query_sequence)  # threshold for the total score

    matching_sequences = matching(query_sequence, gene_sequences, k, m, g, score_threshold, top_n)

    print(f"For k = {k} and top_n = {top_n}, the results are:")
    if matching_sequences:
        for gene_name, total_score in matching_sequences:
            print(f"Matched sequence: {gene_name} with a total score of {total_score}")
        highest_match = max(matching_sequences, key=lambda x: x[1])  # find the sequence with the highest score
        print(f"Highest matching sequence: {highest_match[0]} with a score of {highest_match[1]}")
    else:
       print("No matching sequences found.")
    print()
