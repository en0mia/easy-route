# @author Simone Nicol <en0mia.dev@gmail.com>
# @created 23/07/23
import unittest
from unittest.mock import MagicMock

from flask import Response

from easy_route.routes.route import Route


class TestRoute(unittest.TestCase):
    def setUp(self) -> None:
        self.request = MagicMock()
        self.controller = MagicMock()
        self.route = Route(self.request, self.controller)

    def tearDown(self) -> None:
        self.request = None
        self.controller = None
        self.route = None

    def testWithMiddleware_addMiddleware_whenCalled(self):
        # Arrange
        middleware = MagicMock()

        # Act
        self.route.add_middleware(middleware)

        # Assert
        self.assertEqual([middleware], self.route.middlewares)

    def testWithMiddlewares_addMiddlewares_whenCalled(self):
        # Arrange
        middlewares = [MagicMock(), MagicMock()]

        # Act
        self.route.add_middlewares(middlewares)

        # Assert
        self.assertEqual(middlewares, self.route.middlewares)

    def testDispatch_callDispatchOnEachMiddleware_whenCalled(self):
        # Arrange
        middlewares = [MagicMock(), MagicMock()]
        for middleware in middlewares:
            middleware.dispatch.return_value = None
        self.route.add_middlewares(middlewares)

        # Act
        self.route.dispatch()

        # Assert
        for middleware in middlewares:
            middleware.dispatch.assert_called_once()
        self.controller.execute.assert_called_once()

    def testDispatch_stopOnFirstMiddleware_whenFirstMiddlewareFail(self):
        # Arrange
        first_middleware = MagicMock()
        second_middleware = MagicMock()
        self.route.add_middlewares([first_middleware, second_middleware])
        first_middleware.dispatch.return_value = Response('', 400)

        # Act
        result = self.route.dispatch()

        # Assert
        first_middleware.dispatch.assert_called_once()
        second_middleware.dispatch.assert_not_called()
        self.controller.execute.assert_not_called()
        self.assertEqual(400, result.status_code)
