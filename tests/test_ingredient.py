import pytest
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestIngredient:
    def test_get_name_returns_name(self):
        ingredient = Ingredient(INGREDIENT_TYPE_FILLING, "Говяжья котлета", 450)
        assert ingredient.get_name() == "Говяжья котлета"

    def test_get_price_returns_price(self):
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, "Бургер-соус", 150)
        assert ingredient.get_price() == 150

    @pytest.mark.parametrize('ingredient_type, name, price, expected_type', (
            (INGREDIENT_TYPE_SAUCE, 'Тартар', 49, 'SAUCE'),
            (INGREDIENT_TYPE_FILLING, 'Рыбная котлета', 250, 'FILLING')
    ))
    def test_get_type_returns_type(self, ingredient_type, name, price, expected_type):
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_type() == expected_type
