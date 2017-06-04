from __future__ import unicode_literals
from django.utils import timezone

from django.db import models

class BetaAccount(models.Model):
    
    created_date = models.DateTimeField(
            default=timezone.now)
    email = models.TextField()

    def __str__(self):
        return self.email