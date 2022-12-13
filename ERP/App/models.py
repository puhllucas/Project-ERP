from django.db import models


class Apps(models.Model):

    user_name = models.CharField(max_length=255)
    user_email = models.CharField(max_length=255)

