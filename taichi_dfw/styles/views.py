# from django.shortcuts import render
# from json import dumps

from django.views.generic import DetailView, ListView

from .models import (  # SeriesResource, Style, StyleResource,; Members,
    Meeting,
    Series,
    Style,
)

# from taichi_dfw.locations.models import Location


class StyleListView(ListView):
    model = Style


style_list_view = StyleListView.as_view()


class ActiveSeriesMixin:
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        sty = context["style"]
        context["resources"] = sty.styleResource.all()
        ser = sty.seriesStyle.all()
        context["series"] = ser
        return context


class StyleDetailView(ActiveSeriesMixin, DetailView):
    model = Style


style_detail_view = StyleDetailView.as_view()


class SeriesDetailView(DetailView):
    model = Series


series_detail_view = SeriesDetailView.as_view()


class MeetingSiteMixin:
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        meet = kwargs["object"]
        context["meetGeo"] = meet.location.geolocation
        context["meetTitle"] = meet.location.title
        return context


class MeetingDetailView(MeetingSiteMixin, DetailView):
    model = Meeting


meeting_detail_view = MeetingDetailView.as_view()
