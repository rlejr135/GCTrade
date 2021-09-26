from django.urls import path
from .views import SignInView, SignUpView


urlpatterns = [
    path('login', SignInView.as_view()),
    # path('/logout', views.Logout, name='logout'),
    path('signup', SignUpView.as_view()),
]


