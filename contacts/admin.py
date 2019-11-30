from django.contrib import admin

from contacts.models import Person


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    pass
