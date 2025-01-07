from django.contrib import admin
from .models import Memo

# Register your models here.


class MemoAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "content")
    search_filelds = "title"


admin.site.register(Memo, MemoAdmin)
