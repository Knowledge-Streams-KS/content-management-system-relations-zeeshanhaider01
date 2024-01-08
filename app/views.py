from django.shortcuts import render
from django.http import HttpResponse
from .forms import CreateCategoryForm, CreateUserForm, CreateArticleForm
from .models import Category, User, Article
from django.utils import timezone

def createcategory(request):

    if request.method=="POST":
        form=CreateCategoryForm(request.POST)

        if form.is_valid():
            name=form.cleaned_data["name"]
            Category.objects.create(name=name)
            return HttpResponse("Category successfully created.")
        
    else:
        form=CreateCategoryForm()
        return render(request,"app/catform.html",{"form":form})
    


def createuser(request):

    if request.method=="POST":
        form=CreateUserForm(request.POST)

        if form.is_valid():
            name=form.cleaned_data["username"]
            email=form.cleaned_data["email"]
            password=form.cleaned_data["password"]
            User.objects.create(username=name,email=email,password=password)
            return HttpResponse("User successfully created.")
        
    else:
        form=CreateUserForm()
        return render(request,"app/createuser.html",{"form":form})
    


def createarticle(request):

    if request.method=="POST": 
        form=CreateArticleForm(request.POST)
        title=form.data["title"]
        Content=form.data["Content"]
        Categories=form.data.getlist('Category')

        categorylist=[]
        for id in Categories:
            cat=Category.objects.get(id=int(id))
            categorylist.append(cat)

        author_id=int(form.data["author"][0])
        author=User.objects.get(id=author_id)
        
        article=Article.objects.create(title=title,Content=Content,publicationdate=timezone.now(),authors=author)
        article.save()

        print("categorylist: ",categorylist)
        for item in categorylist:
            article.Categories.add(item)
            print("###################################article: ",article)
            article.save()
        return HttpResponse("Article successfully created.")
        
    else:
        form=CreateArticleForm()
        return render(request,"app/artform.html",{"form":form})
    

def listofcategories(request):
    categories=Category.objects.all()
    return render(request,"app/categories.html",{"categories":categories})


def listof_articles_against_a_category(request,cat_id):
    # print("testtesttesttesttesttesttesttesttesttesttesttest")
    # print("#######################cat_id",cat_id,"type: ",type(cat_id))
    category=Category.objects.get(id=int(cat_id))
    # print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@category: ",category)
    # articles=Article.objects.filter(Categories__in=[category])
    articles=Article.objects.filter(Categories__in=[category])
    print("articles: ",articles)
    return render(request,"app/artlist.html",{"articles":articles})


def article_detail(request,id):
    article=Article.objects.get(id=int(id))
    return render(request,"app/article_details.html",{"article":article})



