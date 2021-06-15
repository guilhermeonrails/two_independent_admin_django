from django.contrib import admin
from django.urls import path
from eventos.admin import eventos_admin
from financeiro.admin import financeiro_admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('eventos-admin/', eventos_admin.urls),
    path('financeiro-admin/', financeiro_admin.urls),
]