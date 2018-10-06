import datetime
import os
from uuid import uuid4
from userauthentication.models import Users as User
from django.db import models


def upload_image(instance, filename):
    """Creates the path of image and renames the image

    Arguments:
        instance {reference} -- instance of the model to access the model fields
        filename {str} -- file name that user uploaded
    """
    extention = filename.split('.')[-1]
    if instance.name:
        filename = "{}.{}".format(instance.name.replace(' ', '_'), extention)
    else:
        filename = '{}.{}'.format(uuid4().hex, extention)

    return os.path.join(instance.upload_to(), filename)


class Categories(models.Model):
    """Model that defines the Table structure of categories table

    Arguments:
        models {class} -- Base class for model
    """

    name = models.CharField(("Category Name"), primary_key=True, max_length=30)
    image = models.ImageField(("Category Image"), upload_to=upload_image)
    active = models.BooleanField(default=True)
    add_date = models.DateField(("Added Date"))
    modified_date = models.DateField(
        ("Modified Date"), default=datetime.date.today)

    def __str__(self):
        return self.name

    def upload_to(self):
        return 'wallpaper_media/categories/'


class Wallpapers(models.Model):
    """Model that defines the Table structure of categories table

    Arguments:
        models {class} -- Base class for model
    """

    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to=upload_image)
    category = models.ForeignKey(Categories, on_delete=models.DO_NOTHING, related_name='category')
    tags = models.TextField()
    location = models.CharField(max_length=50)
    description = models.TextField()
    likes = models.IntegerField(default=0)
    downloads = models.IntegerField(default=0)
    views = models.IntegerField(default=0)
    uploader = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    def upload_to(self):
        return 'wallpaper_media/wallpapers/'
