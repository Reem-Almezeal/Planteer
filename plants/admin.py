from django.contrib import admin
from .models import Plant
from django.contrib import admin
from .models import Plant,Comment



@admin.register(Plant)
class PlantAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'is_edible', 'created_at')
    list_filter = ('category', 'is_edible')
    search_fields = ('name', 'about', 'used_for')

    fields = (
        'name',
        'image',
        'category',
        'about',
        'used_for',
        'light_requirement',
        'watering',
        'is_edible',
    )
    
class PlantAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'is_edible', 'created_at')
    list_filter = ('category', 'is_edible')
    search_fields = ('name', 'about', 'used_for')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'plant', 'created_at')
    search_fields = ('name', 'content')
