from django.test import TestCase
from ..models import Category, Producer, Discount, Promocode, Cashback
from django.urls import reverse


class TestCategoriesView(TestCase):
    fixtures = ["api/tests/fixtures/fixture_categories.json", ]

    def test_categories_all_view(self):
        response = self.client.get(reverse('categories-all'))
        self.assertIsInstance(response.data, list)
        self.assertEqual(response.data, [
            {
                'id': 1,
                'name': 'category1',
                'description': 'some description'
            },
            {
                'id': 2,
                'name': 'category2',
                'description': 'some description1'
            },
            {
                'id': 3,
                'name': 'category3',
                'description': 'some description2'
            },
        ])


class TestProducersView(TestCase):
    fixtures = ["api/tests/fixtures/fixture_producers.json", ]

    def test_produsers_all_view(self):
        response = self.client.get(reverse('producers-all'))
        self.assertIsInstance(response.data, list)
        self.assertEqual(response.data, [
            {
                'id': 1,
                'name': 'producer1',
            },
            {
                'id': 2,
                'name': 'producer2',
            },
            {
                'id': 3,
                'name': 'producer3',
            }
        ])


class TestDiscountsView(TestCase):
    fixtures = ["api/tests/fixtures/fixture_discounts.json", ]

    def test_discounts_all_view(self):

        response = self.client.get(reverse('discounts-all'))
        self.assertIsInstance(response.data, list)
        self.assertEqual(response.data, [
            {
                'id': 1,
                'name': 'discount1',
                'percent': 40,
                'expire_date': "2022-12-17T17:52:08Z"
            },
            {
                'id': 2,
                'name': 'discount2',
                'percent': 20,
                'expire_date': "2022-12-17T17:15:20Z"
            },
        ])


class TestPromocodesView(TestCase):
    fixtures = ["api/tests/fixtures/fixture_promocodes.json", ]

    def test_promocodes_all_view(self):
        response = self.client.get(reverse('promocodes-all'))
        self.assertIsInstance(response.data, list)
        self.assertEqual(response.data, [
            {
                'id': 1,
                'name': 'promocode1',
                'percent': 10,
                'expire_date': '2022-12-17T16:24:22Z',
                'is_allowed_to_sum_with_discounts': True
            },
        ])

#
# class TestProductsView(TestCase):
#     fixtures = [
#                 "api/tests/fixtures/fixture_products.json",
#                 "api/tests/fixtures/fixture_categories.json",
#                 "api/tests/fixtures/fixture_discounts.json",
#                 "api/tests/fixtures/fixture_producers.json",
#                 ]
#
#     def test_products_all_view(self):
#         response = self.client.get(reverse('products-all'))
#         self.assertIsInstance(response.data, list)
#         keys_list_expected = ["id", "name"]
#         self.assertEqual(list(response.data.keys()), keys_list_expected)
#         [
#             {
#                 "id": 1,
#                 "name": "Coca-Cola",
#                 "price": 5,
#                 "count_on_stock": 1000,
#                 "producer": 1,
#                 "category": 1,
#                 "discount": 1
#             },
#         ])
