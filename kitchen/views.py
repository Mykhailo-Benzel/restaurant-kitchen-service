from django.shortcuts import render

from kitchen.models import Cook, Dish, DishType, Ingredient


def index(request):
    """View function for the home page of the site."""

    num_cooks = Cook.objects.count()
    num_dish = Dish.objects.count()
    num_dish_types = DishType.objects.count()
    num_ingredients = Ingredient.objects.count()

    context = {
        "num_cooks": num_cooks,
        "num_dish": num_dish,
        "num_dish_types": num_dish_types,
        "num_ingredients": num_ingredients,
    }

    return render(request, "kitchen/index.html", context=context)
