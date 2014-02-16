openraMapAPImirror
==================

See https://github.com/OpenRAOpenRA-Content-Engine/wiki/Set-up-MapAPI-mirror for details

This project only requires Django Web Framework to be installed.

You can run it either using Django embedded web server:

```
python manage.py runserver 127.0.0.1:8000
```

or you can follow "Setup Production" part of the next guide:
https://github.com/ihptru/OpenRA-Content-Engine/blob/master/INSTALL.md

Do not forget to change ```PATH_TO_MAPS``` setting in ```openraMapAPI/settings.py``` to point it to a location where maps fetched over RSYNC are stored.
