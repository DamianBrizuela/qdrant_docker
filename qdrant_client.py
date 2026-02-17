"""
=========================================================================================================================================
File:           qdrant_client.py
Description:    conexión a qdrant.py
Author:         Damian Brizuela
Date:           2026-02-16
Update:         

=========================================================================================================================================
Notas:
- https://python-client.qdrant.tech/#examples
=========================================================================================================================================
"""

import os
import logging
from dotenv import load_dotenv
from qdrant_client import QdrantClient
from qdrant_client.models import VectorParams, Distance


logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s -\n %(message)s'
)

logger = logging.getLogger("QdrantClient -")
logger.setLevel(logging.DEBUG)



# Cargar variables del .env
load_dotenv()

class QdrantClient:

    def __init__(self):

        distance = {
            'euclidean': Distance.COSINE,
            'Manhattan': Distance.MANHATTAN,
            'dot': Distance.DOT,
            'cosine': Distance.COSINE
        }

        self.host = os.getenv('QDRANT_HOST', 'localhost')
        self.port = int(os.getenv('QDRANT_PORT', 8100))

        self.distance = distance[os.getenv('QDRANT_DISTANCE', 'cosine')]
        self.collection_size = int(os.getenv('QDRANT_VECTOR_SIZE', 100))
        
        self.qdrantClient = QdrantClient(
            host= self.host, 
            port= self.port
        )
        
    def create_collection(self, collection_name: str) -> bool:
        try:
            if not self.qdrantClient.collection_exists(collection_name):
                self.qdrantClient.create_collection(
                collection_name= collection_name,
                vectors_config=VectorParams(
                    size=self.collection_size, 
                    distance= self.distance
                ),
            )
        except Exception as e:

        

