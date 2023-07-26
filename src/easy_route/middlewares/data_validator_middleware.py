# @author Simone Nicol <en0mia.dev@gmail.com>
# @created 23/07/23
from abc import ABC, abstractmethod
from typing import Optional

from flask import Request, Response

from easy_route.middlewares.abstract_middleware import AbstractMiddleware


class DataProvider(ABC):
    """Since the data can be passed into many ways in HTTP Requests, this abstract class
    defines a provider to extract the data to validate from the Request.
    """

    @abstractmethod
    def get_data(self, request: Request) -> Optional[dict]:
        """Returns the data to validate as key-value pairs.
        :param request: the Request from which the data should be extracted
        :return: dict | None
        """
        pass


class DataValidatorMiddleware(AbstractMiddleware):
    """Validates the JSON input using a rule mapping."""
    def __init__(self, rules: dict, data_provider: DataProvider):
        """
        :param rules: A map in the form field_name => validation_method
        """
        self.rules = rules
        self.data_provider = data_provider
        super().__init__()

    def dispatch(self, request: Request) -> Optional[Response]:
        """Validates the JSON input by means of the validation methods in the rules map.
        :param request: the Request to run the middleware check against
        :return: Response | None
        """
        data = self.data_provider.get_data(request)

        if not data:
            return Response('', 400)

        for argument, validator in self.rules.items():
            if not data[argument] or not validator(data[argument]):
                return Response('', 400)
        return None
