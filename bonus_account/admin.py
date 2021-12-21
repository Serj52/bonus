from django.contrib import admin
from .models import Account, Trasaction


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname', 'tel_number', 'card_number', 'balance')
    search_fields = ('surname', 'tel_number', 'card_number')

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ['balance', 'card_number']
        else:
            return self.readonly_fields


@admin.register(Trasaction)
class TrasactionAdmin(admin.ModelAdmin):
    list_display = ('type', 'sum', 'date', 'account')
    list_filter = ('type', 'date')




# Register your models here.
