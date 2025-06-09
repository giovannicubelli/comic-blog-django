from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy # reverse_lazy ya está importado, bien.
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin # Mixins
from django.contrib.auth.decorators import login_required # Decorador
from .models import Post
from .forms import PostForm

# Vista para Home (FBV)
def home_view(request):
    latest_posts = Post.objects.all()[:3] # Los 3 más recientes
    return render(request, 'home.html', {'latest_posts': latest_posts})

# Vista para About (FBV)
def about_view(request):
    return render(request, 'about.html')

# CBV para listar Posts (nuestro "pages/")
class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'
    paginate_by = 6

# CBV para el detalle de un Post
class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'

# CBV para crear un Post (requiere login)
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'
    # --- CORRECCIÓN AQUÍ ---
    success_url = reverse_lazy('blog:post_list') # Añadido 'blog:'

    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)

# CBV para actualizar un Post (requiere login y ser el autor)
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'

    def get_success_url(self):
        # --- CORRECCIÓN AQUÍ ---
        return reverse_lazy('blog:post_detail', kwargs={'pk': self.object.pk}) # Añadido 'blog:'

    def form_valid(self, form):
        # No es estrictamente necesario asignar el autor aquí de nuevo si el post ya tiene uno
        # y solo el autor puede editar. Pero no hace daño si la lógica es que el último en editar
        # se considera el "actualizador" o si quisieras cambiar el autor (lo cual no es el caso aquí).
        # Si el objetivo es solo asegurar que el autor original se mantiene, esta línea no es crítica
        # para la actualización si UserPassesTestMixin ya verifica la autoría.
        # form.instance.autor = self.request.user # Puedes mantenerla o comentarla.
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.autor

# CBV para borrar un Post (requiere login y ser el autor)
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'blog/post_confirm_delete.html'
    # --- CORRECCIÓN AQUÍ ---
    success_url = reverse_lazy('blog:post_list') # Añadido 'blog:'

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.autor