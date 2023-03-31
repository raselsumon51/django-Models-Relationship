from datetime import date
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from app1.models import Author, Book, Customer, Order


def app(request):

    john_doe = Author.objects.create(name='John Doe')
    jane_smith = Author.objects.create(name='Jane Smith')

    # Insert books
    book_1 = Book.objects.create(title='The Book Title', author=john_doe)
    book_2 = Book.objects.create(title='Another Book', author=john_doe)
    book_3 = Book.objects.create(title='Third Book', author=jane_smith)
    return HttpResponse("Hello world!")


def app2(request):

    # insert_data.py

    # Create a customer
    customer = Customer.objects.create(
        name='John Doe', email='johndoe@example.com')

# Create orders for the customer
    order1 = Order.objects.create(
        customer=customer, product_name='Product A', price=10.00, quantity=2, order_date=date.today())
    order2 = Order.objects.create(
        customer=customer, product_name='Product B', price=20.00, quantity=1, order_date=date.today())

    return HttpResponse("Hello world! 2")
