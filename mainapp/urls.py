from django.urls import path
from .views import *


urlpatterns = [
    path('', HomePage.as_view(), name='index'),
    path('about/', AboutView.as_view(), name='about'),
    path('blog/', PostView.as_view(), name='blog'),
    # path('portfolio/', portfolio, name='portfolio'),
    path('<int:pk>/post-single/', PostDetailView.as_view(), name='sngl'),
]