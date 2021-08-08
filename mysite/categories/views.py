from django.db import models
from categories.models import Laptop, Mobile, PC_table
from django.shortcuts import render
from django.views.generic import ListView, DetailView


def slidebar(request):
    return render(request, 'categories/index_categories.html')


class PCListView(ListView):
    model = PC_table
    template_name = 'categories/table_pc.html'
    context_object_name = 'pc'


class LaptopListView(ListView):
    model = Laptop
    template_name = 'categories/laptop_categories.html'
    context_object_name = 'laptop'


class MobileListView(ListView):
    model = Mobile
    template_name = 'categories/mobile_categories.html'
    context_object_name = 'mobile'


class LaptopMoreDetails(DetailView):
    model = Laptop
    template_name = 'categories/laptop_details.html'
    context_object_name = 'laptop'
