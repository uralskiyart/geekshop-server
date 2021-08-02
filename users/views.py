from django.contrib.auth.context_processors import auth
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponseRedirect, request
from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy, reverse
from django.contrib.auth import login as auth_login

from common.views import CommonContextMixin, CommonSendVerifyMailMixin

from users.forms import UserLoginForm, UserRegistrationForm, UserProfileForm
from baskets.models import Basket

from users.models import User


class UserLoginView(LoginView):
    template_name = 'users/login.html'
    form_class = UserLoginForm
    title = 'GeekShop - Login'


class UserRegistrationView(CommonContextMixin, CommonSendVerifyMailMixin, SuccessMessageMixin, CreateView):
    model = User
    form_class = UserRegistrationForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:login')
    success_message = 'Registration succes!'
    title = 'GeekShop - Registration'


class UserVerifyView(LoginView):
    model = User
    template_name = 'users/verify.html'
    title = 'GeekShop - Verify'

    @staticmethod
    def verify(request, email, activation_key):
        user = User.objects.filter(email=email).first()
        if user:
            if user.activation_key == activation_key and not user.is_activation_key_expired():
                user.is_active = True
                user.save()
                auth_login(request, user)
            return render(request, 'users/verify.html')
        return HttpResponseRedirect(reverse('users:login'))


class UserProfileView(CommonContextMixin, UpdateView):
    model = User
    form_class = UserProfileForm
    template_name = 'users/profile.html'
    title = 'GeekShop - Profile'

    def get_success_url(self):
        return reverse_lazy('users:profile', args=(self.object.id,))

    def get_context_data(self, **kwargs):
        context = super(UserProfileView, self).get_context_data(**kwargs)
        context['baskets'] = Basket.objects.filter(user=self.object)
        return context


class UserLogoutView(LogoutView):
    pass

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


# def logout(request):
#     auth.logout(request)
#     return HttpResponseRedirect(reverse('index'))
