import os
import sys
import yaml
import logging
import pandas as pd
from src.data_processing import SpatialFilter, RecordFilter
from src.network_builder import MerchantNetworkBuilder
from src.feature_engineering import FeatureExtractor

# Setup logging environment
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class MerchantAnalyticsPipeline:
    def __init__(self, config_path: str):
        with open(config_path, 'r') as f:
            self.config = yaml.safe_load(f)
            
    def run(self):
        logger.info("Initializing Merchant Network Feature Engineering Pipeline...")
        
        # 1. Spatial Filtering & Preprocessing
        logger.info("Step 1: Applying spatial filters to transactional records...")
        spatial_filter = SpatialFilter(bbox=self.config['network']['spatial_bounding_box'])
        filtered_records = spatial_filter.process(self.config['data']['raw_transactions'])
        
        # 2. Network Reconstruction
        logger.info("Step 2: Reconstructing consumer-bridge network topology...")
        builder = MerchantNetworkBuilder(min_weight=self.config['network']['min_shared_customers'])
        network = builder.build(filtered_records)
        
        # 3. Topology & Vector Embedding Extraction
        logger.info("Step 3: Engineering structural and Node2Vec embeddings...")
        extractor = FeatureExtractor(dimensions=self.config['embeddings']['dimensions'])
        features_df = extractor.generate(network)
        
        # 4. Export Configuration
        output_path = self.config['data']['processed_features']
        features_df.to_csv(output_path, index=False)
        logger.info(f"Pipeline executed successfully. Structural signals written to: {output_path}")

if __name__ == "__main__":
    pipeline = MerchantAnalyticsPipeline(config_path="config/config.yaml")
    pipeline.run()
