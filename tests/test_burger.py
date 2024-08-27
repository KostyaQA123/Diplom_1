from unittest.mock import Mock
from praktikum.burger import Burger


class TestBurger:
    def test_set_buns_with_mock_bun_sets_buns_properly(self, mock_bun):
        burger = Burger()
        burger.set_buns(mock_bun)
        assert burger.bun is mock_bun

    def test_add_ingredient_with_mock_ingredient_adds_ingredient_properly(self, mock_ingredient):
        burger = Burger()
        burger.add_ingredient(mock_ingredient)
        assert mock_ingredient in burger.ingredients

    def test_remove_ingredient_with_mock_ingredient_removes_ingredient_properly(self, mock_ingredient):
        burger = Burger()
        burger.add_ingredient(mock_ingredient)
        burger.remove_ingredient(0)
        assert mock_ingredient not in burger.ingredients

    def test_move_ingredient_with_valid_index_moves_ingredient_properly(self, mock_ingredient):
        burger = Burger()
        another_ingredient = Mock()
        burger.add_ingredient(mock_ingredient)
        burger.add_ingredient(another_ingredient)
        burger.move_ingredient(0, 1)
        assert burger.ingredients[0] is another_ingredient

    def test_get_price_with_mock_bun_and_ingredient_calculates_price_properly(self, mock_bun, mock_ingredient):
        burger = Burger()
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient)
        expected_price = mock_bun.get_price() * 2 + mock_ingredient.get_price()
        assert burger.get_price() == expected_price

    def test_get_receipt_with_mock_bun_and_ingredient_generates_receipt_properly(self, mock_bun, mock_ingredient):
        burger = Burger()
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient)

        expected_receipt = [
            f"(==== {mock_bun.get_name()} ====)",
            f"= {mock_ingredient.get_type().lower()} {mock_ingredient.get_name()} =",
            f"(==== {mock_bun.get_name()} ====)\n",
            f"Price: {burger.get_price()}"
        ]

        assert burger.get_receipt() == '\n'.join(expected_receipt)
