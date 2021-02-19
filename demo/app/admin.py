from django.contrib import admin

from .models import Author, Book, Category, Person, Persona
from excel_exporter.admin import ExportAdmin



class BookAdmin(ExportAdmin):
    list_display = ('name', 'author', 'added')
    list_filter = ['categories', 'author']
    export_fields = ('name', 'author', 'added', 'author_email', 'published', 'published_time', 'price')
admin.site.register(Book, BookAdmin)


class PersonAdmin(ExportAdmin):
    list_display = ( 'name', 'address', 'int', 'bool', 'dec', 'float', 'time', 'date', 'datetime', 'image')
    export_fields = ('name', 'address', 'int', 'bool', 'dec', 'float', 'time', 'date', 'datetime', 'image', 'books')

admin.site.register(Person, PersonAdmin)

from excel_exporter.action import Xlsx, Docx, Xls
class PersonExportXlsx(Xlsx):
    desc = 'persons to xlsx'
    tpl = 'persons.xlsx'
    queryset_name = 'ps'
    obj_name = 'p'

    def get_payloads(self, queryset, list_display):
        payloads = self.get_extra_payloads(queryset, list_display)
        payload = self.get_default_payload(queryset, list_display, tpl_name='images')
        payloads.append(payload)
        return payloads

class PersonExportXls(Xls):
    desc = 'persons to xls'
    tpl = 'persons.xls'
    queryset_name = 'ps'
    obj_name = 'p'

    def get_payloads(self, queryset, list_display):
        payloads = self.get_extra_payloads(queryset, list_display)
        payload = self.get_default_payload(queryset, list_display, tpl_name='images')
        payloads.append(payload)
        return payloads

class PersonExportDocx(Docx):
    desc = 'persons to docx'
    tpl = 'persons.docx'
    queryset_name = 'ps'

    def get_payloads(self, queryset, list_display):
        payload = super().get_payloads(queryset, list_display)
        payload['test'] = 'A Big Company'
        payload['logo'] = 'staticfiles/1.jpg'
        return payload

class PersonaAdmin(ExportAdmin):
    list_display = ( 'name', 'address', 'int', 'bool', 'dec', 'float', 'time', 'date', 'datetime', 'image')
    export_actions = [PersonExportXlsx, PersonExportXls, PersonExportDocx]

admin.site.register(Persona, PersonaAdmin)
