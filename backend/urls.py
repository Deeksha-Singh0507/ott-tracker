from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from ott import views as ott_views

urlpatterns = [
    path('admin/', admin.site.urls),

    # 🔸 Auth URLs
    path('accounts/login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('accounts/signup/', ott_views.signup_view, name='signup'),

    # 🔸 Main Views
    path('', ott_views.show_list_view, name='home'),  # Home = Show List
    path('view/', ott_views.show_list_view, name='show-list'),
    path('watchlist-view/', ott_views.watchlist_view, name='watchlist-html'),
]
