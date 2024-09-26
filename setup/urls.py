
from django.contrib import admin
from django.urls import path

from django.contrib import admin
from django.urls import path, include
from receitas.views import ReceitasViewSet, ReceitasRetriveView
from rest_framework import routers 

router = routers.DefaultRouter()
router.register('receitas', ReceitasViewSet, basename='receitas')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('Tarefa/<int:pk>/', ReceitasRetriveView.as_view(), name="receitas-retrive"),
]
