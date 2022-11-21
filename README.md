<b>Universidad Galileo</b><br/>
<b>Maestría de Ciencia de Datos</b><br/>
<b>Product Development</b><br/>
<b>Jose Godoy</b><br/>
<b>Carnet 22000570</b><br/>
<b>20 de octubre 2022</b><br/>
<br/>
<b>Publicación del modelo en sitio web</b><br/>
<br/>
<br/>
<b>Instrucciones de instalación</b><br/>
<br/>
<br/>
sudo apt update<br/>
sudo apt install software-properties-common<br/>
sudo add-apt-repository ppa:deadsnakes/ppa<br/>
sudo apt install python3.9<br/>
sudo apt install python3-pip<br/>
sudo apt install python3.9-distutils<br/>
python3.9 -m pip install --upgrade pip<br/>
python3.9 -m pip install virtualenv<br/>
<br/>
cd<br/>
mkdir proyecto<br/>
cd proyecto<br/>
<br/>
virtualenv --python=python3.9 env<br/>
source env/bin/activate<br/>
python -m pip install Django<br/>
pip install djangorestframework<br/>
pip install tensorflow --no-cache-dir<br/>
pip install pandas<br/>
 <br/>
upload apirest folder<br/>
cd apirest<br/>
<br/>
nano restapi/settings.py<br/>
Agregar el nombre de dominio a la lista de ALLOWED_HOSTS<br/>
<br/>
python manage.py migrate<br/>
python manage.py runserver nombre_de_dominio:80
