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
    name = models.CharField(max_length=100) # Resource id
    image = models.CharField(max_length=100) # Resource id
    
    def __repr__(self):
        return self.name

class Ability(BaseModel):
    name = models.CharField(max_length=100) # Resource id
    in_fight_description = models.CharField(max_length=100, null=True) # Resource id
    out_fight_description = models.CharField(max_length=100, null=True) # Resource id
    
    def __repr__(self):
        return self.name

class EVBonus(BaseModel, AttributeValues):
    pass

class EggGroup(BaseModel):
    name = models.CharField(max_length=100) # Resource id
    
    def __repr__(self):
        return self.name

class Pokemon(BaseModel, AttributeValues):
    name = models.CharField(max_length=100) # Contains resource id like name_0150MX
    number = models.IntegerField()
    type1 = models.ForeignKey(PokemonType, related_name="type1")
    type2 = models.ForeignKey(PokemonType, related_name="type2", null=True)
    abilities = models.ManyToManyField(Ability)
    
    ancestor = models.ForeignKey("Pokemon", null=True)
    evolution_path = models.CharField(max_length=100, null=True) # Contains resource id like evolution_path_0150MX 

    size = models.FloatField()
    weight = models.FloatField()
    ev = models.ForeignKey(EVBonus)
    catchRate = models.IntegerField()
    gender = models.FloatField()
    hatch = models.IntegerField()
    eggGroup = models.ManyToManyField(EggGroup)
    
    def __repr__(self):
        type1 = self.type1 if hasattr(self, "type1") else "None"
        type2 = self.type2 if hasattr(self, "type1") else "None"
        eggGroups = self.eggGroups.all().values_list("name", flat=True) if hasattr(self, "type1") else []
        ancestor = self.ancestor if hasattr(self, "type1") else "None"
        abilities = self.abilities.all().values_list("name", flat=True) if hasattr(self, "type1") else []
        
        return "{name} ({number}) [{type1},{type2}] [Attrs: {size},{weight},{cachRate},{gender},{hatch},{eggGroup}] [Stat: {life},{attack},{defense},{sp_attack},{sp_defense},{speed}] [Evo: {ancestor} ({path})] [Abilities: {abilities}]".format(
            name=self.name,
            number=self.number,
            type1=type1,
            type2=type2,
            size=self.size,
            weight=self.weight,
            cachRate=self.catchRate,
            gender=self.gender,
            hatch=self.hatch,
            eggGroup=eggGroups,
            life=self.life,
            attack=self.attack,
            defense=self.defense,
            sp_attack=self.sp_attack,
            sp_defense=self.sp_defense,
            speed=self.speed,
            ancestor=ancestor,
            path=self.evolution_path,
            abilities=abilities
        )
    

