# Données OpenData de Paris

## Datasets

### Zones de circulation apaisée à Paris

* Identifiant du jeu de données: `zones-de-circulation-apaisee-a-paris`

* Source: [https://opendata.paris.fr/explore/dataset/zones-de-circulation-apaisee-a-paris/information/](https://opendata.paris.fr/explore/dataset/zones-de-circulation-apaisee-a-paris/information/)

* Carte:

<script src="https://embed.github.com/view/geojson/parisenselle/planvelo-carte/master/opendata.paris.fr/zones-de-circulation-apaisee.geojson"></script>

* "Fraicheur des données": Septembre 2016

* Licence: [ODbL](https://opendatacommons.org/licenses/odbl/)

### Stationnement sur voie publique - emplacements

* Identifiant du jeu de données: `stationnement-voie-publique-emplacements`

* Source: [https://opendata.paris.fr/explore/dataset/stationnement-voie-publique-emplacements/information/](https://opendata.paris.fr/explore/dataset/stationnement-voie-publique-emplacements/information/)

* Requête API: `q= regpar="Vélos" OR (regpri="2 Roues" AND regpar="Mixte")`

* Carte: FIXME

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

## API

### Console

* v1: [https://opendata.paris.fr/api/v1/console/datasets/1.0/search/](https://opendata.paris.fr/api/v1/console/datasets/1.0/search/)
* v2:  [https://opendata.paris.fr/api/v2/console](https://opendata.paris.fr/api/v2/console)

### Documentation

* v1: [https://opendata.paris.fr/api/v1/documentation](https://opendata.paris.fr/api/v1/documentation)
* v2:  [http://docs.opendatasoft.com/en/using_api/v2/index.html](http://docs.opendatasoft.com/en/using_api/v2/index.html)
