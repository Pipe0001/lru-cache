import time
import unittest
from lru_cache import lruCache, lruNode
from app import fetch_weatherbit
import requests
from collections import OrderedDict

class TestLRUCache(unittest.TestCase):
    def test_put_and_get(self):
        cache = lruCache(2)
        cache.put("A", 1)
        cache.put("B", 2)
        self.assertEqual(cache.get("A"), 1)
        self.assertEqual(cache.get("B"), 2)

    def test_eviction(self):
        cache = lruCache(2)
        cache.put("A", 1)
        cache.put("B", 2)
        cache.get("A")  
        cache.put("C", 3) 
        self.assertEqual(cache.get("A"), 1)
        self.assertEqual(cache.get("B"), -1)
        self.assertEqual(cache.get("C"), 3)

    def test_update(self):
        cache = lruCache(2)
        cache.put("A", 1)
        cache.put("A", 2)  # Actualiza "A"
        self.assertEqual(cache.get("A"), 2)

class TestAPICachePerformance(unittest.TestCase):
    
    def test_api_performance(self):
        
        city = "Bogota"
        cache = lruCache(3)

        # Primera consulta → Debería ir a la API
        start = time.perf_counter()
        data1 = fetch_weatherbit(city, cache)
        elapsed_first = time.perf_counter() - start

        # Segunda consulta → Debería venir de la caché
        start = time.perf_counter()
        data2 = fetch_weatherbit(city, cache)
        elapsed_second = time.perf_counter() - start

        # Asegurarse de que las respuestas son iguales
        self.assertEqual(data1, data2, "Los datos obtenidos de la API y la caché no coinciden.")

        # Asegurarse de que la segunda consulta sea más rápida que la primera
        self.assertTrue(elapsed_second < elapsed_first, "La segunda llamada no fue más rápida que la primera.")

        # Imprimir los tiempos de ejecución
        print(f"\nTiempo de respuesta sin caché: {elapsed_first:.4f} segundos")
        print(f"Tiempo de respuesta con caché: {elapsed_second:.4f} segundos")


if __name__ == "__main__":
    unittest.main()
