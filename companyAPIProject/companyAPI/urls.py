from django.contrib import admin
from django.urls import path
from .views import CompanyListView

urlpatterns = [
    path('company/', CompanyListView.as_view, name='company_list' ),
]
