from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_reposnse import HttpReponse

class TagCreatorView:
    """
        responsability for interacting with HTTP
    """

    def validate_and_create(self, http_request: HttpRequest) -> HttpReponse:
        # body = http_request.body
        # product_code = body["product_code"]

        # logica de regra de negocio
        print("Estou na minha view")
        print(http_request)
        # retorno do http
        return HttpReponse(status_code=200, body={"hello": "world"})
    