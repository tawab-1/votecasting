from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse


class User(AbstractUser):
    admin = 'admin'
    team = 'team'
    voter = 'voter'
    candidate = 'candidate'
    chairmen = 'chairmen'

    ROLE = [
        (admin, 'Admin'),
        (team, 'Team'),
        (voter, 'Voter'),
        (candidate, 'Candidate'),
        (chairmen, 'Chairmen')
    ]

    role = models.CharField(choices=ROLE, max_length=255, null=True, blank=True)
    identity_card = models.CharField(max_length=255, null=True, blank=True, unique=True)
    area_code = models.CharField(max_length=255, null=True, blank=True)

    def get_absolute_url(self):
        return reverse('users:detail', kwargs={"username":self.username})

