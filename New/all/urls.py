from django.urls import path
from . import views
urlpatterns = [
    path('', views.all, name = 'all'),
    path('agents/', views.agent_view.as_view(), name = 'agent'),
    path('product/', views.product_view.as_view(), name = 'product')
]