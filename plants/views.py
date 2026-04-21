from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import Plant, Comment
from .forms import PlantForm
from django.db.models import Q


def plant_detail(request:HttpRequest, plant_id:int):
    plant = get_object_or_404(Plant, id=plant_id)

    if request.method == "POST":
        name = request.POST.get("name")
        content = request.POST.get("content")

        if name and content:
            Comment.objects.create(
                plant=plant,
                name=name,
                content=content
            )
            return redirect('plant_detail', plant_id=plant.id)

    related_plants = Plant.objects.filter(
        category=plant.category
    ).exclude(id=plant.id)[:4]

    comments = plant.comments.order_by('-created_at')

    context = {
        'plant': plant,
        'related_plants': related_plants,
        'comments': comments,
    }

    return render(request, 'plants/plant_detail.html', context)




def all_plants(request:HttpRequest):
    plants = Plant.objects.all()

    selected_category = request.GET.get('category', '')
    selected_is_edible = request.GET.get('is_edible', '')
    search_query = request.GET.get('search', '')

    if selected_category:
        plants = plants.filter(category=selected_category)

    if selected_is_edible == 'true':
        plants = plants.filter(is_edible=True)
    elif selected_is_edible == 'false':
        plants = plants.filter(is_edible=False)

    if search_query:
        plants = plants.filter(name__icontains=search_query)

    return render(request, 'plants/all_plants.html', {
        'plants': plants,
        'categories': Plant.CategoryChoices.choices,
        'selected_category': selected_category,
        'selected_is_edible': selected_is_edible,
        'search_query': search_query,
    })

def plant_create(request:HttpRequest):
    if request.method == 'POST':
        form = PlantForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('all_plants')
    else:
        form = PlantForm()

    return render(request, 'plants/plant_form.html', {
        'form': form,
        'page_title': 'Add New Plant'
    })


def plant_update(request, plant_id:HttpRequest):
    plant = get_object_or_404(Plant, id=plant_id)

    if request.method == 'POST':
        form = PlantForm(request.POST, request.FILES, instance=plant)
        if form.is_valid():
            form.save()
            return redirect('plant_detail', plant_id=plant.id)
    else:
        form = PlantForm(instance=plant)

    return render(request, 'plants/plant_form.html', {
        'form': form,
        'page_title': 'Update Plant'
    })


def plant_delete(request, plant_id:HttpRequest):
    plant = get_object_or_404(Plant, id=plant_id)

    if request.method == 'POST':
        plant.delete()
        return redirect('all_plants')

    return render(request, 'plants/plant_confirm_delete.html', {
        'plant': plant
    })


def search_plants(request:HttpRequest):
    search_query = request.GET.get('search', '').strip()
    category = request.GET.get('category', '')
    is_edible = request.GET.get('is_edible', '')

    plants = Plant.objects.all()

    if search_query:
        plants = plants.filter(name__icontains=search_query)

    if category:
        plants = plants.filter(category=category)

    if is_edible:
        plants = plants.filter(is_edible=True)

    context = {
        'plants': plants,
        'search_query': search_query,
        'selected_category': category,
        'selected_edible': is_edible,
    }

    return render(request, 'plants/all_plants.html', context)