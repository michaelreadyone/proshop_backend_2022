# Changes that do not reveal in code

- S3L12
  - `pip install django==3.1.4`
  - `django-admin startproject backend .`
  - `python manage.py startapp base`
  - `pip install djangorestframework==3.12.2`
- S3L13
  - set CORS, allow django to be visited by frontend urls
    - `pip install django-cors-headers==3.6.0`
- S3L14
  - `python manage.py migrate`
  - `python manage.py createsuperuser`
- S4L15
  - `python manage.py makemigrations`
- S4L16
  - `pip install pillow==8.0.1`
  - By default, the image from model will be saved into root folder
- S6L32
  - `pip install djangorestframework-simplejwt==5.0.0`
  - Customize expired time from 5 min to 1 day
- S6L33
  - JWT customize 1 encode other information in token
  - JWT customize 2 show other information in api return together with token
  - [TokenObtainPairSerializer](<https://github.com/jazzband/djangorestframework-simplejwt/blob/master/rest_framework_simplejwt/serializers.py>)
- S6L37
  - Django signal to make username to email