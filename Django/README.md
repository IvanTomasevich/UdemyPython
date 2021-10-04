## Django terminal
### Para iniciar el servidor
python manage.py runserver
```
Type 'manage.py help' for usage.
PS C:\Users\Ivan\Udemy\UdemyPython\Django\rdi_site> python manage.py runserver 127.0.0.1:5000
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).

You have 18 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
Run 'python manage.py migrate' to apply them.
October 01, 2021 - 16:34:17
Django version 3.2.7, using settings 'rdi_site.settings'
Starting development server at http://127.0.0.1:5000/
Quit the server with CTRL-BREAK.
[01/Oct/2021 16:34:27] "GET / HTTP/1.1" 200 10697
[01/Oct/2021 16:34:30] "GET /static/admin/css/fonts.css HTTP/1.1" 200 423
[01/Oct/2021 16:34:30] "GET /static/admin/fonts/Roboto-Bold-webfont.woff HTTP/1.1" 200 86184
[01/Oct/2021 16:34:30] "GET /static/admin/fonts/Roboto-Regular-webfont.woff HTTP/1.1" 200 85876
[01/Oct/2021 16:34:30] "GET /static/admin/fonts/Roboto-Light-webfont.woff HTTP/1.1" 200 85692
Not Found: /favicon.ico
[01/Oct/2021 16:34:31] "GET /favicon.ico HTTP/1.1" 404 2112

```
### Para migrar admin, auth, etc
python manage.py migrate
```
PS C:\Users\Ivan\Udemy\UdemyPython\Django\rdi_site> python manage.py migrate
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, sessions
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying admin.0003_logentry_add_action_flag_choices... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying auth.0007_alter_validators_add_error_messages... OK
  Applying auth.0008_alter_user_username_max_length... OK
  Applying auth.0009_alter_user_last_name_max_length... OK
  Applying auth.0010_alter_group_name_max_length... OK
  Applying auth.0011_update_proxy_permissions... OK
  Applying auth.0012_alter_user_first_name_max_length... OK
  Applying sessions.0001_initial... OK

```
### Inicializar app
```
PS C:\Users\Ivan\Udemy\UdemyPython\Django\rdi_site> django-admin startapp courses
```
### Preparar la migracion, ejecutar y arrancar la app

 python manage.py makemigrations course

 python manage.py migrate courses
 
django-admin startapp courses
```
Quit the server with CTRL-BREAK.
PS C:\Users\Ivan\Udemy\UdemyPython\Django\rdi_site> python manage.py makemigrations courses
Migrations for 'courses':
  courses\migrations\0001_initial.py
    - Create model Course
PS C:\Users\Ivan\Udemy\UdemyPython\Django\rdi_site> python manage.py migrate courses
Operations to perform:
  Apply all migrations: courses
Running migrations:
  Applying courses.0001_initial... OK
PS C:\Users\Ivan\Udemy\UdemyPython\Django\rdi_site> django-admin startapp courses

```
### Shell Django

 python manage.py shell

```
PS C:\Users\Ivan\Udemy\UdemyPython\Django\rdi_site> python manage.py shell
Python 3.9.7 (tags/v3.9.7:1016ef3, Aug 30 2021, 20:19:38) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
>>>

```


```

```
