from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from kitchen.forms import DishTypeForm, DishForm
from kitchen.models import Cook, Dish, DishType, Ingredient


@login_required
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


class IngredientListView(LoginRequiredMixin, generic.ListView):
    model = Ingredient
    paginate_by = 5
    template_name = "kitchen/ingredient_list.html"


class IngredientCreateView(LoginRequiredMixin, generic.CreateView):
    model = Ingredient
    fields = "__all__"
    success_url = reverse_lazy("kitchen:ingredient-list")


class DishTypeListView(LoginRequiredMixin, generic.ListView):
    model = DishType
    paginate_by = 5
    context_object_name = "dish_type_list"
    template_name = "kitchen/dish_type_list.html"


class DishTypeCreateView(LoginRequiredMixin, generic.CreateView):
    model = DishType
    form_class = DishTypeForm
    template_name = "kitchen/dish_type_form.html"
    success_url = reverse_lazy("kitchen:dish-type-list")


class DishListView(LoginRequiredMixin, generic.ListView):
    model = Dish


class DishDetailView(LoginRequiredMixin, generic.DetailView):
    model = Dish


class DishCreateView(LoginRequiredMixin, generic.CreateView):
    model = Dish
    form_class = DishForm
    success_url = reverse_lazy("kitchen:dish-list")


class CookListView(LoginRequiredMixin, generic.ListView):
    model = Cook


class CookDetailView(LoginRequiredMixin, generic.DetailView):
    model = Cook
