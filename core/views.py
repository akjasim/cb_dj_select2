import json

from django.http import JsonResponse
from django.shortcuts import render
from core.forms import EntryCreationForm
from core.models import Entry, Language


def home(request):
    form = EntryCreationForm()
    if request.is_ajax():
        qs = Language.objects.all().filter(title__icontains=request.GET.get('term'))
        form = EntryCreationForm()
        return JsonResponse(list(qs.values()), safe=False)
    return render(request, 'core/home.html', {'form': form})