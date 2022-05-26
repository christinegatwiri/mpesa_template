from time import timezone
from django.db import models

'''
1. Create transaction model with
    -ID, timestamp, amount, phone no., account number, transaction status
2. Create util to call the MPESA API (under api.pokea.co)
3. Initiate transaction(STK Push)
4. Listen for transaction status update
'''

class Transaction(models.Model):
    id = models.BigAutoField(primary_key=True, unique=True)
    timestamp = models.DateTimeField(default=timezone.now)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=30)
    # user field

    def __str__(self) -> str:
        return super().__str__()