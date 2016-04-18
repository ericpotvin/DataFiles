#!/bin/bash

# URLS
# http://www.nanpa.com/reports/area_code_relief_planning.html
# http://www.nanpa.com/nanp1/npa_report.csv

# definitions:
# http://www.nanpa.com/area_codes/AreaCodeDatabaseDefinitions.xls

FILE="nanpa.csv"
FILE_TMP="nanpa_tmp.csv"

if [ ! -f "$FILE" ] ; then
    wget -q http://www.nanpa.com/nanp1/npa_report.csv -O "$FILE"
else
	echo "File $FILE exists"
	exit 1
fi

# Clean the files

## Remove first line
tail -n +2 "$FILE" > "$FILE_TMP"
mv "$FILE_TMP" "$FILE"

## Get the columns we need

cat "$FILE" | cut -d',' -f 1,9,10,11 | grep Y > "$FILE_TMP"
mv "$FILE_TMP" "$FILE"

cat "$FILE" | egrep -v 'NANP AREA|^600,|^622,|^670,|^710,' > "$FILE_TMP"
mv "$FILE_TMP" "$FILE"

## Renaming US States

sed -i 's/,AL,/,ALABAMA,/g' "$FILE"
sed -i 's/,AK,/,ALASKA,/g' "$FILE"
sed -i 's/,AZ,/,ARIZONA,/g' "$FILE"
sed -i 's/,AR,/,ARKANSAS,/g' "$FILE"
sed -i 's/,CA,/,CALIFORNIA,/g' "$FILE"
sed -i 's/,CO,/,COLORADO,/g' "$FILE"
sed -i 's/,CT,/,CONNECTICUT,/g' "$FILE"
sed -i 's/,DC,/,DISTRICT OF COLUMBIA,/g' "$FILE"
sed -i 's/,DE,/,DELAWARE,/g' "$FILE"
sed -i 's/,FL,/,FLORIDA,/g' "$FILE"
sed -i 's/,GA,/,GEORGIA,/g' "$FILE"
sed -i 's/,HI,/,HAWAII,/g' "$FILE"
sed -i 's/,ID,/,IDAHO,/g' "$FILE"
sed -i 's/,ID,/,IDAHO,/g' "$FILE"
sed -i 's/,IL,/,ILLINOIS,/g' "$FILE"
sed -i 's/,IN,/,INDIANA,/g' "$FILE"
sed -i 's/,IA,/,IOWA,/g' "$FILE"
sed -i 's/,KS,/,KANSAS,/g' "$FILE"
sed -i 's/,KY,/,KENTUCKY,/g' "$FILE"
sed -i 's/,LA,/,LOUISIANA,/g' "$FILE"
sed -i 's/,ME,/,MAINE,/g' "$FILE"
sed -i 's/,MD,/,MARYLAND,/g' "$FILE"
sed -i 's/,MA,/,MASSACHUSETTS,/g' "$FILE"
sed -i 's/,MI,/,MICHIGAN,/g' "$FILE"
sed -i 's/,MN,/,MINNESOTA,/g' "$FILE"
sed -i 's/,MS,/,MISSISSIPPI,/g' "$FILE"
sed -i 's/,MO,/,MISSOURI,/g' "$FILE"
sed -i 's/,MT,/,MONTANA,/g' "$FILE"
sed -i 's/,NE,/,NEBRASKA,/g' "$FILE"
sed -i 's/,NV,/,NEVADA,/g' "$FILE"
sed -i 's/,NH,/,NEW HAMPSHIRE,/g' "$FILE"
sed -i 's/,NJ,/,NEW JERSEY,/g' "$FILE"
sed -i 's/,NM,/,NEW MEXICO,/g' "$FILE"
sed -i 's/,NY,/,NEW YORK,/g' "$FILE"
sed -i 's/,NC,/,NORTH CAROLINA,/g' "$FILE"
sed -i 's/,ND,/,NORTH DAKOTA,/g' "$FILE"
sed -i 's/,OH,/,OHIO,/g' "$FILE"
sed -i 's/,OK,/,OKLAHOMA,/g' "$FILE"
sed -i 's/,OR,/,OREGON,/g' "$FILE"
sed -i 's/,PA,/,PENNSYLVANIA,/g' "$FILE"
sed -i 's/,RI,/,RHODE ISLAND,/g' "$FILE"
sed -i 's/,SC,/,SOUTH CAROLINA,/g' "$FILE"
sed -i 's/,SD,/,SOUTH DAKOTA,/g' "$FILE"
sed -i 's/,TN,/,TENNESSEE,/g' "$FILE"
sed -i 's/,TX,/,TEXAS,/g' "$FILE"
sed -i 's/,UT,/,UTAH,/g' "$FILE"
sed -i 's/,VT,/,VERMONT,/g' "$FILE"
sed -i 's/,VA,/,VIRGINIA,/g' "$FILE"
sed -i 's/,WA,/,WASHINGTON,/g' "$FILE"
sed -i 's/,WV,/,WEST VIRGINIA,/g' "$FILE"
sed -i 's/,WI,/,WISCONSIN,/g' "$FILE"
sed -i 's/,WY,/,WYOMING,/g' "$FILE"

## Renaming country

sed -i 's/,CANADA/,CA/g' "$FILE"

## Cut the last column
cat "$FILE" | cut -d',' -f 1-3 > "$FILE_TMP"
mv "$FILE_TMP" "$FILE"
