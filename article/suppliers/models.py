from django.db import models


class Supplier(models.Model):
    company = models.CharField(max_length=150, null=True, blank=True)
    first_name = models.CharField(max_length=100)
    last_name  = models.CharField(max_length=100)
    phone1 = models.CharField(max_length=10, null=True, blank=True)
    phone2 = models.CharField(max_length=10, null=True, blank=True)
    photo  = models.ImageField(upload_to='media/computers/images/', null=True, blank=True)
    creation_date = models.DateTimeField(auto_now_add=True)
    is_partner= models.BooleanField(default=False)
    town      = models.CharField(max_length=200)
    lat  = models.CharField(max_length=200, null=True, blank=True)
    lon  = models.CharField(max_length=200, null=True, blank=True)
    
    class Meta:
        verbose_name_plural = "Suppliers"
        ordering = ("-creation_date",)

    def __str__(self):
        return self.last_name

class Partner(models.Model):
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    creation_date = models.DateTimeField(auto_now_add=True)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        verbose_name_plural = "Partners"
        ordering = ("-creation_date",)

    def __str__(self):
        return f"{self.supplier.first_name} {self.supplier.last_name}"
