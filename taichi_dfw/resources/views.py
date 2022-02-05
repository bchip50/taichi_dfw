# from django.shortcuts import render
from django.views.generic import DetailView, ListView

from .models import Resource


class ResourceListView(ListView):
    model = Resource


resource_list_view = ResourceListView.as_view()


class ResourceDetailView(DetailView):
    model = Resource


resource_detail_view = ResourceDetailView.as_view()
