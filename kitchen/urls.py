from django.urls import path

from kitchen.views import (
    index,
    IngredientListView,
    DishTypeListView,
    IngredientCreateView,
    DishTypeCreateView,
    DishListView,
    DishCreateView,
)

urlpatterns = [
    path("", index, name="index"),
    path("ingredien/", IngredientListView.as_view(), name="ingredient-list"),
    path("ingredien/create/", IngredientCreateView.as_view(), name="ingredient-create"),
    path("dish_type/", DishTypeListView.as_view(), name="dish-type-list"),
    path("dish_type/create", DishTypeCreateView.as_view(), name="dish-type-create"),
    path("dish", DishListView.as_view(), name="dish-list"),
    path("dish/create", DishCreateView.as_view(), name="dish-create")

]

app_name = "kitchen"
