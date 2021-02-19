from django.urls import path, include
from rest_framework.routers import DefaultRouter
from recipe_management_api import views


router = DefaultRouter()
router.register('profile', views.UserProfileViewSet)
router.register('recipe', views.UserRecipeViewSet)



urlpatterns = [
    path('hello-view', views.HelloAPiView.as_view()),
    path('login',views.UserLoginApiView.as_view()),
    path('change_password/<int:pk>/', views.ChangePasswordView.as_view(), name='change_password'),
    path('',include(router.urls))
]