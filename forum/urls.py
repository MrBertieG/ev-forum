from . import views
from django.urls import path

urlpatterns =[
    path('', views.CategoryList.as_view(), name='home'),
    path('category/<str:name>/', views.CategoryDetail.as_view(),
        name='category_detail'),
    path('add-post/', views.PostAdd.as_view(), name='add_post'),
    path('edit-post/<int:id>/', views.PostEdit.as_view(), name='edit_post'),
    path('contact-us/', views.ContactUs.as_view(), name='contact_us'),
]