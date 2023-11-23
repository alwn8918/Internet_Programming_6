from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=50, unique=True, allow_unicode=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Categories'

class Tag(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/guide/tag/{self.slug}/'

class Guide(models.Model):
    title = models.CharField(max_length=50, null=True)
    period = models.CharField(max_length=50, null=True)

    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.SET_NULL)
    tag = models.ManyToManyField(Tag, blank=True)

    image = models.URLField(null=True)
    delight_link = models.URLField(null=True)

    def __str__(self):
        return f'[{self.pk}] {self.title}'
