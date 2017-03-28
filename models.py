from django.db import models
class quiz(models.Model):
    exam=models.CharField(max_length=50)
    s_no=models.CharField(max_length=30)
    ans=models.CharField(max_length=50)
    
    


    def __unicode__(self):
        return self.exam
    
