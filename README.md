# Django-rest
Es un minibackend para enterder el funcionamiento de despliegues


## Para ejecutarlo 


Crear un entorno y activarlo
```
python3 -m venv mi_entorno  

source mi_entorno/bin/.activate 
```

instalar los requerimientos 

```
pip install -r requirements.txt
```

Hacer migraciones necesarias 

```
python manage.py makemigrations
python manage.py migrate
```

Ejecutar :   
Por default sale en el puerto 8000 pero si lo tienes ocupa ver en la consola cual te asigno  
```
python manage.py runserver

```