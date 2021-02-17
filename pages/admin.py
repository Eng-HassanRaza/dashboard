from django.contrib import admin
from nested_inline.admin import NestedStackedInline, NestedModelAdmin
from .models import Pricing_Page,Impacx_Page,Digitialization_Page
from main.models import Pricing, Pricing_Features,Pricing_Features_Value
import nested_admin
# Register your models here.

class Pricing_Features_ValueInline(nested_admin.NestedStackedInline):
    model = Pricing_Features_Value

    extra = 0

class Pricing_FeaturesInline(nested_admin.NestedStackedInline):
    model = Pricing_Features
    # sortable_field_name = "title"
    inlines = [Pricing_Features_ValueInline]
    extra = 0

class Pricing_PageAdmin(nested_admin.NestedModelAdmin):
    inlines = [Pricing_FeaturesInline]
    # readonly_fields = ['page_path']

    def has_delete_permission(self, request, obj=None):
        return False
admin.site.register(Pricing_Page, Pricing_PageAdmin)

@admin.register(Impacx_Page)
class Impacx_PageAdmin(admin.ModelAdmin):
    def has_add_permission(self, request, obj=None):
        return False
    def has_delete_permission(self, request, obj=None):
        return False

@admin.register(Digitialization_Page)
class Impacx_PageAdmin(admin.ModelAdmin):
    def has_add_permission(self, request, obj=None):
        return False
    def has_delete_permission(self, request, obj=None):
        return False
