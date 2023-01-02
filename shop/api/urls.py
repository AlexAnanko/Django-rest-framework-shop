from django.urls import path, re_path
from .views import CategoriesListView, DiscountsListView, ProducersListView, ProductsListView, PromocodesListView, \
    CategoryProductsView, ProducerProductView, DiscountProductView, RegistrationView, ActivateAccountView, \
    LoginView, BasketView


urlpatterns = [
    path('categories-all', CategoriesListView.as_view(), name='categories-all'),
    path('discounts-all', DiscountsListView.as_view(), name='discounts-all'),
    path('products-all', ProductsListView.as_view(), name='products-all'),
    path('producers-all', ProducersListView.as_view(), name='producers-all'),
    path('promocodes-all', PromocodesListView.as_view(), name='promocodes-all'),
    path('category/<int:cat_id>/', CategoryProductsView.as_view()),
    path('producer/<int:producer_id>/', ProducerProductView.as_view()),
    path('discount/<int:discount_id>/', DiscountProductView.as_view()),
    re_path(r'^register/', RegistrationView.as_view()),
    re_path(r'^login/', LoginView.as_view()),
    re_path(r'^basket/', BasketView.as_view()),

    path('activate/<slug:uidb64>/<slug:token>/', ActivateAccountView.as_view(), name='activate'),

]
