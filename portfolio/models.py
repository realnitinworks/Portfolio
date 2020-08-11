import sys
from io import BytesIO

from django.contrib.auth.models import AbstractUser
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.utils.text import slugify
from PIL import Image


class CustomUser(AbstractUser):
    pass


def image_path(instance, filename):
    portfolio_category = f"{instance.__class__.__name__.lower()}s"
    return f"{portfolio_category}/{instance.slug}/{filename}"


def compress_image(image):
    tmp_image = Image.open(image)
    output_io_stream = BytesIO()
    tmp_image.save(output_io_stream, format="JPEG", quality=30)
    output_io_stream.seek(0)
    name = image.name.split(".")[0]
    image = InMemoryUploadedFile(
        output_io_stream,
        "ImageField",
        f"{name}.jpg",
        "image/jpeg",
        sys.getsizeof(output_io_stream),
        None,
    )
    return image


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

    def save(self, *args, **kwargs):
        self.image = compress_image(self.image)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.title}"

    def get_absolute_url(self):
        return reverse("portfolio:project_detail", args=[self.id, self.slug])


class CertificateGroup(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, blank=True)
    description = models.CharField(max_length=500)
    image = models.ImageField(upload_to=image_path)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        self.image = compress_image(self.image)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name}"

    def get_absolute_url(self):
        return reverse("portfolio:certificate_group_detail", args=[self.id, self.slug])


class Certificate(models.Model):
    name = models.CharField(max_length=250)
    url = models.URLField(blank=True)
    group = models.ForeignKey(
        CertificateGroup,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="certificates",
    )
    completed = models.DateField(default=timezone.now)

    class Meta:
        ordering = ("-completed", "name")

    def __str__(self):
        return f"{self.name}"


class OpenSourceProject(models.Model):
    project_name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, blank=True)
    description = models.CharField(max_length=500)
    image = models.ImageField(upload_to=image_path)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.project_name)
        self.image = compress_image(self.image)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.project_name}"

    def get_absolute_url(self):
        return reverse("portfolio:opensource_project_detail", args=[self.id, self.slug])


class OpenSourceContribution(models.Model):
    name = models.CharField(max_length=250)
    url = models.URLField(blank=True)
    project = models.ForeignKey(
        OpenSourceProject, on_delete=models.CASCADE, related_name="contributions"
    )
    contributed_on = models.DateField()

    class Meta:
        ordering = ("-contributed_on", "name")

    def __str__(self):
        return f"{self.name}"


class CodingProfile(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, blank=True)
    url = models.URLField()
    image = models.ImageField(upload_to=image_path)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        self.image = compress_image(self.image)
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return f"{self.name}"
