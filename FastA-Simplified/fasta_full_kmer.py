import itertools
import re

# A function that reads fasta files and stores every sequence and its name into tuples and store them into a list.
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

# A function that generates every possible k-mer and stores them with their positions.
def indexKmers(sequence, k):
    positions = {}
    for i in range(len(sequence) - k + 1):
        kmer = sequence[i:i + k]
        if kmer not in positions:
            positions[kmer] = []
        positions[kmer].append(i)
    return positions

# A function that calculates the alignment scores between a query sequence and a database sequence.
def calculate_S(query_kmers, database_kmers, query_len, database_len):
    S = [0] * (query_len + database_len - 1)  # create a S array to store alignment scores

    for kmer in query_kmers:
        if kmer in database_kmers:
            for q_pos in query_kmers[kmer]:
                for d_pos in database_kmers[kmer]:
                    d = (q_pos - d_pos) + (database_len - 1)  # calculate the position in the S array
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
        if abs(filtered_indices[i] - filtered_indices[i-1]) <= g:  # check if the current index is within the maximum gap size (positive or negative) 
            current_score += S[filtered_indices[i]]  
        else:
            total_score += current_score 
            current_score = S[filtered_indices[i]] 
    total_score += current_score  
    return total_score  

# A function that processes each gene sequence to find matches with the query sequence.
def matching(query_sequence, gene_sequences, n, m, g, score_threshold):
    query_len = len(query_sequence)
    query_kmers = indexKmers(query_sequence, n)  # index kmers of the query sequence
    results = []

    for gene_name, gene_sequence in gene_sequences:
        database_kmers = indexKmers(gene_sequence, n)  # index kmers of the gene sequence
        S = calculate_S(query_kmers, database_kmers, query_len, len(gene_sequence))  # calculate alignment scores between the query and the gene sequence
        filtered_indices = filter_S(S, m)  # filter regions with scores larger than the minimum size criterion (m)
        total_score = join_regions(filtered_indices, S, g)

        if total_score >= score_threshold:
            results.append((gene_name, total_score))

    return results

def main(filepath1, filepath2):
    query_sequence_data = loadfile(filepath1)
    gene_sequences_data = loadfile(filepath2)

    query_sequence = query_sequence_data[0][1]  # because we know there is only one sequence in the query file
    gene_sequences = gene_sequences_data

    # Define parameters for the alignment process
    n = 5  # length of the matched word (kmers)
    m = 20  # minimum size of matched diagonals (S[i])
    g = 3  # maximum gap size before joining regions
    score_threshold = 0.5 * len(query_sequence)  # threshold for the total score

    matching_sequences = matching(query_sequence, gene_sequences, n, m, g, score_threshold)

    if matching_sequences:
        for gene_name, total_score in matching_sequences:
            print(f"Matched sequence: {gene_name} with a total score of {total_score}")
        highest_match = max(matching_sequences, key=lambda x: x[1])  # find the sequence with the highest score
        print(f"Highest matching sequence: {highest_match[0]} with a score of {highest_match[1]}")
    else:
        print("No matching sequences found.")
