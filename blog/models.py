from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

from ckeditor.fields import RichTextField



CATEGORY_CHOICES = [
    ('DSA', 'DSA'),
    ('CN', 'CN'),
    ('OS', 'OS'),
    ('DBMS', 'DBMS'),
    ('LINUX', 'LINUX'),
    ('OTHERS', 'OTHERS'),
]

class Article(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True, editable=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)
    content = RichTextField()
    image = models.ImageField(null=True, blank=True,upload_to='images/')
    category = models.CharField(max_length=200, choices=CATEGORY_CHOICES)
    #change default to false
    active = models.BooleanField(default=True)
    
    class Meta:
        ordering = ['-created_on']
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('post_detail', kwargs={"slug":self.slug})




class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    image = models.ImageField(null=True, blank=True,upload_to='images/')
    favourite = models.ManyToManyField(Article, related_name="favourite", null=True, blank=True)
    read_later = models.ManyToManyField(Article, related_name='read_later', null=True, blank=True)

    def __str__(self):
        return str(self.user)




class Comments(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name="comments")
    title = models.CharField(max_length=200, blank=True, null=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    #change default to false in production
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ['created_on']