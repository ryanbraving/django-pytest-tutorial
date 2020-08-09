from django.test import RequestFactory
from django.urls import reverse
from django.contrib.auth.models import User, AnonymousUser
from products.views import product_detail
from mixer.backend.django import mixer
from django.test import TestCase
import pytest


# Approach1
# class TestViews:
#
#     def test_product_detail_authenticated(self):
#         mixer.blend('products.Product')
#         path = reverse('detail', kwargs={'pk': 1})
#         request = RequestFactory().get(path)
#         request.user = mixer.blend(User)
#
#         response = product_detail(request, pk=1)
#         assert response.status_code == 200
#
#     def test_product_detail_unauthenticated(self):
#         mixer.blend('products.Product')
#         path = reverse('detail', kwargs={'pk': 1})
#         request = RequestFactory().get(path)
#         request.user = AnonymousUser()
#
#         response = product_detail(request, pk=1)
#         # assert response.status_code == 302
#         assert 'accounts/login' in response.url



# # Approach2: Merge with unittest
# @pytest.mark.django_db
# class TestViews(TestCase):
#
#     @classmethod
#     def setUpClass(cls):
#         super(TestViews, cls).setUpClass()
#         cls.path = reverse('detail', kwargs={'pk': 1})
#         cls.factory = RequestFactory()
#
#
#     def test_product_detail_authenticated(self):
#         mixer.blend('products.Product')
#         path = self.path
#         request = self.factory.get(path)
#         request.user = mixer.blend(User)
#
#         response = product_detail(request, pk=1)
#         assert response.status_code == 200
#
#     def test_product_detail_unauthenticated(self):
#         mixer.blend('products.Product')
#         path = self.path
#         request = self.factory.get(path)
#         request.user = AnonymousUser()
#
#         response = product_detail(request, pk=1)
#         # assert response.status_code == 302
#         assert 'accounts/login' in response.url


# Approach3 : fixtures
@pytest.fixture
def factory():
    return RequestFactory()

@pytest.fixture
def product(db):
    return mixer.blend('products.Product')

@pytest.fixture
def path(db):
    return reverse('detail', kwargs={'pk': 1})

def test_product_detail_authenticated(factory, product, path):
    request = factory.get(path)
    request.user = mixer.blend(User)

    response = product_detail(request, pk=1)
    assert response.status_code == 200

def test_product_detail_unauthenticated(factory, product, path):
    request = factory.get(path)
    request.user = AnonymousUser()

    response = product_detail(request, pk=1)
    # assert response.status_code == 302
    assert 'accounts/login' in response.url
