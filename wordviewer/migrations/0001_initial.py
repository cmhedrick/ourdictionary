# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'WordEntry'
        db.create_table('wordviewer_wordentry', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('part', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('definition', self.gf('django.db.models.fields.CharField')(max_length=140)),
            ('synonyms', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('example_sentence', self.gf('django.db.models.fields.CharField')(max_length=140, blank=True)),
            ('photo', self.gf('stdimage.fields.StdImageField')(blank=True, max_length=100, thumbnail_size={'width': 300, 'force': None, 'height': 225}, size={'width': 1024, 'force': None, 'height': 768})),
            ('caption', self.gf('django.db.models.fields.CharField')(max_length=140, blank=True)),
            ('user_creator', self.gf('django.db.models.fields.related.ForeignKey')(related_name='entry_creators', to=orm['auth.User'])),
            ('user_last_modified', self.gf('django.db.models.fields.related.ForeignKey')(related_name='entry_modifiers', to=orm['auth.User'])),
            ('date_created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('date_modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal('wordviewer', ['WordEntry'])

    def backwards(self, orm):
        # Deleting model 'WordEntry'
        db.delete_table('wordviewer_wordentry')

    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'wordviewer.wordentry': {
            'Meta': {'object_name': 'WordEntry'},
            'caption': ('django.db.models.fields.CharField', [], {'max_length': '140', 'blank': 'True'}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'definition': ('django.db.models.fields.CharField', [], {'max_length': '140'}),
            'example_sentence': ('django.db.models.fields.CharField', [], {'max_length': '140', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'part': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'photo': ('stdimage.fields.StdImageField', [], {'blank': 'True', 'max_length': '100', 'thumbnail_size': "{'width': 300, 'force': None, 'height': 225}", 'size': "{'width': 1024, 'force': None, 'height': 768}"}),
            'synonyms': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'user_creator': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'entry_creators'", 'to': "orm['auth.User']"}),
            'user_last_modified': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'entry_modifiers'", 'to': "orm['auth.User']"})
        }
    }

    complete_apps = ['wordviewer']