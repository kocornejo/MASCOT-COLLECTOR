from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Mascot
from .forms import FeedingForm






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
  feeding_form = FeedingForm()
  return render(request, 'mascots/detail.html', {
    'mascot': mascot, 'feeding_form': feeding_form
  })

def add_feeding(request, mascot_id):
  form = FeedingForm(request.POST)
  if form.is_valid():
    new_feeding = form.save(commit=False)
    new_feeding.mascot_id = mascot_id
    new_feeding.save()
  return redirect('detail', mascot_id=mascot_id)

class MascotCreate(CreateView):
    model = Mascot
    fields = '__all__'

class MascotUpdate(UpdateView):
  model = Mascot
  fields = ['product', 'description', 'age']

class MascotDelete(DeleteView):
  model = Mascot
  success_url = '/mascots/'
