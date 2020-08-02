from django.urls import path, include
from . import views

app_name = 'cashier'

urlpatterns = [
    path('', views.ListCashier.as_view(), name='allList'),
    path('history/', views.ListHistory.as_view(), name='historyList'),
    path('history/<pk>', views.DetailHistory.as_view(), name='detailHistory'),
    path('create/', views.CreateCashier.as_view(), name='createCashier'),
    path('<pk>/', views.DetailCashier.as_view(), name='detailCashier'),
    path('<pk>/in/create/',views.CreateInPos.as_view(), name='createIn'),
]
