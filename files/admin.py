from django.contrib import admin
from .models import File
from django.utils.html import format_html
from hashids import Hashids
import os

secret_key = os.getenv('SECRET_KEY', 'secret salt')
hashids = Hashids(min_length=4, salt=secret_key)

class FileAdmin(admin.ModelAdmin):
    list_display = ('id', 'get_url', 'expiration_date')

    @admin.display(empty_value='???')
    def get_filename(self, obj : File):
        return os.path.basename(obj.file.name)

    @admin.display(empty_value='blank')
    def get_url(self, obj : File):
        return format_html(
            f'<a href=http://127.0.0.1:8000/get/{self.get_hash(obj)}>{obj.file.name}</a>'
        )

    def get_hash(self, obj: File):
        hashid = hashids.encode(obj.id)
        return hashid



admin.site.register(File, FileAdmin)
