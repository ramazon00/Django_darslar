from django.contrib import admin
from django.urls import path

from store.views import frontpage, single, category_detail

urlpatterns = [
    path('admin/', admin.site.urls),
# store
    path('', frontpage, name='frontpage'),
    path('<slug:category_slug>/<slug:slug>/', single, name='single'),
    path('<slug:slug>/', category_detail, name='category_detail'),
]