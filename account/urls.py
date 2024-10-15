from django.urls import path
from .views import *

urlpatterns = [
    # url-адреса входа и выхода
    path('login/', LoginCustomView.as_view(), name='login'),
    path('logout/', LogoutCustomView.as_view(), name='logout'),

    # url-адреса смены пароля
    path('password-change/',
         PasswordChangeСustomView.as_view(),
         name='password_change'),
    path('password-change/done/',
         PasswordChangeDoneCustomView.as_view(),
         name='password_change_done'),

    # url-адреса сброса пароля
    path('password-reset/',
         PasswordResetCustomView.as_view(),
         name='password_reset'),
    path('password-reset/done/',
         PasswordResetDoneCustomView.as_view(),
         name='password_reset_done'),
    path('password-reset/<uidb64>/<token>/',
         PasswordResetConfirmCustomView.as_view(),
         name='password_reset_confirm'),
    path('password-reset/complete/',
         PasswordResetCompleteCustomView.as_view(),
         name='password_reset_complete'),
]