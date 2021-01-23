from django.urls import path

from api.views import get_token_view, AddFriendView, RemoveFriendView

app_name = 'api'

urlpatterns = [
    path('get-token/', get_token_view, name='get_token'),
    path('friend/<int:pk>/add/', AddFriendView.as_view(), name='add_friend'),
    path('friend/<int:pk>/remove/', RemoveFriendView.as_view(), name='remove_friend'),
]

