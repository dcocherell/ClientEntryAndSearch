from django.contrib.admin.views.decorators import staff_member_required
from django.http import HttpResponseRedirect
from django.urls import reverse

@staff_member_required
def browse(request):
    return HttpResponseRedirect(reverse('admin:clients_client_changelist'))

@staff_member_required
def search(request):
    return HttpResponseRedirect(reverse('admin:clients_client_changelist'))

@staff_member_required
def create(request):
    return HttpResponseRedirect(reverse('admin:clients_client_add'))
