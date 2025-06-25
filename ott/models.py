from django.db import models
from django.contrib.auth.models import User

# 🎬 OTT Show model
class OTTShow(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    genre = models.CharField(max_length=100)
    rating = models.FloatField()
    platform = models.CharField(max_length=100)  # Netflix, Prime, etc.
    release_date = models.DateField()

    def __str__(self):
        return self.title

# 📝 Watchlist model
class Watchlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    show = models.ForeignKey(OTTShow, on_delete=models.CASCADE)
    watched = models.BooleanField(default=False)          # 👈 Add this
    watch_later = models.BooleanField(default=False)      # 👈 And this
    added_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.show.title}"
