from django.db import models


class AdvancedManager(models.Manager):
    """Contains advanced functions, but nothing related to StandardLookup tables, such as get_if_exist(**kwargs)"""
    
    def get_if_exist(self, **kwargs):
        """Returns the matching object if it uniquely exists, None otherwise"""
        try:
            return self.get(**kwargs)
        except (self.model.DoesNotExist, self.model.MultipleObjectsReturned) as e:
            print e
            return None
    


class BaseModel(models.Model):
    objects = AdvancedManager()
    
    class Meta:
        abstract = True


class AttributeValues(models.Model):
    life = models.IntegerField()
    attack = models.IntegerField()
    defense = models.IntegerField()
    sp_attack = models.IntegerField()
    sp_defense = models.IntegerField()
    speed = models.IntegerField()
    
    class Meta:
        abstract = True

class PokemonType(BaseModel):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class Weakness(BaseModel):
    base_type = models.ForeignKey(PokemonType, related_name="base_type")
    receiving_type = models.ForeignKey(PokemonType, related_name="receiving_type")
    weakness = models.CharField(max_length=50)
    
    def __str__(self):
        return str(self.base_type) + " " + self.weakness + " to " + str(self.receiving_type)

class Ability(BaseModel):
    # Identifier used to retrieve the resource idsResource id
    identifier = models.CharField(max_length=100)
    # Resource ids will be in the form "ability_name_<identifier>", "ability_infight_<identifier>", "ability_outfight_<identifier>"
    
    def __str__(self):
        return self.identifier

class EVBonus(BaseModel, AttributeValues):
    def __str__(self):
        return ",".join([str(self.life), str(self.attack), str(self.defense), str(self.sp_attack), str(self.sp_defense), str(self.speed)])

class EggGroup(BaseModel):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class Pokemon(BaseModel, AttributeValues):
    name = models.CharField(max_length=100)
    number = models.IntegerField()
    type1 = models.ForeignKey(PokemonType, related_name="type1")
    type2 = models.ForeignKey(PokemonType, related_name="type2", null=True)
    abilities = models.ManyToManyField(Ability)
    
    ancestor = models.ForeignKey("Pokemon", null=True)
    evolution_path = models.CharField(max_length=100, null=True)

    size = models.FloatField()
    weight = models.FloatField()
    ev = models.ForeignKey(EVBonus)
    catch_rate = models.IntegerField()
    gender = models.FloatField()
    hatch = models.IntegerField()
    egg_group = models.ManyToManyField(EggGroup)
    
    def __str__(self):
        type1 = "None"
        type2 = "None"
        ancestor = "None"
        
        if hasattr(self, "type1"): type1 = self.type1 
        if hasattr(self, "type1"): type2 = self.type2
        if hasattr(self, "ancestor") and self.ancestor: ancestor = self.ancestor.name
        abilities = self.abilities.all().values_list("identifier", flat=True)
        egg_group = self.egg_group.all().values_list("name", flat=True)
        
        return "{name} ({number}) [{type1},{type2}] [Attrs: {size},{weight},{catch_rate},{gender},{hatch},{egg_group}] [Stat: {life},{attack},{defense},{sp_attack},{sp_defense},{speed}] [EVs: {ev}] [Evo: {ancestor} ({path})] [Abilities: {abilities}]".format(
            name=self.name,
            number=self.number,
            type1=type1,
            type2=type2,
            size=self.size,
            weight=self.weight,
            catch_rate=self.catch_rate,
            gender=self.gender,
            hatch=self.hatch,
            egg_group=egg_group,
            life=self.life,
            attack=self.attack,
            defense=self.defense,
            sp_attack=self.sp_attack,
            sp_defense=self.sp_defense,
            speed=self.speed,
            ancestor=ancestor,
            path=self.evolution_path,
            ev=self.ev,
            abilities=abilities
        )
        
