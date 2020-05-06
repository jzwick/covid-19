#!/bin/bash

cd ~/Documents/coronavirus-data
git fetch upstream
git rebase upstream/master
python ../Python\ Scripts/archive_covid_data.py ~/Documents/coronavirus-data/ ~/Documents/COVID/covid-data-archive/ False

cd ~/Documents/Covid19Canada
git fetch upstream
git rebase upstream/master