from django.shortcuts import render
from django.views.generic import (
    TemplateView,
    CreateView,
    ListView,
    UpdateView,
    DeleteView,
)
from .models import Memo
from django.urls import reverse_lazy


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


class MemoDeleteView(DeleteView):
    model = Memo
    success_url = reverse_lazy("list")
