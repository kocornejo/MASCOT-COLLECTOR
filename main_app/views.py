from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Mascot, Product
from .forms import FeedingForm
from django.views.generic import ListView, DetailView


# Define the home view
def home(request):
  return HttpResponse('<marquee  behavior="scroll" direction="left"><img src="/static/css/imgs/tony.jpg" alt="tony the tiger"></marquee>')

def about(request):
  return render(request, 'about.html')

def mascots_index(request):
  mascots = Mascot.objects.all()  
  return render(request, 'mascots/index.html', { 'mascots': mascots })

def mascots_detail(request, mascot_id):
  mascot = Mascot.objects.get(id=mascot_id)
  products_mascot_doesnt_endorse = Product.objects.exclude(id__in = mascot.products.all().values_list('id'))
  feeding_form = FeedingForm()
  return render(request, 'mascots/detail.html', {'mascot': mascot, 'feeding_form': feeding_form, 'products': products_mascot_doesnt_endorse})


def assoc_product(request, mascot_id, product_id ):
  mascot = Mascot.objects.get(id=mascot_id)
  mascot.products.add(product_id)
  return redirect('detail', mascot_id=mascot_id)

def add_feeding(request, mascot_id):
  form = FeedingForm(request.POST)
  if form.is_valid():
    new_feeding = form.save(commit=False)
    new_feeding.mascot_id = mascot_id
    new_feeding.save()
  return redirect('detail', mascot_id=mascot_id)

class MascotCreate(CreateView):
    model = Mascot
    fields = ['name', 'company', 'description', 'age']

class MascotUpdate(UpdateView):
  model = Mascot
  fields = ['company', 'description', 'age']

class MascotDelete(DeleteView):
  model = Mascot
  success_url = '/mascots/'

class ProductList(ListView):
  model = Product

class ProductDetail(DetailView):
  model = Product

class ProductCreate(CreateView):
  model = Product
  fields = '__all__'

class ProductUpdate(UpdateView):
  model = Product
  fields = ['name', 'color']

class ProductDelete(DeleteView):
  model = Product
  success_url = '/products/'
