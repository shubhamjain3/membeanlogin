from django.db import models
class join (models.Model):
    f_name=models.CharField(max_length=50)
    l_name=models.CharField(max_length=50)
    email=models.EmailField()
    ref_id=models.CharField(max_length=50)

    def __unicode__(self):
        return u'%s %s' %(self.f_name,self.l_name)

    

class uploads (models.Model):
    title=models.CharField(max_length=50)
    file=models.FileField(upload_to="C:/Users/Anshul/Downloads/Django-1.4.22/django/bin/rweb/static/media")
    
    def __unicode__(self):
        return self.title
