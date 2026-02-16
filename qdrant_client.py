"""
=========================================================================================================================================
File:           qdrant_client.py
Description:    conexión a qdrant.py
Author:         Damian Brizuela
Date:           2026-02-16
Update:         

=========================================================================================================================================
Notas:
-
=========================================================================================================================================
"""

import os
from dotenv import load_dotenv
from qdrant_client import QdrantClient
from qdrant_client.models import VectorParams, Distance

# Cargar variables del .env
load_dotenv()

class QdrantClient:

    def __init__(self):
        self.host = os.getenv('QDRANT_HOST', 'localhost')
        self.port = int(os.getenv('QDRANT_PORT', 8100))

        self.distance = os.getenv('QDRANT_DISTANCE', Distance.COSINE)
        
        qdrantClient = QdrantClient(
            host= self.host, 
            port= self.port
        )
        
    def create_collection(self, collection_name: str) -> str:
        if not client.collection_exists(collection_name):
            client.create_collection(
            collection_name= collection_name,
            vectors_config=VectorParams(size=100, distance=Distance.COSINE),
        )
        

