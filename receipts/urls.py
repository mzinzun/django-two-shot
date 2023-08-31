from django.urls import path

# import view functions
from receipts.views import (
    receipt_list,
    create_receipt,
    category_list,
    account_list,
    create_category,
)

# register views
urlpatterns = [
    path("", receipt_list, name="home"),
    path("create/", create_receipt, name="create_receipt"),
    path("categories/", category_list, name="category_list"),
    path("categories/create/", create_category, name="create_category"),
    path("accounts/", account_list, name="account_list"),
]
