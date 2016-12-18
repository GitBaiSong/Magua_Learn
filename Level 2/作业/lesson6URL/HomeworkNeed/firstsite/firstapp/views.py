from django.shortcuts import render, redirect
from firstapp.models import Article, Comment, UserProfile
from firstapp.forms import CommentForm
from django.contrib.auth.models import User
# Create your views here.

def detail(request,page_num):
    if request.method == 'GET':
        form = CommentForm
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_vaild():
            comment = form.cleaned_data["comment"]
            article = Article.objects.get(id = id)
        c = Comment(comment = comment, belong_article =article)
        c.save()
        return redirect(to= 'detail')

    context = {}



