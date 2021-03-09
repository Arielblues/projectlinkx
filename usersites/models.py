from django.db import models
from django.utils import timezone
from django_countries.fields import CountryField
from django.contrib.auth.models import User
from django.urls import reverse


class Keywordss(models.Model):
    kwords = models.CharField(max_length=200) 
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    class Meta: 
        verbose_name_plural = "multikwords" 
    def __unicode__(self): 
        return self.title

    def __str__(self):
        return self.title


# Create your models here. 
class Sitecategory(models.Model): 
    title = models.CharField(max_length=200) 
    slug = models.SlugField(max_length=40, unique=True) 
    description = models.TextField() 
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    class Meta: 
        verbose_name_plural = "Categories" 
    def __unicode__(self): 
        return self.title

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('xxpost-detail', kwargs={'pk': self.pk})


# Create your models here.
class Usersites(models.Model):
    DEFAULTL = 'el'
    LANGUAGE_CHOICES = [
		('af', 'Afrikaans'),
		('am', 'Amharic	'),
		('bg', 'Bulgarian	'),
		('ca', 'Catalan	'),
		('zh-HK', 'Chinese (Hong Kong)	'),
		('zh-CN', 'Chinese (PRC)	'),
		('zh-TW', 'Chinese (Taiwan)	'),
		('hr', 'Croatian	'),
		('cs', 'Czech	'),
		('da', 'Danish	'),
		('nl', 'Dutch	'),
		('en-GB', 'English (UK)'),
		('en-US', 'English (US)	'),
		('et', 'Estonian	'),
		('fil', 'Filipino	'),
		('fi', 'Finnish	'),
		('fr-CA', 'French (Canada)	'),
		('fr-FR', 'French (France)	'),
		('de', 'German	'),
		('el','Greek	'),
		('he', 'Hebrew	'),
    ]
    url = models.URLField(max_length=200)
    country = CountryField(blank_label='(select country)')
    language = models.CharField(default=DEFAULTL, max_length=5, choices=LANGUAGE_CHOICES)
    date_posted = models.DateTimeField(default=timezone.now)
    categories = models.ForeignKey(Sitecategory, blank=True, null=True, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    kwordsss = models.ForeignKey(Keywordss, blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.url



    def get_absolute_url(self):
        return reverse('xpost-detail', kwargs={'pk': self.pk})




