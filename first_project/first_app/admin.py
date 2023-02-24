from django.contrib import admin
from first_app.models import AccessRecord, Topic, Webpage
# Register your models here.

# Register models to admin, so it's ready to be use with the admin interface
admin.site.register(AccessRecord)
admin.site.register(Topic)
admin.site.register(Webpage)

# In order to actually fully use the database with the admin interface, we need to create a super user.
# Only people who were creating the website and has acess to all of this info could create a super user





