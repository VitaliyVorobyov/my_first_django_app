from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.index, name='index'),
    path('message', views.message, name='message'),
    path('<int:pk>', views.MessageDetailView.as_view(), name='message_view'),
    path('<int:pk>/update', views.MessageUpdateView.as_view(), name='message_update'),
    path('<int:pk>/delete', views.MessageDeleteView.as_view(), name='message_delete'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
