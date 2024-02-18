from django.urls import path
from .views import BoardList, BoardDetail, BoardCreate, BoardUpdate, BoardDelete, BoardListUser
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
   path('', BoardList.as_view(), name='post_list'),
   path('<int:pk>/', BoardDetail.as_view(), name='post_detail'),
   path('create/', BoardCreate.as_view(), name='post_create'),
   path('<int:pk>/update/', BoardUpdate.as_view(), name='post_update'),
   path('<int:pk>/delete/', BoardDelete.as_view(), name='post_delete'),
   path('myboard/', BoardListUser.as_view(), name='post_list_user')
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
