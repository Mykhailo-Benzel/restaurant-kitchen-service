from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from kitchen.models import DishType

DISH_TYPE_URL = reverse("kitchen:dish-type-list")


class PublicDishTypeTest(TestCase):
    def test_login_required(self):
        res = self.client.get(DISH_TYPE_URL)

        self.assertNotEqual(res.status_code, 200)


class PrivateDishTypeTest(TestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(
            username="test",
            password="test1234"
        )

        self.client.force_login(self.user)

    def test_retrieve_manufacturer(self):
        DishType.objects.create(name="Pizza")
        DishType.objects.create(name="Cake")

        response = self.client.get(DISH_TYPE_URL)
        dish_type = DishType.objects.all()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            list(response.context["dish_type_list"]),
            list(dish_type)
        )


class PrivetCookTest(TestCase):
    def setUp(self) -> None:
        self.cook = get_user_model().objects.create_user(
            username="test",
            password="test1234"
        )

        self.client.force_login(self.cook)

    def test_create_cook(self):
        form_data = {
            "username": "test_user",
            "password1": "test12345",
            "password2": "test12345",
            "first_name": "First",
            "last_name": "Last",
            "years_of_experience": 10
        }

        self.client.post(reverse("kitchen:cook-create"), data=form_data)
        user = get_user_model().objects.get(username=form_data["username"])

        self.assertEqual(user.first_name, form_data["first_name"])
        self.assertEqual(user.last_name, form_data["last_name"])
        self.assertEqual(user.years_of_experience, form_data["years_of_experience"])
