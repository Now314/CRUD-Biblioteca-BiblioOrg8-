import requests

API_URL = "https://biblioorg.onrender.com"


def get(endpoint: str):
    try:
        response = requests.get(f"{API_URL}{endpoint}", timeout=10)
        response.raise_for_status()
        return response.json()

    except requests.RequestException as e:
        print(f"Error al conectar con la API: {e}")
        return None