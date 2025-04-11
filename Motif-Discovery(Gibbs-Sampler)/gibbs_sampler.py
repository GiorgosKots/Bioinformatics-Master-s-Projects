import numpy as np
from random import randint
import regex as re

def loadfile(file_path):
    """Load DNA sequences from a file."""
    seqs = []
    with open(file_path, 'r') as f:
        for line in f:
            if not re.match("\n", line):
                seqs.append(line.rstrip())
    return seqs

def kmers_regen(sequences, k):
    """Generate random k-mers from sequences."""
    random_kmers = []
    for sequence in sequences:
        choose_k_mer = randint(0, len(sequence) - k)
        random_kmers.append(sequence[choose_k_mer:choose_k_mer + k])
    return random_kmers

def pwm(sequences):
    """Calculate the Position Weight Matrix (PWM) for a set of sequences."""
    nuc = ['A', 'C', 'G', 'T']
    profile = [[0 for _ in range(len(sequences[0]))] for _ in range(len(nuc))]
    for instance in sequences:
        for j in range(len(instance)):
            residue = instance[j]
            profile[nuc.index(residue)][j] += 1
    pwm_matrix = np.array(profile) / len(sequences)
    return pwm_matrix

def matching(pwm, sequence):
    """Find the k-mer in a sequence that best matches the PWM."""
    nuc = ['A', 'C', 'G', 'T']
    best_score = float("-inf")
    pwm_length = len(pwm[0])
    best_instance = None
    for i in range(len(sequence) - pwm_length + 1):
        instance = sequence[i:i + pwm_length]
        score = sum(pwm[nuc.index(instance[l])][l] for l in range(len(instance)))
        if score > best_score:
            best_instance = instance
            best_score = score
    return best_instance, best_score

def pwmEntropyInfo(pwm, k):
    """Calculate the entropy information for a PWM."""
    info = np.zeros([1, k])
    for i in range(k):
        info[0, i] = 2 - abs(sum([elem * np.log2(elem) for elem in pwm[:, i] if elem > 0]))
    sumInfo = np.sum(info)
    scaledSumInfo = sumInfo / k
    return info, sumInfo, scaledSumInfo

def GibbsSampler(k, file_path):
    """Run the Gibbs Sampler to discover motifs."""
    ScaledSumInfo = []
    sequences = loadfile(file_path)
    kmers = kmers_regen(sequences, k)
    mypwm = pwm(kmers)
    motifs_pwm = None
    motifs = None
    total_info = 0

    while len(ScaledSumInfo) == 0 or ScaledSumInfo[-1] < 1.7:
        for i in range(len(sequences)):
            best_match, _ = matching(mypwm, sequences[i])
            kmers[i] = best_match
        mypwm = pwm(kmers)
        ScaledSumInfo.append(pwmEntropyInfo(mypwm, k)[2])
        if total_info < ScaledSumInfo[-1]:
            total_info = ScaledSumInfo[-1]
            motifs_pwm = mypwm
            motifs = kmers
        if len(ScaledSumInfo) == 1000:
            break

    return motifs_pwm, total_info, motifs

if __name__ == "__main__":
    # Example usage
    file_path = "path/to/your/motifs_in_sequence.fa"
    for k in range(3, 8):
        print(f"For k-mer with k = {k}")
        print("The motifs' PWM table and the most suitable kmers are:")
        print(GibbsSampler(k, file_path))
        print()
