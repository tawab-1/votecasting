from django.contrib import admin
from home.models import Party, Candidate

@admin.register(Party)
class PartyAdmin(admin.ModelAdmin):
    list_display = ['name', 'chairmen']


@admin.register(Candidate)
class CandidateAdmin(admin.ModelAdmin):
    list_display = ['user', 'party']



