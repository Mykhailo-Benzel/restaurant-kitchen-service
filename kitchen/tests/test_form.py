from django.test import TestCase

from kitchen.forms import CookSearchForm, DishSearchForm, DishTypeSearchForm, IngredientSearchForm, CookForm


class FormsTests(TestCase):

    def test_cook_creation_form_with_first_last_name_years_of_experience_is_valid(self):
        form_data = {
            "username": "username",
            "password1": "user1234ewq",
            "password2": "user1234ewq",
            "first_name": "user",
            "last_name": "test",
            "years_of_experience": 10
        }
        form = CookForm(data=form_data)
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data, form_data)

    def test_cook_search_form(self):
        form_data = {"username": "username"}
        form = CookSearchForm(data=form_data)

        self.assertTrue(form.is_valid())

    def test_dish_search_form(self):
        form_data = {"name": "name"}
        form = DishSearchForm(data=form_data)

        self.assertTrue(form.is_valid())

    def test_dish_type_search_form(self):
        form_data = {"name": "name"}
        form = DishTypeSearchForm(data=form_data)

        self.assertTrue(form.is_valid())

    def test_ingredient_search_form(self):
        form_data = {"name": "name"}
        form = IngredientSearchForm(data=form_data)

        self.assertTrue(form.is_valid())
