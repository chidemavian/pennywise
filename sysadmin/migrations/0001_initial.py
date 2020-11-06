# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'tblincome'
        db.create_table(u'sysadmin_tblincome', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('year', self.gf('django.db.models.fields.CharField')(max_length=375)),
            ('month', self.gf('django.db.models.fields.CharField')(max_length=75)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=75, null=True, blank=True)),
            ('amount', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('datee', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('timee', self.gf('django.db.models.fields.CharField')(max_length=20)),
        ))
        db.send_create_signal(u'sysadmin', ['tblincome'])

        # Adding model 'tblbudget'
        db.create_table(u'sysadmin_tblbudget', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('income', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sysadmin.tblincome'])),
            ('month', self.gf('django.db.models.fields.CharField')(max_length=75)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=75, null=True, blank=True)),
            ('amount', self.gf('django.db.models.fields.CharField')(max_length=20)),
        ))
        db.send_create_signal(u'sysadmin', ['tblbudget'])

        # Adding model 'tblevents'
        db.create_table(u'sysadmin_tblevents', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('budget', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sysadmin.tblbudget'])),
            ('month', self.gf('django.db.models.fields.CharField')(max_length=75)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=75, null=True, blank=True)),
            ('amount', self.gf('django.db.models.fields.CharField')(max_length=20)),
        ))
        db.send_create_signal(u'sysadmin', ['tblevents'])


    def backwards(self, orm):
        # Deleting model 'tblincome'
        db.delete_table(u'sysadmin_tblincome')

        # Deleting model 'tblbudget'
        db.delete_table(u'sysadmin_tblbudget')

        # Deleting model 'tblevents'
        db.delete_table(u'sysadmin_tblevents')


    models = {
        u'sysadmin.tblbudget': {
            'Meta': {'object_name': 'tblbudget'},
            'amount': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'income': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sysadmin.tblincome']"}),
            'month': ('django.db.models.fields.CharField', [], {'max_length': '75'})
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