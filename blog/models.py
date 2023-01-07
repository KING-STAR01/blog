from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

from ckeditor.fields import RichTextField

class Article(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True, editable=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)
    content = RichTextField()
    image = models.ImageField(null=True, blank=True,upload_to='images/')
    category = models.CharField(max_length=200)
    
    class Meta:
        ordering = ['-created_on']
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('post_detail', kwargs={"slug":self.slug})




class UserProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(null=True, blank=True,upload_to='images/')
    favourite = models.ManyToManyField(Article, related_name="favourite", null=True, blank=True)
    read_later = models.ManyToManyField(Article, related_name='read_later', null=True, blank=True)

<<<<<<< HEAD



=======
>>>>>>> 830b7db (blog website)
class Comments(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
<<<<<<< HEAD

    class Meta:
        ordering = ['created_on']
=======
    active = models.BooleanField(default = True)

    class Meta:
        ordering = ['created_on']
    
>>>>>>> 830b7db (blog website)
