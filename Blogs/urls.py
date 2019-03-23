from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from posts.views import posts_list,posts_detail,post_create,posts_update,posts_delete,user_create
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('admin/', admin.site.urls),
    path('posts/', posts_list,name="home"),
    path('posts/create', post_create),
    path('login/',auth_views.LoginView.as_view(template_name='posts/login.html'),name="login"),
    path('logout/',auth_views.LogoutView.as_view(template_name='posts/logout.html'),name="logout"),
    path('posts/author',user_create,name="register"),
    path('posts/<slug>/delete',posts_delete,name="delete"),
    path('password_reset/',auth_views.PasswordResetView.as_view(template_name="posts/password_reset.html"),name="reset_password"),
    path('password-reset-confirm/',auth_views.PasswordResetConfirmView.as_view(template_name="posts/password_reset_confirm.html"),name="password_reset_confirm"),
    path('password_reset/done/',auth_views.PasswordResetDoneView.as_view(template_name="posts/password_reset_done.html"),name="password_reset_done"),
    path('posts/<slug>',posts_detail),
    path('posts/<slug>/update',posts_update),
    path('posts/<slug>/delete',posts_delete,name="delete")



] +  static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
