from django.contrib.admin import AdminSite
from financeiro.models import Financeiro

class FinanceiroAdminSite(AdminSite):
    site_header = "Admin do Financeiro"
    site_title = "O portal de admin do Financeiro"
    index_title = "Seja bem vindo ao Admin Financeiro"

financeiro_admin = FinanceiroAdminSite(name='financeiro_admin')

# registrando os modelos neste Admin
financeiro_admin.register(Financeiro)
