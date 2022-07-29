# from django.shortcuts import render
from django.views import View
from .models import Company
from django.http import JsonResponse

# Create your views here.
class CompanyListView (View):
    def get (self, request):
        list = Company.objects.all()
        return JsonResponse(list, False)

    # def post (self, request):
    #     pass
    # def put (self, request):
    #     pass
    # def delete (self, request):
    #     pass

class CompanyDetailView (View):
    def get (self, request):
        list = Company.objects.get(pk=pk)
        return JsonResponse(list, False)

    # def post (self, request):
    #     pass
    # def put (self, request):
    #     pass
    # def delete (self, request):
    #     pass
    