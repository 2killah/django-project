from django.db import models


class Product(models.Model):
    name = models.CharField("Название", max_length=120)
    slug = models.SlugField(unique=True)
    description = models.TextField("Описание")
    category = models.CharField("Категория", max_length=60)
    price = models.DecimalField("Цена", max_digits=10, decimal_places=2)
    glyph = models.CharField("Символ", max_length=8, default="✳")
    is_featured = models.BooleanField("На главной", default=False)

    class Meta:
        ordering = ["name"]
        verbose_name = "товар"
        verbose_name_plural = "товары"

    def __str__(self):
        return self.name