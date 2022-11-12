from django.db import models
from django.db.models.base import Model

# Create your models here.
class Author(models.Model):
     id_author = models.AutoField(primary_key=True)
     name_author=models.CharField(max_length=35,default='unknown')
     age_author=models.IntegerField();
     mobile_number=models.IntegerField();
     email_author=models.EmailField();

     def __str__(self):
         return self.name_author
          
    


class Note(models.Model):
     note_id= models.AutoField(primary_key=True)
     note_title=models.CharField(max_length=35,default='unknown',)
     Note_content=models.TextField();
     date_created_note=models.DateField();
     note_author_name=models.CharField(max_length=35,default='unknown',)
     note_author_id=models.ForeignKey(Author, on_delete=models.CASCADE)
   
     def __str__(self):
         return self.note_title
    


