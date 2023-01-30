from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.home, name="home"),
    path('sendmail/', views.send_mails, name="sendmail"),
    path('login/', views.login, name="login"),
    path('signup/', views.signup, name="signup"),
    path('logout/', views.signout, name="logout"),
    path('create/', views.write, name="write"),
    path('profile/<int:pk>/', views.profile, name="profile"),
    path('add_fav/<slug:slug>/', views.add_to_fav, name="favourite"),
    path('get_fav/<str:type>/', views.go_to_type, name="type"),
    path('read_later/<slug:slug>/', views.add_to_readlater, name="readlater"),
    path('add_comment/<slug:slug>/', views.add_comment, name="comment"),
    path('category/<str:cat>/', views.getCategory, name = 'categoryview'),
    path('<slug:slug>/', views.detailView, name="detail"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)