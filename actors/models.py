from django.db import models

NATIONALITY_CHOICES =(
    ('BRAZIL', 'Brasil'),
    ('USA', 'Estados Unidos'),
)

class Actor(models.Model):
    name=models.CharField(max_length=200,null=False,blank=False)
    birthday=models.DateField(null=True,blank=True)
    nationality=models.CharField(max_length=200,choices=NATIONALITY_CHOICES,null=True,blank=True)

    def __str__(self):
        return self.name