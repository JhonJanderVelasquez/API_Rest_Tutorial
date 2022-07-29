# from django.shortcuts import render
from django.views import View
from .models import Company
from django.http import JsonResponse

# Convierte el modelo a un diccionario
from django.forms.models import model_to_dict

# Create your views here.
class CompanyListView (View):
    def get (self, request):
        clist = Company.objects.all()
        return JsonResponse(list(clist.values()), safe=False)

    # def post (self, request):
    #     pass
    # def put (self, request):
    #     pass
    # def delete (self, request):
    #     pass

class CompanyDetailView (View):
    def get (self, request, pk):
        company = Company.objects.get(pk=pk)
        return JsonResponse(model_to_dict(company))

    # def post (self, request):
    #     pass
    # def put (self, request):
    #     pass
    # def delete (self, request):
    #     pass
    