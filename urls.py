from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("<int:gid>/follow", views.follow, name="follow"),
    path("<int:gid>/f_wers", views.f_wers, name="f_wers"),
    path("<int:gid>/f_wings", views.f_wings, name="f_wings"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("search", views.search, name="search"),
    path("editacc", views.editacc, name="editacc"),
    path("Account", views.Account, name="Account"),
    path("myaccount", views.myaccount, name="myaccount"),
    path("<int:fid>", views.gprofile, name="gprofile"),
]
if settings.DEBUG:urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)