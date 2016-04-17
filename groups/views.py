from django.shortcuts import render
from .models import Group, UserGroup
from django.contrib.auth.models import User
from django.shortcuts import redirect, render, get_object_or_404
from django.core.urlresolvers import reverse, reverse_lazy
from django.views import generic
from django.conf import settings
from django.views.generic import CreateView, UpdateView, DetailView


class IndexView(generic.ListView):
    template_name = 'groups/index.html'

    def get_queryset(self):
        return Group.objects.all()


class GroupDetail(generic.DetailView):
    model = Group
    template_name = 'groups/detail.html'


class GroupCreate(generic.CreateView):
    model = Group
    fields = ['name', 'description', 'area', 'is_public', 'creator']


class ShowUsers(generic.ListView):
    template_name = 'groups/joined.html'

    def get_queryset(self):
        return UserGroup.objects.all()

class JoinGroup(generic.CreateView):
    model = UserGroup
    template_name = 'groups/join.html'
    fields = ['user', 'group']
    success_url = reverse_lazy('groups:index')
