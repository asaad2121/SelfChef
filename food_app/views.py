from django.shortcuts import render
from food_app.models import Recipes
from .forms import RecipesForm
from django.db.models import Q

def is_valid_queryparam(param):
    return param != '' and param is not None

def index(request):
    query = request.GET.get("q","")
    dataDet = Recipes.objects.filter(Q(rname__icontains=query) or Q(ringredients__icontains=query)) 
    # ADD OR Q(ringredients__icontains=query)
    template_name = "food_app/index.html"
    return render(request, "food_app/index.html", { 'dataDet':dataDet})

def rec(request):
    dataDet = Recipes.objects.all()
    # ADD OR Q(ringredients__icontains=query)
    template_name = "food_app/food_det.html"
    return render(request, "food_app/food_det.html", { 'dataDet':dataDet})

def food_det(request, id):
    recipes = Recipes.objects.get(pk=id)
    dataDet = Recipes.objects.all()[:5]
    return render(request, "food_app/food_det.html", {'dataDet':dataDet,'recipes':recipes})
