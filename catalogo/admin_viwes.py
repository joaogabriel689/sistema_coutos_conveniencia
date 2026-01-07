from django.contrib.admin.views.decorators import staff_member_required
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from django.core.management import call_command

@staff_member_required
def sync_produtos_admin(request):
    try:
        call_command("importar_produtos")
        messages.success(request, "✅ Catálogo sincronizado com sucesso!")
    except Exception as e:
        messages.error(request, f"❌ Erro na sincronização: {e}")

    return HttpResponseRedirect(reverse("admin:index")) 