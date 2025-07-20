# ALS-LLPS Protein Analysis

This project investigates statistical and sequence-based differences between ALS-associated proteins and non-ALS proteins that undergo Liquid-Liquid Phase Separation (LLPS). The focus is on analyzing Low Complexity Regions (LCRs) and Compositionally Biased Regions (CBRs) using bioinformatics tools and statistical tests.

## 🔬 Objectives
- Understand the role of LCRs and CBRs in ALS-related LLPS proteins.
- Compare ALS-LLPS proteins to non-ALS LLPS proteins using statistical methods.

## 🧰 Tools Used
- BioPython
- PlatoLoCo
- SEG (Low Complexity Regions)
- CAST (Compositionally Biased Regions)
- SciPy / NumPy / Pandas
- Matplotlib / Seaborn

## 📄 Project Report
Full background, methodology, and result interpretation are detailed in:
**[Project_Report.pdf](./Project_Report.pdf)**


## 📊 Key Results
- ALS-LLPS proteins show significantly higher LCR and CBR sequence coverage.
- ALS-related sequences are enriched in glycine and proline.
- Higher overlap exists between low-complexity and biased regions in ALS-LLPS proteins.

## 📁 Files
- `ALS_LLPS_Statistical_Analysis.ipynb`: Main Jupyter notebook for analysis.
- `Project_Report.pdf`: Full report of the study including background, methods, and results.

```bash
pip install -r requirements.txt
