from django.db import models


def custom_upload_to(instance, filename):
    old_instance = Profile.objects.get(pk=instance.pk)
    old_instance.avatar.delete()
    return 'profiles/' + filename


# Create your models here.
class Profile(models.Model):
    RELATION_CHOICES = [
        ('family', 'Family'),
        ('friends', 'Friends'),
        ('work', 'Work'),
        ('partner', 'Partner'),
        ('unknown', 'Unknown')
    ]
    user = models.CharField(max_length=200)
    relation = models.CharField(max_length=200, choices=RELATION_CHOICES)
    avatar = models.ImageField(upload_to='profiles', null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True,)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['relation']

    def __str__(self):
        return self.user
