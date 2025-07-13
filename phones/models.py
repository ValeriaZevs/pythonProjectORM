from django.db import models


class Phone(models.Model):
    # id, name, price, image, release_date, lte_exists и slug
    id = models.CharField(primary_key=True)
    name = models.CharField(max_length=120)
    price = models.IntegerField()
    image = models.URLField()
    release_date = models.DateField()
    lte_exists = models.BooleanField()
    slug = models.SlugField()

    def __str__(self):
        return f"{self.id};" \
               f" {self.name};" \
               f" {self.price};" \
               f" {self.image};" \
               f" {self.release_date};" \
               f" {self.lte_exists};" \
               f" {self.slug}"
    pass
