from django.core.management.base import BaseCommand

from shop.models import Product


PRODUCTS = [
    {
        "name": "Лампа «Полдень»",
        "slug": "lamp-noon",
        "description": "Мягкий свет для долгих вечеров и спокойного утра.",
        "category": "Для дома",
        "price": "4290.00",
        "glyph": "☼",
        "is_featured": True,
    },
    {
        "name": "Керамическая ваза",
        "slug": "ceramic-vase",
        "description": "Небольшая серия ручной работы, каждая чуть особенная.",
        "category": "Для дома",
        "price": "3150.00",
        "glyph": "◒",
        "is_featured": True,
    },
    {
        "name": "Наушники «Тихо»",
        "slug": "quiet-headphones",
        "description": "Чистый звук и тишина, когда она особенно нужна.",
        "category": "Техника",
        "price": "6890.00",
        "glyph": "♫",
        "is_featured": True,
    },
    {
        "name": "Термокружка «Маршрут»",
        "slug": "route-mug",
        "description": "Сохраняет напиток горячим и помещается в рюкзак.",
        "category": "Аксессуары",
        "price": "1890.00",
        "glyph": "☕",
        "is_featured": False,
    },
    {
        "name": "Плед «Выходной»",
        "slug": "weekend-throw",
        "description": "Мягкий хлопок и правильный повод никуда не спешить.",
        "category": "Для дома",
        "price": "5290.00",
        "glyph": "≈",
        "is_featured": False,
    },
    {
        "name": "Блокнот «Мысли»",
        "slug": "thoughts-notebook",
        "description": "Плотная бумага для планов, заметок и внезапных идей.",
        "category": "Аксессуары",
        "price": "790.00",
        "glyph": "✎",
        "is_featured": False,
    },
]


class Command(BaseCommand):
    help = "Добавить демонстрационные товары, если их еще нет"

    def handle(self, *args, **options):
        for product in PRODUCTS:
            Product.objects.update_or_create(slug=product["slug"], defaults=product)
        self.stdout.write(self.style.SUCCESS(f"Загружено товаров: {len(PRODUCTS)}"))