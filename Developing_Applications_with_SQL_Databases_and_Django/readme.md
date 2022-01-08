# Django:  

django-admin startproject project_name  
cd project_name  
python manage.py startapp app_name  

The scaffold contains the fundamental configuration and setting files for a Django project and app:  

    For project-related files:  
        manage.py is a command-line interface used to interact with the Django project to perform tasks such as starting the server, migrating models, and so on.  
        project/settings.py contains the settings and configurations information.  
        project/urls.py contains the URL and route definitions of your Django apps within the project.  

    For app-related files:  
        app/admin.py: is for building an admin site  
        app/models.py: contains model classes  
        app/views.py: contains view functions/classes  
        app/urls.py: contains URL declarations and routing for the app  
        app/apps.py: contains configuration meta data for the app  
        app/migrations/: model migration scripts folder  

# Before starting the app:  

run python manage.py makemigrations  
python manage.py migrate !Seems to work fine to just run migrate to make and migrate, but not confirmed.  

# Start server:  

python manage.py runserver  
