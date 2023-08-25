from django.db import models

# Create your models here.


class Party(models.Model):
    name = models.CharField(max_length=255)
    symbol = models.ImageField(upload_to='media')
    chairmen = models.ForeignKey('users.User', on_delete=models.CASCADE, null=True, blank=True)
    total_vote = models.IntegerField(null=True, blank=True)
    created_at = models.DateTimeField(auto_created=True)

    def __str__(self):
        return self.name


class Candidate(models.Model):

    MPA = 'MPA'
    MNA = 'MNA'

    SEAT = [
        (MPA, 'MPA'),
        (MNA, 'MNA')
    ]
    user = models.ForeignKey('users.User', on_delete=models.CASCADE, null=True, blank=True)
    party = models.ForeignKey('home.Party', on_delete=models.CASCADE, null=True, blank=True)
    seat = models.CharField(max_length=255, choices=SEAT)
    city = models.CharField(max_length=255)
    halka = models.CharField(max_length=255, null=True, blank=True)
    votes = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f'{self.user.username}-{self.party.name}'


