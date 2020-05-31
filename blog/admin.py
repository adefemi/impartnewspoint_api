from django.contrib import admin
from .models import (BlogTag, Blog, BlogComment, )

# Register your models here.
admin.site.register(
    (BlogTag, Blog, BlogComment,)
)
