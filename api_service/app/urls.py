from django.urls import path
from .views import AdDetailView, UserCreate, AdListView

urlpatterns = [
    #путь к списку объявлений
    path('ads/<int:id>/', AdDetailView.as_view(), name='ad-detail'),
    path('ads/', AdListView.as_view(), name='ad_list'),
    #путь к созданию пользователя
    path('register/', UserCreate.as_view(), name='user-create'),
]
