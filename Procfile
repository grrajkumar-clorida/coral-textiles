Procfile
web: gunicorn ProductionManagement.wsgi --log-file - 
#or works good with external database
web: python manage.py migrate && gunicorn ProductionManagement.wsgi

