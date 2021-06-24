from django.db import models


class Serie(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField()

    class Meta:
        ordering = ("name",)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f"/{self.slug}/"


class Brand(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField()

    class Meta:
        ordering = ("name",)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f"/{self.slug}/"


class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField()

    class Meta:
        ordering = ("name",)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f"/{self.slug}/"


class Product(models.Model):
    id1 = models.CharField(max_length=50)
    id2 = models.CharField(blank=True, null=True, max_length=50)
    name = models.CharField(max_length=255)
    slug = models.SlugField()
    category = models.ForeignKey(
        Category, related_name="products", on_delete=models.CASCADE
    )
    unit = models.CharField(max_length=25)
    serie = models.ForeignKey(Serie, related_name="products", on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, related_name="products", on_delete=models.CASCADE)
    subID = models.CharField(blank=True, null=True, max_length=50)
    subID2 = models.CharField(blank=True, null=True, max_length=50)
    minReq = models.DecimalField(blank=True, null=True, max_digits=6, decimal_places=2)
    maxReq = models.DecimalField(blank=True, null=True, max_digits=6, decimal_places=2)
    departmentPrice = models.DecimalField(max_digits=6, decimal_places=2)
    rate = models.DecimalField(max_digits=6, decimal_places=2)
    specialAttr = models.TextField(blank=True, null=True)
    cost = models.DecimalField(max_digits=6, decimal_places=2)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ("-date_added",)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f"/{self.category.slug}/{self.brand.slug}/{self.serie.slug}/{self.slug}/"
