from django.contrib import admin
from .models import Category, MenuItem


class MenuItemInline(admin.TabularInline):
    model = MenuItem
    extra = 1


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    inlines = [MenuItemInline]
    list_display = ("name",)
    search_fields = ("name",)


@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ("name", "category", "price", "is_available")
    list_filter = ("is_available", "category")
    search_fields = ("name", "description")
