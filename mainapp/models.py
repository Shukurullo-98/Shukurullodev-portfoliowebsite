from django.db import models

import datetime as dt


class Portfolio(models.Model):
    title = models.CharField(max_length=82)
    image = models.ImageField(upload_to='media/')
    url = models.URLField()

    def __str__(self):
        return self.title


class Blog(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']


class AboutPage(models.Model):
    years = models.IntegerField(default=1998, null=True, blank=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        k = dt.datetime.now().year - self.years
        k = str(k)
        return k
