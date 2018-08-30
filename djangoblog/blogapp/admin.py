from django.contrib import admin
from .models import author, category,article

class authorModel(admin.ModelAdmin):

    list_display = ["__str__"]
    search_fields = ["__str__","details"]
    class Meta:
        Model:author


admin.site.register(author,authorModel)

# Register your models here.

class categoryModel(admin.ModelAdmin):

    list_display = ["__str__"]
    search_fields = ["__str__"]

    class Meta:
        Model:category

admin.site.register(category,categoryModel)

class articleModel(admin.ModelAdmin):

    list_display = ["__str__","post_on"]
    search_fields = ["__str__","details"]
    list_filter = ["post_on","category"]
    class Meta:
        Model:article
admin.site.register(article,articleModel)