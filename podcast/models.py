from django.db import models
from django.utils import timezone
# Create your models here.


LIST_CATEGORY = (
    ("TERROR","Terror"),
    ("COMEDIA","Comédia"),
    ("SUSPENSE","Suspense"),
    ("HUMOR", "Humor"),
    ("ACAO", "Ação"),
    ("AVENTURA", "Aventura"),
    ("DRAMA", "Drama"),
    ("INFANTIL", "Infantil"),
)

# Create podcast
class Podcast(models.Model):
        title = models.CharField(max_length=100)
        thumb = models.ImageField(upload_to='thumbPodcast')
        description  = models.TextField(max_length=100)
        category = models.CharField(max_length=100, choices=LIST_CATEGORY)
        views = models.IntegerField(default=0)
        date_creation = models.DateTimeField(default=timezone.now)

        def __str__(self):
            return self.title



# Create episodes
