"""Модуль классов дополнительного функционала"""


class MixinLog:
    """Класс для вывода информации в консоль о том, что был создан объект."""

    def __init__(self) -> None:
        """Инициализация экземпляра класса"""
        super().__init__()

    def __repr__(self) -> str:
        """Метод для вывода отладочной информации"""
        args_list = [f"'{value}'" if isinstance(value, str) else str(value) for value in self.__dict__.values()]
        return f"{self.__class__.__name__}({', '.join(args_list)})"
