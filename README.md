
# LRU Cache

Este repositorio implementa una **caché LRU (Least Recently Used)** en Python, que almacena un número limitado de elementos y elimina los menos usados cuando se alcanza la capacidad máxima. Además, se incluye un sistema de caché para hacer peticiones a la API de **Weatherbit** y optimizar las consultas mediante el uso de la caché.

## Características

- Implementación de una caché LRU.
- Integración con la API de Weatherbit para obtener datos climáticos.
- Soporte para almacenar y recuperar datos de la caché.
- Evicción de los elementos menos utilizados cuando se supera la capacidad de la caché.
- Test unitarios para verificar el correcto funcionamiento de la caché LRU y la optimización del rendimiento de la API.

## Estructura del proyecto

- **`lru_cache.py`**: Implementación de la clase `lruCache` y `lruNode`, que gestionan la lógica de la caché LRU.
- **`app.py`**: Función para obtener datos del clima desde la API de Weatherbit, utilizando la caché LRU para mejorar el rendimiento.
- **`lru_test.py`**: Pruebas unitarias para verificar la correcta funcionalidad de la caché LRU y su rendimiento con la API.

## Instalación

1. Clona el repositorio en tu máquina local:

   ```bash
   git clone https://github.com/tu_usuario/lru-cache.git
   ```

2. Navega a la carpeta del proyecto:

   ```bash
   cd lru-cache
   ```

## Uso

### Crear una caché LRU

Puedes crear una caché LRU de la siguiente manera:

```python
from lru_cache import lruCache

# Crear una caché con capacidad 3
cache = lruCache(3)

# Agregar elementos a la caché
cache.put("A", 1)
cache.put("B", 2)

# Obtener elementos de la caché
print(cache.get("A"))  # Devuelve 1
```

### Uso con la API de Weatherbit

Para obtener el clima de una ciudad, puedes utilizar la función `fetch_weatherbit`:

```python
from app import fetch_weatherbit
from lru_cache import lruCache

# Crear una caché con capacidad 3
cache = lruCache(3)

# Obtener el clima de Bogotá
weather_data = fetch_weatherbit("Bogota", cache)
print(weather_data)
```

### Ejecutar las pruebas

Puedes ejecutar las pruebas unitarias para verificar que todo funcione correctamente:

```bash
python -m unittest test_lru_cache.py
```

## Pruebas

Se incluyen pruebas unitarias para verificar:

- La correcta inserción y recuperación de elementos de la caché.
- El comportamiento de la caché cuando se alcanza su capacidad máxima.
- El rendimiento de la API con y sin caché.



