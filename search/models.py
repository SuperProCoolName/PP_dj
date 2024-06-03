from django.db import models
from django.db.models.signals import post_delete
from django.dispatch import receiver
from django.utils import timezone
from django.core.validators import MinValueValidator, MaxValueValidator
import os


# Create your models here.


class Ad(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(100000000)])
    image = models.ImageField(upload_to='ad/%Y/%m/%d/',
                              default='default_image.jpg')
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title


@receiver(post_delete, sender=Ad)
def delete_image(sender, instance, **kwargs):
    if instance.image:
        # Save the image file path
        image_path = instance.image.path

        # Disconnect the delete_image function from the post_delete signal
        post_delete.disconnect(delete_image, sender=Ad)

        # Delete the ad
        instance.delete()

        # Reconnect the delete_image function to the post_delete signal
        post_delete.connect(delete_image, sender=Ad)

        # Delete the image file
        if os.path.isfile(image_path):
            os.remove(image_path)


post_delete.connect(delete_image, sender=Ad)
