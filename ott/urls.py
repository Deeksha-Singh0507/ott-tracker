from django.urls import path
from .views import OTTShowListCreate, WatchlistListCreate, show_list_view, watchlist_view, signup_view

urlpatterns = [
    path('shows/', OTTShowListCreate.as_view(), name='show-list'),
    path('watchlist/', WatchlistListCreate.as_view(), name='watchlist-list'),
    path('view/', show_list_view, name='show-list'),              # HTML shows
    path('watchlist-view/', watchlist_view, name='watchlist-html'),  # ✅ comma added here
    path('signup/', signup_view, name='signup')                     # ✅ last item, no comma needed
]
