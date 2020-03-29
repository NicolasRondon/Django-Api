# Multiuser Blog Academlo
 Un api que cuenta con artículos, autenticacion, perfiles, comentarios, favoritos, seguir, etiquetas,
 paginacíon y filtros 
 
 ### Instalación
 ```
git clone https://github.com/NicolasRondon/Django-Api.git
pip3 install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
```

###  Endpoints
Endpoints para realizar las peticiones http
#### Usuarios
##### Registrar
###### Url
 ```
{{url}}/api/users/
```

###### Headers 
 ```
Content-Type: application/json
X-Requested-With: XMLHttpRequest
```
###### Body
 ```
{"user":{"email":"a@gmail.com", "password":"{{PASSWORD}}", "username":"{{USERNAME}}"}}
```



