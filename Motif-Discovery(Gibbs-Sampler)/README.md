# Motif Discovery using Gibbs Sampler

## Overview

This project implements the Gibbs Sampler algorithm for discovering hidden motifs in DNA sequences. The Gibbs Sampler is a statistical method used to iteratively sample from a probability distribution, which is particularly useful for motif discovery in bioinformatics.

## Key Concepts

- **Gibbs Sampler**: An iterative algorithm used to approximate the distribution of a set of variables when direct sampling is difficult.
- **Motif Discovery**: The process of identifying recurring patterns or motifs in DNA sequences that may have biological significance.
- **Position Weight Matrix (PWM)**: A matrix representing the frequency of each nucleotide at each position in a motif, used to score potential motif instances.

## Applications

The Gibbs Sampler is widely used in bioinformatics for:

- **Sequence Alignment**: Identifying conserved regions across multiple sequences.
- **Gene Regulation**: Discovering regulatory elements like transcription factor binding sites.
- **Genome Annotation**: Annotating functional elements in genomic sequences.

## Implementation Details

### Part 1: Gibbs Sampler Implementation

- **Input**: A dataset of DNA sequences.
- **Process**:
  1. Initialize random k-mers in the sequences.
  2. Iteratively update the k-mers based on the Position Weight Matrix (PWM) until convergence.
  3. Calculate the information content of the discovered PWMs.
- **Output**: The most probable motifs and their corresponding PWMs.

### Part 2: Information Content Calculation

- **Information Content**: A measure of the conservation of nucleotides at each position in the motif, calculated from the PWM.

## Example Data and Outputs

### Example Sequences

The dataset consists of 50 short DNA sequences with an embedded motif. The Gibbs Sampler is used to discover this motif for various values of \( k \) (motif length).

#### Example Output for \( k = 3 \):

- **PWM**:
  ```python
  [[0., 0., 0.06],
  [0., 0., 0.46],
  [0., 1., 0.02],
  [1., 0., 0.46]]

- **Motifs**: `['TGT', 'TGC', 'TGT', ...]`

## Tools Used

- **Python**: The primary programming language used for implementation.
- **NumPy**: Used for numerical operations and matrix manipulations.
- **Regex**: Used for pattern matching and data processing.

## Repository Structure

- **code/**: Contains the Python scripts for implementing the Gibbs Sampler.
- **data/**: Includes example DNA sequences used in the analysis.
- **documentation/**: Detailed reports and findings from the analysis.
- **README.md**: This file, providing an overview of the project.

## Setup Instructions

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/your-repository-name.git
   cd your-repository-name/Motif-Discovery

2. **Install Dependencies**:
   ```bash
   pip install numpy regex
   
3. **Run the Code**:
   ```bash
   python code/gibbs_sampler.py

4. **Custom Usage**:
   Modify the sequence variable in the script or pass it as an argument to the main function for different inputs.
