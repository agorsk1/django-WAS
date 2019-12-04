from django.contrib import admin

from django.utils.translation import gettext_lazy as _
from contacts.models import Person, Email, Address, Phone

admin.site.site_header = _('Addressbook')
admin.site.index_title = _('Dashboards')


class AddressInline(admin.StackedInline):
    model = Address
    extra = 0
    radio_fields = {
        'role': admin.HORIZONTAL
    }


class PhoneInline(admin.TabularInline):
    model = Phone
    extra = 0


class EmailInline(admin.TabularInline):
    model = Email
    extra = 0


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    inlines = [AddressInline, PhoneInline, EmailInline]
    radio_fields = {
        'gender': admin.VERTICAL
    }
