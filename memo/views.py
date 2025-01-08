from django.shortcuts import render
from django.views.generic import TemplateView, CreateView
from .models import Memo

# Create your views here.


class TopView(TemplateView):
    template_name = "top.html"


class MemoCreateView(CreateView):
    model = Memo
    fields = "__all__"
