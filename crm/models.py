from django.db import models

from django.conf import settings


#creates Unique path for image uploaded by user
def get_image_path(instance, image_name):
    return f"{instance.created_by.id}/{image_name}"


class Contact(models.Model):
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="contacts", on_delete=models.CASCADE)
    first_name = models.CharField("Fisrt Name", max_length=64)
    last_name = models.CharField("Last Name", max_length=64)
    email = models.EmailField(max_length=250, blank=True)
    address1 = models.CharField("Address line 1", max_length=1000, blank=True)
    address2 = models.CharField("Address line 2", max_length=1000, blank=True)
    city = models.CharField("City", max_length=1000, blank=True)
    state = models.CharField("State", max_length=15, blank=True)
    zip_code = models.CharField("Zip Code", max_length=15, blank=True)
    profile_picture = models.ImageField(upload_to=get_image_path, blank=True)
    created_at = models.DateTimeField("Created At", auto_now_add=True)
    modified_at = models.DateTimeField("Last Modified", auto_now=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    @property
    def can_send_postcard(self):
        return all([self.address1, self.city, self.state, self.zip_code])

class PostCard(models.Model):
    contact = models.ForeignKey(Contact, related_name="postcard", on_delete=models.CASCADE, default="")
    time_sent = models.DateTimeField("Time Sent")

    
    
