from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=50, unique=True, allow_unicode=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/guide/category/{self.slug}'

    class Meta:
        verbose_name_plural = 'Categories'

class TagType(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True, allow_unicode=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/guide/tagtype/{self.slug}/'

class TagTeam(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True, allow_unicode=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/guide/tagteam/{self.slug}/'

class Guide(models.Model):
    title = models.CharField(max_length=50, null=True)
    starttime = models.DateTimeField(null=True)
    endtime = models.DateTimeField(null=True)

    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.SET_NULL)
    tagtype = models.ManyToManyField(TagType, blank=True)
    tagteam = models.ManyToManyField(TagTeam, blank=True)

    image = models.URLField(null=True)
    delight_link = models.URLField(null=True)

    def __str__(self):
        return f'[{self.pk}] {self.title}'
