#!/bin/bash

docker run -p 6333:6333 \
    -v $(pwd)/qdrant_storage:/qdrant/storage \
    -v $(pwd)/qdrant_config.yaml:/qdrant/config/custom_config.yaml \
    qdrant/qdrant:v1.2.2 \
    ./qdrant --config-path config/custom_config.yaml