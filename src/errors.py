"""Модуль объектов исключений"""


class ZeroProductQuantity(Exception):
    """Класс исключения пустого списка продуктов"""

    def __init__(self, *args: str) -> None:
        """Инициализация экземпляра класса"""
        self.message = args[0] if args else "Неизвестная ошибка"

    def __str__(self) -> str:
        """Строковое представление экземпляра класса"""
        return self.message
