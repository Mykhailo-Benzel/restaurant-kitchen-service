from django.urls import path

from kitchen.views import (
    index,
    IngredientListView,
    DishTypeListView,
    IngredientCreateView,
    DishTypeCreateView,
    DishListView,
    DishDetailView,
    DishCreateView,
    CookListView,
    CookDetailView,
)

urlpatterns = [
    path("", index, name="index"),
    path("ingredien/", IngredientListView.as_view(), name="ingredient-list"),
    path("ingredien/create/", IngredientCreateView.as_view(), name="ingredient-create"),
    path("dish_type/", DishTypeListView.as_view(), name="dish-type-list"),
    path("dish_type/create", DishTypeCreateView.as_view(), name="dish-type-create"),
    path("dish", DishListView.as_view(), name="dish-list"),
    path("dish/<int:pk>", DishDetailView.as_view(), name="dish-detail"),
    path("dish/create", DishCreateView.as_view(), name="dish-create"),
    path("cook/", CookListView.as_view(), name="cook-list"),
    path("cook/<int:pk>/", CookDetailView.as_view(), name="cook-detail")

]

app_name = "kitchen"
