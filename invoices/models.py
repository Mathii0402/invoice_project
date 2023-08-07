from django.db import models

class Invoice(models.Model):
    date = models.DateField()
    invoice_no = models.IntegerField()
    cust_name = models.CharField(max_length=25)
    def __str__(self):
        return f"{self.invoice_no}"

class InvoiceDetail(models.Model):
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE,related_name='details')
    description = models.TextField()
    quantity = models.IntegerField()
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return f"{self.invoice} {self.description}{self.quantity}{self.unit_price}{self.price}{self.invoice}"
