from taichi_dfw.resources.models import Resource
from taichi_dfw.styles.models import Style


def style_menu(request):
    sty_menu = {"style_menu": Style.objects.values("title", "slug")}
    return sty_menu


def resource_menu(request):
    res_menu = {
        "res_menu": Resource.objects.values("title", "link_type", "link", "visibility")
    }
    return res_menu
