import os
import sys
import django
import random
from datetime import date

# ✅ Step 1: Project root directory (jahan manage.py hai) ko Python path me daalo
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, BASE_DIR)

# ✅ Step 2: Correct settings module set karo
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backend.settings")

# ✅ Step 3: Django initialize karo
django.setup()

# ✅ Step 4: Ab models import karo
from ott.models import OTTShow

# ✅ Step 5: Dummy data create karo
titles = ["Sacred Games", "Mirzapur", "Panchayat", "Family Man", "Asur", "Scam 1992"]
genres = ["Drama", "Thriller", "Comedy", "Action"]
platforms = ["Netflix", "Prime Video", "Disney+ Hotstar"]
descriptions = [
    "A thrilling Indian crime drama.",
    "A gritty tale of power and politics.",
    "A light-hearted village comedy.",
    "A spy thriller filled with twists.",
    "A mythological techno-crime story.",
    "Based on Harshad Mehta scam."
]

# ✅ Step 6: Data ko loop se DB me add karo
for i in range(len(titles)):
    OTTShow.objects.create(
        title=titles[i],
        description=descriptions[i],
        genre=random.choice(genres),
        rating=round(random.uniform(3.5, 5.0), 1),
        platform=random.choice(platforms),
        release_date=date(2020+i, random.randint(1, 12), random.randint(1, 28))
    )

print("✅ Fake shows added to DB.")
