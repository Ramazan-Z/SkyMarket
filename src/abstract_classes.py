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
    def create_product(cls, *args: Any, **kwargs: Any) -> Any:
        """Метод альтернативного создания экземпляра класса"""
        pass


class AbstractOrder(ABC):
    """Абстрактный базовый класс для класса заказов и категорий"""

    @abstractmethod
    def __init__(self) -> None:
        """Инициализация экземпляра класса"""
        super().__init__()

    @abstractmethod
    def get_products(self) -> Any:
        """Метод получения содержания экземпляра класса"""
        pass

    @abstractmethod
    def add_product(self, arg: Any) -> None:
        """Метод добавления содержания экземпляра класса"""
        pass
