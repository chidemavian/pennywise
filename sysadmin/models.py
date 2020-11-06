from django.db import models

class tblincome(models.Model):
    year = models.CharField('Exam Type', max_length=375)
    month = models.CharField('Subject', max_length=75)
    description= models.CharField('Session', max_length=75, null=True, blank=True)
    amount = models.CharField('Class', max_length=20)
    datee = models.CharField('Class', max_length=20)
    timee = models.CharField('Class', max_length=20)

    def __unicode__(self):
        return '%s %s %s'%(self.year,self.month,self.amount)



class tblbudget(models.Model):
    year = models.CharField('Year', max_length=375)
    datee = models.CharField('Date', max_length=20)
    timee = models.CharField('Time', max_length=20)
    month = models.CharField('Month', max_length=75)
    description= models.CharField('Description', max_length=75, null=True, blank=True)
    amount = models.CharField('Amount', max_length=20)


    def __unicode__(self):
        return '%s %s %s'%(self.year,self.month,self.amount)


class tblevents(models.Model):
    budget = models.ForeignKey(tblbudget)
    month = models.CharField('Month', max_length=75)
    description= models.CharField('Description', max_length=75, null=True, blank=True)
    amount = models.CharField('Amount', max_length=20)
    datee = models.CharField('Date', max_length=20)
    timee = models.CharField('Time', max_length=20)

    def __unicode__(self):
        return '%s %s %s'%(self.month,self.amount)
