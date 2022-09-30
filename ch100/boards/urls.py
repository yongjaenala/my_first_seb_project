from django.urls import path, re_path
from boards import views

app_name = 'boards'

urlpatterns=[
    
    # Example:/boards/
    path('',views.BoardLV.as_view(), name='index'),

    # Example:/boards/post/
    path('boards/', views.BoardLV.as_view(), name='boards_list'),

    # Exampe:/boards/detail/django-example/
    re_path(r'^board/(?P<slug>[-\w]+)/$', views.BoardDV.as_view(), name='board_detail'),

    # Example:/boards/add/
    path('add/', views.BoardCreateView.as_view(), name='add'),

    # Example:/boards/change/
    path('change/', views.BoardChangeLV.as_view(), name='change'),
    
    # Example:/boards/99/update/    
    path('<int:pk>/update/', views.BoardUpdateView.as_view(), name='update'),
    
    # Example:/boards/add/99/delete/    
    path('<int:pk>/delete/', views.BoardDeleteView.as_view(), name='delete'),


]