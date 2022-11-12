# personal_notes project 
#Build a web API to add, list, retrieve, delete personal notes


note:i create two models {Author has fields (id_author,name_author,age_author,mobile_number,email_author )}
{Note has fields(note_id,note_title,Note_content,date_created_note,note_author_name,note_author_id{In order to connect the above two tables together})

First we decompress lib.rar to get the folder that contains the project libraries
we go to project folder to use mange.py
Execute the following command on cmd (python manage.py runserver) to run server
note: i use  PostgreSQL for the relational database So you must download the postgresql and create database (name of database is personal_note)
note 2:You may need to modify the values of some parameters (like user and password ) in setting file 

my One API endpoint url is: http://127.0.0.1:8000/api/note (we work in our local machine)
first to add  a note you  request.method=='POST' (post) and send three attribute paramter in body request (note_author_name , note_title , note_content)
note: if the author name is not exist we create new record (new author) in author model (table) with default values (This process is automatic)


next to Listing all notes and Retrieving one note by id.  we use the link with request.method=='GET' (GET) and send one parameter(type) and We distinguish two cases
first case : If the parameter (type) value is 'all' will return all note (Listing all notes)

The second case: If the parameter (type) value is not 'all' Additional parameter must be sent (id) to Select the note you want to restore (Retrieving one note by id)

next: to Deleting a note . we use the link with request.method=='DELETE' (DELETE) and send one parameter (id) To delete this note (we use id paramter to determine the note ) 

examlple: to delete note by id we send the link http://127.0.0.1:8000/api/note?id=6 (DELETE) (to delete the note id=6)

____ to show specific note  we use http://127.0.0.1:8000/api/note?type=&id=6 (GET)_____
 ____ to show all note  we have we use http://127.0.0.1:8000/api/note?type=all
 
 
For any questions about the project, please contact us (aymansh113@gmail.com)




