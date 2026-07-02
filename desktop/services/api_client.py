import requests

API_URL = "https://biblioorg.onrender.com"


def get(endpoint: str):
    url = f"{API_URL}{endpoint}"
    print(f"Solicitando: {url}")

    try:
        response = requests.get(url, timeout=30)
        print(f"Status: {response.status_code}")
        response.raise_for_status()
        return response.json()

    except requests.RequestException as e:
        print(f"Error al conectar con la API: {e}")
        return None