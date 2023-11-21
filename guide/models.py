from django.db import models

class Guide(models.Model):
    title = models.CharField(max_length=50, null=True)
    period = models.CharField(max_length=50, null=True)

    image = models.URLField(null=True)
    delight_link = models.URLField(null=True)

    def __str__(self):
        return f'[{self.pk}] {self.title}'
