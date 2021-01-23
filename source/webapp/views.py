from urllib import request

from django.shortcuts import render
from django.views.generic import ListView
from django.contrib.auth.models import User


class IndexView(ListView):
    template_name = 'index.html'
    context_object_name = 'friends'
    paginate_by = 10
    paginate_orphans = 0
    model = User
    ordering = ['username']

    def get_queryset(self):
        data = super().get_queryset()
        # if not self.request.GET.get('is_admin', None):
        #     data = data.filter(status='moderated')
        return data