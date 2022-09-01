from django.db import models
from django.urls import reverse

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=50)
    color = models.CharField(max_length=20)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('products_detail', kwargs={'pk': self.id})

class Mascot(models.Model):
    name = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    age = models.IntegerField()
    products = models.ManyToManyField(Product)

    def get_absolute_url(self):
      return reverse('detail', kwargs={'mascot_id': self.id})

MEALS = (
    ('B', 'Breakfast'),
    ('L', 'Lunch'),
    ('D', 'Dinner')
)

class Feeding(models.Model):
  date = models.DateField()
  meal = models.CharField(
    max_length=1,
    choices=MEALS,
    default=MEALS[0][0]
  )

  mascot = models.ForeignKey(Mascot, on_delete=models.CASCADE)

  def __str__(self):
    return f"{self.get_meal_display()} on {self.date}"

  class Meta:
    ordering = ['-date']