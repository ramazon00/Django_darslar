from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse
from ckeditor.fields import RichTextField

class Music(models.Model):
    caption = models.CharField(max_length=150)
    file = models.FileField(upload_to='music/%y')

    def __str__(self):
        return self.caption

class Video(models.Model):
    caption = models.CharField(max_length=150)
    file = models.FileField(upload_to='video/%y')

    def __str__(self):
        return self.caption





class Article(models.Model):
    class NewManager(models.Manager):
        def get_queryset(self):
            return super().get_queryset() .filter(status='published')


    title = models.CharField(max_length=200)
    summary = models.CharField(max_length=200, blank=True)
    body = RichTextField()
    photo = models.ImageField(upload_to='images/', blank=True)
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('article_detail', args = [self.id])    

class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name = 'comments')
    comment = models.CharField(max_length=150)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.comment

    def get_absolute_url(self):
        return reverse('article_list')        