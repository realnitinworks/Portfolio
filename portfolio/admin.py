from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DefaultUserAdmin

from . import models


@admin.register(models.CustomUser)
class UserAdmin(DefaultUserAdmin):
    pass


@admin.register(models.Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("title", "slug", "active", "image")
    readonly_fields = ("created", "updated")
    prepopulated_fields = {"slug": ("title",)}


@admin.register(models.Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ("name", "slug")
    prepopulated_fields = {"slug": ("name",)}


@admin.register(models.CertificateGroup)
class CertficateGroupAdmin(admin.ModelAdmin):
    list_display = ("name", "slug", "image")


@admin.register(models.Certificate)
class CertificateAdmin(admin.ModelAdmin):
    list_display = ("name", "group", "url", "completed")


@admin.register(models.OpenSourceProject)
class OpenSourceProjectAdmin(admin.ModelAdmin):
    list_display = ("project_name", "slug", "image")


@admin.register(models.OpenSourceContribution)
class OpenSourceContributionAdmin(admin.ModelAdmin):
    list_display = ("name", "project", "url", "contributed_on")


@admin.register(models.CodingProfile)
class CodingProfileAdmin(admin.ModelAdmin):
    list_display = ("name", "slug", "image", "url")
