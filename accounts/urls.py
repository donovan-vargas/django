# coding=utf-8
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^registro/$', views.register_user_view, name='accounts.registro'),
    url(r'gracias/(?P<username>[\w.%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4})/$', views.thanks_view, name='accounts.gracias'),
    url(r'^$', views.index_view, name='accounts.index'),
    url(r'^login/$', views.login_view, name='accounts.login'),
    url(r'^logout/$', views.logout_view, name='accounts.logout'),
    url(r'^editar_email/$', views.edit_email_view, name='accounts.editar_email'),
    url(r'^editar_foto/$', views.edit_photo_view, name='accounts.editar_foto'),
    url(r'^editar_contrasena/$', views.edit_password_view, name='accounts.editar_contrasena'),
    url(r'^password_reset/$',
        'django.contrib.auth.views.password_reset',
        {'post_reset_redirect': 'accounts.password_reset_done', 'template_name': 'accounts/password_reset_form.html'},
        name='accounts.password_reset'),
    url(r'^password_reset_done/$',
        'django.contrib.auth.views.password_reset_done',
        {'template_name': 'accounts/password_reset_done.html'},
        name='accounts.password_reset_done'),
    url(r'^password_reset_confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$',
        'django.contrib.auth.views.password_reset_confirm',
        {'template_name': 'accounts/password_reset_confirm.html'},
        name='password_reset_confirm'),
    url(r'^password_done/$',
        'django.contrib.auth.views.password_reset_complete',
        {'template_name': 'accounts/password_reset_complete.html'},
        name='password_reset_complete'),
]
