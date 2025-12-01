from django.contrib import admin

from .models import People
from .models import Starships

admin.site.register(People)
admin.site.register(Starships)
