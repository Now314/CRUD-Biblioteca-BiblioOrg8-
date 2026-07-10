from services.api_client import post

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