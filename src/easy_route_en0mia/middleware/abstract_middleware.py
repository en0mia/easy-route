# @author Simone Nicol <en0mia.dev@gmail.com>
# @created 23/07/23
from abc import ABC, abstractmethod
from typing import Optional

from flask import Request, Response


class AbstractMiddleware(ABC):
    """An abstract class representing a Middleware."""
    def __init__(self):
        pass

    @abstractmethod
    def dispatch(self, request: Request) -> Optional[Response]:
        """Executes the middleware.
        It returns a Response object if the middleware failed (i.e. 401, 400, ...) or None
        if the request has been validated and the stack can proceed.
        In case a Response is returned, the route flow will block and the response is returned
        to the client.
        :param request: the Request to run the middleware check against
        :return: Response | None
        """
        pass
