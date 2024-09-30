from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .models import Article
from .forms import ArticleForm
from django.contrib.auth import views as auth_views
from django.utils import timezone


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            return render(request, 'blog/login.html', {'error': 'Invalid credentials'})
    return render(request, 'blog/login.html')



def home(request):
    articles = Article.objects.all().order_by('-publication_date')
    return render(request, 'blog/home.html', {'articles': articles})

def article_detail(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    return render(request, 'blog/article_detail.html', {'article': article})

@login_required
def logout_view(request):
    logout(request)
    return redirect('login')

# Dashboard
@login_required
def dashboard(request):
    articles = Article.objects.all().order_by('-publication_date')
    return render(request, 'blog/dashboard.html', {'articles': articles})


#vista para crear
@login_required
def add_article(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)  
            article.publication_date = timezone.now()  
            article.save()  
            return redirect('dashboard')
    else:
        form = ArticleForm()
    return render(request, 'blog/add_article.html', {'form': form})


#vista para editar
@login_required
def edit_article(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = ArticleForm(instance=article)
    return render(request, 'blog/edit_article.html', {'form': form, 'article': article})


def delete_article_view(request, article_id):
    article = get_object_or_404(Article, id=article_id)

    if request.method == 'POST':
        article.delete()
        return redirect('dashboard')  

    return render(request, 'blog/delete_article.html', {'article': article})

