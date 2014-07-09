# -*- coding: utf-8 -*- 

def main(data):
    data = data.split("\n")
    
    
    talents = []
    
    for row in data:
        row = row.split("\t")
        talent = {
            "name": row[0],
            "eng_name": row[1],
            "in_fight": row[2].replace("\"", "\\\"")
        }
        
        
        if len(row) > 3 and row[3] != "—":
            talent["out_fight"] = row[3].replace("\"", "\\\"")
        else:
            talent["out_fight"] = ""
        
        talents.append(talent)
    
    
    for talent in talents:
        namefr = talent["name"].strip().replace("é", "e").replace("ê", "e").replace("è", "e").replace("É", "E").replace("û", "U").replace("-", "_").replace(" ", "_").replace(".", "").upper()
        name = talent["eng_name"].strip().replace("-", "_").replace(" ", "_").replace(".", "").upper()
        # Abilities.java
        # print '    {0} (R.string.ability_name_{1}, R.string.ability_infight_{1}, R.string.ability_outfight_{1}),'.format(name, name.lower())
        
        # abilities.xml - fr
        print "    <string name=\"ability_name_{}\">{}</string>".format(name.lower(), talent["name"].strip())
        print "    <string name=\"ability_infight_{}\">{}</string>".format(name.lower(), talent["in_fight"].replace("'", "\\'").strip())
        print "    <string name=\"ability_outfight_{}\">{}</string>".format(name.lower(), talent["out_fight"].replace("'", "\\'").strip())
        print ""
        
    
data = """Absentéisme 	Truant 	Le Pokémon n'attaque qu'un tour sur deux. 	—
Absorb Eau 	Water Absorb 	Les attaques de type eau reçues par le Pokémon régénèrent 1/4 de ses PV. 	—
Absorb Volt 	Volt Absorb 	Les attaques de type électrique reçues par le Pokémon régénèrent 1/4 de ses PV. 	—
Agitation 	Hustle 	Statistiques : Augmente l'attaque de 50% mais baisse la précision de 20%. 	Augmente de 50% les chances de rencontrer un Pokémon sauvage de haut niveau.É
Air Lock 	Air Lock 	Annule les effets du climat. 	—
Anti-Bruit 	Soundproof 	Annule les effets dus à une attaque sonore. 	—
Armumagma 	Magma Armor 	Immunise contre le gel. 	Divise par deux le nombre de pas nécessaire à l'éclosion d'un oeuf.É
Armurbaston 	Battle Armor 	Annule les chances de coups critiques du Pokémon ennemi. 	—
Attention 	Inner Focus 	Immunise contre la peur. 	—
Benêt 	Oblivious 	Immunise contre le charme. 	—
Boom Final 	Aftermath 	Enlève 1/4 de ses PV totaux au Pokémon ennemi assénant un coup fatal. 	—
Brasier 	Blaze 	Augmente la puissance des attaques de type Feu de 50% lorsque le Pokémon a moins d'1/3 de ses PV totaux. 	—
Cacophonie 	Cacophony 	Annule les effets dus à une attaque sonore. 	—
Calque 	Trace 	Copie le talent du Pokémon adverse. 	—
Chanceux 	Super Luck 	Double les chance de porter un coup critique. 	—
Chlorophyle 	Chlorophyll 	Statistiques : Augmente la vitesse au soleil. 	—
Ciel Gris 	Cloud Nine 	Annule les effets du climat. 	—
Coloforce 	Huge Power 	Statistiques : Double l'attaque du Pokémon. 	—
Coque Armure 	Shell Armor 	Annule les chances de coups critiques du Pokémon ennemi. 	—
Corps Ardent 	Flame Body 	30% de chance de provoquer une brûlure sur le Pokémon adverse ayant attaqué. 	Divise par deux le nombre de pas nécessaire à l'éclosion d'un oeuf.É
Corps Sain 	Clear Body 	Statistiques : Empêche la diminution de statistiques par le Pokémon adverse. 	—
Crachin 	Drizzle 	Fait tomber la pluie tant que le Pokémon est en jeu. 	—
Cran 	Guts 	Statistiques : Augmente de 50% l'attaque du Pokémon s'il subit un changement de statut. 	—
Cuvette 	Rain Dish 	Régénère 1/16ème des PV par temps de pluie. 	—
Déguisement 	Color Change 	Change le type du Pokémon en celui de la dernière attaque subie. 	—
Écaille Spé. 	Marvel Scale 	Statistiques : Augmente la défense de 50% lorsque le Pokémon subit un changement de statut. 	—
Échauffement 	Limber 	Immunise contre la paralysie. 	—
Écran Fumée 	White Smoke 	Empêche la diminution de statistiques par le Pokémon adverse. 	Réduit de 50% les chances d'être attaqué par un Pokémon sauvage.É
Écran Poudre 	Shield Dust 	Empêche les effets secondaires des attaques subies. 	—
Engrais 	Overgrow 	Augmente la puissance des attaques de type Plante de 50% lorsque le Pokémon a moins d'1/3 de ses PV totaux. 	—
Esprit Vital 	Vital Spirit 	Empêche le Pokémon d'être endormi. 	Augmente de 50% les chances de rencontrer un Pokémon sauvage de haut niveau.É
Essaim 	Swarm 	Augmente la puissance des attaques de type Insecte de 50% lorsque le Pokémon a moins d'1/3 de ses PV totaux. 	Augmente les chances d'entendre le cri d'un Pokémon sauvage.É
Fermeté 	Sturdy 	Immunise contre les attaques OHKO.* 	—
Force Pure 	Pure Power 	Statistiques : Double l'attaque du Pokémon. 	—
Fuite 	Run Away 	Assure la fuite contre les Pokémon sauvages. 	—
Garde Mystik 	Wonder Guard 	Ne subit que les dégâts d'attaques super efficaces. 	—
Glissade 	Swift Swim 	Statistiques : Double la vitesse par temps de pluie. 	—
Glue 	Sticky Hold 	Empêche la perte de l'objet tenu. 	Facilite la capture des Pokémon pêchés.É
Hyper Cutter 	Hyper Cutter 	Statistiques : Empêche la diminution d'attaque du Pokémon. 	—
Ignifu-Voile 	Water Veil 	Immunise contre la brûlure. 	—
Insomnia 	Insomnia 	Empêche le Pokémon d'être endormi. 	—
Intimidation 	Intimidate 	Statistiques : Diminue d'un niveau l'attaque du Pokémon adverse. 	Réduit de 50% les chances d'être attaqué par un Pokémon sauvage de bas niveau.É
Isograisse 	Thick Fat 	Les dégâts provoqués par les attaques des types Feu ou Glace sont divisés par 2. 	—
Joli Sourire 	Cute Charm 	30% de chance de provoquer l'attirance du Pokémon adverse ayant attaqué. 	Augmente de 50% les chances d'être attaqué par un Pokémon sauvage du sexe opposé.É
Lévitation 	Levitate 	Immunise contre les attaques de type Sol. 	—
Lumiattirance 	Illuminate 	— 	Augmente les chances de rencontrer des Pokémon sauvages.RS
Magnépiège 	Magnet Pull 	Empêche la fuite et le changement des Pokémon de type Acier. 	Augmente de 50% les chances de rencontrer un Pokémon sauvage de type acier.É
Marque Ombre 	Shadow Tag 	Empêche la fuite des Pokémon sauvage et le changement du Pokémon adverse. 	—
Matinal 	Early Bird 	Réduit le nombre de tours de sommeil du Pokémon. 	—
Médic Nature 	Natural Cure 	Le Pokémon est soigné de toute altération d'état lorsqu'il est changé ou en fin de combat. 	—
Météo 	Forecast 	Change le type et la forme du Pokémon selon le climat. 	—
Minus 	Minus 	Statistiques : Augmente l'attaque spéciale de 50% en match double, si le partenaire à le talent « Plus ». 	—
Moiteur 	Damp 	Émpêche l'utilisation d'attaques auto-destructrices par le Pokémon adverse. 	—
Mue 	Shed Skin 	À chaque tour, le Pokémon a 33% de chance d'être soigné d'une altération d'état. 	—
Oeil Composé 	Compoundeye 	Statistiques : Double la précision du Pokémon. 	Augmente les chances de rencontrer un Pokémon sauvage tenant un objet.É
Paratonnerre 	Lightningrod 	Attire toutes les attaques de type électrique.* 	Augmente les chances de recevoir un appel sur le PokéNav.É
Peau Dure 	Rough Skin 	Fait perdre 1/16è des PV du Pokémon adverse lors d'une attaque directe. 	—
Piège 	Arena Trap 	Empêche la fuite et le changement du Pokémon adverse, s'il touche le sol. 	Augmente de 50% les chances d'être attaqué par un Pokémon sauvage.É
Plus 	Plus 	Statistiques : Augmente l'attaque spéciale de 50% en match double, si le partenaire à le talent « Minus ». 	—
Point Poison 	Poison Point 	30% de chance de provoquer l'empoisonnement du Pokémon adverse ayant attaqué. 	—
Pose Spore 	Effect Spore 	30% de chance de provoquer l'empoisonnement, le sommeil ou la paralysie du Pokémon adverse ayant attaqué. 	—
Pression 	Pressure 	Double l'utilisation de PP des attaques offensives du Pokémon adverse. 	Augmente de 50% les chances d'être attaqué par un Pokémon sauvage.É
Puanteur 	Stench 	— 	Diminue les chances de rencontrer des Pokémon sauvages.RS
Ramassage 	Pickup 	Donne une chance au Pokémon de ramasser un objet après un combat. 	—
Regard Vif 	Keen Eye 	Statistiques : Empêche la perte de précision. 	Réduit de 50% les chances d'être attaqué par un Pokémon sauvage de bas niveau.É
Sable Volant 	Sand Stream 	Déclenche une tempête de sable tant que le Pokémon est en jeu. 	—
Sécheresse 	Drought 	Crée un temps ensoleillé tant que le Pokémon est en jeu. 	—
Sérénité 	Serene Grace 	Double les chances de réussite des effets secondaires des attaques. 	—
Statik 	Static 	30% de chance de provoquer la paralysie du Pokémon adverse ayant attaqué. 	Augmente de 50% les chances de rencontrer un Pokémon sauvage de type électrique.É
Suintement 	Liquid Ooze 	Les attaques vampiriques du Pokémon adverse lui font perdre des PV. 	—
Synchro 	Synchronize 	Toute altération d'état subie est transmise au Pokémon adverse. 	Augmente les chances de rencontrer un Pokémon sauvage ayant la même nature.É
Tempo Perso 	Own Tempo 	Immunise contre la confusion. 	—
Tête de Roc 	Rock Head 	Le Pokémon ne subit pas de dégâts de contrecoup. 	—
Torche 	Flash Fire 	Annule les dégâts des attaques de type Feu subies, et augmente de 50% la puissance des attaques de type Feu lancées. 	—
Torrent 	Torrent 	Augmente la puissance des attaques de type Eau de 50% lorsque le Pokémon a moins d'1/3 de ses PV totaux. 	—
Turbo 	Speed Boost 	Statistiques : La vitesse du Pokémon augmente à chaque tour. 	—
Vaccin 	Immunity 	Immunise contre l'empoisonnement. 	—
Ventouse 	Suction Cups 	Empêche d'être changé de force par une attaque adverse. 	Facilite la capture des Pokémon pêchés.É
Voile Sable 	Sand Veil 	Statistiques : Augmente l'esquive de 20% lors d'une tempête de sable, et immunise contre les dégâts de la tempête de sable. 	Réduit de 50% les chances d'être attaqué par un Pokémon sauvage lors d'une tempête de sable.É
Adaptabilité 	Adaptability 	STAB : Si ce Pokémon utilise une attaque de son type, la puissance de l'attaque est multipliée par 2 au lieu de 1.5. 	—
Alerte Neige 	Snow Warning 	Le Pokémon déclenche une grêle lorsqu'il est envoyé au combat. 	—
Annule Garde 	No Guard 	Toutes les attaques du Pokémon et de son adversaire ont une précision de 100%. 	Augmente les chances de rencontrer un Pokémon sauvage.
Anticipation 	Anticipation 	Alerte et protège lorsque le Pokémon adverse possède certaines attaques. 	—
Brise Moule 	Mold Breaker 	Peut toucher un Pokémon adverse malgré son talent. 	—
Cherche Miel 	Honey Gather 	— 	Le Pokémon peut trouver du Miel après un combat.
Colérique 	Anger Point 	Statistiques : L'attaque du Pokémon est fortement augmentée lorsqu'il subit un coup critique. 	—
Corps Gel 	Ice Body 	Régénère 1/16ème des PV par temps de grêle. Immunise les Pokémon n'ayant pas le type glace contre la grêle. 	—
Début Calme 	Slow Start 	Statistiques : Divise par deux l'attaque et la vitesse du Pokémon pendant 5 tours. 	—
Délestage 	Unburden 	Statistiques : Augmente la vitesse lorsqu'un objet tenu est utilisé, lancé ou perdu. 	—
Don Floral 	Flower Gift 	Statistiques : Augmente l'attaque et la défense spéciale de 50% par temps ensoleillé. 	—
Feuil. Garde 	Leaf Guard 	Soigne les altérations d'état par temps ensoleillé. 	—
Filtre 	Filter 	Retire 1/4 des dégâts subits lors d'une attaque super efficace. 	—
Force Soleil 	Solar Power 	Statistiques : Augmente l'attaque spéciale de 50% par temps ensoleillé, mais diminue les PV de 1/8ème par tour. 	—
Fouille 	Frisk 	Permet de connaitre l'objet tenu d'un Pokémon adverse. 	—
Frein 	Stall 	Le Pokémon attaque toujours en second pour deux attaques de même priorité. 	—
Garde Magik 	Magic Guard 	Le Pokémon ne subit de dégâts que lors d'attaques directes. 	—
Gloutonnerie 	Gluttony 	Le Pokémon utilise la baie portée lorsque les PV descendent en dessous de 50%. 	—
Hydratation 	Hydration 	Soigne les altérations d'état par temps de pluie. 	—
Ignifuge 	Heatproof 	Divise par 2 les dégâts des attaques de type feu et les effets de brûlure subis par le Pokémon. 	—
Impassible 	Steadfast 	Statistiques : Augmente d'un niveau la vitesse du Pokémon lorsqu'il est apeuré. 	—
Inconscient 	Unaware 	Ignore les améliorations de statistiques du Pokémon adverse, à l'exception de sa Vitesse. 	—
Lavabo 	Storm Drain 	Attire toutes les attaques de type eau.* 	—
Lentiteintée 	Tinted Lens 	Double les dégâts des attaques peu efficaces portées au Pokémon adverse. 	—
Maladresse 	Klutz 	Empêche l'utilisation et/ou ignore l'effet des objets tenus en combat. 	—
Mauvais Rêve 	Bad Dreams 	Fait perdre 1/8ème de ses PV au Pokémon adverse s'il est endormi. 	—
Motorisé 	Motor Drive 	Immunise le Pokémon contre les attaques de type électrique. Augmente la vitesse du Pokémon d'un niveau par attaque électrique subie. 	—
Multi-Coups 	Skill Link 	Utilise toujours le nombre de coups maximum d'une attaque. 	—
Multitype 	Multitype 	Le type et la forme du Pokémon changent en fonction de la plaque qu'il porte. 	—
Normalise 	Normalize 	Toutes les attaques du Pokémon sont considérées comme étant de type Normal. 	—
Peau Sèche 	Dry Skin 	Les attaques de type eau soignent le Pokémon, qui regagne 1/4 de ses PV totaux. Par temps de pluie, il gagne 1/8ème de ses PV par tour. Les attaques de type feu infligent 25% de dégâts en plus. Par temps ensoleillé, il perd 1/8ème de ses PV par tour. 	—
Pied Confus 	Tangled Feet 	Statistiques : Augmente l'esquive de 20% lorsque le Pokémon est confus. 	—
Pied Véloce 	Quick Feet 	Statistiques : Augmente la vitesse de 50% lorsque le Pokémon subit une altération d'état. 	—
Poing de Fer 	Iron Fist 	Augmente de 20% la puissance des attaques de "Poing". 	—
Prédiction 	Forewarn 	Alerte le Pokémon de l'attaque la plus puissante du Pokémon adverse. 	—
Querelleur 	Scrappy 	Permet de toucher les Pokémon de type Spectre avec des attaques de type Normal ou Combat. 	—
Rideau Neige 	Snow Cloak 	Statistiques : Augmente l'esquive de 20% par temps de grêle. Immunise les Pokémon n'ayant pas le type glace contre la grêle. 	—
Rivalité 	Rivalry 	Statistiques : Augmente l'attaque et l'attaque spéciale de 25% si le Pokémon adverse est de même sexe. Les diminue s'il est de sexe opposé. 	—
Simple 	Simple 	Double les effets des modifications de statistiques, positives ou négatives. 	—
Sniper 	Sniper 	Triple la puissance des coups critiques. 	—
Soin Poison 	Poison Heal 	Le Pokémon récupère 1/8è de ses PV par tour lors d'un empoisonnement. 	Le Pokémon empoisonné perd tout de même ses PV lorsque son dresseur se déplace.*
Solide Roc 	Solid Rock 	Retire 1/4 des dégâts subits lors d'une attaque super efficace. 	—
Technicien 	Technician 	Augmente de 50% la puissance des attaques faibles (de puissance inférieure ou égale à 60). 	—
Télécharge 	Download 	Statistiques : Augmente l'attaque ou l'attaque spéciale du Pokémon, selon la statistique de défense la plus faible du Pokémon adverse. 	—
Téméraire 	Reckless 	Augmente de 20% la puissance des attaques infligeant des dégâts de recul. 	—
Acharné 	Defiant 	Statistiques : Monte l'Attaque du Pokémon de deux niveau si l'une de ses statistiques est baissée par l'adversaire.
Analyste 	Analytic 	Si le Pokémon frappe en dernier durant le tour, la puissance de son attaque est augmentée de 30%.
Armurouillée 	Weak Armor 	Statistiques : Le Pokémon touché par une attaque physique voit sa défense diminuer d'un niveau et sa vitesse augmenter d'un niveau.
Baigne Sable 	Sand Rush 	Statistiques : Double la Vitesse du Pokémon lors d'une tempête de sable. Immunise contre les dégâts de la tempête.
Coeur de Coq 	Big Pecks 	Empêche la défense du Pokémon d'être baissée par les attaques adverses.
Coeur Noble 	Justified 	Statistiques : Si le Pokémon est touché par une attaque de type ténèbres, son attaque augmente d'un niveau.
Coeur Soin 	Healer 	À la fin de chaque tour, le Pokémon a 30% de chance de guérir ses alliés d'une altération d'état en combat double ou triple.
Contestation 	Contrary 	Statistiques : Inverse les effets des attaques modifiant les statistiques.
Corps Maudit 	Cursed Body 	Toute attaque portée par l'adversaire a 30% de chance de s'entraver.
Défaitiste 	Defeatist 	Statistiques : Divise par deux l'attaque et l'attaque spéciale du Pokémon s'il a moins de la moitié de ses PV totaux.
Envelocape 	Overcoat 	Immunise contre les dégâts causés par la grêle et les tempêtes de sable.
Épine de Fer 	Iron Barbs 	Retire 1/8ème de ses PV à l'adversaire lorsque celui-ci porte une attaque physique.
Farceur 	Prankster 	Augmente la priorité des attaques de statut d'un niveau.
Force Sable 	Sand Force 	Lors d'une tempête de sable, la puissance des attaques de type acier, roche et sol augmente de 30 %.
Garde Amie 	Friend Guard 	Réduire de 25% les dégâts infligés aux alliés en combat double ou triple.
Heavy Metal 	Heavy Metal 	Double la masse du Pokémon.
Herbivore 	Sap Sipper 	Statistiques : Si le Pokémon est touché par une attaque de type plante, son attaque augmente d'un niveau.
Illusion 	Illusion 	Lorsqu'il entre en combat, le Pokémon prend l'apparence du dernier Pokémon de l'équipe.
Imposteur 	Imposter 	Le Pokémon entrant en combat prend automatiquement l'apparence du Pokémon adverse.
Impudence 	Moxie 	Statistiques : Monte l'attaque du Pokémon d'un niveau lorsqu'il met un adversaire K.O.
Infiltration 	Infiltrator 	Empêche les attaques de protection adverses de fonctionner. (N'influe pas sur Détection et Abri.)
Light Metal 	Light Metal 	Divise par deux la masse du Pokémon.
Lunatique 	Moody 	Statistiques : Aléatoirement, à la fin de chaque tour, une statistique du Pokémon augmente de deux niveaux, et une autre baisse d'un niveau (précision et esquive comprises).
Miroir Magik 	Magic Bounce 	Retourne les attaques de statut contre l'adversaire.
Mode Transe 	Zen Mode 	Le Pokémon change de forme et modifie la répartition de ses statistiques lorsque ses PV sont inférieurs à 50%.
Momie 	Mummy 	Si le Pokémon subit une attaque physique, le talent de l'adversaire devient "Momie". Ce talent est sans effet en elle-même.
Multiécaille 	Multiscale 	Si le Pokémon possède 100% de ses PV, alors les dégâts infligés par l'adversaire sont divisés par deux.
Peau Miracle 	Wonder Skin 	50% de chance de faire échouer les attaques de statut portées par l'adversaire.
Phobique 	Rattled 	Statistiques : Si le Pokémon est touché par une attaque de type insecte, spectre ou ténèbres, sa vitesse augmente d'un niveau.
Pickpocket 	Pickpocket 	Si le Pokémon subit une attaque physique, il récupère l'objet tenu par son adversaire.
Rage Brûlure 	Flare Boost 	Statistiques : Augmente l'attaque spéciale du Pokémon de 50% en cas de brûlure.
Rage Poison 	Toxic Boost 	Statistiques : Augmente l'attaque du Pokémon de 50% en cas d'empoisonnement.
Récolte 	Harvest 	Une baie consommée par le Pokémon a 50% de chances d'être récupérée à la fin de chaque tour.
Régé-Force 	Regenerator 	Restaure 1/3 des PV totaux si le Pokémon est retiré du combat.
Sans Limite 	Sheer Force 	Augmente de 30% la puissance des attaques pouvant avoir un effet secondaire. L'effet secondaire est annulé.
Télépathe 	Telepathy 	Anticipe et évite les attaques des alliés en combat double ou triple.
Tension 	Unnerve 	Empêche l'adversaire de consommer sa baie.
Téra-Voltage 	Teravolt 	Peut toucher un Pokémon adverse malgré son talent.
Toxitouche 	Poison Touch 	Peut empoisonner l'adversaire après lui avoir porté une attaque physique.
TurboBrasier 	Turboblaze 	Peut toucher un Pokémon adverse malgré son talent.
Victorieux 	Victory Star 	Statistiques : Monte de 10% la précision des alliés en combat double ou triple.
Ailes Bourrasque 	Gale Wings 	Augmente la priorité des capacités de type vol.
Amour Filial 	Parental Bond 	Permet au lanceur de porter deux coups par tour au lieu d'un.
Aroma-Voile 	Aroma Veil 	Protège les Pokémon alliés des capacités qui ont un effet sur l'état mental.
Aura Féérique 	Fairy Aura 	Augmente la puissance des attaques de type fée des Pokémon présents sur le terrain.
Aura Inversée 	Aura Break 	Inverse les effets des talents Aura.
Aura Ténébreuse 	Dark Aura 	Augmente la puissance des attaques de type ténèbres des Pokémon présents sur le terrain.
Bajoues 	Cheek Pouch 	Lorsque le Pokémon mange une Baie, il obtient ses effets et regagne des PV en prime.
Battant 	Competitive 	Augmente l'Attaque Spéciale par deux niveaux lorsque n'importe quelle stat est baissée par un Pokémon adverse.
Déclic Tactique 	Stance Change 	Change la forme du Pokémon selon le combat.
Flora-Voile 	Flower Veil 	Empêche la diminution des statistiques des alliés de type plante par les Pokémon adverses.
Gluco-Voile 	Sweet Veil 	Empêche les Pokémon alliés de s'endormir.
Griffe Dure 	Tough Claws 	Augmente la puissance des attaques à base de griffe.
Magicien 	Magician 	Vole l'objet d'une cible après l'avoir touché avec une attaque directe.
Méga Blaster 	Mega Launcher 	Un Pokémon doté de ce talent verra la puissance de ses capacités d'aura augmentée.
Pare-Balles 	Bulletproof 	Protège contre les capacités balles et bombes, par exemple Balle Graine ou Canon Graine.
Peau Céleste 	Aerilate 	Transforme les capacités de type normal en type vol.
Peau Féérique 	Pixilate 	Transforme les capacités de type normal en type fée.
Peau Gelée 	Refrigerate 	Transforme les capacités de type normal en type glace.
Poisseux 	Gooey 	Baisse la Vitesse des Pokémon qui touchent ce Pokémon avec une attaque directe.
Prognathe 	Strong Jaw 	Augmente la puissance des attaques à base de morsures.
Protéen 	Protean 	Change le type du Pokémon en celui de toute capacité qu'il utilise.
Symbiose 	Symbiosis 	Passe un objet tenu à un Pokémon allié lorsque l'allié utilise son objet.
Toison Épaisse 	Fur Coat 	Divise par deux les dégâts reçus lors d'une attaque physique.
Toison Herbue 	Grass Pelt 	Augmente la Défense lorsque Champ Herbu est en vigueur."""

main(data)
