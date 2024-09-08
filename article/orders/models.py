from django.db import models
from  ..computers.models import Computer

class Commend(models.Model):
    first_name = models.CharField(max_length=250)
    last_name  = models.CharField(max_length=250)
    computer   = models.ForeignKey(Computer, related_name = "commend",on_delete=models.CASCADE)
    phone      = models.CharField(max_length=250)
    number         = models.PositiveIntegerField(default=1)
    creation_date  = models.DateTimeField(auto_now_add=True)
    delivery_date  = models.DateField(auto_now=False, auto_now_add=False, blank=True, null=True)
    location   = models.CharField(max_length=250)
    
    class Meta:
        verbose_name_plural = "User commend"
        ordering = ("-creation_date",)
        
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
