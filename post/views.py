from typing import List
from django.shortcuts import render

from django.views.generic import ListView

from post.models import Publisher

# Create your views here.

class PublisherListView(ListView):
    model = Publisher
