from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views import generic
from django.views.generic import View
from .models import Food

class IndexView(generic.ListView):
	template_name='ulam/index.html'
	context_object_name = 'all_food'

	def get_queryset(self):
		return Food.objects.all()

class DetailView(generic.DetailView):
	model = Food
	template_name='ulam/detail.html'

class FoodCreate(CreateView):
	model = Food
	fields = ['food_name', 'food_caption', 'food_picture']

class FoodUpdate(UpdateView):
	model = Food
	fields = ['food_name', 'food_caption', 'food_picture']

class FoodDelete(DeleteView):
	model = Food
	success_url = reverse_lazy('ulam:index')

















