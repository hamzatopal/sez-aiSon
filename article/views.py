from django.shortcuts import render,redirect,get_object_or_404,reverse
from django.http import HttpResponse
from .forms import ArticleForm
from .models import Article,Comment
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.contrib.auth.models import User
from django.views.generic import ListView
# Create your views here.


# Create your views here.
def articles(request):
    keyword=request.GET.get('keyword')
    if keyword:
        articles=Article.objects.filter(title__contains=keyword)
        return render(request,"articles.html",{"articles":articles})
    
    


    articles = Article.objects.all()
    paginator = Paginator(articles, 3) # Show 25 contacts per page.

    page = request.GET.get('page')
    articles = paginator.get_page(page)
    return render(request, 'articles.html', {'articles': articles})


    
    
    class Meta:
        ordering=['- created_date']

def about(request):
    return render(request,"about.html")

@login_required(login_url="user:login")
def dashboard(request):
    articles=Article.objects.filter(author=request.user)
    context={
        'articles':articles
    }
    return render(request,"dashboard.html",context) 
@login_required(login_url="user:login")      
def addArticle(request):
    form=ArticleForm(request.POST or None,request.FILES or None)
    if form.is_valid():
        article=form.save(commit=False)
        article.author=request.user
        article.save()
        messages.success(request,'Makale Basariyla Kaydedildi')
        return redirect('article:dashboard')
    return render(request,"addarticle.html",{'form':form})     

def detail(request,id):
    #article=Article.objects.filter(id=id).first()
    article=get_object_or_404(Article,id=id)
    comments=article.comments.all()
    return render(request,'detail.html',{'article':article,'comments':comments})

@login_required(login_url="user:login")
def updateArticle(request,id):
    article=get_object_or_404(Article,id=id)
    form=ArticleForm(request.POST or None,request.FILES or None,instance=article)
    if form.is_valid():
        article=form.save(commit=False)
        article.author=request.user
        article.save()
        messages.success(request,'Makale Basariyla Güncellendi')
        return redirect('article:dashboard')
    return render(request,"update.html",{"form":form})

@login_required(login_url="user:login")
def deleteArticle(request,id):
    article=get_object_or_404(Article,id=id)
    article.delete()
    messages.success(request,'Makale Basariyla Silindi')
    return redirect('article:dashboard')
@login_required(login_url="user:login")   
def addComment(requset,id):
    article=get_object_or_404(Article,id=id)
    if requset.method=='POST':
       
        #comment_author=requset.POST.get('comment_author')
        comment_author=requset.user
        comment_content=requset.POST.get('comment_content')

        newComment=Comment(comment_author=comment_author,comment_content=comment_content)
        newComment.article=article
        newComment.save()
    return redirect(reverse('article:detail',kwargs={'id':id}))    
    #return redirect('/articles/article/'+str(id))    
    class Meta:
        ordering=['- comment_date']

    

