from django.urls import path

from kitchen.views import (
    index,
    IngredientListView,
    DishTypeListView,
    IngredientCreateView,
)

urlpatterns = [
    path("", index, name="index"),
    path("ingredien/", IngredientListView.as_view(), name="ingredient-list"),
    path("ingredien/create/", IngredientCreateView.as_view(), name="ingredient-create"),
    path("dish_type/", DishTypeListView.as_view(), name="dish-type-list"),

]

app_name = "kitchen"
