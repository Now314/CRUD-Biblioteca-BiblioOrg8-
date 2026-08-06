"""Conexión de la app desktop con la API."""

import requests

# URL general de la API.
API_URL = "https://biblioorg.onrender.com"


def get(endpoint: str):
    """Devuelve una URL de la API según sea el caso."""

    url = f"{API_URL}{endpoint}"
    print(f"Solicitando: {url}")

    try:
        response = requests.get(url, timeout=55)
        print(f"Status: {response.status_code}")
        response.raise_for_status()
        return response.json()

    except requests.RequestException as e:
        print(f"Error al conectar con la API: {e}")
        return None

def post(endpoint: str, data: dict):

    url = f"{API_URL}{endpoint}"

    try:
        response = requests.post(
            url,
            json=data,
            timeout=30
        )

        response.raise_for_status()

        return response.json()

    except requests.RequestException as e:
        print(e)
        return None

def put (endpoint: str, data: dict):
    url = f"{API_URL}{endpoint}"
    try:
        response = requests.put(
            url,
            json=data,
            timeout=30
        )
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(e)
        return None