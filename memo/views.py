from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, ListView, UpdateView
from .models import Memo


# Create your views here.


class TopView(TemplateView):
    template_name = "top.html"


class MemoListView(ListView):
    model = Memo


class MemoCreateView(CreateView):
    model = Memo
    fields = "__all__"


class MemoUpdateView(UpdateView):
    model = Memo
    fields = "__all__"
    template_name_suffix = "_update_form"
