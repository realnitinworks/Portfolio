from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse


class CustomUser(AbstractUser):
    pass


def image_path(instance, filename):
    return f"projects/{instance.slug}/{filename}"


class Skill(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=50)

    def __str__(self):
        return f"{self.name}"


class Project(models.Model):
    title = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250)
    summary = models.CharField(max_length=600)
    detail = models.TextField()
    skills = models.ManyToManyField(Skill, related_name="projects", blank=True)
    image = models.ImageField(upload_to=image_path)
    active = models.BooleanField(default=True)
    repository = models.URLField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ("-created",)

    def __str__(self):
        return f"{self.title}"

    def get_absolute_url(self):
        return reverse("portfolio:project_detail", args=[self.id, self.slug])
