from django.contrib import admin
from receipts.models import ExpenseCategory, Account, Receipt


# Register your models here.
@admin.register(ExpenseCategory)
class ExpenseCategory(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(Account)
class Account(admin.ModelAdmin):
    list_display = ("name", "number")


@admin.register(Receipt)
class Receipt(admin.ModelAdmin):
    list_display = ("vendor",)
