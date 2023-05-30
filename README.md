# sw-project
vamos a hacer un buen proyecto 

# PASOS
# 1. iniciar servidor apache de mysql, xampp o wamp
# 2. seguir estos pasos
# // create py enviroment
# .. despues del git clone .. en la carpeta raiz hacer..
py -m venv venv

# linux
source venv/Scripts/activate
source venv/bin/activate

# windows
.\venv\Scripts\activate

# Luego por consola..
pip list
pip install django
pip install mysqlclient
# con el comando pip list miramos que este intalado django y mysqlclient, luego..

# hacer la migracion a la bd, luego..
py manage.py migrate

# crear el usuario admin, luego..
py manage.py createsuperuser
# con: [username: admin, email: admin@admin.com, password: admin1234]
# despues oprimir [Y] en la consola para aceptar
# Por último arrancar el projecto..

# // run [comando para arrancar el projecto django]
py manage.py runserver

