# pylint: disable=no-self-use

from django.contrib import admin

from . import models


@admin.register(models.Voter)
class VoterAdmin(admin.ModelAdmin):

    # List

    search_fields = [
        'first_name',
        'last_name',
        'email',
    ]

    list_display = [
        'name',
        'email',
        'birth_date',
        'zip_code',
        'email_confirmed',
        'email_subscribed',
    ]

    list_filter = [
        'regions',
        'email_confirmed',
        'email_subscribed',
    ]

    filter_horizontal = [
        'regions'
    ]

    # Detail

    raw_id_fields = ['user']
    related_lookup_fields = {
        'fk': ['user']
    }


@admin.register(models.Status)
class StatusAdmin(admin.ModelAdmin):

    def fetch_and_update_registration(self, _request, queryset):
        for status in queryset:
            status.fetch_and_update_registration()

    search_fields = [
        'voter__first_name',
        'voter__last_name',

        'election__name',
    ]

    list_display = [
        'id',
        'voter',
        'election',

        'registered',
        'read_sample_ballot',
        'located_polling_location',
        'voted',
    ]

    list_filter = [
        'election',

        'registered',
        'read_sample_ballot',
        'located_polling_location',
        'voted',
    ]

    actions = [fetch_and_update_registration]
