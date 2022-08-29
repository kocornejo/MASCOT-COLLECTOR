from django.shortcuts import render
from django.http import HttpResponse
from .models import Mascot

# Add the following import



# class Mascot:
#     def __init__(self, name, product, description, age):
#         self.name = name
#         self.product = product
#         self.description = description
#         self.age = age

# mascots = [
#     Mascot('Tony the Tiger', 'cereal', 'tiger', 61),
#     Mascot('The Energizer Bunny', 'batteries', 'bunny', 34),
#     Mascot('The Noid', 'pizza', 'humanoid with rabbit ears', 36),
#     Mascot('Toomgis', 'convenience store chain', 'humanoid comprised of snacks', 6),
#     Mascot('Little Lad', 'candy', 'british guy', 15)
# ]





# Define the home view
def home(request):
  return HttpResponse('<h1>Hello /ᐠ｡‸｡ᐟ\ﾉ</h1>')

def about(request):
  return render(request, 'about.html')

def mascots_index(request):
  mascots = Mascot.objects.all()  
  return render(request, 'mascots/index.html', { 'mascots': mascots })

def mascots_detail(request, mascot_id):
  mascot = Mascot.objects.get(id=mascot_id)
  return render(request, 'mascots/detail.html', { 'mascot': mascot })
