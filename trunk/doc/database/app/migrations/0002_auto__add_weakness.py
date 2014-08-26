# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Weakness'
        db.create_table(u'app_weakness', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('base_type', self.gf('django.db.models.fields.related.ForeignKey')(related_name='base_type', to=orm['app.PokemonType'])),
            ('receiving_type', self.gf('django.db.models.fields.related.ForeignKey')(related_name='receiving_type', to=orm['app.PokemonType'])),
            ('weakness', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'app', ['Weakness'])

        # Deleting field 'PokemonType.image'
        db.delete_column(u'app_pokemontype', 'image')


    def backwards(self, orm):
        # Deleting model 'Weakness'
        db.delete_table(u'app_weakness')

        # Adding field 'PokemonType.image'
        db.add_column(u'app_pokemontype', 'image',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=100),
                      keep_default=False)


    models = {
        u'app.ability': {
            'Meta': {'object_name': 'Ability'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'identifier': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'app.egggroup': {
            'Meta': {'object_name': 'EggGroup'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'app.evbonus': {
            'Meta': {'object_name': 'EVBonus'},
            'attack': ('django.db.models.fields.IntegerField', [], {}),
            'defense': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'life': ('django.db.models.fields.IntegerField', [], {}),
            'sp_attack': ('django.db.models.fields.IntegerField', [], {}),
            'sp_defense': ('django.db.models.fields.IntegerField', [], {}),
            'speed': ('django.db.models.fields.IntegerField', [], {})
        },
        u'app.pokemon': {
            'Meta': {'object_name': 'Pokemon'},
            'abilities': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['app.Ability']", 'symmetrical': 'False'}),
            'ancestor': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['app.Pokemon']", 'null': 'True'}),
            'attack': ('django.db.models.fields.IntegerField', [], {}),
            'catch_rate': ('django.db.models.fields.IntegerField', [], {}),
            'defense': ('django.db.models.fields.IntegerField', [], {}),
            'egg_group': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['app.EggGroup']", 'symmetrical': 'False'}),
            'ev': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['app.EVBonus']"}),
            'evolution_path': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True'}),
            'gender': ('django.db.models.fields.FloatField', [], {}),
            'hatch': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'life': ('django.db.models.fields.IntegerField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'number': ('django.db.models.fields.IntegerField', [], {}),
            'size': ('django.db.models.fields.FloatField', [], {}),
            'sp_attack': ('django.db.models.fields.IntegerField', [], {}),
            'sp_defense': ('django.db.models.fields.IntegerField', [], {}),
            'speed': ('django.db.models.fields.IntegerField', [], {}),
            'type1': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'type1'", 'to': u"orm['app.PokemonType']"}),
            'type2': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'type2'", 'null': 'True', 'to': u"orm['app.PokemonType']"}),
            'weight': ('django.db.models.fields.FloatField', [], {})
        },
        u'app.pokemontype': {
            'Meta': {'object_name': 'PokemonType'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'app.weakness': {
            'Meta': {'object_name': 'Weakness'},
            'base_type': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'base_type'", 'to': u"orm['app.PokemonType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'receiving_type': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'receiving_type'", 'to': u"orm['app.PokemonType']"}),
            'weakness': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['app']