# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'PokemonType'
        db.create_table(u'app_pokemontype', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('image', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'app', ['PokemonType'])

        # Adding model 'Ability'
        db.create_table(u'app_ability', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('identifier', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'app', ['Ability'])

        # Adding model 'EVBonus'
        db.create_table(u'app_evbonus', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('life', self.gf('django.db.models.fields.IntegerField')()),
            ('attack', self.gf('django.db.models.fields.IntegerField')()),
            ('defense', self.gf('django.db.models.fields.IntegerField')()),
            ('sp_attack', self.gf('django.db.models.fields.IntegerField')()),
            ('sp_defense', self.gf('django.db.models.fields.IntegerField')()),
            ('speed', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'app', ['EVBonus'])

        # Adding model 'EggGroup'
        db.create_table(u'app_egggroup', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'app', ['EggGroup'])

        # Adding model 'Pokemon'
        db.create_table(u'app_pokemon', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('life', self.gf('django.db.models.fields.IntegerField')()),
            ('attack', self.gf('django.db.models.fields.IntegerField')()),
            ('defense', self.gf('django.db.models.fields.IntegerField')()),
            ('sp_attack', self.gf('django.db.models.fields.IntegerField')()),
            ('sp_defense', self.gf('django.db.models.fields.IntegerField')()),
            ('speed', self.gf('django.db.models.fields.IntegerField')()),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('number', self.gf('django.db.models.fields.IntegerField')()),
            ('type1', self.gf('django.db.models.fields.related.ForeignKey')(related_name='type1', to=orm['app.PokemonType'])),
            ('type2', self.gf('django.db.models.fields.related.ForeignKey')(related_name='type2', null=True, to=orm['app.PokemonType'])),
            ('ancestor', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['app.Pokemon'], null=True)),
            ('evolution_path', self.gf('django.db.models.fields.CharField')(max_length=100, null=True)),
            ('size', self.gf('django.db.models.fields.FloatField')()),
            ('weight', self.gf('django.db.models.fields.FloatField')()),
            ('ev', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['app.EVBonus'])),
            ('catch_rate', self.gf('django.db.models.fields.IntegerField')()),
            ('gender', self.gf('django.db.models.fields.FloatField')()),
            ('hatch', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'app', ['Pokemon'])

        # Adding M2M table for field abilities on 'Pokemon'
        db.create_table(u'app_pokemon_abilities', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('pokemon', models.ForeignKey(orm[u'app.pokemon'], null=False)),
            ('ability', models.ForeignKey(orm[u'app.ability'], null=False))
        ))
        db.create_unique(u'app_pokemon_abilities', ['pokemon_id', 'ability_id'])

        # Adding M2M table for field egg_group on 'Pokemon'
        db.create_table(u'app_pokemon_egg_group', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('pokemon', models.ForeignKey(orm[u'app.pokemon'], null=False)),
            ('egggroup', models.ForeignKey(orm[u'app.egggroup'], null=False))
        ))
        db.create_unique(u'app_pokemon_egg_group', ['pokemon_id', 'egggroup_id'])


    def backwards(self, orm):
        # Deleting model 'PokemonType'
        db.delete_table(u'app_pokemontype')

        # Deleting model 'Ability'
        db.delete_table(u'app_ability')

        # Deleting model 'EVBonus'
        db.delete_table(u'app_evbonus')

        # Deleting model 'EggGroup'
        db.delete_table(u'app_egggroup')

        # Deleting model 'Pokemon'
        db.delete_table(u'app_pokemon')

        # Removing M2M table for field abilities on 'Pokemon'
        db.delete_table('app_pokemon_abilities')

        # Removing M2M table for field egg_group on 'Pokemon'
        db.delete_table('app_pokemon_egg_group')


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
            'image': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['app']