from django.urls import path
from .views import product_view , product_detail ,product_cat
app_name = "blog"

urlpatterns = [
path('' , product_view, name='index'),
path('detail/<int:pk>' , product_detail, name='detail'),
path('category/<slug:slug_cat>',product_cat, name='category'),
]
