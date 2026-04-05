from django.db import models
from django.utils import timezone

# Create your models here.
class chaiVarity(models.Model):
    CHAI_TYPES_CHOICES = [
        ('ML', 'Masala'),
        ('GR', 'Ginger'),
        ('CD', 'Cardamom'),
        ('TL', 'Tulsi'),
        ('LM', 'Lemon'),
        ('SP', 'Spices'),
        ('PL', 'Plain'),
    ]
    name=models.CharField(max_length=100)
    image=models.ImageField(upload_to='chais/')
    date_added=models.DateTimeField(default=timezone.now)
    type=models.CharField(max_length=2, choices=CHAI_TYPES_CHOICES)
    def __str__(self):
        return self.name