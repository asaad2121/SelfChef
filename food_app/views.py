from django.shortcuts import render, redirect
from food_app.models import Recipes
from .forms import RecipesForm
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages

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

@login_required(login_url='login')
def recepie_page(request):
    query = request.GET.get("q","")
    recepi =  Recipes.objects.filter(
        rauthor=request.user
    ).order_by('-rname')
    recepi = recepi.filter(Q(rname__icontains=query) or Q(ringredients__icontains=query)) 
    return render(request, "food_app/recepies.html", { 'recepi':recepi})


@login_required(login_url='login')
def add_recepie(request):

    context = {
        'values':request.POST
    }

    if request.method == 'GET':
        return render(request,'food_app/add_recepie.html',context)
    
    if request.method == 'POST':
        rname= request.POST.get('rname','')
        rdescription = request.POST.get('rdescription','')
        ringredients = request.POST.get('ringredients','')
        rthumbnail = request.FILES.get('rthumbnail','')
        rstep1 = request.POST.get('rstep1','')
        rstep2 = request.POST.get('rstep2','')
        rstep3 = request.POST.get('rstep3','')
        rstep4 = request.POST.get('rstep4','')
        rstep5 = request.POST.get('rstep5','')
        
        
        if rname == '':
            messages.error(request,'Name cannot be empty')
            return render(request,'food_app/add_recepie.html',context)
        
        if rdescription == '':
            messages.error(request,'Description cannot be empty')
            return render(request,'food_app/add_recepie.html',context)
        
        if ringredients == '':
            messages.error(request,' Ingrediants cannot be empty')
            return render(request,'food_app/add_recepie.html',context)
        
        if rthumbnail == '':
            messages.error(request,' Image Missing')
            return render(request,'food_app/add_recepie.html',context)

        if rstep1 == '':
            messages.error(request,'Step 1 missing')
            return render(request,'food_app/add_recepie.html',context)
        if rstep2 == '':
            messages.error(request,'Step 2 missing')
            return render(request,'food_app/add_recepie.html',context)
        if rstep3 == '':
            messages.error(request,'Step 3 missing')
            return render(request,'food_app/add_recepie.html',context)
        if rstep4 == '':
            messages.error(request,'Step 4 missing')
            return render(request,'food_app/add_recepie.html',context)
        if rstep5 == '':
            messages.error(request,'Step 5 missing')
            return render(request,'food_app/add_recepie.html',context)

        Recipes.objects.create(
            rauthor=request.user,
            rname=rname,
            rdescription=rdescription,
            ringredients=ringredients.split(","),
            rthumbnail=rthumbnail,
            rstep1=rstep1,
            rstep2=rstep2,
            rstep3=rstep3,
            rstep4=rstep4,
            rstep5=rstep5,
        ).save()

        messages.success(request,'Recipie Saved Successfully')
        return redirect('recepie_page')

@login_required(login_url='login')
def edit_recepie(request,id):
    
    if  Recipes.objects.filter(id=id,rauthor=request.user).exists():
         recepi =  Recipes.objects.get(id=id,rauthor=request.user)
    
    else:
        messages.error(request,'Something went Wrong. Please Try Again')
        return redirect('recepie_page')
    
    if  recepi.rauthor != request.user:
        messages.error(request,'Something Went Wrong')
        return redirect('recepie_page')
    recepi.ringredients=", ".join(recepi.ringredients)
    print(recepi.ringredients)
    context = {
        'recepi':recepi,
        'values': recepi,
    }

    if request.method == 'GET':
        return render(request,'food_app/edit_recepie.html',context)

    if request.method == 'POST':

        rname= request.POST.get('rname','')
        rdescription = request.POST.get('rdescription','')
        ringredients = request.POST.get('ringredients','')
        rthumbnail = request.FILES.get('rthumbnail','')
        rstep1 = request.POST.get('rstep1','')
        rstep2 = request.POST.get('rstep2','')
        rstep3 = request.POST.get('rstep3','')
        rstep4 = request.POST.get('rstep4','')
        rstep5 = request.POST.get('rstep5','')
        
        if rname == '':
            messages.error(request,'Name cannot be empty')
            return render(request,'food_app/add_recepie.html',context)
        
        if rdescription == '':
            messages.error(request,'Description cannot be empty')
            return render(request,'food_app/add_recepie.html',context)
        
        if ringredients == '':
            messages.error(request,' Ingrediants cannot be empty')
            return render(request,'food_app/add_recepie.html',context)
        
        if rthumbnail == '':
            messages.error(request,' Image Missing')
            return render(request,'food_app/add_recepie.html',context)

        if rstep1 == '':
            messages.error(request,'Step 1 missing')
            return render(request,'food_app/add_recepie.html',context)
        if rstep2 == '':
            messages.error(request,'Step 2 missing')
            return render(request,'food_app/add_recepie.html',context)
        if rstep3 == '':
            messages.error(request,'Step 3 missing')
            return render(request,'food_app/add_recepie.html',context)
        if rstep4 == '':
            messages.error(request,'Step 4 missing')
            return render(request,'food_app/add_recepie.html',context)
        if rstep5 == '':
            messages.error(request,'Step 5 missing')
            return render(request,'food_app/add_recepie.html',context)


        
        recepi.rname=rname
        recepi.rdescription=rdescription
        recepi.rthumbnail=rthumbnail
        recepi.ringredients=ringredients.split(",")
        recepi.rstep1=rstep1
        recepi.rstep2=rstep2
        recepi.rstep3=rstep3
        recepi.rstep4=rstep4
        recepi.rstep5=rstep5
        recepi.save()

        messages.success(request,'Recipie Updated Successfully')
        return redirect('recepie_page')

@login_required(login_url='login')
def delete_recepie(request,id):

    if Recipes.objects.filter(id=id,rauthor=request.user).exists():
        recepi = Recipes.objects.get(id=id,rauthor=request.user)
        
        if recepi.rauthor != request.user:
            messages.error(request,'Something Went Wrong')
            return redirect('recepie_page')
        
        else:
            recepi.delete()
            messages.success(request,'Recipie Deleted Successfully')
            return redirect('recepie_page')
    else:
        messages.error(request,'Something went Wrong. Please Try Again')
        return redirect('recepie_page')        