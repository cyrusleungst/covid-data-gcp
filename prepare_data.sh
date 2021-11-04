#!/bin/bash

cd /Users/cyrus/development/covid-data-gcp

source "/Users/cyrus/development/covid-data-gcp/venv/bin/activate"
python3 get_covid.py

now=$(date +'%Y-%m-%d')

cat data.json | jq -c '.[]' > $now.json

python3 gs_load.py

rm -f data.json
rm -f $now.json
