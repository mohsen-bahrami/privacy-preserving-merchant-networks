# Privacy-Preserving Merchant Network Analytics for Alternative Credit Scoring

[![Journal](https://img.shields.io/badge/Journal-Nature%20Scientific%20Reports-blue)](https://www.nature.com/articles/s41598-023-36624-0)
[![Python](https://img.shields.io/badge/Python-3.9%2B-blue)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)

An end-to-end network science and machine learning feature engineering pipeline that transforms raw, sensitive credit card transaction records into privacy-preserving structural topologies to predict the financial performance of Small and Medium Enterprises (SMEs).

Developed based on research methodologies published in **Nature Scientific Reports**, this repository implements consumer-bridge network transformations. It extracts robust alternative risk parameters using graph centrality matrices and Node2Vec geometric embeddings to assess credit risks without exposing proprietary merchant revenue balances.

---

## 📋 Value Proposition & Problem Framework
Traditional small-business risk underwriting models rely entirely on sensitive internal accounting audits (e.g., net revenue sheets, margin statements, and direct consumer transaction volumes). Sharing these granular portfolios with third-party investors creates profound data security concerns. 

This framework solves the privacy bottleneck by converting transactional logs into a **Co-visitation Graph Topology**. Rather than assessing direct dollar velocities, our model measures the structural stability, network centralities, and demographic diversity of a merchant's underlying ecosystem.

### Architectural Components:
1. **Bipartite Network Projections:** Models transaction data streams as a user-to-vendor bipartite system, projecting it onto a weighted merchant-to-merchant network where links represent shared customer volume within targeted temporal intervals.
2. **Topological Feature Engineering:** Calculates macro-level graph metrics (Degree, Closeness, Eigenvector centralities, and Shannon ego-network diversity profiles).
3. **Geometric Representational Embeddings:** Harnesses a Node2Vec framework to perform random walks across complex business networks, learning dense low-dimensional structural embeddings that capture indirect systemic relationships.

---

## Repository & Component Layout

```text
┌──────────────────────┐
│  Raw Transaction Log │ ──► Input stream containing customer-to-merchant interactions
└──────────────────────┘
           │
           ▼
┌──────────────────────┐
│ Spatial-Temporal     │ ──► Bounds operations within target urban coordinate boxes
│ Filtering Framework  │
└──────────────────────┘
           │
           ▼
┌──────────────────────┐
│ Bipartite Projection │ ──► Computes edge weights based on co-visitation linkages
└──────────────────────┘
           │
           ▼
┌────────────────────────────────────────────────────────┐
│             Feature Extraction Engine                  │
├────────────────────────────┬───────────────────────────┤
│ Graph Centralities         │ Node2Vec Deep Embeddings  │ ──► Privacy-preserving indicators
│ (Degree, Eigen, Closeness) │ (Geometric Walk Tensors)  │
└────────────────────────────┴───────────────────────────┘
```

---

## Performance Benchmarks & Key Insights

- Parity on Privacy: Classification models trained solely on anonymous structural features match the predictive accuracy (AUC/F1) of traditional baseline models built using highly sensitive revenue streams.
- Systemic Risk Proxies: Eigenvector centrality scores successfully isolate indirect supply-chain vulnerabilities and shifting customer trends before they register on classic monthly statements.
- Ego-Network Resiliency: High Shannon consumer diversity scores are a strong indicator of long-term commercial survival and revenue stability during market downturns.

---

## Citation
```bibtex
If you utilize this network engine, processing logic, or alternative feature extractors in your professional research, please cite the original peer-reviewed publication:

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
