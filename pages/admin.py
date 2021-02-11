from django.contrib import admin
from nested_inline.admin import NestedStackedInline, NestedModelAdmin
from .models import Pricing_Page,Impacx_Page,Digitialization_Page
from main.models import Pricing
import nested_admin
# Register your models here.
class PricingInline(nested_admin.NestedStackedInline):
    model = Pricing
    # sortable_field_name = "title"
    extra = 0


class Pricing_PageAdmin(nested_admin.NestedModelAdmin):
    inlines = [PricingInline]
    readonly_fields = ['page_path']

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
