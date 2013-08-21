# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'PageTemplate'
        db.create_table('flatterpages_pagetemplate', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('main_content', self.gf('django.db.models.fields.TextField')()),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('last_updated_by', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
        ))
        db.send_create_signal('flatterpages', ['PageTemplate'])

        # Adding model 'Stylesheet'
        db.create_table('flatterpages_stylesheet', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('css', self.gf('django.db.models.fields.TextField')()),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('last_updated_by', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('path', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('flatterpages', ['Stylesheet'])

        # Adding model 'UserTemplate'
        db.create_table('flatterpages_usertemplate', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('css', self.gf('django.db.models.fields.TextField')()),
            ('main_content', self.gf('django.db.models.fields.TextField')()),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('global_css', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['flatterpages.Stylesheet'], null=True, blank=True)),
        ))
        db.send_create_signal('flatterpages', ['UserTemplate'])

        # Adding model 'Page'
        db.create_table('flatterpages_page', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('parent_page', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['flatterpages.Page'], null=True, blank=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('url', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('meta_description', self.gf('django.db.models.fields.TextField')(max_length=155)),
            ('main_image', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('head_content', self.gf('django.db.models.fields.TextField')()),
            ('main_content', self.gf('django.db.models.fields.TextField')()),
            ('css', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('footer_content', self.gf('django.db.models.fields.TextField')()),
            ('comments', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('page_template', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['flatterpages.PageTemplate'])),
            ('user_template', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['flatterpages.UserTemplate'], null=True, blank=True)),
            ('stylesheet', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['flatterpages.Stylesheet'], null=True, blank=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('last_updated_by', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
        ))
        db.send_create_signal('flatterpages', ['Page'])

        # Adding M2M table for field sites on 'Page'
        db.create_table('flatterpages_page_sites', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('page', models.ForeignKey(orm['flatterpages.page'], null=False)),
            ('site', models.ForeignKey(orm['sites.site'], null=False))
        ))
        db.create_unique('flatterpages_page_sites', ['page_id', 'site_id'])

        # Adding model 'PageMedia'
        db.create_table('flatterpages_pagemedia', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('media', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
            ('media_type', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('page', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['flatterpages.Page'])),
        ))
        db.send_create_signal('flatterpages', ['PageMedia'])

    def backwards(self, orm):
        # Deleting model 'PageTemplate'
        db.delete_table('flatterpages_pagetemplate')

        # Deleting model 'Stylesheet'
        db.delete_table('flatterpages_stylesheet')

        # Deleting model 'UserTemplate'
        db.delete_table('flatterpages_usertemplate')

        # Deleting model 'Page'
        db.delete_table('flatterpages_page')

        # Removing M2M table for field sites on 'Page'
        db.delete_table('flatterpages_page_sites')

        # Deleting model 'PageMedia'
        db.delete_table('flatterpages_pagemedia')

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
        'flatterpages.page': {
            'Meta': {'object_name': 'Page'},
            'comments': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'css': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'footer_content': ('django.db.models.fields.TextField', [], {}),
            'head_content': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_updated_by': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
            'main_content': ('django.db.models.fields.TextField', [], {}),
            'main_image': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'meta_description': ('django.db.models.fields.TextField', [], {'max_length': '155'}),
            'page_template': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['flatterpages.PageTemplate']"}),
            'parent_page': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['flatterpages.Page']", 'null': 'True', 'blank': 'True'}),
            'sites': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['sites.Site']", 'symmetrical': 'False'}),
            'stylesheet': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['flatterpages.Stylesheet']", 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'user_template': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['flatterpages.UserTemplate']", 'null': 'True', 'blank': 'True'})
        },
        'flatterpages.pagemedia': {
            'Meta': {'object_name': 'PageMedia'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'media': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'media_type': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'page': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['flatterpages.Page']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        },
        'flatterpages.pagetemplate': {
            'Meta': {'object_name': 'PageTemplate'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_updated_by': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
            'main_content': ('django.db.models.fields.TextField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        'flatterpages.stylesheet': {
            'Meta': {'object_name': 'Stylesheet'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'css': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_updated_by': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
            'path': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        'flatterpages.usertemplate': {
            'Meta': {'object_name': 'UserTemplate'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'css': ('django.db.models.fields.TextField', [], {}),
            'global_css': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['flatterpages.Stylesheet']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'main_content': ('django.db.models.fields.TextField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'sites.site': {
            'Meta': {'ordering': "('domain',)", 'object_name': 'Site', 'db_table': "'django_site'"},
            'domain': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['flatterpages']