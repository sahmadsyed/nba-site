# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Player.last_name'
        db.delete_column(u'app1_player', 'last_name')

        # Deleting field 'Player.first_name'
        db.delete_column(u'app1_player', 'first_name')

        # Adding field 'Player.name'
        db.add_column(u'app1_player', 'name',
                      self.gf('django.db.models.fields.CharField')(default='DEFAULT', max_length=50),
                      keep_default=False)

        # Deleting field 'Statistics.first_name'
        db.delete_column(u'app1_statistics', 'first_name')

        # Deleting field 'Statistics.last_name'
        db.delete_column(u'app1_statistics', 'last_name')

        # Adding field 'Statistics.name'
        db.add_column(u'app1_statistics', 'name',
                      self.gf('django.db.models.fields.CharField')(default='DEFAULT', max_length=50),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'Player.last_name'
        db.add_column(u'app1_player', 'last_name',
                      self.gf('django.db.models.fields.CharField')(default='DEFAULT', max_length=50),
                      keep_default=False)

        # Adding field 'Player.first_name'
        db.add_column(u'app1_player', 'first_name',
                      self.gf('django.db.models.fields.CharField')(default='DEFAULT', max_length=50),
                      keep_default=False)

        # Deleting field 'Player.name'
        db.delete_column(u'app1_player', 'name')

        # Adding field 'Statistics.first_name'
        db.add_column(u'app1_statistics', 'first_name',
                      self.gf('django.db.models.fields.CharField')(default='DEFAULT', max_length=50),
                      keep_default=False)

        # Adding field 'Statistics.last_name'
        db.add_column(u'app1_statistics', 'last_name',
                      self.gf('django.db.models.fields.CharField')(default='DEFAULT', max_length=50),
                      keep_default=False)

        # Deleting field 'Statistics.name'
        db.delete_column(u'app1_statistics', 'name')


    models = {
        u'app1.player': {
            'Meta': {'object_name': 'Player'},
            'draft_year': ('django.db.models.fields.IntegerField', [], {'default': '-1'}),
            'height': ('django.db.models.fields.CharField', [], {'default': "'DEFAULT'", 'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'name': ('django.db.models.fields.CharField', [], {'default': "'DEFAULT'", 'max_length': '50'}),
            'position': ('django.db.models.fields.CharField', [], {'default': "'DEFAULT'", 'max_length': '50'}),
            'weight': ('django.db.models.fields.CharField', [], {'default': "'DEFAULT'", 'max_length': '50'})
        },
        u'app1.statistics': {
            'Meta': {'object_name': 'Statistics'},
            'apg': ('django.db.models.fields.FloatField', [], {'default': '-1'}),
            'bpg': ('django.db.models.fields.FloatField', [], {'default': '-1'}),
            'fg': ('django.db.models.fields.FloatField', [], {'default': '-1'}),
            'ft': ('django.db.models.fields.FloatField', [], {'default': '-1'}),
            'gp': ('django.db.models.fields.FloatField', [], {'default': '-1'}),
            'gs': ('django.db.models.fields.FloatField', [], {'default': '-1'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mpg': ('django.db.models.fields.FloatField', [], {'default': '-1'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "'DEFAULT'", 'max_length': '50'}),
            'ppg': ('django.db.models.fields.FloatField', [], {'default': '-1'}),
            'rpg': ('django.db.models.fields.FloatField', [], {'default': '-1'}),
            'season': ('django.db.models.fields.CharField', [], {'default': "'DEFAULT'", 'max_length': '50'}),
            'spg': ('django.db.models.fields.FloatField', [], {'default': '-1'}),
            'team': ('django.db.models.fields.CharField', [], {'default': "'DEFAULT'", 'max_length': '50'}),
            'tfg': ('django.db.models.fields.FloatField', [], {'default': '-1'})
        }
    }

    complete_apps = ['app1']