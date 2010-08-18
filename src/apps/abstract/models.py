from django.db import models
from django.utils.translation import ugettext_lazy as _

class CommonModel(models.Model):
    """
    This is an abstract model which will be inherited by nearly all models. 
    When the object is created it will get a date_created timestamp and each 
    time it is modified it will recieve a date_modified time stamp as well.
    """
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        abstract = True

