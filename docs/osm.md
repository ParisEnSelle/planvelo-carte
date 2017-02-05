# Extraction des données OSM

## Outils utilisés

Ces cartes sont réalisées à partir de données [OpenStreetMap](openstreetmap.org) (OSM), grâce à l'API [Overpass Turbo](http://overpass-turbo.eu/#).

Les références des pistes cyclables sont expliquées dans le [wiki](https://wiki.openstreetmap.org/wiki/Bicycle).

## Générer les cartes

Les requêtes `Overpass` et les noms des fichiers de carte cibles se trouvent dans le dict python `queries` du script python `extract.py`.

### Prérequis

* Se placer dans le répertoire `osm`
* Installer les paquets python nécessaires
```bash
virtualenv ~/path/to/dedicated/virtualenv #facultatif
source ~/path/to/dedicated/virtualenv/bin/activate #facultatif
pip install -r requirements.txt
```

### Extraction

* Lancer la commande suivante
```bash
python extract.py
```
Les cartes sont générées à la racine du dossier où le script est lancé. Ce dernier écrase les précédentes.
