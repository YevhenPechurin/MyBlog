from django.shortcuts import render, render_to_response
from django.http.response import HttpResponse
from django.template.loader import get_template

# Create your views here.
from article.models import Article, Comments


def basic_one(request):
    view = "basic_one"
    html = "<html><body>This is sparta!!! %s </body></html>" % view
    return HttpResponse(html)


def template_two(request):
    view = "template_two"
    html = get_template('myview.html').render({'name': view})
    return HttpResponse(html)


def template_three(request):
    view = 'template three'
    return render(request, 'myview.html', {'name': view})


def articles(request):
    return render(request, 'articles.html', {'articles': Article.objects.all()})


def article(request, article_id=1):
    return render_to_response('article.html', {'article': Article.objects.get(id=article_id),
                                               'comments': Comments.objects.filter(
                                                   comments_article_id=article_id)})
