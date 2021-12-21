from django.http import HttpResponse, QueryDict
from .models import Account, Trasaction
from django.views.decorators.http import require_POST, require_GET
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
from django.shortcuts import render
from .forms import AccountForm
import json


@require_GET
def get_all_accounts(request):
    content = serializers.serialize('json', Account.objects.all())
    return HttpResponse(content, content_type='application/json')


@csrf_exempt
@require_POST
def get_account(request):
    card =  json.loads(request.body)
    res = card['card']
    return HttpResponse(res)







    # account = Account.objects.get(card_number=request.POST.get(card))
    # tras = Trasaction.objects.filter(account=account).values('type', 'date')
    # content = serializers.serialize('json',[account,])
    # return HttpResponse(content, content_type='application/json')



@csrf_exempt
@require_POST
def add_tras(request):
    Trasaction.objects.create(type=request.POST.get('type'),
                              sum=request.POST.get('sum'),
                              date=request.POST.get('date'),
                              account=Account.objects.get(id=request.POST.get('id')))
    return HttpResponse(content='Добавлена транзакция', status='200')


def add_account(request):
    if request.method == 'POST':
        form = AccountForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse(content='Добавлен аккаунт', status='200')
        else:
            return render(request, 'form.html', {'form': form})
    else:
        form = AccountForm()
    return render(request, 'form.html', {'form': form})
