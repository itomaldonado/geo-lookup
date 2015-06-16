# Geo-Lookup

Simple program that reads a csv file (with headers) and looks up the lat/long of the locations using Google Maps API.

## Requirements
Should only require pygeocoder.

```pip install -r requirements.txt```

## How to use
At this early stage you need to modify it in order to point it to the file you want to geocode.

modify the variable ``` file_location = "Locations to Visit.csv" ```

to modify the headers your file has look for the following comment:
``` # Headers are used here. ```

