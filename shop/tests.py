from django.test import TestCase
from django.urls import reverse

from .models import Product


class ShopTests(TestCase):
    def setUp(self):
        self.product = Product.objects.create(
            name="Тестовая лампа",
            slug="test-lamp",
            description="Описание товара",
            category="Для дома",
            price="1200.00",
        )

    def test_catalog_shows_products(self):
        response = self.client.get(reverse("home"))
        self.assertContains(response, self.product.name)

    def test_cart_add_and_checkout(self):
        self.client.post(reverse("cart_add", args=[self.product.pk]))
        response = self.client.get(reverse("cart"))
        self.assertContains(response, self.product.name)
        self.assertContains(response, "1200")

        response = self.client.post(reverse("checkout"))
        self.assertContains(response, "Заказ принят")
        self.assertEqual(self.client.session.get("cart"), {})