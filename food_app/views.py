from django.shortcuts import render
from food_app.models import Recipes, UserData
from .forms import RecipesForm, UserForm
from django.db.models import Q


def index(request):
    query = request.GET.get("q","")
    # dataDet = Recipes.objects.filter(Q(rname__icontains=query))
    dataDet = Recipes.objects.all()
    return render(request, "food_app/index.html", { 'dataDet':dataDet})
# Create your views here.
