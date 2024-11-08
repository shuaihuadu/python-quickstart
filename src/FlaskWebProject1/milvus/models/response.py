from typing import Any, Optional


class Response:
    def __init__(
        self, code: int | None = 200, message: str | None = None, data: Any = None
    ) -> None:
        self.code = code
        self.message = message
        self.data = data