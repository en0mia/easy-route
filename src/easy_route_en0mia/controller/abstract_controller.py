# @author Simone Nicol <en0mia.dev@gmail.com>
# @created 23/07/23
from abc import ABC, abstractmethod

from flask import Response, Request


class AbstractController(ABC):
    """Abstract class to represent a Controller."""
    @abstractmethod
    def execute(self, request: Request) -> Response:
        """
        Abstract method called by the routes when starting the stack.
        :param request: the request the stack will work on.
        :return: HTTP Response.
        """
        pass
