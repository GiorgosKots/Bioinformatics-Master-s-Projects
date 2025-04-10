# Suffix Trie Construction

## Overview

This project explores the construction of suffix tries from suffix arrays of DNA sequences. The goal is to analyze how the complexity of a DNA sequence affects the size and structure of its suffix trie.

## Key Concepts

- **Suffix Tries**: Tree-like data structures used to represent all suffixes of a given string.
- **Suffix Arrays**: Sorted lists of all suffixes of a string, used as a basis for constructing suffix tries.
- **Sequence Complexity**: The analysis focuses on how different sequences (with varying lengths and substrings) influence the structure of the suffix trie.

## Applications of Suffix Tries

Suffix tries are highly useful in various fields, including:

- **Bioinformatics**: For sequence alignment, genome assembly, and motif finding in DNA sequences.
- **Text Processing**: Efficiently searching for patterns and substrings within large text datasets.
- **Data Compression**: Identifying repeated patterns to achieve better compression ratios.
- **Computational Biology**: Analyzing genetic sequences to identify genes, regulatory elements, and mutations.

## Tools Used

- **Python**: The primary programming language used for implementation.
- **Graphviz**: Used for visualizing the suffix tries.

## Repository Structure

- **code/**: Contains the Python scripts for generating suffixes, building the trie, and visualizing it.
- **data/**: Includes example DNA sequences used in the analysis.
- **documentation/**: Detailed reports and findings from the analysis.
- **README.md**: This file, providing an overview of the project.

## Setup Instructions

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/GiorgosKots/Bioinformatics-Master-s-Projects.git
   cd Bioinformatics-Master-s-Projects/Suffix-Trie-Construction
