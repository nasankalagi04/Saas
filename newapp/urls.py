from django.urls import path
from .views import subscription_list, add_subscription,edit_subscription

urlpatterns = [
    path('', subscription_list, name='list'),
    path('add/', add_subscription, name='add'),
    path('edit/<int:id>/',edit_subscription, name='edit'),
]
