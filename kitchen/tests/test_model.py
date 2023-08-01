from django.contrib.auth import get_user_model
from django.test import TestCase

from kitchen.models import Ingredient, DishType, Dish


class ModelTest(TestCase):
    def test_ingredient_str(self):
        ingredient = Ingredient.objects.create(
            name="Tomato",
        )

        self.assertEqual(
            str(ingredient),
            f"{ingredient.name}"
        )

    def test_dish_type_str(self):
        dish_type = DishType.objects.create(
            name="Pizza",
        )

        self.assertEqual(
            str(dish_type),
            f"{dish_type.name}"
        )

    def test_dish_str(self):
        dish_type = DishType.objects.create(
            name="Pizza",
        )
        dish = Dish.objects.create(
            name="Сake",
            description="Test1234",
            price=10.00,
            dish_type=dish_type,
        )

        self.assertEqual(str(dish), dish.name)

    def test_cook_str(self):
        cook = get_user_model().objects.create_user(
            username="test",
            password="test1234",
            first_name="user",
            last_name="admin"
        )

        self.assertEqual(
            str(cook),
            f"{cook.first_name} {cook.last_name}"
        )

    def test_cook_years_of_experience(self):
        username = "test"
        password = "test1234"
        years_of_experience = 10
        cook = get_user_model().objects.create_user(
            username=username,
            password=password,
            years_of_experience=years_of_experience
        )

        self.assertEqual(cook.username, username)
        self.assertTrue(cook.check_password(password))
        self.assertEqual(cook.years_of_experience, years_of_experience)