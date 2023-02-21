from django.db import models

# Create your models here.

class Blog(models.Model):
    author = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    pub_date = models.DateTimeField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='images/')

    class Meta:
        ordering = ['-pub_date'] # newest first

    def __str__(self):
        return self.title # show title 

    def summary(self):
        return self.body[:100] # show first 100 characters 

    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e %Y') # show date in month day year format

    