from services.api_client import post, put

class CRUDService:

    @staticmethod
    def create(endpoint: str, data: dict) -> bool:
        """
        Crea un nuevo registro en la API.

        Args:
            endpoint: Endpoint de la API.
            data: Diccionario con la información a registrar.

        Returns:
            True si el registro fue creado correctamente.
            False en caso contrario.
        """

        response = post(endpoint, data)

        return response is not None

    @staticmethod
    def update(endpoint: str, data: dict) -> bool:
        """Edita un registro en la API."""

        response = put(endpoint, data)

        return response is not False