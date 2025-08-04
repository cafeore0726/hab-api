from django.db import models

# Create your models here.

from django.db import models

class Record(models.Model):
    name = models.CharField(max_length=100)
    amount = models.IntegerField()
    recorded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.amount}円)"
