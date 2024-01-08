from django.db import models

class Category(models.Model):
    name=models.CharField(max_length=100, unique=True)

    def __str__(self):
        return f"name: {self.name}"


class User(models.Model):
    username=models.CharField(max_length=100)
    email=models.EmailField(unique=True)
    password=models.CharField(max_length=50)

    def __str__(self):
        return f"username: {self.username},email: {self.email}, password: {self.password}"


class Article(models.Model):
    title=models.CharField(max_length=100)
    Content=models.CharField(max_length=500)
    publicationdate=models.DateTimeField(auto_now_add=True)
    Categories=models.ManyToManyField(Category)
    authors=models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return f"title: {self.title}, content: {self.Content}, publicationdate: {self.publicationdate}, Categories: {list(self.Categories.all())}, author: {self.authors}"