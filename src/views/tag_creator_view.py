from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_reposnse import HttpReponse
from src.controllers.tag_creator_controller import TagCreatorController

class TagCreatorView:
    """
        responsability for interacting with HTTP
    """

    def validate_and_create(self, http_request: HttpRequest) -> HttpReponse:
        tag_creator_controller = TagCreatorController()

        body = http_request.body
        product_code = body["product_code"]

        # logica de regra de negocio
        formatted_response = tag_creator_controller.create(product_code)

        # retorno do http
        return HttpReponse(status_code=200, body=formatted_response)
    