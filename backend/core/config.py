"""Módulo de configuración para el backend."""
# External libraries
from functools import lru_cache

import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('uvicorn.info')


@lru_cache()
def get_log():
    """Creación del logger de la aplicación"""
    return logging.getLogger('uvicorn.info')
