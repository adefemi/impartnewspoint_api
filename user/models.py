from django.db import models

# Create your models here.


class GenericFileUpload(models.Model):
    file = models.FileField(upload_to="generics")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.file}"


class Marketting(models.Model):
    caption = models.CharField(max_length=250, null=True, blank=True)
    link = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.caption}"


class MarkettingBanners(models.Model):
    marketting = models.ForeignKey(
        Marketting, related_name="banners", on_delete=models.CASCADE)
    banner = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.caption}"
