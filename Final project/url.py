from django.contrib import admin  # Add this import statement
from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', views.myproject, name='myproject'),
    path('cart/', views.cart, name='cart'),
    path('remove_cart_item/<cart_item_uid>/', views.remove_cart_item, name='remove_cart'),
    path('add_cart/<movie_uid>/', views.add_cart, name="add-cart"),
    path('login/', views.login_page, name="login"),
    path('register/', views.register_page, name="register"),
    path("admin/", admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()
