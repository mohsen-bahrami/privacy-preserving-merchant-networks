# Privacy-Preserving Merchant Network Analytics for Alternative Credit Scoring

[![Journal](https://img.shields.io/badge/Journal-Nature%20Scientific%20Reports-blue)](https://www.nature.com/articles/s41598-023-36624-0)
[![Python](https://img.shields.io/badge/Python-3.9%2B-blue)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)

An end-to-end network science and machine learning feature engineering pipeline that transforms raw credit card transaction streams into privacy-preserving structural topologies to evaluate small and medium enterprise (SME) performance.

Published in [**Nature Scientific Reports**](https://www.nature.com/articles/s41598-023-36624-0), this framework implements consumer-bridge network transformations to extract alternative risk signals via graph centralities. This allows financial institutions to evaluate commercial credit health without requiring merchants to expose highly sensitive revenue footprints or proprietary tracking logs.

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

## Running the End-to-End Pipeline

The data engineering and validation execution sequences can be run sequentially based on definitions stored inside config.yaml:

```bash
# 1. Apply geospatial bounding-box filter over raw checkout streams
python spatial_filter.py

# 2. Prune records based on operational thresholds and target MCC codes
python filter_records.py --bank x

# 3. Construct the projected user-bridge merchant co-visitation graph
python construct_network.py --bank x

# 4. Extract topological network features (centralities, entropy) and generate performance targets
python generate_features_labels.py --bank x --weight weight

# 5. Execute cross-validated machine learning predictive modeling experiments
python run_experiment.py -O results/ -E merchant_experiment -L labels/labels_x.csv -F features/filtered_network_features_weight_x.csv
```
---

## Replication Flow (pre-processed Data)
You do not need access to raw merchant transaction records to test or evaluate the machine learning architectures. The files located within `data/pre-processed/` bypass the spatial-temporal parsing steps and allow immediate execution of the evaluation suite:

To evaluate the predictive power of these network features against traditional financial indicators, execute the experiment suite using the provided scripts:

```bash
# Evaluate models using ONLY demographic proxies
python run_experiment.py -O results/ -E demographics_baseline -L data/pre-processed/label_indicators.csv -F data/pre-processed/demographics_x.csv

# Evaluate models using ONLY revenue baseline metrics
python run_experiment.py -O results/ -E revenue_baseline -L data/pre-processed/label_indicators.csv -F data/pre-processed/revenue_x.csv

# Evaluate models using privacy-safe structural network features
python run_experiment.py -O results/ -E network_features_only -L data/pre-processed/label_indicators.csv -F data/pre-processed/filtered_network_features_weight_x.csv

# Evaluate the fully integrated multi-modal model (Demographics + Revenue + Network Topologies)
python run_experiment.py -O results/ -E full_multimodal_model -L data/pre-processed/label_indicators.csv -F data/pre-processed/demographics_x.csv data/pre-processed/revenue_x.csv data/pre-processed/filtered_network_features_weight_x.csv
```

For a high-level walkthrough of model accuracy curves, ROC-AUC comparisons, and feature importance interpretations, reference the master `src/eval.ipynb` file.

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

[**Research Paper**](https://www.nature.com/articles/s41598-023-36624-0)

Developed under the research umbrellas of MIT Connection Science and the Institute for Data, Systems, and Society (IDSS). For integration questions, reach out to the corresponding author [Mohsen Bahrami](mailto:bahrami@mit.edu).
