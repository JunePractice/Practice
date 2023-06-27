from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect

from .models import NotificationModel
from .item import Item
from django.http import HttpResponse


@csrf_protect
def notification(request):
    allData = []
    if request.method == "POST":
        posts = NotificationModel.objects.all()
        # for i in range(len(posts)):
        #     print(posts[i].text)
        #     # item = Item
        #     # text = item.text
        #     # result = f'<div>Новое уведомление: {posts[i].text}</div>'
        #     allData.append(posts[i].text)

        return render(request, 'notification.html', {'textData': posts})
    return render(request, 'notification.html')
