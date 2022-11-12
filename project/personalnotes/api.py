from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from datetime import datetime
from .models import Author, Note
from .serializers import noteserizlizers
from django.core.exceptions import ObjectDoesNotExist

@api_view(['GET','PoST','DELETE'])
def work_on_note(request):
#for Listing all notes.and Retrieving one note by id.       
    if request.method=='GET':
        ass=request.GET
        print(ass) 
        if ass['type']=='all':
             queryset = Note.objects.all()
             serializer = noteserizlizers(queryset , many = True)
             return Response(serializer.data) 
        else:
              rr=Note.objects.filter(note_id=ass['id']).values()
              g=rr.count()
              if g>0:
                   return Response(rr,content_type="application/json")
              else:
                   return Response({'a':"error the id is not exist "},content_type="application/json")

     #to add note              
    if request.method=='POST':
          ass=request.POST
          try:
              rr=Author.objects.get(name_author=ass['note_author_name'])
          except ObjectDoesNotExist:
               a1=Author()
               a1.name_author=ass['note_author_name']
               a1.age_author=99
               a1.email_author='example@gmail.com'
               a1.mobile_number=999999999
               a1.save()
               rr=a1   
          print(ass)
          s1=Note()
          s1.note_title= ass['note_title']
          s1.Note_content=ass['note_content']
          s1.date_created_note=datetime.now()
          s1.note_author_name=ass['note_author_name']
          s1.note_author_id=rr
          s1.save()
          return Response({'a':'the note add successfully'})
   #to delete note by id       
    if request.method=='DELETE':
          ass=request.POST
          rr=Note.objects.filter(note_id=ass['id'])
          g=rr.count()
          if g>0:
                note_to_delete = Note.objects.get(note_id=ass['id'])
                note_to_delete.delete()
                return Response({'s':"Deleted successfully"},content_type="application/json")
          else:
                return Response({'a':"error the id is not exist "},content_type="application/json")