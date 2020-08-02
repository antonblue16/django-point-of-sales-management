from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth import get_user_model
import uuid

# Create your models here.

User = get_user_model()

class InPos(models.Model):
    name = models.CharField(max_length=256)
    user = models.ForeignKey(User, related_name="userInPos", on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    unitPrice = models.DecimalField(max_digits=15, decimal_places=0)
    price = models.DecimalField(max_digits=15, decimal_places=0)
    created_date = models.TimeField(default=timezone.now)

    def __str__(self):
        return self.name +" | " + str(self.price)

    def get_absolute_url(self):
        return reverse("cashier:inPosDetail", kwargs={"pk": self.pk})

    class Meta:
        ordering = ['-created_date']
    

class OutPos(models.Model):
    name = models.CharField(max_length=256)
    user = models.ForeignKey(User, related_name="userOutPos", on_delete=models.CASCADE)
    detail = models.TextField()
    nominal = models.DecimalField(max_digits=15, decimal_places=0)
    created_date = models.TimeField(default=timezone.now)

    def __str__(self):
        return self.name +" | " + str(self.nominal)
    
    def get_absolute_url(self):
        return reverse("cashier:outPosDetail", kwargs={"pk": self.pk})

    class Meta:
        ordering = ['-created_date']


class CashierPos(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    checkIn = models.ManyToManyField(InPos, blank=True)
    checkOut = models.ManyToManyField(OutPos, blank=True)
    created_date = models.DateTimeField(default=timezone.now)
    closed_date = models.DateTimeField(null=True, blank=True)

    class Meta:
        ordering = ['created_date']

    def __str__(self):
        return str(self.id)

    def cashierClose(self):
        self.closed_date = timezone.now()
        self.save()

    def get_absolute_url(self):
        return reverse('cashier:detailCashier', kwargs={"pk": self.pk})
