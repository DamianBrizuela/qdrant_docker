# Uso de Qdrant - RAG simple

## instalación de entorno
Para poder usar este repositorio es necesario configurar un entorno virtual y ejecutar el docker de qdrant. <br>

**El código se proporciona tal cual, sin responsabilidad por su uso o ejecución por parte del autor<br>Qdrant, LangChain, y demas librerias son propiedad de sus respectivos dueños.**
### docker:
Con el repositorio descargado, ejecuta: <br>

`docker compose up`
### entorno virtual
Para crear el entorno virtual de python y instalar las dependencias<br>
1. `python3 -m venv venv`

2. `source venv/bin/activate`

3. `pip install -r requeriments.txt`

## Ejecutar script
El codigo básico esta dentro del main.py, usa una clase Qdrant_Client que encapsula el cliente qdrant y facilita adicionar texto a la base de datos vectoriales.<br>
`python3 main.py`
