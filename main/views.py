from django.shortcuts import render, redirect, get_object_or_404
from main.forms import NewsForm
from main.models import News
from django.http import HttpResponse
from django.core import serializers

def show_main(request):
    news_list = News.objects.all()

    context = {
        'npm' : '2406414025',
        'name': 'Jonathan Hans Emanuelle',
        'class': 'PBP B',
        'news_list': news_list
    }

    return render(request, "main.html", context)

def create_news(request):
    # Logika yang diperbaiki untuk menangani GET dan POST
    if request.method == 'POST':
        # Saat request adalah POST, proses data form dan file
        form = NewsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('main:show_main')
    else:
        # Saat request adalah GET, buat form kosong
        form = NewsForm()

    context = {'form': form}
    return render(request, "create_news.html", context)


def show_news(request, id):
    news = get_object_or_404(News, pk=id)
    news.increment_views()

    context = {
        'news': news
    }

    return render(request, "news_detail.html", context)

def show_xml(request):
    news_list = News.objects.all()
    
def show_xml(request):
    news_list = News.objects.all()
    xml_data = serializers.serialize("xml", news_list)
    return HttpResponse(xml_data, content_type="application/xml")

def show_json(request):
    news_list = News.objects.all()

def show_json(request):
    news_list = News.objects.all()
    json_data = serializers.serialize("json", news_list)
    return HttpResponse(json_data, content_type="application/json")

def show_xml_by_id(request, news_id):
    try:
        news_item = News.objects.filter(pk=news_id)
        xml_data = serializers.serialize("xml", news_item)
        return HttpResponse(xml_data, content_type="application/xml")
    except News.DoesNotExist:
        return HttpResponse(status=404)

def show_json_by_id(request, news_id):
    try:
        news_item = News.objects.get(pk=news_id)
        json_data = serializers.serialize("json", [news_item])
        return HttpResponse(json_data, content_type="application/json")
    except News.DoesNotExist:
        return HttpResponse(status=404)