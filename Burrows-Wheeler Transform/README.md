# 🔁 Burrows-Wheeler Transform (BWT) & Inverse BWT

This project implements both the **Burrows-Wheeler Transform (BWT)** and its reverse (**iBWT**) in Python, commonly used in data compression and bioinformatics.

---

## 🧠 What is BWT?

The **Burrows-Wheeler Transform** rearranges a string into runs of similar characters, making it more efficient for compression. It's reversible — given the transformed string and a sentinel (like `$`), you can reconstruct the original.

## 🧪 Bioinformatics Use Cases

BWT is a core step in genome indexing (e.g., in tools like Bowtie, BWA).

Examples:

| Type     | Original Sequence | BWT Output     |
|----------|-------------------|----------------|
| DNA      | `AATCGGTTCAG$`    | `TTCAGG$AATC`  |
| RNA      | `AUGCAUGC$`       | `AUGC$AUGC`    |
| Protein  | `LVLQLKQA$`       | `LKQA$LVLQ`    |

> Always append a unique end character like `$` to ensure reversibility.

## 📂 Files

- `bwt.py` – Forward BWT transformation
- `ibwt.py` – Reverse (inverse) BWT
