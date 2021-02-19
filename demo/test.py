# -*- coding: utf-8 -*-

import os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")
django.setup()

from excel_exporter.action import get_tpl_file
from app.models import Person
from app.admin import PersonExportDocx

class PersonExport(PersonExportDocx):
    debug = True

    def save(self, conten, fname):
        f = open(fname, 'wb')
        f.write(conten)
        f.close()

def export():
    action = PersonExport()
    fname = get_tpl_file(action.tpl)
    action.get_writer(fname)
    qs = Person.objects.all()[:10]
    content = action.get_export_data(qs, [])
    action.save(content, 'hello.docx')

export()
