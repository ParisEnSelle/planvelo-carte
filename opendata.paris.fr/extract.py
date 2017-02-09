#!/usr/bin/env python
import geojson
import requests
import sys

queries = {'zones-de-circulation-apaisee.geojson': 'https://opendata.paris.fr/explore/dataset/zones-de-circulation-apaisee-a-paris/download/?format=geojson&timezone=Europe/Berlin',
          }

def main():
    for outputfile,url in queries.iteritems():
        r = requests.get(url)
        if r.status_code == 200:
            print('Writing {} ...'.format(outputfile))
            GeoJSONFeatureCollectionAsString = geojson.dumps(r.json(), indent=4, sort_keys=True).decode('unicode-escape').encode('utf8')
            f = file(outputfile, 'w')
            f.write(GeoJSONFeatureCollectionAsString)
            f.close()
        else:
            print 'Error HTTP {}'.format(r.status_code)

if __name__ == "__main__":
    main()
