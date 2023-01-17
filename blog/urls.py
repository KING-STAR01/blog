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
    path('<slug:slug>/', views.detailView, name="detail"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)