from django.shortcuts import render, HttpResponse, redirect
from firstapp.models import People, Aritcle, Comment
from django.template import Context, Template
from firstapp.form import CommentForm

def index (request):
    # print(request)
    # print('='*50)
    # print(dir(request))
    # print('='*50)
    # print(type(request))
    get_requeset = request.GET.get('tag')
    if get_requeset:
        article_list = Aritcle.objects.filter(tag=get_requeset)
    else:
        article_list = Aritcle.objects.all()
    print(get_requeset)
    context = {}
    context['article_list'] = article_list
    return render(request, 'first_web_2.html', context)


# def detail(request, page_num):
#     if request.method == "GET":
#         form = CommentForm
#     if request.method == 'POST':
#         form = CommentForm(request.POST)
#         if form.is_valid():
#             name = form.cleaned_data['name']
#             comment = form.cleaned_data['comment']
#             a = Aritcle.objects.get(id = page_num)
#             c = Comment(name = name, comment = comment, belong_to = a)
#             c.save()
#             return redirect(to = 'detail',page_num=page_num)
#     context = {}
#     # comment_list = Comment.objects.all()
#     article = Aritcle.objects.get(id = page_num)
#     best_comment = Comment.objects.filter(best_comment = True, belong_to = article)
#     if best_comment:
#         context['best_comment'] = best_comment[0]
#     context['article'] = article
#     # context['comment_list'] = comment_list
#     context['form'] = form
#     return render(request, 'article-detail.html', context)


def detail(request, page_num, error_form=None):
    form = CommentForm
    context = {}
    article = Aritcle.objects.get(id = page_num)
    best_comment = Comment.objects.filter(best_comment = True, belong_to = article)
    if best_comment:
        context['best_comment'] = best_comment[0]
    context['article'] = article
    if error_form is not None:
        context['form'] = error_form
    else:
        context['form'] = form
    return render(request, 'article-detail.html', context)

def detail_comment(request,page_num):
    form = CommentForm(request.POST)
    if form.is_valid():
        name = form.cleaned_data['name']
        comment = form.cleaned_data['comment']
        a = Aritcle.objects.get(id = page_num)
        c = Comment(name = name, comment = comment, belong_to = a)
        c.save()
    else:
        return detail(request,page_num=page_num, error_form=form)

    return redirect(to = 'detail',page_num=page_num)
