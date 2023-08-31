from django.urls import path

# import view functions
from receipts.views import receipt_list, create_receipt

# register views
urlpatterns = [
    path("", receipt_list, name="home"),
    path("create/", create_receipt, name="create_receipt"),
]
