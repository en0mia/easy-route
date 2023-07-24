# @author Simone Nicol <en0mia.dev@gmail.com>
# @created 23/07/23
from typing import Optional

from flask import Request, Response

from easy_route.middlewares.abstract_middleware import AbstractMiddleware


class DataValidatorMiddleware(AbstractMiddleware):
    """Validates the JSON input using a rule mapping."""
    def __init__(self, rules):
        """
        :param rules: A map in the form field_name => validation_method
        """
        self.rules = rules
        super().__init__()

    def dispatch(self, request: Request) -> Optional[Response]:
        """Validates the JSON input by means of the validation methods in the rules map.
        :param request: the Request to run the middleware check against
        :return: Response | None
        """
        data = request.get_json(silent=True)
        if not data:
            return Response('', 400)

        for argument, validator in self.rules.items():
            if not data[argument] or not validator(data[argument]):
                return Response('', 400)
        return None
