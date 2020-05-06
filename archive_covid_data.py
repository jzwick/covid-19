import pandas as pd
import sys
import datetime

#
# USAGE: archive_covid_data.py path_newdata path_archive
#

path_newdata = sys.argv[1]
path_archive = sys.argv[2]
verbose=sys.argv[3]

filenames=['boro.csv','by-age.csv','by-sex.csv','case-hosp-death.csv','tests-by-zcta.csv']

summary=pd.read_csv(path_newdata+"summary.csv",header=None)

if verbose:
    print(summary)
dateindex = list(summary[0]).index('As of:')
datestr = summary[1][dateindex]
if verbose:
    print(datestr)
monthstr=datestr.split(" ")[0]
daystr=datestr.split(" ")[1].split(",")[0]

if verbose:
	print(datestr, monthstr, daystr)

monthdict={'January':1,
          'February':2,
          'March':3,
          'April':4,
          'May':5,
          'June':6,
          'July':7,
          'August':8,
          'September':9,
          'October':10,
          'November':11,
          'December':12}

datadate = datetime.date(2020,monthdict[monthstr],int(daystr))
datadate_str = str(datadate)

summary.to_csv(path_archive+datadate_str+"_"+"summary.csv")
for file in filenames:
	tmp=pd.read_csv(path_newdata+file)
	if file != 'case-hosp-death.csv':
		tmp['date']=datadate
	tmp.to_csv(path_archive+datadate_str+"_"+file)
	if verbose:
		print("Copied file ",file," from ",path_newdata," to ",path_archive)
		

