from django.db import models
from django.utils import timezone

class Post(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    partnr = models.PositiveSmallIntegerField()
    text = models.TextField()
    updated = models.DateTimeField(blank = True, null = True)

    def publish(self):
        self.updated = timezone.now()
        self.safe()

    def __str__(self):
        return self.title + ' ' + str(self.partnr)
