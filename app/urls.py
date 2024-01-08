from django.urls import path
from app import views

app_name="app"

urlpatterns=[
    path("createcategory/",views.createcategory),
    path("createcategory/form/",views.createcategory),
    path("createuser/",views.createuser),
    path("createuser/form/",views.createuser),
    path("createarticle/",views.createarticle),
    path("createarticle/form/",views.createarticle),
    path("homepage/",views.listofcategories),
    path("articles_for_category/<int:cat_id>/",views.listof_articles_against_a_category, name="articles"),
    path("article_details/<int:id>/",views.article_detail, name="article_detail")
]