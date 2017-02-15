# Données OpenStreetMap

## Outils utilisés

Ces cartes sont réalisées à partir de données [OpenStreetMap](openstreetmap.org) (OSM), grâce à l'API [Overpass Turbo](http://overpass-turbo.eu/#).

Les références des pistes cyclables sont expliquées dans le [wiki](https://wiki.openstreetmap.org/wiki/Bicycle).

## Extraire les données

Les requêtes `Overpass` et les noms des fichiers de carte cibles se trouvent dans le dict python `queries` du script  `extract.py`.

### Prérequis

* Se placer dans le répertoire `osm`
* Installer les paquets python nécessaires

~~~
virtualenv ~/path/to/dedicated/virtualenv #facultatif
source ~/path/to/dedicated/virtualenv/bin/activate #facultatif
pip install -r requirements.txt
~~~

### Extraction

* Lancer la commande `python extract.py`.

## Les cartes

<script src="https://embed.github.com/view/geojson/parisenselle/planvelo-carte/master/osm/bus.geojson"></script>

<script src="https://embed.github.com/view/geojson/parisenselle/planvelo-carte/master/osm/voies_separees_un_seul_sens.geojson"></script>

<script src="https://embed.github.com/view/geojson/parisenselle/planvelo-carte/master/osm/voies_separees.geojson"></script>
