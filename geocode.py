import csv
from pygeocoder import Geocoder, GeocoderError

# Should have a CSV file with headers, the minimun headers should be:
# 'Street'  'City'  'State'  'Zip Code'

geocoder = Geocoder()
# geocoder = Geocoder(api_key='MY_SIMPLE_API_KEY') # if you have an api key, use it here...

# CSV File location
file_location = "Locations to Visit.csv"

with open( file_location, "rb" ) as theFile:
    reader = csv.DictReader( theFile )
    print 'Longitude, Latitude'
    for line in reader:
        # line is { 'workers': 'w0', 'constant': 7.334, 'age': -1.406, ... }
        # e.g. print( line[ 'workers' ] ) yields 'w0'

        # Headers are used here.
        address = line['Street'] + ", " + line['City'] + ", " + line['State'] + " " + line['Zip Code']
        results = geocoder.geocode(address)
        print str(results[0].coordinates[1]) + ', ' + str(results[0].coordinates[0])

