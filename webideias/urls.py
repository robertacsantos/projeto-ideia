from django.urls import path, include
from webideias.views import index, sobre, login, cadastrar_ideia, home, remover_ideia
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', home),
    path('index', index),
    path('sobre', sobre),
    path('login', login),
    path('ideias', cadastrar_ideia),
    path('remover_ideia/<int:id>/', remover_ideia),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
