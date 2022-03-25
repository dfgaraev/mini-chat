import json

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.template.defaultfilters import date
from django.views.decorators.http import require_POST

from chat.models import Msg


@csrf_exempt
def msg(request):
    all_msg = Msg.objects.all()
    msg_list = []
    for item in all_msg:
        msg_list.append({'sender': item.sender,
                         'text': item.text,
                         'date': str(date(item.date, 'j.m.y G:i:s')), })
    return JsonResponse({'data': msg_list})


@csrf_exempt
@require_POST
def add_msg(request):
    error = ''
    try:
        body = request.body.decode()
    except:
        body = None
    if body:
        try:
            body_dict = json.loads(body)
        except:
            body_dict = {}
        sender = body_dict.get('sender', '').strip()
        text = body_dict.get('text', '').strip()
        if sender and text:
            new_msg = Msg()
            new_msg.sender = sender
            new_msg.text = text
            new_msg.save()
        else:
            error = 'Не указан отправитель или текст'
    else:
        error = 'Тело запроса пустое'

    return JsonResponse({'ok': True if error == '' else False, 'error': error})
