from mixer.backend.django import mixer
from products.models import Product
import pytest
from datetime import datetime


# if you don't use @pytest.mark.django_db you will get below error message
# RuntimeError: Mixer (products.Product): Database access not allowed,
# use the "django_db" mark, or the "db" or "transactional_db" fixtures to enable it.

# # Approach1
# @pytest.mark.django_db
# class TestModels:
#
#     def test_product_is_in_stock_with_mixer(self):
#         product = mixer.blend('products.Product', quantity=1)
#         assert product.is_in_stock == True
#
#     def test_product_is_in_stock(self):
#         product = Product.objects.create(name='Book',
#                             description='An awesome book about Django',
#                             price='19.99',
#                             quantity=1,
#                             published_on=datetime.now())
#
#         assert product.is_in_stock == True
#         # assert product.pk == 1
#
#
#     def test_product_is__not_in_stock(self):
#         product = mixer.blend('products.Product', quantity=0)
#         assert product.is_in_stock == False
#
#     def test_product_str_method(self):
#         product = mixer.blend('products.Product', name='ryan')
#         assert str(product) == 'ryan'

# Approach2 : pytest fixtues and parameters
@pytest.fixture
def product(request, db):
    return mixer.blend('products.Product', quantity=request.param)
    # return mixer.blend('products.Product', name=request.param, quantity=request.param)


@pytest.mark.parametrize('product', [1], indirect=True)
def test_product_is_in_stock_with_mixer(product):
    assert product.is_in_stock == True

@pytest.mark.parametrize('product', [0], indirect=True)
def test_product_is__not_in_stock(product):
    assert product.is_in_stock == False
