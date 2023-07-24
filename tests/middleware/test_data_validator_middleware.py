# @author Simone Nicol <en0mia.dev@gmail.com>
# @created 23/07/23
import json
import unittest
import uuid
from unittest.mock import MagicMock

from easy_route.middlewares.data_validator_middleware import DataValidatorMiddleware


class TestDataValidatorMiddleware(unittest.TestCase):
    def setUp(self) -> None:
        self.request = MagicMock()
        self.validator = MagicMock()

    def tearDown(self) -> None:
        self.request = None
        self.validator = None

    def testDispatch_return400_whenDataIsEmpty(self):
        # Arrange
        rules = {}
        middleware = DataValidatorMiddleware(rules)

        self.request.get_json.return_value = None

        # Act
        result = middleware.dispatch(self.request)

        # Assert
        self.request.get_json.assert_called_once()
        self.assertEqual(400, result.status_code)
        self.assertFalse(result.data)

    def testDispatch_return400_whenInvalidParameter(self):
        # Arrange
        rules = {
            'uuid': self.validator.is_uuid
        }
        middleware = DataValidatorMiddleware(rules)

        self.validator.is_uuid.return_value = False
        self.request.get_json.return_value = {
            'uuid': 'invalid uuid'
        }

        # Act
        result = middleware.dispatch(self.request)

        # Assert
        self.request.get_json.assert_called_once()
        self.assertEqual(400, result.status_code)
        self.assertFalse(result.data)

    def testDispatch_return400_whenParameterIsNotSet(self):
        # Arrange
        rules = {
            'uuid': self.validator.is_uuid
        }
        middleware = DataValidatorMiddleware(rules)

        self.validator.is_uuid.return_value = False
        self.request.get_json.return_value = {}

        # Act
        result = middleware.dispatch(self.request)

        # Assert
        self.request.get_json.assert_called_once()
        self.validator.is_uuid.assert_not_called()
        self.assertEqual(400, result.status_code)
        self.assertFalse(result.data)

    def testDispatch_returnNone_whenValidParameters(self):
        # Arrange
        rules = {
            'uuid': self.validator.is_uuid,
            'name': lambda name: self.validator.is_string(name) and name,
        }
        middleware = DataValidatorMiddleware(rules)

        self.validator.is_uuid.return_value = True
        self.validator.is_string.return_value = True
        self.request.get_json.return_value = {
            'uuid': str(uuid.uuid4()),
            'name': 'name'
        }

        # Act
        result = middleware.dispatch(self.request)

        # Assert
        self.request.get_json.assert_called_once()
        self.assertIsNone(result)
