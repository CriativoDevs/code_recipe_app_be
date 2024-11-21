from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static # para que o django importe os ficheiros estáticos
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/", include("cooking.urls")),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT) # aqui o Django vai saber onde buscar nossos static files
