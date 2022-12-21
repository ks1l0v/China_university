from django.shortcuts import render, redirect
from . import models


def index(request):
    article = models.Article.objects.order_by('-ar_date')

    return render(request, 'main_page/Main.html', {'article': article})

def news(request, pk):
    new = models.Article.objects.get(id=pk)
    com = models.Comments.objects.filter(com_to=pk)
    return render(request, 'main_page/news.html', {'new': new, 'com': com})

def send_com(request, pk):
    if request.method == 'POST':
        post = models.Article.objects.get(id=pk)
        comment = models.Comments(com_to=pk,
                                  com_text=str(request.POST.get('message')),
                                  com_name=str(request.POST.get('name')))
        post.ar_com += 1
        post.save()
        comment.save()
    return redirect(f'/news/{pk}')

