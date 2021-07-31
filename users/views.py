from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy, reverse
from django.contrib import messages
from django.core.mail import send_mail

from common.views import CommonContextMixin
from geekshop import settings
from users.forms import UserLoginForm, UserRegistrationForm, UserProfileForm
from baskets.models import Basket

from users.models import User


class UserVerifyMail:
    def verify(self, email, activation_key):
        pass

    def send_verify_mail(self, user):
        subject = 'Verify your account'
        link = reverse('users:verify', args=[user.email, user.activation_key])
        message = f'{settings.DOMAIN}{link}'
        return send_mail(subject, message, settings.EMAIL_HOST_USER, [user.email], fail_silently=False)


# def login(request):
#     if request.method == 'POST':
#         form = UserLoginForm(data=request.POST)
#         if form.is_valid():
#             username = request.POST['username']
#             password = request.POST['password']
#             user = auth.authenticate(username=username, password=password)
#             if user and user.is_active:
#                 auth.login(request, user)
#                 return HttpResponseRedirect(reverse('index'))
#     else:
#         form = UserLoginForm()
#     context = {'tittle': 'Geekshop - Login', 'form': form}
#     return render(request, 'users/login.html', context)


class UserLoginView(LoginView):
    template_name = 'users/login.html'
    form_class = UserLoginForm
    title = 'GeekShop - Login'


# def register(request):
#     if request.method == 'POST':
#         form = UserRegisterForm(data=request.POST)
#         if form.is_valid():
#             form.save()
#             messages.success(request, 'Registration is succes!')
#             return HttpResponseRedirect(reverse('users:login'))
#     else:
#         form = UserRegisterForm()
#     context = {'tittle': 'Geekshop - Register', 'form' : form}
#     return render(request, 'users/register.html', context)


class UserRegistrationView(CommonContextMixin, SuccessMessageMixin, CreateView, UserVerifyMail):
    model = User
    form_class = UserRegistrationForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:login')
    success_message = 'Registration succes!'
    title = 'GeekShop - Registration'


    def post(self, request, *args, **kwargs):
        """
        Handle POST requests: instantiate a form instance with the passed
        POST variables and then check if it's valid.
        """
        form = self.get_form()
        print(form, '!')
        if form.is_valid():
            user = form.save()
            print(user)
            print(form)
            if self.send_verify_mail(user):
                print('succes sanding')
            else:
                print('sending failed')
            return self.form_valid(form)
        else:
            return self.form_invalid(form)


# @login_required
# def profile(request):
#     user = request.user
#     if request.method == 'POST':
#         form = UserProfileForm(data=request.POST, files=request.FILES, instance=user)
#         if form.is_valid():
#             form.save()
#             messages.success(request, 'Profile is changed!')
#             return HttpResponseRedirect(reverse('users:profile'))
#         else:
#             print(form.errors)
#     else:
#         form = UserProfileForm(instance=user)
#         context = {
#             'title': 'GeekShop - Profile',
#             'form': form,
#             'baskets': Basket.objects.filter(user=user),
#         }
#     return render(request, 'users/profile.html', context)


class UserProfileView(CommonContextMixin, UpdateView):
    model = User
    form_class = UserProfileForm
    template_name = 'users/profile.html'
    title = 'GeekShop - Profule'

    def get_success_url(self):
        return reverse_lazy('users:profile', args=(self.object.id,))

    def get_context_data(self, **kwargs):
        context = super(UserProfileView, self).get_context_data(**kwargs)
        context['baskets'] = Basket.objects.filter(user=self.object)
        return context

# def logout(request):
#     auth.logout(request)
#     return HttpResponseRedirect(reverse('index'))


class UserLogoutView(LogoutView):
    pass


