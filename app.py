import requests
from lru_cache import lruCache, lruNode

API_KEY = "1914d65b01794850b5de17b12936d02e"
BASE_URL = "https://api.weatherbit.io/v2.0/current"

def fetch_weatherbit(city: str, cache: lruCache) -> dict:
    url = f"{BASE_URL}?city={city}&key={API_KEY}&units=metric"
    
    cached_response = cache.get(url)
    if cached_response != -1:
        print(f"[CACHE HIT] {city}")
        return cached_response
    else:
        print(f"[CACHE MISS] {city} - realizando petición a la API...")
        try:
            response = requests.get(url)
            response.raise_for_status()  
            data = response.json()
            cache.put(url, data)
            return data
        except requests.exceptions.RequestException as e:
            print(f"Error al obtener datos de la API: {e}")
            return {}

if __name__ == "__main__":
    cache = lruCache(3)

  
    print("Clima en Bogotá (primera consulta):")
    weather = fetch_weatherbit("Bogota", cache)
    print(weather)

   
    print("\nClima en Bogotá (segunda consulta):")
    weather = fetch_weatherbit("Bogota", cache)
    print(weather)

 
    print("\nClima en Madrid (primera consulta):")
    weather = fetch_weatherbit("Madrid", cache)
    print(weather)

 
    print("\nClima en Madrid (segunda consulta):")
    weather = fetch_weatherbit("Madrid", cache)
    print(weather)

  
    print("\nClima en Buenos Aires (primera consulta):")
    weather = fetch_weatherbit("Buenos Aires", cache)
    print(weather)

    print("\nClima en Lima (primera consulta):")
    weather = fetch_weatherbit("Lima", cache)
    print(weather)

  
    print("\nContenido de la caché después de agregar Lima:")
    print(cache.cache)


