from django.contrib.admin import AdminSite
from eventos.models import Evento

class EventosAdminSite(AdminSite):
    site_header = "Admin de Eventos"
    site_title = "O portal de admin de Eventos"
    index_title = "Seja bem vindo ao Admin de Eventos"

eventos_admin = EventosAdminSite(name='eventos_admin')

# registrando os modelos neste Admin
eventos_admin.register(Evento)
