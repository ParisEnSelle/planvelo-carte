#!/usr/bin/env python
import geojson
import overpass
import sys

queries = {'bus.geojson': 'area(3600007444)->.searchArea;(node["highway"]["cycleway:right"="share_busway"](area.searchArea);way["highway"]["cycleway:right"="share_busway"](area.searchArea);relation["highway"]["cycleway:right"="share_busway"](area.searchArea);node["highway"]["cycleway:left"="share_busway"](area.searchArea);way["highway"]["cycleway:left"="share_busway"](area.searchArea);relation["highway"]["cycleway:left"="share_busway"](area.searchArea);node["highway"]["cycleway:both"="share_busway"](area.searchArea);way["highway"]["cycleway:both"="share_busway"](area.searchArea);relation["highway"]["cycleway:both"="share_busway"](area.searchArea);node["highway"]["cycleway"="share_busway"](area.searchArea);way["highway"]["cycleway"="share_busway"](area.searchArea);relation["highway"]["cycleway"="share_busway"](area.searchArea););',
           'voies_separees_un_seul_sens.geojson': 'area(3600007444)->.searchArea;(node["highway"]["cycleway:left"="lane"](area.searchArea);way["highway"]["cycleway:left"="lane"](area.searchArea);relation["highway"]["cycleway:left"="lane"](area.searchArea);node["highway"]["cycleway:right"="lane"](area.searchArea);way["highway"]["cycleway:right"="lane"](area.searchArea);relation["highway"]["cycleway:right"="lane"](area.searchArea););',
           'voies_separees.geojson': 'area(3600007444)->.searchArea;(node["highway"="cycleway"](area.searchArea);way["highway"="cycleway"](area.searchArea);relation["highway"="cycleway"](area.searchArea);node["highway"]["cycleway:both"="lane"](area.searchArea);way["highway"]["cycleway:both"="lane"](area.searchArea);relation["highway"]["cycleway:both"="lane"](area.searchArea);node["highway"]["cycleway:left"="lane"]["cycleway:right"="lane"](area.searchArea);way["highway"]["cycleway:left"="lane"]["cycleway:right"="lane"](area.searchArea);relation["highway"]["cycleway:left"="lane"]["cycleway:right"="lane"](area.searchArea);node["highway"]["cycleway"="track"](area.searchArea);way["highway"]["cycleway"="track"](area.searchArea);relation["highway"]["cycleway"="track"](area.searchArea);node["highway"]["cycleway:both"="track"](area.searchArea);way["highway"]["cycleway:both"="track"](area.searchArea);relation["highway"]["cycleway:both"="track"](area.searchArea);node["highway"]["cycleway:left"="track"]["cycleway:right"="track"](area.searchArea);way["highway"]["cycleway:left"="track"]["cycleway:right"="track"](area.searchArea);relation["highway"]["cycleway:left"="track"]["cycleway:right"="track"](area.searchArea););'
          }

def main():
    api = overpass.API()
    for outputfile,query in queries.iteritems():
        print('Writing {} ...'.format(outputfile))
        response = api.Get(query)
        GeoJSONFeatureCollectionAsString = geojson.dumps(response, indent=4, sort_keys=True).decode('unicode-escape').encode('utf8')
        f = file(outputfile, 'w')
        f.write(GeoJSONFeatureCollectionAsString)
        f.close()

if __name__ == "__main__":
    main()
