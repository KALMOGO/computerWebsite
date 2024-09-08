from django.db import models
from ..suppliers.models import *
from django.core.exceptions import ValidationError
import random
from computerWebsite.settings import image_max_height, image_max_width

class Computer(models.Model):
    screen = models.CharField(max_length=100, blank=True, null=True)
    processor_brand = models.CharField(max_length=100, blank=True, null=True)
    processor_type = models.CharField(max_length=100, blank=True, null=True)
    processor_speed = models.CharField(max_length=100, blank=True, null=True)
    number_of_cores = models.IntegerField(blank=True, null=True)
    ram = models.CharField(max_length=100, blank=True, null=True)
    hard_drive = models.CharField(max_length=100, blank=True, null=True)
    keyboard_description = models.TextField(blank=True, null=True)
    os = models.CharField(max_length=100, blank=True, null=True)  # Operating System
    generation = models.CharField(max_length=100, blank=True, null=True)
    disk_type = models.CharField(max_length=100, blank=True, null=True)
    color = models.CharField(max_length=100, blank=True, null=True)
    weight = models.FloatField(blank=True, null=True)
    seller_warranty = models.CharField(max_length=100, blank=True, null=True)
    screen_resolution = models.CharField(max_length=100, blank=True, null=True)
    graphics_card_description = models.TextField(blank=True, null=True)
    gpu = models.CharField(max_length=100, blank=True, null=True)
    ram_type = models.CharField(max_length=100, blank=True, null=True)  # RAM type
    connectivity_type = models.CharField(max_length=100, blank=True, null=True)
    technology_type = models.CharField(max_length=100, blank=True, null=True)
    bluetooth = models.BooleanField(default=False, blank=True, null=True)
    hardware_interface = models.CharField(max_length=100)
    number_of_hdmi_ports = models.IntegerField(blank=True, null=True)
    number_of_usb_2_0_ports = models.IntegerField(blank=True, null=True)
    number_of_usb_3_0_ports = models.IntegerField(blank=True, null=True)
    connector_type = models.CharField(max_length=100, blank=True, null=True)
    included_software = models.TextField(blank=True, null=True)
    miscellaneous = models.TextField(blank=True, null=True)
    availability_of_spare_parts = models.BooleanField(default=True)
    description = models.TextField(blank=True, null=True)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    stock = models.IntegerField(default=0)
    brand = models.CharField(max_length=100, blank=True, null=True) 
    creation_date = models.DateTimeField(auto_now_add=True)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, related_name='computers')
    unit_cost = models.DecimalField(max_digits=10, decimal_places=2)
    commission = models.FloatField(default=0.0)

    class Meta:
        verbose_name_plural = "Computer List"
        ordering = ("-creation_date",)

    def __str__(self):
        return f"{self.brand.name} - {self.model}"



def max_image_size(image):
    # Vérifie la taille de l'image téléchargée
    # Ici, vous pouvez spécifier la taille maximale en pixels
    
    height = image.height
    width = image.width

    if height > image_max_height or width > image_max_width:
        raise ValidationError("La taille de l'image ne doit pas dépasser 1000x1000 pixels.")
    
    

class ComputerPhoto(models.Model):
    image = models.ImageField(upload_to='media/computers/images/', validators=[max_image_size])
    computer = models.ForeignKey(Computer, on_delete=models.CASCADE, related_name='photos')
    slug = models.SlugField("Slug")
    creation_date = models.DateTimeField(auto_now_add=True)
    url = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        verbose_name_plural = "Computer Photos"
        ordering = ("-creation_date",)

    def save(self, *args, **kwargs) -> None:
        self.slug = f"{self.computer.pk + random.random() * 100}"
        super().save(*args, **kwargs)


