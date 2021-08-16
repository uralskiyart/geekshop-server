import hashlib
from random import random

from django.contrib import messages
from django.urls import reverse
from django.core.mail import send_mail

from baskets.models import Basket
from geekshop import settings
from users.forms import ExtendUserProfileForm


class CommonContextMixin:
    title = None

    def get_context_data(self, **kwargs):
        context = super(CommonContextMixin, self).get_context_data(**kwargs)
        context['title'] = self.title
        return context


class CommonSendVerifyMailMixin:
    def form_valid(self, form):
        response = super().form_valid(form)
        success_message = self.get_success_message(form.cleaned_data)
        if success_message:
            user = form.save()
            if self.send_verify_mail(user):
                print('Succes sanding')
            else:
                print('Sending failed')
            messages.success(self.request, success_message)
        return response

    def send_verify_mail(self, user):
        subject = 'Verify your account'
        self.generate_activation_key(user)
        print(user.email, user.activation_key)
        link = reverse('users:verify', args=[user.email, user.activation_key])
        message = f'{settings.DOMAIN}{link}'
        return send_mail(subject, message, settings.EMAIL_HOST_USER, [user.email], fail_silently=False)

    @staticmethod
    def generate_activation_key(user):
        user.is_active = False
        salt = hashlib.sha1(str(random()).encode('utf8')).hexdigest()[:6]
        user.activation_key = hashlib.sha1((user.email + salt).encode('utf8')).hexdigest()
        user.save()


class CommonExtendMProfileMixin:
    extend_form_class = ExtendUserProfileForm
    extend_form = None

    def get_context_data(self, **kwargs):
        context = super(CommonExtendMProfileMixin, self).get_context_data(**kwargs)
        context['extend_form'] = self.extend_form_class(self.request.GET or None, instance=self.request.user.extenduser)
        return context

    def post(self, request, *args, **kwargs):
            form = self.form_class(request.POST, request.FILES, instance=request.user)
            extend_form = self.extend_form_class(request.POST, instance=request.user.extenduser)
            if form.is_valid() and extend_form.is_valid():
                return self.form_valid(form)
            else:
                return self.get_context_data(form=form, extend_form=extend_form)
