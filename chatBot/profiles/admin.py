from django.contrib import admin
from profiles.models import Profile


# Register your models here.
class ProfileAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')


admin.site.register(Profile, ProfileAdmin)
