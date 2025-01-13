from django.urls import path
from .views import signup_view
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('signup/', signup_view, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login')
    # path('', views.authenticate, name='authenticate'),
    # path('login/', views.login, name='login'),
    # path('signup/', views.signup, name='signup')
]
