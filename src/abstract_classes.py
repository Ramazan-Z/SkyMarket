"""Модуль абстрактных классов"""

from abc import ABC, abstractmethod
from typing import Any


class BaseProduct(ABC):
    """Абстрктный базовый класс для класса продуктов"""

    @abstractmethod
    def __init__(self) -> None:
        """Инициализация экземпляра класса"""
        super().__init__()

    @abstractmethod
    def __add__(self, other: Any) -> float:
        """Метод сложения стоимостей товаров"""
        pass

    @abstractmethod
    def create_product(cls, name: str, description: str, price: float, quantity: int, products: list[Any] = []) -> Any:
        """Метод альтернативного создания экземпляра класса"""
        pass
