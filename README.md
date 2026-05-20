# Privacy-Preserving Merchant Network Analytics for Alternative Credit Scoring

[![Journal](https://img.shields.io/badge/Journal-Nature%20Scientific%20Reports-blue)](https://www.nature.com/articles/s41598-023-36624-0)
[![Python](https://img.shields.io/badge/Python-3.9%2B-blue)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)

An end-to-end network science and machine learning feature engineering pipeline that transforms raw credit card transaction streams into privacy-preserving structural topologies to evaluate small and medium enterprise (SME) performance.

Published in **Nature Scientific Reports**, this framework implements consumer-bridge network transformations to extract alternative risk signals via graph centralities. This allows financial institutions to evaluate commercial credit health without requiring merchants to expose highly sensitive revenue footprints or proprietary tracking logs.

---

## Value Proposition & Problem Framework
Traditional small-business risk underwriting models rely heavily on highly sensitive commercial data (e.g., precise net revenue velocities, profit margins, and granular transaction volumes). Sharing these datasets with third-party underwriting organizations poses strict data security and compliance hurdles.. 

This project provides a functional solution by shifting focus from individual transaction values to a **Co-visitation Graph Topology**. By measuring how consumers move sequentially between merchants, we capture ecosystem dynamics that serve as highly reliable proxies for financial well-being.

### Architectural Components:
1. **Geospatial & Behavioral Filtering:** Cleanses raw transactional feeds by bounding coordinates within specific target administrative geo-zones and pruning anomalies based on Merchant Category Codes (MCC).
2. **Bipartite Network Projections:** Transforms customer-to-merchant transaction pairs into a weighted merchant-to-merchant network using `igraph`, where edge weights scale according to shared customer co-visitation counts.
3. **Topological Feature Engineering:** Extracts robust network centrality markers (Degree, Closeness, Betweenness, and Eigenvector metrics) alongside Shannon entropy values to represent consumer base preference diversity.
4. **Predictive Experimentation Engine:** Automates stratified k-fold cross-validation and hyperparameter optimization using Random Forests, Logistic Regression, and Gradient Boosting architectures to classify future performance trajectories.

---

## Data Pipeline & Execution Flow

```text
┌──────────────────────┐
│  Raw Transaction Log │ ──► Input stream containing customer-to-merchant interactions
└──────────────────────┘
           │
           ▼
┌──────────────────────┐
│ Spatial-Temporal     │ ──► Bounds operations within target polygons, and prunes inactive merchants
│ Filtering Framework  │
└──────────────────────┘
           │
           ▼
┌──────────────────────┐
│ Bipartite Projection │ ──► Projects bipartite user-links to merchant graph
└──────────────────────┘
           │
           ▼
┌────────────────────────────────────────────────────────┐
│             Feature Extraction Engine                  │
├────────────────────────────┬───────────────────────────┤
│ Graph Centralities         │ Node2Vec Deep Embeddings  │ ──► Extract centralities, privacy-preserving indicators,
│ (Degree, Eigen, Closeness) │ (Geometric Walk Tensors)  │     and labels
└────────────────────────────┴───────────────────────────┘
           │
           ▼
┌───────────────────────┐
│ Run & Evaluate Models │ ──► Trains ML classifiers and outputs predictive AUC bounds
└───────────────────────┘
```

---

## Performance Benchmarks & Key Insights

- **Parity on Privacy:** Classification models trained solely on anonymous structural features match the predictive accuracy (AUC/F1) of traditional baseline models built using highly sensitive revenue streams.
- **Systemic Risk Proxies:** Eigenvector centrality scores successfully isolate indirect supply-chain vulnerabilities and shifting customer trends before they register on classic monthly statements.
- **Ego-Network Resiliency:** High Shannon consumer diversity scores are a strong indicator of long-term commercial survival and revenue stability during market downturns.

---

## Citation
```bibtex
If you utilize this network modeling approach, processing logic, or alternative feature extractors in your professional research, please cite the original peer-reviewed publication:

@article{bahrami2023predicting,
  title={Predicting merchant future performance using privacy-safe network-based features},
  author={Bahrami, Mohsen and Boz, Hasan Alp and Suhara, Yoshihiko and Balcisoy, Selim and Bozkaya, Burcin and Pentland, Alex},
  journal={Scientific Reports},
  volume={13},
  number={1},
  pages={10073},
  year={2023},
  publisher={Nature Publishing Group},
  doi={10.1038/s41598-023-36624-0}
}
```

--- 

Developed under the research umbrellas of MIT Connection Science and the Institute for Data, Systems, and Society (IDSS). For integration questions, reach out to the corresponding author [Mohsen Bahrami](mailto:bahrami@mit.edu).
