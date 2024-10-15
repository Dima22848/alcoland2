from django.shortcuts import render
from django.contrib.auth import views as auth_view

class LoginCustomView(auth_view.LoginView):
    next_page = '/'
    template_name = 'account/registration/login.html'


class LogoutCustomView(auth_view.LogoutView):
    next_page = 'login'
    template_name = 'registration/logged_out.html'


class PasswordChangeСustomView(auth_view.PasswordChangeView):
    next_page = 'password_change_done'
    template_name = 'registration/password_change_form.html'


class PasswordChangeDoneCustomView(auth_view.PasswordChangeDoneView):
    template_name = 'registration/password_change_done.html'


class PasswordResetCustomView(auth_view.PasswordResetView):
    success_url = 'password_reset_done'
    template_name = 'registration/password_reset_form.html'


class PasswordResetDoneCustomView(auth_view.PasswordChangeDoneView):
    template_name = 'registration/password_reset_done.html'


class PasswordResetConfirmCustomView(auth_view.PasswordResetConfirmView):
    next_page = 'password_reset_complete'
    template_name = 'registration/password_reset_confirm.html'


class PasswordResetCompleteCustomView(auth_view.PasswordResetCompleteView):
    template_name = 'registration/password_reset_complete.html'


