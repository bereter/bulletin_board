from django.urls import path
from .views import BoardList, BoardDetail, BoardCreate, BoardUpdate, BoardDelete, BoardListUser, reply_on, reply_off, \
   CommentDelete, BoardListUserResponse


urlpatterns = [
   path('', BoardList.as_view(), name='post_list'),
   path('<int:pk>/', BoardDetail.as_view(), name='post_detail'),
   path('create/', BoardCreate.as_view(), name='post_create'),
   path('<int:pk>/update/', BoardUpdate.as_view(), name='post_update'),
   path('<int:pk>/delete/', BoardDelete.as_view(), name='post_delete'),
   path('myboard/', BoardListUser.as_view(), name='post_list_user'),
   path('<int:pk>/delete_comment/', CommentDelete.as_view(), name='delete_comment'),
   path('<int:pk>/replyon/', reply_on, name='reply_on'),
   path('<int:pk>/replyoff/', reply_off, name='reply_off'),
   path('myresponse/', BoardListUserResponse.as_view(), name='post_list_user_res'),
]
