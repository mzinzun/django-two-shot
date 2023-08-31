from django.forms import ModelForm
from receipts.models import Receipt, ExpenseCategory


class CreateReceiptForm(ModelForm):
    class Meta:
        model = Receipt
        fields = (
            "vendor",
            "total",
            "tax",
            "date",
            "category",
            "account",
        )


class CreateExpenseCategory(ModelForm):
    class Meta:
        model = ExpenseCategory
        fields = ("name",)
