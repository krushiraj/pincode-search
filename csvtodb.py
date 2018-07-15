import django
import os
import sys

os.environ['DJANGO_SETTINGS_MODULE'] = 'pincodesearch.settings'

django.setup()

from searchapp.models import PincodeRecord
from threading import Thread



with open('pincode.csv') as file:
    lines = file.readlines()
    keys = lines[0].strip().split(',')
    start = int(sys.argv[1])
    lines = list(enumerate(lines))[start:]

    def create_record(vals, i):
        kwargs = dict(zip(keys, vals))
        p = PincodeRecord.objects.create(**kwargs, id=i)
        print(p.id, p.officename, p.pincode, p.officetype)

    for i, line in lines:
        vals = line.strip().split(',')
        create_record(vals, i)
    
    input('Completed press any key to exit')
        