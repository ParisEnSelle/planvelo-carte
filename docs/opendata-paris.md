# Données OpenData de Paris

## Datasets

### Zones de circulation apaisée à Paris

* Source: [https://opendata.paris.fr/explore/dataset/zones-de-circulation-apaisee-a-paris/information/](https://opendata.paris.fr/explore/dataset/zones-de-circulation-apaisee-a-paris/information/)

* Carte:

<script src="https://embed.github.com/view/geojson/parisenselle/planvelo-carte/master/opendata.paris.fr/zones-de-circulation-apaisee.geojson"></script>

* Licence: [ODbL](https://opendatacommons.org/licenses/odbl/)

## Extraire les données


### Prérequis

* Se placer dans le répertoire `opendata.paris.fr`
* Installer les paquets python nécessaires

~~~
virtualenv ~/path/to/dedicated/virtualenv #facultatif
source ~/path/to/dedicated/virtualenv/bin/activate #facultatif
pip install -r requirements.txt
~~~

### Extraction

* Lancer la commande `python extract.py`.
