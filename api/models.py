from django.db import models

# Create your models here.

class Base(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)
    state = models.BooleanField(default=True)
    
    class Meta:
        abstract = True
        
class Company(Base):
    name = models.CharField(max_length=50)
    website = models.URLField(max_length=100)
    foundation = models.PositiveIntegerField()
    
    