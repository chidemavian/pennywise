# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'tblbudget.income'
        db.delete_column(u'sysadmin_tblbudget', 'income_id')


    def backwards(self, orm):
        # Adding field 'tblbudget.income'
        db.add_column(u'sysadmin_tblbudget', 'income',
                      self.gf('django.db.models.fields.related.ForeignKey')(default='i', to=orm['sysadmin.tblincome']),
                      keep_default=False)


    models = {
        u'sysadmin.tblbudget': {
            'Meta': {'object_name': 'tblbudget'},
            'amount': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'datee': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'month': ('django.db.models.fields.CharField', [], {'max_length': '75'}),
            'timee': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'year': ('django.db.models.fields.CharField', [], {'max_length': '375'})
        },
        u'sysadmin.tblevents': {
            'Meta': {'object_name': 'tblevents'},
            'amount': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'budget': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sysadmin.tblbudget']"}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'month': ('django.db.models.fields.CharField', [], {'max_length': '75'})
        },
        u'sysadmin.tblincome': {
            'Meta': {'object_name': 'tblincome'},
            'amount': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'datee': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'month': ('django.db.models.fields.CharField', [], {'max_length': '75'}),
            'timee': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'year': ('django.db.models.fields.CharField', [], {'max_length': '375'})
        }
    }

    complete_apps = ['sysadmin']