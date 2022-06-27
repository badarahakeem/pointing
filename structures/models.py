from django.db import models
from django.contrib.auth.models import User


# Create your models here.
ROLE_CHOICES = (
    ('admin', 'admin'),
    ('agent', 'Agent'),
)



class Society(models.Model):

    name = models.CharField(max_length=155, blank=True, null=True)
    email = models.EmailField(max_length=75, blank=True, null=True)
    tel = models.CharField(("Phone Number"), max_length=20, help_text= 'Enter number with Country Code Eg. 771339090')
    address = models.CharField(max_length=75, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    

    class Meta:
        verbose_name = 'Societé'
        verbose_name_plural = 'Societés'
        ordering = ['-created']

    def __str__(self):
        return "{}".format(self.name)



class Agent(models.Model):
    
    user = models.OneToOneField(User, related_name='agent', on_delete=models.CASCADE)
    firstname = models.CharField("Prenom", max_length=30)
    lastname = models.CharField("Nom", max_length=30)
    tel = models.CharField(("Telephone"), max_length=9)
    email = models.EmailField(blank=True)
    role = models.CharField(("Role"), max_length=7, default='agent', choices=ROLE_CHOICES)
    is_admin = models.BooleanField(default=False)
    is_agent = models.BooleanField(default=False)
    society_id = models.ForeignKey(Society, default=1, verbose_name="Societé", on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    
    def get_fullname(self):
        return f'{self.firstname} {self.lastname}'

    def __str__(self):
        return '{} ({})'.format(self.get_fullname(), self.society_id)



















