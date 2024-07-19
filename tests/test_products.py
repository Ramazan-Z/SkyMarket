"""Тесты модуля products.py"""

from typing import Any

import pytest

from src.categories import Category, CategoryIterator
from src.products import LawnGrass, Product, Smartphone


# Тест инициализации класса Product
def test_product_init(product: Product) -> None:
    assert product.name == "Имя продукта"
    assert product.description == "Описание продукта"
    assert product.price == 10999.99
    assert product.quantity == 100


# Тест сеттера класса Product случай с повышением цены
def test_product_setter_price_up(product: Product) -> None:
    assert product.price == 10999.99
    product.price = 15000.0
    assert product.price == 15000.0


# Тест сеттера класса Product случай с отрицательной ценой
def test_product_setter_price_negative(product: Product, capsys: Any) -> None:
    assert product.price == 10999.99
    product.price = -150
    captured = capsys.readouterr()
    assert captured.out == "Введена некорректная цена\n"
    assert product.price == 10999.99


# Тест сеттера класса Product случай с понижением цены и подтверждением
def test_product_setter_price_down_yes(product: Product, monkeypatch: Any) -> None:
    monkeypatch.setattr("builtins.input", lambda _: "y")
    assert product.price == 10999.99
    product.price = 1000.0
    assert product.price == 1000.0


# Тест сеттера класса Product случай с понижением цены и отказом
def test_product_setter_price_down_no(product: Product, monkeypatch: Any) -> None:
    monkeypatch.setattr("builtins.input", lambda _: "n")
    assert product.price == 10999.99
    product.price = 1000.0
    assert product.price == 10999.99


# Тест метода create_product случай повтора имени и повышения цены
def test_create_product_repeat_name_price_up(product: Product) -> None:
    assert product.price == 10999.99
    assert product.quantity == 100.0
    new_product = Product.create_product(
        [product], name="Имя продукта", description="Описание продукта", price=15000.0, quantity=10
    )
    assert new_product is product
    assert new_product.price == 15000.0
    assert new_product.quantity == 110


# Тест метода create_product случай повтора имени и понижения цены
def test_create_product_repeat_name_price_down(product: Product) -> None:
    assert product.price == 10999.99
    assert product.quantity == 100.0
    new_product = Product.create_product(
        [product], name="Имя продукта", description="Описание продукта", price=5000.0, quantity=10
    )
    assert new_product is product
    assert new_product.price == 10999.99
    assert new_product.quantity == 110


# Тест метода create_product случай нового имени
def test_create_product_new_product(product: Product) -> None:
    assert product.price == 10999.99
    assert product.quantity == 100
    new_product = Product.create_product(
        [product], name="Новый продукт", description="Описание продукта", price=12000.0, quantity=10
    )
    assert new_product is not product
    assert new_product.price == 12000.0
    assert new_product.quantity == 10
    assert product.price == 10999.99
    assert product.quantity == 100


# Тест инициализации класса Category
def test_category_init(category: Category) -> None:
    assert category.name == "Мебель"
    assert category.description == "Для дома и офиса"
    product = category.products[0]
    assert product.name == "Стол компьютерный"
    assert product.description == "Aceline Basic 01 белый"
    assert product.price == 1699
    assert product.quantity == 16
    assert Category.category_count == 1
    assert Category.product_unique_count == 2


# Тест метода add_product
def test_add_product(category: Category) -> None:
    assert len(category.products) == 2
    category.add_product(Product("New name", "New description", 12999.0, 4))
    assert len(category.products) == 3
    assert Category.category_count == 2
    assert Category.product_unique_count == 5


# Тест метода get_products
def test_get_products(category: Category) -> None:
    assert category.get_products() == [
        "Стол компьютерный, 1699.0 руб. Остаток: 16 шт.",
        "Стул, 11390.0 руб. Остаток: 8 шт.",
    ]


# Тест метода __len__ класса Product
def test_len_product(product: Product) -> None:
    assert len(product) == 100


# Тест метода __repr__ класса Product
def test_repr_product(product: Product) -> None:
    assert repr(product) == "Product('Имя продукта', 'Описание продукта', 10999.99, 100)"


# Тест метода __str__ класса Product
def test_str_product(product: Product) -> None:
    assert str(product) == "Имя продукта, 10999.99 руб. Остаток: 100 шт."


# Тест метода __add__ класса Product
def test_magic_add_product(product: Product) -> None:
    new_product = Product("Новый продукт", "Новое описание", 500.0, 20)
    assert product + new_product == 1109999.0


# Тест метода __len__ класса Category
def test_len_category(category: Category) -> None:
    assert len(category) == 24


# Тест метода __repr__ класса Category
def test_repr_category(category: Category) -> None:
    assert repr(category) == (
        "Category('Мебель', 'Для дома и офиса', "
        + "[Product('Стол компьютерный', 'Aceline Basic 01 белый', 1699.0, 16), "
        + "Product('Стул', 'Opus 1 beige / black', 11390.0, 8)])"
    )


# Тест метода __str__ класса Category
def test_str_category(category: Category) -> None:
    assert str(category) == "Мебель, количество продуктов: 24 шт."


# Тест класса CategoryIterator
def test_category_iterator(category: Category) -> None:
    category_iterator = iter(CategoryIterator(category))
    assert repr(next(category_iterator)) == "Product('Стол компьютерный', 'Aceline Basic 01 белый', 1699.0, 16)"
    assert repr(next(category_iterator)) == "Product('Стул', 'Opus 1 beige / black', 11390.0, 8)"
    with pytest.raises(StopIteration):
        next(category_iterator)


# Тест метода __add__ класса Product случай с неверным объектом сложения
def test_magic_add_product_error(lawn_grass: LawnGrass, smartphone: Smartphone) -> None:
    with pytest.raises(TypeError) as e:
        lawn_grass + smartphone
    assert str(e.value) == "Складывать товары можно только из одинаковых классов продуктов."


# Тест метода add_product с объектом Smartphone
def test_add_product_smartphone(category: Category, smartphone: Smartphone) -> None:
    assert len(category.products) == 2
    category.add_product(smartphone)
    assert len(category.products) == 3


# Тест метода add_product с объектом LawnGrass
def test_add_product_lawn_grass(category: Category, lawn_grass: LawnGrass) -> None:
    assert len(category.products) == 2
    category.add_product(lawn_grass)
    assert len(category.products) == 3


# Тест метода add_product с другим объектом
def test_add_product_other(category: Category) -> None:
    assert len(category.products) == 2
    with pytest.raises(TypeError) as e:
        category.add_product("Строка")
    assert str(e.value) == "В категорию можно добавить только объекты класса Product или его подклассов"


# Тест метода create_product в классе Smatrphone
# случай повтора имени и повышения цены
def test_create_product_smartphome_repeat_name_price_up(smartphone: Smartphone) -> None:
    assert smartphone.price == 15000.0
    assert smartphone.quantity == 1
    new_smartphone = Smartphone.create_product(
        [smartphone],
        name="Смартфон",
        description="Описание смартфона",
        price=16000.0,
        quantity=10,
        performance=3,
        model="samsung",
        memory=64,
        color="black",
    )
    assert new_smartphone is smartphone
    assert new_smartphone.price == 16000.0
    assert new_smartphone.quantity == 11


# Тест метода create_product в классе Smatrphone
# случай повтора имени и понижения цены
def test_create_product_smartphome_repeat_name_price_down(smartphone: Smartphone) -> None:
    assert smartphone.price == 15000.0
    assert smartphone.quantity == 1
    new_smartphone = Smartphone.create_product(
        [smartphone],
        name="Смартфон",
        description="Описание смартфона",
        price=14000.0,
        quantity=10,
        performance=3,
        model="samsung",
        memory=64,
        color="black",
    )
    assert new_smartphone is smartphone
    assert new_smartphone.price == 15000.0
    assert new_smartphone.quantity == 11


# Тест метода create_product в классе Smatrphone
# случай нового имени
def test_create_product_smartphone_new(smartphone: Smartphone) -> None:
    assert smartphone.price == 15000.0
    assert smartphone.quantity == 1
    new_smartphone = Smartphone.create_product(
        [smartphone],
        name="Новый смартфон",
        description="Описание смартфона",
        price=14000.0,
        quantity=10,
        performance=3,
        model="samsung",
        memory=64,
        color="black",
    )
    assert new_smartphone is not smartphone
    assert new_smartphone.price == 14000.0
    assert new_smartphone.quantity == 10
    assert smartphone.price == 15000.0
    assert smartphone.quantity == 1


# Тест метода create_product в классе LawnGrass
# случай повтора имени и повышения цены
def test_create_product_lawn_grass_repeat_name_price_up(lawn_grass: LawnGrass) -> None:
    assert lawn_grass.price == 5000.0
    assert lawn_grass.quantity == 10
    new_lawn_grass = LawnGrass.create_product(
        [lawn_grass],
        name="Трава газонная",
        description="Описание газона",
        price=6000.0,
        quantity=10,
        manufacturer="China",
        germination_period=5,
        color="green",
    )
    assert new_lawn_grass is lawn_grass
    assert new_lawn_grass.price == 6000.0
    assert new_lawn_grass.quantity == 20


# Тест метода create_product в классе LawnGrass
# случай повтора имени и понижения цены
def test_create_product_lawn_grass_repeat_name_price_down(lawn_grass: LawnGrass) -> None:
    assert lawn_grass.price == 5000.0
    assert lawn_grass.quantity == 10
    new_lawn_grass = LawnGrass.create_product(
        [lawn_grass],
        name="Трава газонная",
        description="Описание газона",
        price=4000.0,
        quantity=10,
        manufacturer="China",
        germination_period=5,
        color="green",
    )
    assert new_lawn_grass is lawn_grass
    assert new_lawn_grass.price == 5000.0
    assert new_lawn_grass.quantity == 20


# Тест метода create_product в классе LawnGrass
# случай нового имени
def test_create_product_lawn_grass_new(lawn_grass: LawnGrass) -> None:
    assert lawn_grass.price == 5000.0
    assert lawn_grass.quantity == 10
    new_lawn_grass = LawnGrass.create_product(
        [lawn_grass],
        name="Новый газон",
        description="Описание травы",
        price=8000.0,
        quantity=15,
        manufacturer="China",
        germination_period=5,
        color="green",
    )
    assert new_lawn_grass is not lawn_grass
    assert new_lawn_grass.price == 8000.0
    assert new_lawn_grass.quantity == 15
    assert lawn_grass.price == 5000.0
    assert lawn_grass.quantity == 10


# Тест создания продукта с нулевым количеством
def test_product_zero_quantity() -> None:
    with pytest.raises(ValueError, match="Количество товара должно быть больше нуля"):
        Product("name", "description", 500, 0)


# Тест создания смартфона с нулевым количеством
def test_smartphone_zero_quantity() -> None:
    with pytest.raises(ValueError, match="Количество товара должно быть больше нуля"):
        Smartphone("name", "description", 500, 0, 2, "nokia", 128, "blue")


# Тест создания газона с нулевым количеством
def test_lawn_grass_zero_quantity() -> None:
    with pytest.raises(ValueError, match="Количество товара должно быть больше нуля"):
        LawnGrass("name", "description", 500, 0, "Russia", 5, "green")
