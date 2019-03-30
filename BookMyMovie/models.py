from django.db import models
from django.utils.translation import gettext as _
from django.contrib.auth.models import User

# Create your models here.

class Movie(models.Model):

    name = models.CharField(max_length=50)
    desciption = models.TextField()
    genre = models.CharField( max_length=50)
    director = models.CharField( max_length=50)
    language = models.CharField( max_length=50)
    posterURL = models.URLField( max_length=200)
    releaseDate = models.DateField( auto_now=False, auto_now_add=False)
    creationDate = models.DateTimeField( auto_now_add=True)

    class Meta:
        verbose_name = _("Movie")
        verbose_name_plural = _("Movies")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Movie_detail", kwargs={"pk": self.pk})


class Theatre(models.Model):

    name = models.CharField( max_length=50)
    location = models.CharField( max_length=50)
    rows = models.IntegerField()
    seats = models.IntegerField()
    address = models.CharField( max_length=100)
    
    class Meta:
        verbose_name = _("Theatre")
        verbose_name_plural = _("Theatres")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Theatre_detail", kwargs={"pk": self.pk})


class ShowTime(models.Model):
    
    day = models.CharField( max_length=10)
    time = models.CharField(_("Time"), max_length=10)
    price = models.IntegerField(_("Price"))

    class Meta:
        verbose_name = _("ShowTime")
        verbose_name_plural = _("ShowTimes")

    def __str__(self):
        return self.day+self.time

    def get_absolute_url(self):
        return reverse("ShowTime_detail", kwargs={"pk": self.pk})


class Booking(models.Model):

    movie = models.ForeignKey("BookMyMovie.Movie", verbose_name=_("Movie"), on_delete=models.CASCADE)    
    theatre = models.ForeignKey("BookMyMovie.Theatre", verbose_name=_("Theatre"), on_delete=models.CASCADE)
    show = models.ForeignKey("BookMyMovie.ShowTime", verbose_name=_("Show"), on_delete=models.CASCADE)
    user = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
    seats = models.CharField(_("Seats"), max_length=100)
    price = models.IntegerField(_("Price"))
    createTime = models.DateTimeField(_("Booking timestamp"), auto_now_add=True)


    class Meta:
        verbose_name = _("Booking")
        verbose_name_plural = _("Bookings")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Booking_detail", kwargs={"pk": self.pk})
