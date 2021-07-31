from django.urls import reverse
from geekshop import settings
from django.core.mail import send_mail

class CommonContextMixin:
    title = None

    def get_context_data(self, **kwargs):
        context = super(CommonContextMixin, self).get_context_data(**kwargs)
        context['title'] = self.title
        return context


# class CommonUserVerifyMailMixin(CommonContextMixin):
#     def verify(self, email, activation_key):
#         pass
#
#     def send_verify_mail(self, user):
#         subject = 'Verify your account'
#         link = reverse('auth:verify', args=[user.email, user.activation_key])
#         message = f'{settings.DOMAIN}{link}'
#         return send_mail(subject, message, settings.EMAIL_HOST_USER, [user.email], fail_silently=False)