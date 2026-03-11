from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Iterable


class Report(ABC):
    name: str

    @abstractmethod
    def build(self, rows: Iterable[dict[str, str]]) -> list[dict[str, object]]:
        raise NotImplementedError

    @abstractmethod
    def headers(self) -> list[str]:
        raise NotImplementedError