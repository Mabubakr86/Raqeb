from django.db import models

# Create your models here.


class Gold(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=7, decimal_places=2, null=True)

    class Meta:
        verbose_name_plural = 'Gold'

    def __str__(self):
        return self.name
