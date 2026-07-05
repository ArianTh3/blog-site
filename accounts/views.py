from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import redirect
from django.views.generic.edit import CreateView

from .forms import LoginForm, CustomCreateUserForm

User = get_user_model()


class CustomLoginView(LoginView):
    form_class = LoginForm
    template_name = 'accounts/login.html'
    redirect_authenticated_user = True  # already-logged-in users get bounced straight to success_url

    def get_success_url(self):
        return '/'

    def form_valid(self, form):
        # LoginView.form_valid() already calls login(self.request, form.get_user())
        # so you don't need to call authenticate()/login() yourself anymore.
        response = super().form_valid(form)
        messages.add_message(self.request, messages.SUCCESS, "you Logged In successfully")
        return response

    def form_invalid(self, form):
        messages.add_message(self.request, messages.ERROR, "You have done something wrong. Please try again")
        return super().form_invalid(form)


class CustomLogoutView(LoginRequiredMixin, LogoutView):
    next_page = '/'


class RegisterView(CreateView):
    model = User
    form_class = CustomCreateUserForm
    template_name = 'accounts/signup.html'
    success_url = '/'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('/')
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.add_message(self.request, messages.SUCCESS, "you Signed up successfully")
        return response

    def form_invalid(self, form):
        messages.add_message(self.request, messages.ERROR, "You have done something wrong . Please try again")
        return super().form_invalid(form)
    


from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy
from .forms import CustomPasswordResetForm, CustomSetPasswordForm


class CustomPasswordResetView(auth_views.PasswordResetView):
    template_name = 'accounts/password_reset_form.html'
    email_template_name = 'accounts/password_reset_email.txt'
    subject_template_name = 'accounts/password_reset_subject.txt'
    form_class = CustomPasswordResetForm
    success_url = reverse_lazy('accounts:password_reset_done')


class CustomPasswordResetDoneView(auth_views.PasswordResetDoneView):
    template_name = 'accounts/password_reset_done.html'


class CustomPasswordResetConfirmView(auth_views.PasswordResetConfirmView):
    template_name = 'accounts/password_reset_confirm.html'
    form_class = CustomSetPasswordForm
    success_url = reverse_lazy('accounts:password_reset_complete')


class CustomPasswordResetCompleteView(auth_views.PasswordResetCompleteView):
    template_name = 'accounts/password_reset_complete.html'