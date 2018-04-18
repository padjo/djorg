from django.db import models

# Create your models here.
from uuid import uuid4
from django.contrib.auth.models import U ser
from django.db import models

class Note(models.Model):
    id = models.UUIDField(primary_key, default=uuid4, eidtable=False)
    title = models.CharField(max_length=200)
    content = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    @property
    def content_length(self):
        return len(content ) 