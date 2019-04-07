from django.contrib import admin
from .models import Movie, Theatre,ShowDay, ShowTime, Booking

# Register your models here.

admin.site.register(Movie)
admin.site.register(Theatre)
# admin.site.register(ShowDay)
admin.site.register(ShowTime)
admin.site.register(Booking)

