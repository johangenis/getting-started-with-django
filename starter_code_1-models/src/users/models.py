from django.db import models
import datetime


class User(models.Model):
    first_name = models.CharField("the persons first name", max_length=30)
    last_name = models.CharField("the persons last name", max_length=30)
    cars = models.ManyToManyField("Car", verbose_name="the user's cars")


STATUS_CHOICES = {
    ("R", "Reviewed"),
    ("N", "Not reviewed"),
    ("E", "Error"),
    ("A", "Accepted"),
}


class Website(models.Model):
    name = models.CharField(max_length=50)
    url = models.URLField(unique=True)
    release_date = models.DateField()
    rating = models.IntegerField()
    status = models.CharField(choices=STATUS_CHOICES, max_length=1)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        ordering = ["rating"]
        db_table = "website_custom_table_name"
        verbose_name = "the website"
        verbose_name_plural = "the websites"

    def was_released_last_week(self):
        if self.release_date < datetime.date(2020, 5, 16):
            return "Released before last week"
        else:
            return "Released this week"

    @property
    def get_full_name(self):
        return f"This is my website's full name: {self.name}"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f"/websites/{self.id}"

    def save(self, *args, **kwargs):
        print("we are doing something else here...")
        super().save(*args, **kwargs)


class Car(models.Model):
    name = models.CharField(max_length=40, primary_key=True)


class Ox(models.Model):
    class Meta:
        db_table = "ox"
        verbose_name = "the ox"
        verbose_name_plural = "the oxen"
