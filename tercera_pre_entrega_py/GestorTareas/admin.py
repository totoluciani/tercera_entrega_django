from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Task) #Se registran los modelos para poder observarlos desde el admin de Django
admin.site.register(User)
admin.site.register(TaskDescription)