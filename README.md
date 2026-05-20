# Privacy-Preserving Graph Analytics for Merchant Performance Prediction

[![Journal](https://img.shields.io/badge/Journal-Nature%20Scientific%20Reports-blue)](https://www.nature.com/articles/s41598-023-36624-0)
[![Domain](https://img.shields.io/badge/Domain-FinTech%20%2F%20Alternative%20Data-green)](https://github.com/)
[![License](https://img.shields.io/badge/License-MIT-black)](LICENSE)

An open-source implementation of a privacy-preserving network-science pipeline that maps credit card transaction records to graph structures for merchant financial performance prediction. 

This project demonstrates how feature engineering over corporate customer-bridge network topologies can successfully match the predictive capabilities of highly sensitive internal financial records (such as revenue streams and consumer tracking logs) while ensuring high levels of privacy and preventing third-party exposure.

## Business & Research Problem
Small and Medium-sized Enterprises (SMEs) are bedrock drivers of economic expansion, yet reliably accessing critical commercial credit or capital allocations requires exhaustive financial assessments. Standard prediction mechanisms depend completely on exposing highly private internal logs (e.g., transaction accounts, distinct customer base volumes). This framework mitigates privacy bottlenecks by shifting focus from individual transaction amounts to **macro-network connectivity matrices**.

### Key Methodological Contributions:
1. **Network Co-visitation Graph Topology:** Builds structural projections where nodes represent commercial merchants and directed or weighted edges represent implicit linkages generated when distinct consumers visit shared vendors sequentially.
2. **Multi-Perspective Topological Signals:** Translates graph node locations into explicit numeric signals via advanced centrality profiles (Degree, Node Strength, Closeness, Betweenness, and Eigenvector metrics).
3. **Ego-Network Diversity Dynamics:** Implements Shannon entropy modeling to measure merchants' resilience and market flexibility based on their geographical footprint and client base preferences.

---

## System Architecture & Data Flow

```text
  [Transaction Stream] 
           │
           ▼
┌──────────────────────┐
│  Bipartite Mapping   │ ──► Projects Customer-Merchant interactions
└──────────────────────┘
           │
           ▼
┌──────────────────────┐
│ Graph Reconstruction │ ──► Computes edge weights by shared buyer volume
└──────────────────────┘
           │
           ▼
┌──────────────────────┐      ┌──────────────────────────────────────────────┐
│Topological Extraction│ ──►  │ - Centralities (Degree, Closeness, Eigen)    │
└──────────────────────┘      │ - Market & Geo-spatial Diversity Matrices    │
                              └──────────────────────────────────────────────┘
```
--
## Citation
