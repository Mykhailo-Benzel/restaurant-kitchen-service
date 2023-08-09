from django.urls import path

from kitchen.views import (
    IndexView,
    IngredientListView,
    IngredientCreateView,
    IngredientDeleteView,
    DishTypeListView,
    DishTypeCreateView,
    DishTypeDeleteView,
    DishListView,
    DishDetailView,
    DishCreateView,
    DishUpdateView,
    DishDeleteView,
    DishTypeUpdateView,
    CookListView,
    CookDetailView,
    CookCreateView,
    CookUpdateView,
    ToggleAssignToDish,
    CookDeleteView,
)

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("ingredient/", IngredientListView.as_view(), name="ingredient-list"),
    path("ingredient/create/", IngredientCreateView.as_view(), name="ingredient-create"),
    path("ingredient/<int:pk>/delete/", IngredientDeleteView.as_view(), name="ingredient-delete"),
    path("dish_type/", DishTypeListView.as_view(), name="dish-type-list"),
    path("dish_type/create/", DishTypeCreateView.as_view(), name="dish-type-create"),
    path("dish_type/<int:pk>/update/", DishTypeUpdateView.as_view(), name="dish-type-update"),
    path("dish_type/<int:pk>/delete", DishTypeDeleteView.as_view(), name="dish-type-delete"),
    path("dish/", DishListView.as_view(), name="dish-list"),
    path("dish/<int:pk>/", DishDetailView.as_view(), name="dish-detail"),
    path("dish/create/", DishCreateView.as_view(), name="dish-create"),
    path("dish/<int:pk>/update/", DishUpdateView.as_view(), name="dish-update"),
    path("dish/<int:pk>/delete/", DishDeleteView.as_view(), name="dish-delete"),
    path("dishes/<int:pk>/toggle-assign/", ToggleAssignToDish.as_view(), name="toggle-dish-assign",),
    path("cook/", CookListView.as_view(), name="cook-list"),
    path("cook/<int:pk>/", CookDetailView.as_view(), name="cook-detail"),
    path("cook/create/", CookCreateView.as_view(), name="cook-create"),
    path("cook/<int:pk>/update/", CookUpdateView.as_view(), name="cook-update"),
    path("cook/<int:pk>/delete/", CookDeleteView.as_view(), name="cook-delete"),
]

app_name = "kitchen"
