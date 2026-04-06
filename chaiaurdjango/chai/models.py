from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

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
    description=models.TextField(default='')
    price=models.DecimalField(max_digits=5, decimal_places=2)
    def __str__(self):
        return self.name
    
#one to Many

class chaiReview(models.Model):
    RATE_CHOICES = [(i, str(i)) for i in range(1, 6)]
    chai = models.ForeignKey(chaiVarity,on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=RATE_CHOICES)
    comment = models.TextField()
    date_added = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return f"{self.user.username} - {self.chai.name} ({self.rating}/5)"

#many to Many

class Store(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=200)
    chai_vareties = models.ManyToManyField(chaiVarity, related_name='stores')  
    def __str__(self):
        return self.name
    
#one to one

class chaiCertificate(models.Model):
    chai = models.OneToOneField(chaiVarity, on_delete=models.CASCADE, related_name='certificate')
    certificate_number = models.CharField(max_length=50)
    issue_date = models.DateField(default=timezone.now)
    expiry_date = models.DateField()
    
    def __str__(self):
        return f"Certificate for {self.chai.name} - {self.certificate_number}"  