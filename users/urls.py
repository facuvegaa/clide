from django.urls import path
from .views import ClientUserRegisterView, SellerUserRegisterView ,LoginView, UserView, LogoutView

urlpatterns = [
    path('client_register', ClientUserRegisterView.as_view()),
    path('seller_register', SellerUserRegisterView.as_view()),
    path('login', LoginView.as_view()),
    path('user', UserView.as_view()),
    path('logout', LogoutView.as_view())
]
