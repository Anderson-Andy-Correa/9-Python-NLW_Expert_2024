from src.views.http_types.http_reposnse import HttpReponse
from .error_types.http_unprocessable_entity import HttpUnprocessableEntutyError

def handle_errors(error: Exception) -> HttpReponse:
    if isinstance(error, HttpUnprocessableEntutyError):
        return HttpReponse(
            status_code = error.status_code,
            body={
                "errors": [{
                    "title": error.name,
                    "detail": error.message
                }]
            }
        )
    return HttpReponse(
        status_code=500,
        body={
            "errors": [{
                "title": "Server Error",
                "detail": str(error)
            }]
        }
    )
