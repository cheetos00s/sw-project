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
pip install django

pip install mysqlclient

pip list

# migrar bd de django a mysql
py manage.py makemigrations
python3 manage.py migrate

# // run
py manage.py runserver

