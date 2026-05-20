# Repository Data Directory & Replication Guide

This directory contains the necessary structural datasets and preprocessed feature matrices required to fully replicate and validate the machine learning experiments published in [**Nature Scientific Reports**](https://www.nature.com/articles/s41598-023-36624-0).

## Privacy & Compliance Declaration
To comply with strict banking confidentiality regulations, non-disclosure agreements (NDAs), and user privacy protocols, **raw credit card transaction records, customer tracking identifiers, and absolute revenue velocities cannot be publicly shared**.

To resolve this privacy-utility tradeoff, all datasets provided in this directory have been **anonymized, structurally transformed, or aggregated**. This ensuring complete data privacy while fully preserving the underlying network topologies and variance necessary to execute our cross-validated predictive models.

---

## Directory Map & Asset Schema

```text
data/
├─Pre-processed/
│ ├── label_indicators.csv                  # Binary performance target classifications
│ ├── merchant_and_node2vec_features.csv    # Combined baseline demographic & graph vector representations
│ └── all_merchants_attributes_and_labels.csv # Master evaluation join matrix
└── filtered_data/                             # Destination for spatial/record filter pipeline outputs
```
