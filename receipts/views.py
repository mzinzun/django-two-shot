from django.shortcuts import render, redirect
from receipts.models import Receipt, ExpenseCategory, Account
from receipts.forms import CreateReceiptForm
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def receipt_list(request):
    receipts = Receipt.objects.filter(purchaser=request.user)

    context = {
        "receipts": receipts,
    }
    return render(request, "receipts/list.html", context)


@login_required
def create_receipt(request):
    if request.method == "POST":
        form = CreateReceiptForm(request.POST)
        if form.is_valid():
            receipt = form.save(False)
            receipt.purchaser = request.user
            form.save()
            return redirect("home")
    else:
        form = CreateReceiptForm()
    context = {"form": form}
    return render(request, "receipts/createReceipt.html", context)


@login_required
def category_list(request):
    items = ExpenseCategory.objects.filter(owner=request.user)
    context = {"items": items}
    return render(request, "receipts/showCategories.html", context)


def account_list(request):
    items = Account.objects.filter(owner=request.user)
    context = {"items": items}
    return render(request, "receipts/showAccounts.html", context)
