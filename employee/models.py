from django.db import models
from django.dispatch import receiver
from django.db.models.signals import pre_save
from django.contrib.auth.models import User

# Create your models here.
class MainData(models.Model):

    company_name = models.CharField('Company Name', max_length=200,  default='n/a')
    job_title = models.CharField('Job Tittle', max_length=200,  default='n/a')
    contact_name = models.CharField('Contact Name', max_length=200,  default='n/a')
    contact_number = models.CharField('Contact Number', max_length=200,  default='n/a')
    emails = models.CharField('Emails', max_length=200,  default='n/a')
    company_website = models.CharField('Company Website', max_length=200,  default='n/a')
    address = models.CharField('Address', max_length=200,  default='n/a')
    linkedin = models.CharField('Linkedin', max_length=200,  default='n/a')
    jobs = models.CharField('Jobs', max_length=200,  default='n/a')

    class Meta:
        abstract = True

    def __str__(self):
        return self.contact_name

class Leads(MainData):
    pass


@receiver(pre_save, sender=User)
def set_new_user_inactive(sender, instance, **kwargs):
    if instance._state.adding is True:
        instance.is_active = False