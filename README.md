# comic-blog-django
Entrega final - Playground Final project: Blog de cómics con Django
# Comic Blog Project - Playground Final Project

Este proyecto es una aplicación web estilo blog desarrollada en Python con el framework Django. La temática del blog se centra en la venta y discusión de cómics, aunque la estructura base sigue los lineamientos de un proyecto de blog con funcionalidades de administración, perfiles de usuario, registro, páginas (publicaciones de cómics) y formularios.

Este proyecto fue desarrollado como parte de la entrega final para [Nombre del Curso/Playground - Ej: Coderhouse Python/Django Playground].

## Características Principales

*   **Gestión de Publicaciones (Cómics):**
    *   Crear, leer, actualizar y eliminar publicaciones de cómics (CRUD).
    *   Listado de todas las publicaciones con vista previa.
    *   Detalle de cada publicación con imagen, descripción enriquecida (CKEditor), autor, fecha, etc.
    *   Solo los autores autenticados pueden editar o borrar sus propias publicaciones.
*   **Autenticación y Perfiles de Usuario:**
    *   Registro de nuevos usuarios (username, email, password, nombre, apellido).
    *   Inicio y cierre de sesión.
    *   Perfiles de usuario con información personal (nombre, apellido, email, avatar, biografía, link web).
    *   Edición de perfil y cambio de contraseña.
*   **Mensajería Privada:**
    *   Sistema de mensajería interna entre usuarios registrados.
    *   Listado de conversaciones.
    *   Vista de hilo de conversación para leer y enviar mensajes.
*   **Páginas Estándar:**
    *   Página de Inicio (Home).
    *   Página "Acerca de Mí".
*   **Panel de Administración Django:**
    *   Gestión de modelos (Posts, Perfiles, Mensajes) a través del admin de Django.
*   **Diseño Responsivo (Básico):**
    *   Uso de Bootstrap para una interfaz adaptable.

## Tecnologías Utilizadas

*   **Backend:** Python, Django
*   **Base de Datos:** SQLite (por defecto para desarrollo)
*   **Frontend (Básico):** HTML, CSS, Bootstrap
*   **Editor de Texto Enriquecido:** `django-ckeditor`
*   **Manejo de Imágenes:** `Pillow`
*   **Entorno Virtual:** `venv`
*   **Control de Versiones:** Git, GitHub

## Requisitos Previos

*   Python 3.8 o superior
*   pip (gestor de paquetes de Python)
*   Git (para clonar el repositorio)

## Configuración e Instalación Local

Sigue estos pasos para configurar y ejecutar el proyecto en tu entorno local:

1.  **Clonar el Repositorio:**
    ```bash
    git clone https://github.com/TU_USUARIO/TU_REPOSITORIO.git
    cd NOMBRE_DE_LA_CARPETA_DEL_PROYECTO
    ```
    *(Reemplaza `TU_USUARIO`, `TU_REPOSITORIO` y `NOMBRE_DE_LA_CARPETA_DEL_PROYECTO` con tus datos)*

2.  **Crear y Activar un Entorno Virtual:**
    ```bash
    python -m venv venv
    ```
    *   En Windows:
        ```bash
        .\venv\Scripts\activate
        ```
    *   En macOS/Linux:
        ```bash
        source venv/bin/activate
        ```

3.  **Instalar Dependencias:**
    Asegúrate de tener el archivo `requirements.txt` en la raíz del proyecto.
    ```bash
    pip install -r requirements.txt
    ```

4.  **Configurar Archivos Multimedia (Avatares por Defecto):**
    *   Crea una carpeta `media` en la raíz del proyecto.
    *   Dentro de `media`, crea una subcarpeta `avatars`.
    *   Coloca una imagen llamada `default_avatar.png` dentro de `media/avatars/`. Esta imagen se usará como avatar por defecto para los nuevos usuarios.

5.  **Aplicar Migraciones:**
    Esto creará las tablas necesarias en la base de datos (SQLite por defecto).
    ```bash
    python manage.py migrate
    ```

6.  **Crear un Superusuario (Opcional, para acceder al Admin):**
    ```bash
    python manage.py createsuperuser
    ```
    Sigue las instrucciones para crear un nombre de usuario, email y contraseña.

7.  **Ejecutar el Servidor de Desarrollo:**
    ```bash
    python manage.py runserver
    ```
    La aplicación estará disponible en `http://127.0.0.1:8000/`.

## Estructura del Proyecto (Apps Principales)

*   `blog/`: Maneja todo lo relacionado con las publicaciones (posts/cómics).
*   `accounts/`: Gestiona la autenticación, registro y perfiles de usuario.
*   `messaging/`: Implementa el sistema de mensajería entre usuarios.
*   `comic_blog_project/`: Carpeta de configuración principal del proyecto Django (settings, urls globales).

## Funcionalidades Clave y Rutas

*   **Inicio:** `/`
*   **Acerca de Mí:** `/about/`
*   **Publicaciones (Listado):** `/pages/`
*   **Detalle de Publicación:** `/pages/<id_post>/`
*   **Crear Publicación:** `/pages/new/` (Requiere login)
*   **Login:** `/accounts/login/`
*   **Registro:** `/accounts/signup/`
*   **Perfil:** `/accounts/profile/` (Requiere login)
*   **Mensajes:** `/messages/` (Requiere login)
*   **Admin Django:** `/admin/`

## Autor

*   **Giovanni Cubelli**
*   cubelligiovanni@gmail.com
*   (https://github.com/giovannicubelli)
*   (https://www.linkedin.com/in/giovanni-cubelli-b52691266?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app)

## Video Demostrativo

(https://drive.google.com/file/d/1Nwq27MQoTSpGUdLjBU4HtGU3Dn8qTRBR/view)
