from django.urls import path


from .views import (
    AddListAPIView,
    AddDetailAPIView,
    AddCreateAPIView,
    AddDeleteAPIView, 
    AddUpdateAPIView,
)

urlpatterns=[
    path('', AddListAPIView.as_view()),
    path('create/', AddCreateAPIView.as_view()),
    path('update/<int:pk>',AddUpdateAPIView.as_view()),
    path('delete/<int:pk>', AddDeleteAPIView.as_view()),
    path('<int:pk>/', AddDetailAPIView.as_view()),  
]


