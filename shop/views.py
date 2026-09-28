from decimal import Decimal

from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST

from .models import Product


def product_list(request):
    category = request.GET.get("category", "")
    products = Product.objects.all()
    if category:
        products = products.filter(category=category)
    categories = Product.objects.order_by("category").values_list(
        "category", flat=True
    ).distinct()
    return render(
        request,
        "shop/product_list.html",
        {"products": products, "categories": categories, "active_category": category},
    )


def cart_view(request):
    cart = request.session.get("cart", {})
    products = Product.objects.filter(pk__in=cart.keys())
    items = []
    total = Decimal("0.00")
    for product in products:
        quantity = cart.get(str(product.pk), 0)
        subtotal = product.price * quantity
        items.append({"product": product, "quantity": quantity, "subtotal": subtotal})
        total += subtotal
    return render(request, "shop/cart.html", {"items": items, "total": total})


@require_POST
def cart_add(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    cart = request.session.get("cart", {})
    key = str(product.pk)
    cart[key] = cart.get(key, 0) + 1
    request.session["cart"] = cart
    return redirect("cart")


@require_POST
def cart_remove(request, product_id):
    cart = request.session.get("cart", {})
    cart.pop(str(product_id), None)
    request.session["cart"] = cart
    return redirect("cart")


@require_POST
def checkout(request):
    request.session["cart"] = {}
    return render(request, "shop/order_complete.html")