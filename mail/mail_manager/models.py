from django.db import models

# Create your models here.
class NewEmail(models.Model):
    mail_subject = models.CharField(max_length=100,null=False,blank=False)
    task_title = models.CharField(max_length=50,null=False,blank=False)
    deadline = models.DateTimeField(null=False,blank=False)
    description = models.TextField(null=True,blank=True) 
    additional_link = models.URLField(null=True,blank=True)

    class Meta:
        verbose_name="User Email"

    def __str__(self) -> str:
        return str(self.pk)