"""
=========================================================================================================================================
File:           main.py
Description:    archivo inicial de main.py
Author:         Damian Brizuela
Date:           2026-02-16
Update:         

=========================================================================================================================================
Notas:
-
=========================================================================================================================================
"""

import logging
from qdrant_client import QdrantClient

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s -\n %(message)s'
)

logger = logging.getLogger("Main -")
logger.setLevel(logging.INFO)
