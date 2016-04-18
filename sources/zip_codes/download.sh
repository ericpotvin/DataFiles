#!/bin/bash

: '
    zip
    type
    primary_city
    acceptable_cities
    unacceptable_cities
    state
    county
    timezone
    area_codes
    latitude
    longitude
    world_region
    country
    decommissioned
    estimated_population
    notes
'

FILE="zip_code_database.csv"
FILE_TMP="$FILE.tmp"

wget "http://www.unitedstateszipcodes.org/$FILE" -O "$FILE_TMP"
dos2unix -q "$FILE_TMP"

tail -n +2 "$FILE_TMP" > "$FILE"

# Clean values
sed -i 's/ñ/n/g' "$FILE"
sed -i 's/ö/o/g' "$FILE"
sed -i 's/ó/o/g' "$FILE"
