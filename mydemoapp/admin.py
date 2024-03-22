from django.contrib import admin
from mydemoapp.models import registration
from mydemoapp.models import add_teacherinfo
from mydemoapp.models import files
# Register your models here.
admin.site.register(registration)
admin.site.register(add_teacherinfo)
admin.site.register(files)
