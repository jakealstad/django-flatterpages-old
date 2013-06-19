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
            ('template_content', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('flatterpages', ['PageTemplate'])

        # Adding model 'Page'
        db.create_table('flatterpages_page', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50)),
            ('meta_description', self.gf('django.db.models.fields.TextField')(max_length=155)),
            ('main_image', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('head_content', self.gf('django.db.models.fields.TextField')()),
            ('main_content', self.gf('django.db.models.fields.TextField')()),
            ('css', self.gf('django.db.models.fields.TextField')()),
            ('footer_content', self.gf('django.db.models.fields.TextField')()),
            ('comments', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('template', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['flatterpages.PageTemplate'])),
        ))
        db.send_create_signal('flatterpages', ['Page'])

        # Adding M2M table for field sites on 'Page'
        m2m_table_name = db.shorten_name('flatterpages_page_sites')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('page', models.ForeignKey(orm['flatterpages.page'], null=False)),
            ('site', models.ForeignKey(orm['sites.site'], null=False))
        ))
        db.create_unique(m2m_table_name, ['page_id', 'site_id'])

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

        # Deleting model 'Page'
        db.delete_table('flatterpages_page')

        # Removing M2M table for field sites on 'Page'
        db.delete_table(db.shorten_name('flatterpages_page_sites'))

        # Deleting model 'PageMedia'
        db.delete_table('flatterpages_pagemedia')


    models = {
        'flatterpages.page': {
            'Meta': {'object_name': 'Page'},
            'comments': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'css': ('django.db.models.fields.TextField', [], {}),
            'footer_content': ('django.db.models.fields.TextField', [], {}),
            'head_content': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'main_content': ('django.db.models.fields.TextField', [], {}),
            'main_image': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'meta_description': ('django.db.models.fields.TextField', [], {'max_length': '155'}),
            'sites': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['sites.Site']", 'symmetrical': 'False'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'template': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['flatterpages.PageTemplate']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'})
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
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'template_content': ('django.db.models.fields.TextField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'sites.site': {
            'Meta': {'ordering': "('domain',)", 'object_name': 'Site', 'db_table': "'django_site'"},
            'domain': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['flatterpages']