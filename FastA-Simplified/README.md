## FastA-Inspired Sequence Matching (Project)

This project implements two simplified versions of the **FastA algorithm** for local sequence alignment between biological sequences. FastA is a classical algorithm in bioinformatics used to find regions of similarity between a **query sequence** and a **database of target sequences**, enabling fast and efficient homology searches.

---

### 🔍 Project Goals

- Efficiently find the most similar sequence(s) in a FASTA-formatted database given a query sequence.
- Explore two different strategies:
  1. **Full k-mer Diagonal Matching** (accurate, FastA-like)
  2. **Most Common k-mer Heuristic** (fast, approximate)

---

### ⚙️ Method 1: Full k-mer Matching (`1_fasta_full_kmer.py`)

This script implements a simplified version of the original FastA algorithm.

#### 🔬 How it works:
- Generates all k-mers from the query.
- Finds matching k-mers in each database sequence.
- Tracks the diagonal (i - j) between query and target positions.
- Filters low-scoring diagonals and joins nearby diagonals to form alignment blocks.
- Returns the target with the highest summed score.

#### 🧮 Parameters:
- `k = 5`: length of k-mers.
- `m = 20`: minimum hits on a diagonal to be considered.
- `g = 3`: maximum gap between diagonals to be merged.

#### ✅ Example Result:
```python
Matched sequence: YMR021C with a total score of 1754
Highest matching sequence: YMR021C with a score of 1754
```

### ⚡ Method 2: Most Common k-mer Heuristic (`2_fasta_common_kmer.py`)

This script implements a lightweight heuristic approach for fast filtering.

#### 🔬 How it works:
- Counts shared k-mers between query and each target sequence.
- Determines the most common shared k-mer and uses its frequency as a proxy for similarity.
- Returns the target with the highest overlap for the top shared k-mer.

#### 🧮 Parameters:

- `k = 7 or 8`: length of k-mers.
- `top_n = 50 or 100`: number of top k-mers to consider.

#### ✅ Example Result:
```python
For k = 7 and top_n = 100, the results are:
Matched sequence: YMR021C with a total score of 1734
Highest matching sequence: YMR021C with a score of 1734

For k = 8 and top_n = 100, the results are:
Matched sequence: YMR021C with a total score of 1726
Highest matching sequence: YMR021C with a score of 1726

For k = 8 and top_n = 50, the results are:
Matched sequence: YMR021C with a total score of 1726
Highest matching sequence: YMR021C with a score of 1726
```
---

## 🧪 Input Format

- Both scripts use standard **FASTA files**.
- Each file can contain one or more sequences.

---

### 📝 Conclusion

Both implementations effectively identify `YMR021C` as the highest matching sequence. The optimized version provides a much faster solution with only a slight trade-off in score. This demonstrates that focusing on the most common k-mers can greatly enhance performance while still yielding reliable results.

- **Impact of k-mer Length**: Increasing the k-mer length from 7 to 8 slightly reduces the total score from 1734 to 1726. This reduction is likely because longer k-mers are less frequent, reducing the number of matches. However, the identified sequence (`YMR021C`) remains consistent, demonstrating that increasing k improves specificity without significantly altering the outcome.

- **Impact of Top k-mers**: When using the top 100 or top 50 k-mers for `k = 8`, the total score remains the same (1726). This consistency indicates that the most significant matches are captured within the top 50 k-mers, and additional k-mers beyond this do not significantly contribute to the score. Therefore, limiting the number of k-mers can enhance efficiency without compromising accuracy.

This project showcases the balance between computational efficiency and accuracy in sequence alignment, providing insights into optimizing bioinformatics algorithms for large-scale data analysis.
