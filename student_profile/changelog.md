##Personal Changelog

#Version 2

**Improvements**
-Added student_id field to Student.

**Reflections**
-MakeMigrations does not work without registering the app in the settings.py file. 
-Do not put the __init method in the models.py. Yep, it works!
-Change the database in settings.py, if you are using anything other that sqllite. 
-Also create the database if you are using mysql. Django does not create it. 
-When creating a new field, do give a default. Otherwise django loses it's mind.



#Version 1

-added student_details. Bare bones.

#Base (05-Feb-2024)

-added django .gitignore from https://djangowaves.com/tips-tricks/gitignore-for-a-django-project/