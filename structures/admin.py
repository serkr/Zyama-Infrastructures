
from .models import Category, Structure
from django.contrib import admin

class StructureInline(admin.TabularInline):
    model = Structure
    extra = 10

class CategoryAdmin(admin.ModelAdmin):
    inlines = [StructureInline]

admin.site.register(Category, CategoryAdmin)