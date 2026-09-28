from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Product",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=120, verbose_name="Название")),
                ("slug", models.SlugField(unique=True)),
                ("description", models.TextField(verbose_name="Описание")),
                ("category", models.CharField(max_length=60, verbose_name="Категория")),
                ("price", models.DecimalField(decimal_places=2, max_digits=10, verbose_name="Цена")),
                ("glyph", models.CharField(default="✳", max_length=8, verbose_name="Символ")),
                ("is_featured", models.BooleanField(default=False, verbose_name="На главной")),
            ],
            options={
                "verbose_name": "товар",
                "verbose_name_plural": "товары",
                "ordering": ["name"],
            },
        ),
    ]