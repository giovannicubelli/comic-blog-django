from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
from django.urls import reverse_lazy
from django.contrib import messages
from .forms import CustomUserCreationForm, UserUpdateForm, ProfileUpdateForm, CustomPasswordChangeForm
from .models import Profile

class CustomLoginView(LoginView):
    template_name = 'accounts/login.html'
    # success_url ya está definido por LOGIN_REDIRECT_URL en settings.py

# LogoutView ya existe, solo la referenciamos en urls.py
# class CustomLogoutView(LogoutView):
# template_name = 'accounts/logged_out.html' # Opcional si quieres un template específico

def signup_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user) # Loguear al usuario después de registrarse
            messages.success(request, '¡Registro exitoso! Bienvenido.')
            return redirect('home') # O a 'profile'
    else:
        form = CustomUserCreationForm()
    return render(request, 'accounts/signup.html', {'form': form})

@login_required
def profile_view(request):
    # Profile se crea automáticamente con la señal, así que debería existir
    try:
        profile = request.user.profile
    except Profile.DoesNotExist:
        # Si por alguna razón no existe, créalo (aunque la señal debería manejar esto)
        profile = Profile.objects.create(user=request.user)

    return render(request, 'accounts/profile.html', {'profile': profile})

@login_required
def profile_edit_view(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Tu perfil ha sido actualizado exitosamente.')
            return redirect('profile')
        else:
            messages.error(request, 'Por favor corrige los errores.')
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'user_form': user_form,
        'profile_form': profile_form
    }
    return render(request, 'accounts/profile_edit.html', context)

class CustomPasswordChangeView(PasswordChangeView):
    form_class = CustomPasswordChangeForm
    template_name = 'accounts/password_change.html' # Puedes crear este template o usar el de Django
    success_url = reverse_lazy('profile') # O a donde quieras redirigir

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Tu contraseña ha sido cambiada exitosamente.')
        return response