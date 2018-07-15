import django
import os
import sys

os.environ['DJANGO_SETTINGS_MODULE'] = 'pincodesearch.settings'

django.setup()

from searchapp.models import PincodeRecord

file1 = open('pincode.csv')
lines = set(file1.readlines())
file1.close()

dbdata = set()
dbvals = PincodeRecord.objects.all().values()
for val in dbvals:
    dbdata.add(','.join([str(i) for i in val.values()][1:])+'\n')

missing = lines - dbdata
