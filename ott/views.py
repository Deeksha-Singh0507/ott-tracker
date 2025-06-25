from rest_framework import generics
from django.shortcuts import render, redirect
from .models import OTTShow, Watchlist
from .serializers import OTTShowSerializer, WatchlistSerializer
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

# 🔹 API View: List + Create Shows
class OTTShowListCreate(generics.ListCreateAPIView):
    queryset = OTTShow.objects.all()
    serializer_class = OTTShowSerializer

# 🔹 API View: List + Create Watchlist
class WatchlistListCreate(generics.ListCreateAPIView):
    queryset = Watchlist.objects.all()
    serializer_class = WatchlistSerializer

# 🎬 HTML Page View: Show List with Search
def show_list_view(request):
    search_query = request.GET.get('q', '')
    if search_query:
        shows = OTTShow.objects.filter(title__icontains=search_query)
    else:
        shows = OTTShow.objects.all()
    return render(request, 'ott/show_list.html', {'shows': shows})

# 📺 HTML Page View: Watchlist Page (Add, Delete, Toggle)
@login_required
def watchlist_view(request):
    search_query = request.GET.get('q', '')

    if request.method == 'POST':
        # ➕ Add to Watchlist
        show_id = request.POST.get('show_id')
        if show_id:
            show = OTTShow.objects.get(id=show_id)
            Watchlist.objects.get_or_create(user=request.user, show=show)

        # ❌ Delete from Watchlist
        delete_id = request.POST.get('delete_id')
        if delete_id:
            Watchlist.objects.filter(id=delete_id, user=request.user).delete()

        # 🔁 Toggle Watched
        toggle_watched_id = request.POST.get('toggle_watched_id')
        if toggle_watched_id:
            item = Watchlist.objects.get(id=toggle_watched_id, user=request.user)
            item.watched = not item.watched
            item.save()

        # 🔁 Toggle Watch Later
        toggle_later_id = request.POST.get('toggle_later_id')
        if toggle_later_id:
            item = Watchlist.objects.get(id=toggle_later_id, user=request.user)
            item.watch_later = not item.watch_later
            item.save()

        return redirect('watchlist-html')

    # 🔍 Filter by search + user
    if search_query:
        watchlist_items = Watchlist.objects.filter(user=request.user, show__title__icontains=search_query)
    else:
        watchlist_items = Watchlist.objects.filter(user=request.user)

    all_shows = OTTShow.objects.all()

    return render(request, 'ott/watchlist.html', {
        'watchlist_items': watchlist_items,
        'all_shows': all_shows
    })
def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('watchlist-html')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})
# ✨ Signup View
def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # auto login after signup
            return redirect('show-list')  # ya 'watchlist-html' bhi likh sakti ho
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})