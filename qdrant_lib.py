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
from typing import  Optional
from qdrant_client import QdrantClient, models
from langchain_text_splitters import RecursiveCharacterTextSplitter
from ulid import ULID
import uuid

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s -\n %(message)s'
)

logger = logging.getLogger("QdrantClient -")
logger.setLevel(logging.DEBUG)



# Cargar variables del .env
load_dotenv()

class Qdrant_Client:

    def __init__(self):
        """Instancia el cliente qdrant """

        try:
            self.host = os.getenv('QDRANT_HOST', 'localhost')
            self.port = int(os.getenv('QDRANT_PORT', 8100))

            self.model_name= "BAAI/bge-small-en"

            self.qdrantClient = QdrantClient(
                host= self.host, 
                port= self.port,
            )

        except Exception as e:
            logger.error(f"Error {e}")

        
    def _chunk_text(self, text: str, size: int = 400, overlap: int = 50) -> list:
        """Fracciona el texto en chunks manejables por qdrant

        Args:
            text (str): texto a fraccionar
            size (int, optional): tamaño de los chunks a generar
            overlap (int, optional): solapamiento de caracteres

        Returns:
            list: lista de chunks del texto original
        """
        
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=size,
            chunk_overlap= overlap,
            length_function=len
        )

        return text_splitter.split_text(text)
        
    def create_collection(self, collection_name: str) -> bool:
        """Crea una colección con el nombre indicado

        Args:
            collection_name (str): Nombre de colección

        Returns:
            bool: Resultado de creación.
        """
        try:

            if not self.qdrantClient.collection_exists(collection_name= collection_name):
                self.qdrantClient.create_collection(
                    collection_name= collection_name,
                    vectors_config=models.VectorParams(
                        size=self.qdrantClient.get_embedding_size(self.model_name), 
                        distance=models.Distance.COSINE
                    ),
                )

                logger.debug(f"Creada la colección {collection_name}")
                return True
            else:
                logger.debug(f"Ya existe la colección {collection_name}")
                return False
            
        except Exception as e:           
            logger.error(f"No puede crearse una coleccion.Error: {e}")
            return False

    def delete_collection(self, collection_name: str) -> bool:
        """ Remueve una colección creada. """
        result= self.qdrantClient.delete_collection(collection_name, timeout= 10)
        if not result:
            logger.error(f"No puede eliminarse la colección: {collection_name}")
        else:
            logger.debug(f"Colección eliminada.")
        return result
    
    def add_to_collection(self, collection_name: str, content: str, metadata: dict= {}) -> dict:
        """Adiciona a la colección el contenido, y la metadata asociada

        Args:
            collection_name (str): Nombre de la colección
            content (str): texto a vectorizar
            metadata (dict): información adicional asociada a texto de contenido

        Returns:
            dict: diccionario indicando nombre de archivo asociado, puntos generados, id de la operacion y el estado
        """
        
        chunks= self._chunk_text(content)
        file_name = metadata.get("filename", str(ULID()))

        points = []
        for i, chunk in enumerate(chunks):

            data={
                "original_id": file_name, 
                "text": chunk, 
                "chunk_index": f"{file_name}_{i}",
            }

            data.update(metadata)

            points.append(
                models.PointStruct(
                    id=str(uuid.uuid4()),
                    vector=models.Document(
                        text=chunk,
                        model= self.model_name
                    ),
                    payload= data
                )
            )

        upsert = self.qdrantClient.upsert(
            collection_name= collection_name,
            points= points
        )
        data = {
            "name": file_name,
            "points": len(points),
            "operation_id": upsert.operation_id,
            "status": upsert.status.value
        }
        logger.debug(f"{data}")
        return data

    def get_info(self, collection_name: str):
        """ Recupera información de una colección """
        return self.qdrantClient.get_collection(collection_name= collection_name)

    def get_dimension(self, collection_name: str) -> Optional[int]:
        """recupera la dimension de la colección """
        info = self.get_info(collection_name)
        logger.debug(info.config.params.vectors)
        return info.config.params.vectors.size
