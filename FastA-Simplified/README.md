## FastA-Inspired Sequence Matching (Project)

This project implements two simplified versions of the **FastA algorithm** for local sequence alignment between biological sequences. FastA is a classical algorithm in bioinformatics used to find regions of similarity between a **query sequence** and a **database of target sequences**, enabling fast and efficient homology searches.

---

### 🔍 Project Goals

- Efficiently find the most similar sequence(s) in a FASTA-formatted database given a query sequence.
- Explore two different strategies:
  1. **Full k-mer Diagonal Matching** (accurate, FastA-like)
  2. **Most Common k-mer Heuristic** (fast, approximate)

---

## 🧪 Input Format

- Both scripts use standard **FASTA files**.
- Each file can contain one or more sequences.
