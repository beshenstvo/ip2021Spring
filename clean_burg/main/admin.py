from django.contrib import admin
from import_export.admin import ImportExportMixin

from .models import Service, Order, OrderItem


class OrderItemTabularInline(admin.TabularInline):
    model = OrderItem


@admin.register(Service)
class ServiceAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ("name", "price",)
    search_fields = ("name",)


@admin.register(Order)
class OrderAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ("id", "status", "client_name", "client_phone", "client_comment", "created_at",)
    list_filter = ("status", "created_at", "updated_at",)
    list_editable = ("status", )
    search_fields = ("client_name", "client_phone",)
    readonly_fields = ("id", "created_at", "updated_at",)
    fieldsets = (
        (None, {"fields": ("id", "status",)}),
        ("Клиент", {"fields": ("client_name", "client_phone", "client_comment",)}),
        ("Дополнительное", {"fields": ("created_at", "updated_at",)})
    )
    inlines = [OrderItemTabularInline, ]
