from django.db import models

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

    # class Meta:
    #     verbose_name = _("Movie")
    #     verbose_name_plural = _("Movies")

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
    

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Theatre_detail", kwargs={"pk": self.pk})

