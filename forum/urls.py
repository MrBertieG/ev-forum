from . import views
from django.urls import path

urlpatterns =[
    path('', views.CategoryList.as_view(), name='home'),
    path('category/<str:name>/',views.CategoryDetail.as_view(),
        name='category_detail'),
]