from django.contrib import admin
from django.utils.translation import ngettext
from django.utils.html import format_html
from .models import Supplier, Product, Node


admin.site.register(Product)
@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ('name', 'debt', 'link_to_supplier')  # Используем новый метод для отображения ссылки

    def link_to_supplier(self, obj):
        return format_html('<a href="{}">{}</a>', obj.get_absolute_url(), obj.name)

    link_to_supplier.short_description = 'Поставщик'

@admin.register(Node)
class NodeAdmin(admin.ModelAdmin):
    list_display = ('name', 'city', 'level', 'link_to_supplier')
    list_filter = ['city']

    actions = ['clear_debts']

    def clear_debts(self, request, queryset):
        updated_count = queryset.update(debt=0.00)
        self.message_user(request, ngettext(
            '%d задолженность успешно очищена.',
            '%d задолженность успешно очищены.',
            updated_count
        ) % updated_count)

    clear_debts.short_description = "Очистить задолженность"

    def link_to_supplier(self, obj):
        if obj.supplier:
            return format_html('<a href="{}">{}</a>', obj.supplier.get_absolute_url(), obj.supplier.name)
        return '-'

    link_to_supplier.short_description = 'Ссылка Поставщика'
