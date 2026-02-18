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
from qdrant_lib import Qdrant_Client

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s -\n %(message)s'
)

logger = logging.getLogger("Main -")
logger.setLevel(logging.INFO)


client = Qdrant_Client()

# texto a embeber
texto = """
    La corporación Aetheris Dynamics, fundada en 2024 por la ingeniera Elena Vance, tiene su sede principal en la ciudad flotante de Neo-Tokio.
    Su producto estrella es el Núcleo de Fusión Fría 'Ignis-7', que utiliza cristales de Zafiro Sintético para estabilizar la energía. 
    En el último trimestre, reportaron un crecimiento del 12% y anunciaron una alianza estratégica con la empresa de transporte Galactic Rails 
    para alimentar sus trenes de levitación magnética.
"""

# preguntas
"""
Directa: ¿Quién fundó Aetheris Dynamics y en qué año?
De detalle: ¿Qué componente específico se usa para estabilizar la energía en el Ignis-7?
De inferencia simple: ¿Para qué servirá la alianza entre Aetheris Dynamics y Galactic Rails?
Negativa (Prueba de Alucinación): ¿Cuál es el nombre del director de marketing de la empresa? (El texto no lo menciona, el modelo debería decir que no lo sabe). 
"""

