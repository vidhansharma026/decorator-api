from django.urls import path
from . import views

urlpatterns = [
    path('', views.AllData, name='alldata'),
    path('onedata/<str:pk>', views.OneData, name='onedata'),
    path('create/', views.CreateData, name='create'),
    path('update/<str:pk>', views.UpdateData, name='update'),
    path('delete/<str:pk>', views.DeleteData, name='delete'),
]