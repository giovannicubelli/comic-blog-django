from django.urls import path
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
)

app_name = 'blog' # Para el namespace

urlpatterns = [
    path('', PostListView.as_view(), name='post_list'), # /pages/ -> Listado
    path('<int:pk>/', PostDetailView.as_view(), name='post_detail'), # /pages/ID/ -> Detalle
    path('new/', PostCreateView.as_view(), name='post_create'), # /pages/new/ -> Crear
    path('<int:pk>/edit/', PostUpdateView.as_view(), name='post_update'), # /pages/ID/edit/ -> Editar
    path('<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'), # /pages/ID/delete/ -> Borrar
]