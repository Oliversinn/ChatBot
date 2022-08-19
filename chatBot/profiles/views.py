from django.shortcuts import render
from profiles.models import Profile
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView


# Create your views here.
class ProfileListView(ListView):
    model = Profile
    template_name = 'profiles/profile_list'


class ProfileDetailView(DetailView):
    model = Profile
    template_name = 'profiles/profile_detail.html'
