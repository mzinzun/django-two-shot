from django.urls import path

# import view functions
from receipts.views import receipt_list

# register views
urlpatterns = [
    path("", receipt_list, name="home"),
]
