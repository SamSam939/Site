from django.shortcuts import render, get_object_or_404, redirect
from news.models import News, Comments
from news.forms import CommentForm
import xml.etree.ElementTree as ET
from django.http import HttpResponseRedirect

def news_list(request):
    news = News.objects.all()
    return render (request, "news/news_list.html", {"news": news})

def new_single(request, pk):
    new = get_object_or_404(News, id=pk)
    comment = Comments.objects.filter(new=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            form.new = new
            form.save()
            return redirect(new_single, pk)
    else:
        form = CommentForm()
    return render(request, "news/new_single.html",
                {"new": new,
                "comments": comment,
                "form": form})

def export(reguest):
    news = News.objects.all()
    data = ET.Element('data')
    for new in news:
        element = ET.SubElement(data,'new_single')
        element.set('title', new.title)
    ET.ElementTree(data).write("news.xml", encoding="UTF-8")
    return HttpResponseRedirect('/')