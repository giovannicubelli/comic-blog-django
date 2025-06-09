"""
URL configuration for comic_blog_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from blog.views import home_view, about_view # Importar vistas de home y about

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home'), # Ruta para la Home
    path('about/', about_view, name='about'), # Ruta para "Acerca de mí"
    path('blog/', include('blog.urls')), # Incluye las URLs de la app blog bajo /blog/ (o /pages/ si prefieres)
    path('pages/', include(('blog.urls', 'blog'), namespace='blog')), # El namespace es opcional pero buena práctica
    # Esto hará que las URLs sean /pages/, /pages/1/, /pages/new/ etc.
    # Y en los templates usamos {% url 'blog:post_list' %}, {% url 'blog:post_detail' post.pk %}

    # CKEditor URLs
    path('ckeditor/', include('ckeditor_uploader.urls')), # Necesario para subida de imágenes en CKEditor
    path('accounts/', include('accounts.urls')), # Incluye las URLs de la app accounts
    path('ckeditor/', include('ckeditor_uploader.urls')), # Necesario para subida de imágenes en CKEditor
    path('messages/', include('messaging.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) # Opcional si usas collectstatic