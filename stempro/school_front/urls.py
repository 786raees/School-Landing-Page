from django.urls import path
from . import views as SVF

urlpatterns = [
    path("", SVF.IndexView.as_view(), name="index_page"),
]
