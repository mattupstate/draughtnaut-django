# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'UserProfile'
        db.create_table('users_userprofile', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.OneToOneField')(related_name='profile', unique=True, to=orm['auth.User'])),
            ('favorite_beer', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['beer.Beer'], null=True)),
            ('favorite_venue', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['venues.Venue'], null=True)),
        ))
        db.send_create_signal('users', ['UserProfile'])


    def backwards(self, orm):
        
        # Deleting model 'UserProfile'
        db.delete_table('users_userprofile')


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
        'beer.beer': {
            'Meta': {'object_name': 'Beer'},
            'abv': ('django.db.models.fields.DecimalField', [], {'max_digits': '4', 'decimal_places': '2'}),
            'brewery': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'beer_brewed_here'", 'to': "orm['venues.Venue']"}),
            'contributed_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'contributed_beers'", 'null': 'True', 'to': "orm['auth.User']"}),
            'date_approved': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'retired': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'style': ('django.db.models.fields.related.ForeignKey', [], {'default': '0', 'related_name': "'beers'", 'null': 'True', 'blank': 'True', 'to': "orm['beer.BeerStyle']"})
        },
        'beer.beerstyle': {
            'Meta': {'object_name': 'BeerStyle'},
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['beer.BeerStyle']", 'null': 'True', 'blank': 'True'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'moderation.moderationflag': {
            'Meta': {'object_name': 'ModerationFlag'},
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'flagged_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'moderation_flags'", 'to': "orm['auth.User']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'object_id': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'reason': ('django.db.models.fields.TextField', [], {})
        },
        'users.userprofile': {
            'Meta': {'object_name': 'UserProfile'},
            'favorite_beer': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['beer.Beer']", 'null': 'True'}),
            'favorite_venue': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['venues.Venue']", 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'profile'", 'unique': 'True', 'to': "orm['auth.User']"})
        },
        'venues.venue': {
            'Meta': {'object_name': 'Venue'},
            'address1': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'address2': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'contributed_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'contributed_venues'", 'to': "orm['auth.User']"}),
            'country': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'date_approved': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lat': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '11', 'decimal_places': '8'}),
            'lon': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '11', 'decimal_places': '8'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'notes': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'post_code': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'venue_type': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'venues'", 'to': "orm['venues.VenueType']"}),
            'website': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'})
        },
        'venues.venuetype': {
            'Meta': {'object_name': 'VenueType'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['users']
