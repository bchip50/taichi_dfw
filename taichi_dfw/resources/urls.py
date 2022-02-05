from django.urls import path

from .views import resource_detail_view, resource_list_view

app_name = "resources"
urlpatterns = [
    path("<slug:slug>/", view=resource_detail_view, name="detail"),
    path("", view=resource_list_view, name="list"),
]
