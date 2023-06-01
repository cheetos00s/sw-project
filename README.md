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
<<<<<<< HEAD
pip install django

pip install mysqlclient

pip list

# migrar bd de django a mysql
py manage.py makemigrations
py manage.py migrate

# // run
=======
pip list
pip install django
pip install mysqlclient
# con el comando pip list miramos que este intalado django y mysqlclient, luego..

# hacer la migracion a la bd, luego..
py manage.py makemigrations
py manage.py migrate

# crear el usuario admin, luego..
py manage.py createsuperuser
# con: [username: admin, email: admin@admin.com, password: admin1234]
# despues oprimir [Y] en la consola para aceptar
# Por último arrancar el projecto..

# // run [comando para arrancar el projecto django]
>>>>>>> b2582d48cd86ebf359d301421cbf65aa0336f794
py manage.py runserver

