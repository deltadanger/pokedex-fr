# -*- coding: utf-8 -*- 
# from app.models import Ability

def main(data, data_en):
    talents = []
    
    for row in data.split("\n"):
        row = row.split("\t")
        talent = {
            "name": row[0],
            "eng_name": row[1],
            "in_fight": row[2].replace("\"", "\\\"")
        }
        
        
        if len(row) > 3 and row[3] != "�":
            talent["out_fight"] = row[3].replace("\"", "\\\"")
        else:
            talent["out_fight"] = ""
        
        talents.append(talent)
    
    abilities_en = []
    for talent in talents:
        namefr = talent["name"].strip().replace("�", "e").replace("�", "e").replace("�", "e").replace("�", "E").replace("�", "U").replace("-", "_").replace(" ", "_").replace(".", "").upper()
        name = talent["eng_name"].strip().replace("-", "_").replace(" ", "_").replace(".", "").upper()
        
        # Abilities.java
        # print '    {0} (R.string.ability_name_{1}, R.string.ability_infight_{1}, R.string.ability_outfight_{1}),'.format(name, name.lower())
        
        # Database
#         Ability.objects.get_or_create(identifier=name.lower())
        
        # abilities.xml - fr
#         print "    <string name=\"ability_name_{}\">{}</string>".format(name.lower(), namefr)
#         print "    <string name=\"ability_infight_{}\">{}</string>".format(name.lower(), talent["in_fight"].replace("'", "\\'").strip())
#         print "    <string name=\"ability_outfight_{}\">{}</string>".format(name.lower(), talent["out_fight"].replace("'", "\\'").strip())
#         print ""
#         
        abilities_en.append(name.lower())
        
        # Ability name mapping
        
#         print '"' + namefr + '": "' + name.upper() + '",
        
    
    talents = []
    
    for row in data_en.split("\n"):
        row = row.split("    ")
        talent = {
            "name": row[1].strip().replace("-", "_").replace(" ", "_").replace(".", "").lower(),
            "eng_name": row[1].strip(),
            "in_fight": row[2].replace("\"", "\\\"").strip()
        }
        
        if talent["name"] in english_name_unused:
            continue
        
        name_used = english_name_mapping.get(talent["name"])
        if name_used:
            talent["name"] = name_used
        
        talents.append(talent)
    
    for talent in talents:
#         # abilities.xml - en
        print "    <string name=\"ability_name_{}\">{}</string>".format(talent["name"].lower(), talent["eng_name"])
        print "    <string name=\"ability_infight_{}\">{}</string>".format(talent["name"].lower(), talent["in_fight"].replace("'", "\\'"))
        print "    <string name=\"ability_outfight_{}\"></string>".format(talent["name"].lower())
        print ""

english_name_mapping = {
    "compound_eyes" : "compoundeye",
    "lightning_rod" : "lightningrod",
}

english_name_unused = [
    "delta_stream",
    "desolate_land",
    "primordial_sea",
]

data = """Absent�isme 	Truant 	Le Pok�mon n'attaque qu'un tour sur deux. 	�
Absorb Eau 	Water Absorb 	Les attaques de type eau re�ues par le Pok�mon r�g�n�rent 1/4 de ses PV. 	�
Absorb Volt 	Volt Absorb 	Les attaques de type �lectrique re�ues par le Pok�mon r�g�n�rent 1/4 de ses PV. 	�
Agitation 	Hustle 	Statistiques : Augmente l'attaque de 50% mais baisse la pr�cision de 20%. 	Augmente de 50% les chances de rencontrer un Pok�mon sauvage de haut niveau.�
Air Lock 	Air Lock 	Annule les effets du climat. 	�
Anti-Bruit 	Soundproof 	Annule les effets dus � une attaque sonore. 	�
Armumagma 	Magma Armor 	Immunise contre le gel. 	Divise par deux le nombre de pas n�cessaire � l'�closion d'un oeuf.�
Armurbaston 	Battle Armor 	Annule les chances de coups critiques du Pok�mon ennemi. 	�
Attention 	Inner Focus 	Immunise contre la peur. 	�
Ben�t 	Oblivious 	Immunise contre le charme. 	�
Boom Final 	Aftermath 	Enl�ve 1/4 de ses PV totaux au Pok�mon ennemi ass�nant un coup fatal. 	�
Brasier 	Blaze 	Augmente la puissance des attaques de type Feu de 50% lorsque le Pok�mon a moins d'1/3 de ses PV totaux. 	�
Cacophonie 	Cacophony 	Annule les effets dus � une attaque sonore. 	�
Calque 	Trace 	Copie le talent du Pok�mon adverse. 	�
Chanceux 	Super Luck 	Double les chance de porter un coup critique. 	�
Chlorophyle 	Chlorophyll 	Statistiques : Augmente la vitesse au soleil. 	�
Ciel Gris 	Cloud Nine 	Annule les effets du climat. 	�
Coloforce 	Huge Power 	Statistiques : Double l'attaque du Pok�mon. 	�
Coque Armure 	Shell Armor 	Annule les chances de coups critiques du Pok�mon ennemi. 	�
Corps Ardent 	Flame Body 	30% de chance de provoquer une br�lure sur le Pok�mon adverse ayant attaqu�. 	Divise par deux le nombre de pas n�cessaire � l'�closion d'un oeuf.�
Corps Sain 	Clear Body 	Statistiques : Emp�che la diminution de statistiques par le Pok�mon adverse. 	�
Crachin 	Drizzle 	Fait tomber la pluie tant que le Pok�mon est en jeu. 	�
Cran 	Guts 	Statistiques : Augmente de 50% l'attaque du Pok�mon s'il subit un changement de statut. 	�
Cuvette 	Rain Dish 	R�g�n�re 1/16�me des PV par temps de pluie. 	�
D�guisement 	Color Change 	Change le type du Pok�mon en celui de la derni�re attaque subie. 	�
�caille Sp�. 	Marvel Scale 	Statistiques : Augmente la d�fense de 50% lorsque le Pok�mon subit un changement de statut. 	�
�chauffement 	Limber 	Immunise contre la paralysie. 	�
�cran Fum�e 	White Smoke 	Emp�che la diminution de statistiques par le Pok�mon adverse. 	R�duit de 50% les chances d'�tre attaqu� par un Pok�mon sauvage.�
�cran Poudre 	Shield Dust 	Emp�che les effets secondaires des attaques subies. 	�
Engrais 	Overgrow 	Augmente la puissance des attaques de type Plante de 50% lorsque le Pok�mon a moins d'1/3 de ses PV totaux. 	�
Esprit Vital 	Vital Spirit 	Emp�che le Pok�mon d'�tre endormi. 	Augmente de 50% les chances de rencontrer un Pok�mon sauvage de haut niveau.�
Essaim 	Swarm 	Augmente la puissance des attaques de type Insecte de 50% lorsque le Pok�mon a moins d'1/3 de ses PV totaux. 	Augmente les chances d'entendre le cri d'un Pok�mon sauvage.�
Fermet� 	Sturdy 	Immunise contre les attaques OHKO.* 	�
Force Pure 	Pure Power 	Statistiques : Double l'attaque du Pok�mon. 	�
Fuite 	Run Away 	Assure la fuite contre les Pok�mon sauvages. 	�
Garde Mystik 	Wonder Guard 	Ne subit que les d�g�ts d'attaques super efficaces. 	�
Glissade 	Swift Swim 	Statistiques : Double la vitesse par temps de pluie. 	�
Glue 	Sticky Hold 	Emp�che la perte de l'objet tenu. 	Facilite la capture des Pok�mon p�ch�s.�
Hyper Cutter 	Hyper Cutter 	Statistiques : Emp�che la diminution d'attaque du Pok�mon. 	�
Ignifu-Voile 	Water Veil 	Immunise contre la br�lure. 	�
Insomnia 	Insomnia 	Emp�che le Pok�mon d'�tre endormi. 	�
Intimidation 	Intimidate 	Statistiques : Diminue d'un niveau l'attaque du Pok�mon adverse. 	R�duit de 50% les chances d'�tre attaqu� par un Pok�mon sauvage de bas niveau.�
Isograisse 	Thick Fat 	Les d�g�ts provoqu�s par les attaques des types Feu ou Glace sont divis�s par 2. 	�
Joli Sourire 	Cute Charm 	30% de chance de provoquer l'attirance du Pok�mon adverse ayant attaqu�. 	Augmente de 50% les chances d'�tre attaqu� par un Pok�mon sauvage du sexe oppos�.�
L�vitation 	Levitate 	Immunise contre les attaques de type Sol. 	�
Lumiattirance 	Illuminate 	� 	Augmente les chances de rencontrer des Pok�mon sauvages.RS
Magn�pi�ge 	Magnet Pull 	Emp�che la fuite et le changement des Pok�mon de type Acier. 	Augmente de 50% les chances de rencontrer un Pok�mon sauvage de type acier.�
Marque Ombre 	Shadow Tag 	Emp�che la fuite des Pok�mon sauvage et le changement du Pok�mon adverse. 	�
Matinal 	Early Bird 	R�duit le nombre de tours de sommeil du Pok�mon. 	�
M�dic Nature 	Natural Cure 	Le Pok�mon est soign� de toute alt�ration d'�tat lorsqu'il est chang� ou en fin de combat. 	�
M�t�o 	Forecast 	Change le type et la forme du Pok�mon selon le climat. 	�
Minus 	Minus 	Statistiques : Augmente l'attaque sp�ciale de 50% en match double, si le partenaire � le talent � Plus �. 	�
Moiteur 	Damp 	�mp�che l'utilisation d'attaques auto-destructrices par le Pok�mon adverse. 	�
Mue 	Shed Skin 	� chaque tour, le Pok�mon a 33% de chance d'�tre soign� d'une alt�ration d'�tat. 	�
Oeil Compos� 	Compoundeye 	Statistiques : Double la pr�cision du Pok�mon. 	Augmente les chances de rencontrer un Pok�mon sauvage tenant un objet.�
Paratonnerre 	Lightningrod 	Attire toutes les attaques de type �lectrique.* 	Augmente les chances de recevoir un appel sur le Pok�Nav.�
Peau Dure 	Rough Skin 	Fait perdre 1/16� des PV du Pok�mon adverse lors d'une attaque directe. 	�
Pi�ge 	Arena Trap 	Emp�che la fuite et le changement du Pok�mon adverse, s'il touche le sol. 	Augmente de 50% les chances d'�tre attaqu� par un Pok�mon sauvage.�
Plus 	Plus 	Statistiques : Augmente l'attaque sp�ciale de 50% en match double, si le partenaire � le talent � Minus �. 	�
Point Poison 	Poison Point 	30% de chance de provoquer l'empoisonnement du Pok�mon adverse ayant attaqu�. 	�
Pose Spore 	Effect Spore 	30% de chance de provoquer l'empoisonnement, le sommeil ou la paralysie du Pok�mon adverse ayant attaqu�. 	�
Pression 	Pressure 	Double l'utilisation de PP des attaques offensives du Pok�mon adverse. 	Augmente de 50% les chances d'�tre attaqu� par un Pok�mon sauvage.�
Puanteur 	Stench 	� 	Diminue les chances de rencontrer des Pok�mon sauvages.RS
Ramassage 	Pickup 	Donne une chance au Pok�mon de ramasser un objet apr�s un combat. 	�
Regard Vif 	Keen Eye 	Statistiques : Emp�che la perte de pr�cision. 	R�duit de 50% les chances d'�tre attaqu� par un Pok�mon sauvage de bas niveau.�
Sable Volant 	Sand Stream 	D�clenche une temp�te de sable tant que le Pok�mon est en jeu. 	�
S�cheresse 	Drought 	Cr�e un temps ensoleill� tant que le Pok�mon est en jeu. 	�
S�r�nit� 	Serene Grace 	Double les chances de r�ussite des effets secondaires des attaques. 	�
Statik 	Static 	30% de chance de provoquer la paralysie du Pok�mon adverse ayant attaqu�. 	Augmente de 50% les chances de rencontrer un Pok�mon sauvage de type �lectrique.�
Suintement 	Liquid Ooze 	Les attaques vampiriques du Pok�mon adverse lui font perdre des PV. 	�
Synchro 	Synchronize 	Toute alt�ration d'�tat subie est transmise au Pok�mon adverse. 	Augmente les chances de rencontrer un Pok�mon sauvage ayant la m�me nature.�
Tempo Perso 	Own Tempo 	Immunise contre la confusion. 	�
T�te de Roc 	Rock Head 	Le Pok�mon ne subit pas de d�g�ts de contrecoup. 	�
Torche 	Flash Fire 	Annule les d�g�ts des attaques de type Feu subies, et augmente de 50% la puissance des attaques de type Feu lanc�es. 	�
Torrent 	Torrent 	Augmente la puissance des attaques de type Eau de 50% lorsque le Pok�mon a moins d'1/3 de ses PV totaux. 	�
Turbo 	Speed Boost 	Statistiques : La vitesse du Pok�mon augmente � chaque tour. 	�
Vaccin 	Immunity 	Immunise contre l'empoisonnement. 	�
Ventouse 	Suction Cups 	Emp�che d'�tre chang� de force par une attaque adverse. 	Facilite la capture des Pok�mon p�ch�s.�
Voile Sable 	Sand Veil 	Statistiques : Augmente l'esquive de 20% lors d'une temp�te de sable, et immunise contre les d�g�ts de la temp�te de sable. 	R�duit de 50% les chances d'�tre attaqu� par un Pok�mon sauvage lors d'une temp�te de sable.�
Adaptabilit� 	Adaptability 	STAB : Si ce Pok�mon utilise une attaque de son type, la puissance de l'attaque est multipli�e par 2 au lieu de 1.5. 	�
Alerte Neige 	Snow Warning 	Le Pok�mon d�clenche une gr�le lorsqu'il est envoy� au combat. 	�
Annule Garde 	No Guard 	Toutes les attaques du Pok�mon et de son adversaire ont une pr�cision de 100%. 	Augmente les chances de rencontrer un Pok�mon sauvage.
Anticipation 	Anticipation 	Alerte et prot�ge lorsque le Pok�mon adverse poss�de certaines attaques. 	�
Brise Moule 	Mold Breaker 	Peut toucher un Pok�mon adverse malgr� son talent. 	�
Cherche Miel 	Honey Gather 	� 	Le Pok�mon peut trouver du Miel apr�s un combat.
Col�rique 	Anger Point 	Statistiques : L'attaque du Pok�mon est fortement augment�e lorsqu'il subit un coup critique. 	�
Corps Gel 	Ice Body 	R�g�n�re 1/16�me des PV par temps de gr�le. Immunise les Pok�mon n'ayant pas le type glace contre la gr�le. 	�
D�but Calme 	Slow Start 	Statistiques : Divise par deux l'attaque et la vitesse du Pok�mon pendant 5 tours. 	�
D�lestage 	Unburden 	Statistiques : Augmente la vitesse lorsqu'un objet tenu est utilis�, lanc� ou perdu. 	�
Don Floral 	Flower Gift 	Statistiques : Augmente l'attaque et la d�fense sp�ciale de 50% par temps ensoleill�. 	�
Feuil. Garde 	Leaf Guard 	Soigne les alt�rations d'�tat par temps ensoleill�. 	�
Filtre 	Filter 	Retire 1/4 des d�g�ts subits lors d'une attaque super efficace. 	�
Force Soleil 	Solar Power 	Statistiques : Augmente l'attaque sp�ciale de 50% par temps ensoleill�, mais diminue les PV de 1/8�me par tour. 	�
Fouille 	Frisk 	Permet de connaitre l'objet tenu d'un Pok�mon adverse. 	�
Frein 	Stall 	Le Pok�mon attaque toujours en second pour deux attaques de m�me priorit�. 	�
Garde Magik 	Magic Guard 	Le Pok�mon ne subit de d�g�ts que lors d'attaques directes. 	�
Gloutonnerie 	Gluttony 	Le Pok�mon utilise la baie port�e lorsque les PV descendent en dessous de 50%. 	�
Hydratation 	Hydration 	Soigne les alt�rations d'�tat par temps de pluie. 	�
Ignifuge 	Heatproof 	Divise par 2 les d�g�ts des attaques de type feu et les effets de br�lure subis par le Pok�mon. 	�
Impassible 	Steadfast 	Statistiques : Augmente d'un niveau la vitesse du Pok�mon lorsqu'il est apeur�. 	�
Inconscient 	Unaware 	Ignore les am�liorations de statistiques du Pok�mon adverse, � l'exception de sa Vitesse. 	�
Lavabo 	Storm Drain 	Attire toutes les attaques de type eau.* 	�
Lentiteint�e 	Tinted Lens 	Double les d�g�ts des attaques peu efficaces port�es au Pok�mon adverse. 	�
Maladresse 	Klutz 	Emp�che l'utilisation et/ou ignore l'effet des objets tenus en combat. 	�
Mauvais R�ve 	Bad Dreams 	Fait perdre 1/8�me de ses PV au Pok�mon adverse s'il est endormi. 	�
Motoris� 	Motor Drive 	Immunise le Pok�mon contre les attaques de type �lectrique. Augmente la vitesse du Pok�mon d'un niveau par attaque �lectrique subie. 	�
Multi-Coups 	Skill Link 	Utilise toujours le nombre de coups maximum d'une attaque. 	�
Multitype 	Multitype 	Le type et la forme du Pok�mon changent en fonction de la plaque qu'il porte. 	�
Normalise 	Normalize 	Toutes les attaques du Pok�mon sont consid�r�es comme �tant de type Normal. 	�
Peau S�che 	Dry Skin 	Les attaques de type eau soignent le Pok�mon, qui regagne 1/4 de ses PV totaux. Par temps de pluie, il gagne 1/8�me de ses PV par tour. Les attaques de type feu infligent 25% de d�g�ts en plus. Par temps ensoleill�, il perd 1/8�me de ses PV par tour. 	�
Pied Confus 	Tangled Feet 	Statistiques : Augmente l'esquive de 20% lorsque le Pok�mon est confus. 	�
Pied V�loce 	Quick Feet 	Statistiques : Augmente la vitesse de 50% lorsque le Pok�mon subit une alt�ration d'�tat. 	�
Poing de Fer 	Iron Fist 	Augmente de 20% la puissance des attaques de "Poing". 	�
Pr�diction 	Forewarn 	Alerte le Pok�mon de l'attaque la plus puissante du Pok�mon adverse. 	�
Querelleur 	Scrappy 	Permet de toucher les Pok�mon de type Spectre avec des attaques de type Normal ou Combat. 	�
Rideau Neige 	Snow Cloak 	Statistiques : Augmente l'esquive de 20% par temps de gr�le. Immunise les Pok�mon n'ayant pas le type glace contre la gr�le. 	�
Rivalit� 	Rivalry 	Statistiques : Augmente l'attaque et l'attaque sp�ciale de 25% si le Pok�mon adverse est de m�me sexe. Les diminue s'il est de sexe oppos�. 	�
Simple 	Simple 	Double les effets des modifications de statistiques, positives ou n�gatives. 	�
Sniper 	Sniper 	Triple la puissance des coups critiques. 	�
Soin Poison 	Poison Heal 	Le Pok�mon r�cup�re 1/8� de ses PV par tour lors d'un empoisonnement. 	Le Pok�mon empoisonn� perd tout de m�me ses PV lorsque son dresseur se d�place.*
Solide Roc 	Solid Rock 	Retire 1/4 des d�g�ts subits lors d'une attaque super efficace. 	�
Technicien 	Technician 	Augmente de 50% la puissance des attaques faibles (de puissance inf�rieure ou �gale � 60). 	�
T�l�charge 	Download 	Statistiques : Augmente l'attaque ou l'attaque sp�ciale du Pok�mon, selon la statistique de d�fense la plus faible du Pok�mon adverse. 	�
T�m�raire 	Reckless 	Augmente de 20% la puissance des attaques infligeant des d�g�ts de recul. 	�
Acharn� 	Defiant 	Statistiques : Monte l'Attaque du Pok�mon de deux niveau si l'une de ses statistiques est baiss�e par l'adversaire.
Analyste 	Analytic 	Si le Pok�mon frappe en dernier durant le tour, la puissance de son attaque est augment�e de 30%.
Armurouill�e 	Weak Armor 	Statistiques : Le Pok�mon touch� par une attaque physique voit sa d�fense diminuer d'un niveau et sa vitesse augmenter d'un niveau.
Baigne Sable 	Sand Rush 	Statistiques : Double la Vitesse du Pok�mon lors d'une temp�te de sable. Immunise contre les d�g�ts de la temp�te.
Coeur de Coq 	Big Pecks 	Emp�che la d�fense du Pok�mon d'�tre baiss�e par les attaques adverses.
Coeur Noble 	Justified 	Statistiques : Si le Pok�mon est touch� par une attaque de type t�n�bres, son attaque augmente d'un niveau.
Coeur Soin 	Healer 	� la fin de chaque tour, le Pok�mon a 30% de chance de gu�rir ses alli�s d'une alt�ration d'�tat en combat double ou triple.
Contestation 	Contrary 	Statistiques : Inverse les effets des attaques modifiant les statistiques.
Corps Maudit 	Cursed Body 	Toute attaque port�e par l'adversaire a 30% de chance de s'entraver.
D�faitiste 	Defeatist 	Statistiques : Divise par deux l'attaque et l'attaque sp�ciale du Pok�mon s'il a moins de la moiti� de ses PV totaux.
Envelocape 	Overcoat 	Immunise contre les d�g�ts caus�s par la gr�le et les temp�tes de sable.
�pine de Fer 	Iron Barbs 	Retire 1/8�me de ses PV � l'adversaire lorsque celui-ci porte une attaque physique.
Farceur 	Prankster 	Augmente la priorit� des attaques de statut d'un niveau.
Force Sable 	Sand Force 	Lors d'une temp�te de sable, la puissance des attaques de type acier, roche et sol augmente de 30 %.
Garde Amie 	Friend Guard 	R�duire de 25% les d�g�ts inflig�s aux alli�s en combat double ou triple.
Heavy Metal 	Heavy Metal 	Double la masse du Pok�mon.
Herbivore 	Sap Sipper 	Statistiques : Si le Pok�mon est touch� par une attaque de type plante, son attaque augmente d'un niveau.
Illusion 	Illusion 	Lorsqu'il entre en combat, le Pok�mon prend l'apparence du dernier Pok�mon de l'�quipe.
Imposteur 	Imposter 	Le Pok�mon entrant en combat prend automatiquement l'apparence du Pok�mon adverse.
Impudence 	Moxie 	Statistiques : Monte l'attaque du Pok�mon d'un niveau lorsqu'il met un adversaire K.O.
Infiltration 	Infiltrator 	Emp�che les attaques de protection adverses de fonctionner. (N'influe pas sur D�tection et Abri.)
Light Metal 	Light Metal 	Divise par deux la masse du Pok�mon.
Lunatique 	Moody 	Statistiques : Al�atoirement, � la fin de chaque tour, une statistique du Pok�mon augmente de deux niveaux, et une autre baisse d'un niveau (pr�cision et esquive comprises).
Miroir Magik 	Magic Bounce 	Retourne les attaques de statut contre l'adversaire.
Mode Transe 	Zen Mode 	Le Pok�mon change de forme et modifie la r�partition de ses statistiques lorsque ses PV sont inf�rieurs � 50%.
Momie 	Mummy 	Si le Pok�mon subit une attaque physique, le talent de l'adversaire devient "Momie". Ce talent est sans effet en elle-m�me.
Multi�caille 	Multiscale 	Si le Pok�mon poss�de 100% de ses PV, alors les d�g�ts inflig�s par l'adversaire sont divis�s par deux.
Peau Miracle 	Wonder Skin 	50% de chance de faire �chouer les attaques de statut port�es par l'adversaire.
Phobique 	Rattled 	Statistiques : Si le Pok�mon est touch� par une attaque de type insecte, spectre ou t�n�bres, sa vitesse augmente d'un niveau.
Pickpocket 	Pickpocket 	Si le Pok�mon subit une attaque physique, il r�cup�re l'objet tenu par son adversaire.
Rage Br�lure 	Flare Boost 	Statistiques : Augmente l'attaque sp�ciale du Pok�mon de 50% en cas de br�lure.
Rage Poison 	Toxic Boost 	Statistiques : Augmente l'attaque du Pok�mon de 50% en cas d'empoisonnement.
R�colte 	Harvest 	Une baie consomm�e par le Pok�mon a 50% de chances d'�tre r�cup�r�e � la fin de chaque tour.
R�g�-Force 	Regenerator 	Restaure 1/3 des PV totaux si le Pok�mon est retir� du combat.
Sans Limite 	Sheer Force 	Augmente de 30% la puissance des attaques pouvant avoir un effet secondaire. L'effet secondaire est annul�.
T�l�pathe 	Telepathy 	Anticipe et �vite les attaques des alli�s en combat double ou triple.
Tension 	Unnerve 	Emp�che l'adversaire de consommer sa baie.
T�ra-Voltage 	Teravolt 	Peut toucher un Pok�mon adverse malgr� son talent.
Toxitouche 	Poison Touch 	Peut empoisonner l'adversaire apr�s lui avoir port� une attaque physique.
TurboBrasier 	Turboblaze 	Peut toucher un Pok�mon adverse malgr� son talent.
Victorieux 	Victory Star 	Statistiques : Monte de 10% la pr�cision des alli�s en combat double ou triple.
Ailes Bourrasque 	Gale Wings 	Augmente la priorit� des capacit�s de type vol.
Amour Filial 	Parental Bond 	Permet au lanceur de porter deux coups par tour au lieu d'un.
Aroma-Voile 	Aroma Veil 	Prot�ge les Pok�mon alli�s des capacit�s qui ont un effet sur l'�tat mental.
Aura F��rique 	Fairy Aura 	Augmente la puissance des attaques de type f�e des Pok�mon pr�sents sur le terrain.
Aura Invers�e 	Aura Break 	Inverse les effets des talents Aura.
Aura T�n�breuse 	Dark Aura 	Augmente la puissance des attaques de type t�n�bres des Pok�mon pr�sents sur le terrain.
Bajoues 	Cheek Pouch 	Lorsque le Pok�mon mange une Baie, il obtient ses effets et regagne des PV en prime.
Battant 	Competitive 	Augmente l'Attaque Sp�ciale par deux niveaux lorsque n'importe quelle stat est baiss�e par un Pok�mon adverse.
D�clic Tactique 	Stance Change 	Change la forme du Pok�mon selon le combat.
Flora-Voile 	Flower Veil 	Emp�che la diminution des statistiques des alli�s de type plante par les Pok�mon adverses.
Gluco-Voile 	Sweet Veil 	Emp�che les Pok�mon alli�s de s'endormir.
Griffe Dure 	Tough Claws 	Augmente la puissance des attaques � base de griffe.
Magicien 	Magician 	Vole l'objet d'une cible apr�s l'avoir touch� avec une attaque directe.
M�ga Blaster 	Mega Launcher 	Un Pok�mon dot� de ce talent verra la puissance de ses capacit�s d'aura augment�e.
Pare-Balles 	Bulletproof 	Prot�ge contre les capacit�s balles et bombes, par exemple Balle Graine ou Canon Graine.
Peau C�leste 	Aerilate 	Transforme les capacit�s de type normal en type vol.
Peau F��rique 	Pixilate 	Transforme les capacit�s de type normal en type f�e.
Peau Gel�e 	Refrigerate 	Transforme les capacit�s de type normal en type glace.
Poisseux 	Gooey 	Baisse la Vitesse des Pok�mon qui touchent ce Pok�mon avec une attaque directe.
Prognathe 	Strong Jaw 	Augmente la puissance des attaques � base de morsures.
Prot�en 	Protean 	Change le type du Pok�mon en celui de toute capacit� qu'il utilise.
Symbiose 	Symbiosis 	Passe un objet tenu � un Pok�mon alli� lorsque l'alli� utilise son objet.
Toison �paisse 	Fur Coat 	Divise par deux les d�g�ts re�us lors d'une attaque physique.
Toison Herbue 	Grass Pelt 	Augmente la D�fense lorsque Champ Herbu est en vigueur."""

data_en = """091     Adaptability     Powers up moves of the same type.     IV     0     4     5
184     Aerilate     Normal-type moves become Flying-type moves.     VI     1     0     0
106     Aftermath     Damages the foe landing the finishing hit.     IV     0     4     4
076     Air Lock     Eliminates the effects of weather.     III     1     0     0
148     Analytic     Strengthens moves when moving last.     V     0     0     12
083     Anger Point     Raises Attack upon taking a critical hit.     IV     0     3     4
107     Anticipation     Senses the foe’s dangerous moves.     IV     1     4     2
071     Arena Trap     Prevents the foe from fleeing.     III     0     3     0
165     Aroma Veil     Protects allies from attacks that limit their move choices.     VI     0     0     2
188     Aura Break     The effects of "Aura" Abilities are reversed.     VI     1     0     0
123     Bad Dreams     Reduces a sleeping foe’s HP.     IV     1     0     0
004     Battle Armor     The Pokémon is protected against critical hits.     III     2     4     2
145     Big Pecks     Protects the Pokémon from Defense-lowering attacks.     V     0     8     4
066     Blaze     Powers up Fire-type moves in a pinch.     III     18     0     2
171     Bulletproof     Protects the Pokémon from some ball and bomb moves.     VI     0     0     3
—     Cacophony     Avoids sound-based moves.     III     0     0     0
167     Cheek Pouch     Restores HP as well when the Pokémon eats a Berry.     VI     0     3     0
034     Chlorophyll     Boosts the Pokémon’s Speed in sunshine.     III     10     19     6
029     Clear Body     Prevents the Pokémon’s stats from being lowered.     III     7     2     3
013     Cloud Nine     Eliminates the effects of weather.     III     0     2     4
016     Color Change     Changes the Pokémon’s type to the foe’s move.     III     1     0     0
172     Competitive     Boosts the Sp.Atk stat when a stat is lowered.     VI     0     7     1
014     Compound Eyes     The Pokémon’s accuracy is boosted.     III     2     6     1
126     Contrary     Inverts stat modifiers.     V     0     2     5
130     Cursed Body     Has a 30% chance of Disabling any move that hits the Pokémon.     V     0     2     3
056     Cute Charm     Contact with the Pokémon may cause infatuation.     III     1     12     1
006     Damp     Prevents combatants from self destructing.     III     0     8     10
186     Dark Aura     Powers up each Pokémon's Dark-type moves.     VI     1     0     0
129     Defeatist     Halves Attack and Special Attack below 50% HP.     V     2     0     0
128     Defiant     Raises Attack two stages upon having any stat lowered.     V     0     2     10
 ???     Delta Stream     Eliminates weather effects and eliminates weaknesses of Flying-type Pokémon.     VI     1     0     0
 ???     Desolate Land     Creates harsh sunlight.     VI     1     0     0
088     Download     Adjusts power according to the foe’s lowest defensive stat.     IV     1     3     0
002     Drizzle     The Pokémon makes it rain if it appears in battle.     III     1     0     1
070     Drought     The Pokémon makes it sunny if it is in battle.     III     2     0     2
087     Dry Skin     Reduces HP if it is hot. Water restores HP.     IV     0     6     1
048     Early Bird     The Pokémon awakens quickly from sleep.     III     0     13     2
027     Effect Spore     Contact may paralyze, poison, or cause sleep.     III     2     4     1
187     Fairy Aura     Powers up each Pokémon's Fairy-type moves.     VI     1     0     0
111     Filter     Powers down supereffective moves.     IV     1     2     0
049     Flame Body     Contact with the Pokémon may burn the foe.     III     9     5     4
138     Flare Boost     Increases Special Attack to 1.5× when burned.     V     0     0     2
018     Flash Fire     Powers up Fire-type moves if hit by a fire move.     III     4     10     4
122     Flower Gift     Powers up party Pokémon when it is sunny.     IV     1     0     0
166     Flower Veil     Prevents lowering of ally Grass-type Pokémon's stats.     VI     3     0     0
059     Forecast     Transforms with the weather.     III     1     0     0
108     Forewarn     Determines what moves the foe has.     IV     0     6     0
132     Friend Guard     Decreases damage inflicted against ally Pokémon.     V     0     0     8
119     Frisk     The Pokémon can check the foe’s held item.     IV     0     12     8
169     Fur Coat     Halves damage from physical moves.     VI     1     0     0
177     Gale Wings     Gives priority to Flying-type moves.     VI     0     0     3
082     Gluttony     Encourages the early use of a held Berry.     IV     6     4     9
183     Gooey     Contact with the Pokémon lowers the attacker's Speed stat.     VI     0     0     3
179     Grass Pelt     Boosts the Defense stat in Grassy Terrain.     VI     0     0     2
062     Guts     Boosts Attack if there is a status problem.     III     3     14     4
139     Harvest     Restores any held Berry after the turn on which it is used.     V     0     0     5
131     Healer     Has a 30% chance of curing each adjacent ally of any major status ailment after each turn.     V     2     2     3
085     Heatproof     Weakens the power of Fire-type moves.     IV     0     2     0
134     Heavy Metal     Doubles the Pokémon's weight.     V     0     0     5
118     Honey Gather     The Pokémon may gather Honey from somewhere.     IV     1     0     1
037     Huge Power     Raises the Pokémon’s Attack stat.     III     1     3     2
055     Hustle     Boosts the Attack stat, but lowers accuracy.     III     3     7     8
093     Hydration     Heals status problems if it is raining.     IV     2     10     9
052     Hyper Cutter     Prevents the Attack stat from being lowered.     III     0     9     0
115     Ice Body     The Pokémon regains HP in a hailstorm.     IV     3     7     4
035     Illuminate     Raises the likelihood of meeting wild Pokémon.     III     0     6     0
149     Illusion     Takes the appearance of the last conscious party Pokémon upon being sent out until hit by a damaging move.     V     2     0     0
017     Immunity     Prevents the Pokémon from getting poisoned.     III     1     1     1
150     Imposter     Transforms upon entering battle.     V     0     0     1
151     Infiltrator     Ignores Light Screen, Reflect, and Safeguard.     V     0     7     14
039     Inner Focus     The Pokémon is protected from flinching.     III     4     16     6
015     Insomnia     Prevents the Pokémon from falling asleep.     III     0     11     3
022     Intimidate     Lowers the foe’s Attack stat.     III     5     19     3
160     Iron Barbs     Damages attacking Pokémon for 1/8 their max HP on contact.     V     2     0     0
089     Iron Fist     Boosts the power of punching moves.     IV     0     5     7
154     Justified     Raises Attack when hit by Dark-type moves.     V     4     0     5
051     Keen Eye     Prevents the Pokémon from losing accuracy.     III     5     21     5
103     Klutz     The Pokémon can’t use any held items.     IV     0     6     1
102     Leaf Guard     Prevents status problems in sunny weather.     IV     1     6     7
026     Levitate     Gives full immunity to all Ground-type moves.     III     30     2     0
135     Light Metal     Halves the Pokémon's weight.     V     0     0     5
031     Lightning Rod     The Pokémon draws in all Electric-type moves.     III     0     9     5
007     Limber     The Pokémon is protected from paralysis.     III     1     7     2
064     Liquid Ooze     Inflicts damage on foes using any draining move.     III     0     4     0
156     Magic Bounce     Reflects most non-damaging moves back at their user.     V     1     0     3
098     Magic Guard     The Pokémon only takes damage from attacks.     IV     0     7     3
170     Magician     The Pokémon steals the held item of a Pokémon it hits with a move.     VI     0     0     4
040     Magma Armor     Prevents the Pokémon from becoming frozen.     III     0     3     0
042     Magnet Pull     Prevents Steel-type Pokémon from escaping.     III     0     5     0
063     Marvel Scale     Boosts Defense if there is a status problem.     III     1     0     2
178     Mega Launcher     Powers up aura and pulse moves.     VI     3     0     0
058     Minus     Boosts Sp. Atk if another Pokémon has Plus.     III     1     3     2
104     Mold Breaker     Moves can be used regardless of Abilities.     IV     4     6     8
141     Moody     Raises a random stat two stages and lowers another one stage after each turn.     V     0     0     7
078     Motor Drive     Raises Speed if hit by an Electric-type move.     IV     1     2     1
153     Moxie     Raises Attack one stage upon KOing a Pokémon.     V     0     5     8
136     Multiscale     Halves damage taken from full HP.     V     0     0     2
121     Multitype     Changes type to match the held Plate.     IV     1     0     0
152     Mummy     Contact with this Pokémon spreads this Ability.     V     2     0     0
030     Natural Cure     All status problems are healed upon switching out.     III     3     12     0
099     No Guard     Ensures the Pokémon and its foe’s attacks land.     IV     2     3     3
096     Normalize     All the Pokémon’s moves become the Normal type.     IV     0     2     0
012     Oblivious     Prevents the Pokémon from becoming infatuated.     III     0     16     3
142     Overcoat     Protects against damage from weather.     V     0     5     12
065     Overgrow     Powers up Grass-type moves in a pinch.     III     18     0     2
020     Own Tempo     Prevents the Pokémon from becoming confused.     III     0     15     5
185     Parental Bond     Parent and child attack together.     VI     1     0     0
124     Pickpocket     Steals attacking Pokémon's held item on contact.     V     0     0     7
053     Pickup     The Pokémon may pick up items.     III     1     14     0
182     Pixilate     Normal-type moves become Fairy-type moves.     VI     1     0     1
057     Plus     Boosts Sp. Atk if another Pokémon has Minus.     III     1     3     4
090     Poison Heal     Restores HP if the Pokémon is poisoned.     IV     0     2     1
038     Poison Point     Contact with the Pokémon may poison the foe.     III     0     16     0
143     Poison Touch     Has a 30% chance of poisoning Pokémon upon contact when attacking.     V     0     3     4
158     Prankster     Raises non-damaging moves' priority by one stage.     V     4     2     8
046     Pressure     The Pokémon raises the foe’s PP usage.     III     18     3     4
 ???     Primordial Sea     Causes heavy rain.     VI     1     0     0
168     Protean     Changes the Pokémon's type to the same type of the move it is using.     VI     0     0     4
074     Pure Power     Boosts the power of physical attacks.     III     3     0     0
095     Quick Feet     Boosts Speed if there is a status problem.     IV     0     5     4
044     Rain Dish     The Pokémon gradually recovers HP in rain.     III     0     3     8
155     Rattled     Raises Speed one stage upon being hit by a Dark, Ghost, or Bug move.     V     0     0     11
120     Reckless     Powers up moves that have recoil damage.     IV     0     3     8
174     Refrigerate     Normal-type moves become Ice-type moves.     VI     2     0     0
144     Regenerator     Heals for 1/3 max HP upon leaving battle.     V     0     3     14
079     Rivalry     Raises Attack if the foe is of the same gender.     IV     0     14     4
069     Rock Head     Protects the Pokémon from recoil damage.     III     2     16     5
024     Rough Skin     Inflicts damage to the foe on contact.     III     2     1     3
050     Run Away     Enables sure getaway from wild Pokémon.     III     0     16     8
159     Sand Force     Strengthens Rock, Ground, and Steel moves to 1.3× their power during a sandstorm.     V     1     2     11
146     Sand Rush     Doubles Speed during a sandstorm.     V     0     4     2
045     Sand Stream     The Pokémon summons a sandstorm in battle.     III     3     0     0
008     Sand Veil     Boosts the Pokémon’s evasion in a sandstorm.     III     7     6     7
157     Sap Sipper     Absorbs Grass moves, raising Attack one stage.     V     2     6     8
113     Scrappy     Enables moves to hit Ghost-type foes.     IV     0     2     8
032     Serene Grace     Boosts the likelihood of added effects appearing.     III     2     8     2
023     Shadow Tag     Prevents the foe from escaping.     III     2     0     3
061     Shed Skin     The Pokémon may heal its own status problems.     III     11     5     0
125     Sheer Force     Strengthens moves with extra effects to 1.3× their power, but prevents their extra effects.     V     1     6     17
075     Shell Armor     The Pokémon is protected against critical hits.     III     1     13     7
019     Shield Dust     Blocks the added effects of attacks taken.     III     4     3     0
086     Simple     The Pokémon is prone to wild stat changes.     IV     0     3     2
092     Skill Link     Increases the frequency of multi-strike moves.     IV     0     2     4
112     Slow Start     Temporarily halves Attack and Speed.     IV     1     0     0
097     Sniper     Powers up moves if they become critical hits.     IV     0     9     5
081     Snow Cloak     Raises evasion in a hailstorm.     IV     4     3     1
117     Snow Warning     The Pokémon summons a hailstorm in battle.     IV     3     0     2
094     Solar Power     Boosts Sp. Atk, but lowers HP in sunshine.     IV     0     3     5
116     Solid Rock     Powers down supereffective moves.     IV     0     4     0
043     Soundproof     Gives full immunity to all sound-based moves.     III     3     6     3
003     Speed Boost     The Pokémon’s Speed stat is gradually boosted.     III     1     2     8
100     Stall     The Pokémon moves after even slower foes.     IV     0     1     0
176     Stance Change     The Pokémon changes form depending on how it battles.     VI     1     0     0
009     Static     Contact with the Pokémon may cause paralysis.     III     9     5     1
080     Steadfast     Raises Speed each time the Pokémon flinches.     IV     2     3     5
001     Stench     The stench may cause the target to flinch.     III     0     6     1
060     Sticky Hold     Protects the Pokémon from item theft.     III     0     8     0
114     Storm Drain     The Pokémon draws in all Water-type moves.     IV     0     4     3
173     Strong Jaw     The Pokémon's strong jaw gives it tremendous biting power.     VI     2     0     0
005     Sturdy     The Pokémon is protected against 1-hit KO attacks.     III     8     22     5
021     Suction Cups     Negates moves that force switching out.     III     2     3     0
105     Super Luck     Heightens the critical-hit ratios of moves.     IV     0     6     3
068     Swarm     Powers up Bug-type moves in a pinch.     III     4     16     4
175     Sweet Veil     Prevents itself and its allies from falling asleep.     VI     2     0     0
033     Swift Swim     Boosts the Pokémon’s Speed in rain.     III     8     20     10
180     Symbiosis     The Pokémon can pass an item to an ally.     VI     0     0     3
028     Synchronize     Passes on a burn, poison, or paralysis to the foe.     III     3     12     0
077     Tangled Feet     Raises evasion if the Pokémon is confused.     IV     0     5     2
101     Technician     Powers up the Pokémon’s weaker moves.     IV     0     9     5
140     Telepathy     Protects against damaging moves from friendly Pokémon.     V     0     2     14
164     Teravolt     Moves can be used regardless of Abilities.     V     2     0     0
047     Thick Fat     Raises resistance to Fire- and Ice-type moves.     III     0     16     5
110     Tinted Lens     Powers up “not very effective” moves.     IV     0     4     5
067     Torrent     Powers up Water-type moves in a pinch.     III     18     0     2
181     Tough Claws     Powers up moves that make direct contact.     VI     2     2     0
137     Toxic Boost     Increases Attack to 1.5× when poisoned.     V     0     0     1
036     Trace     The Pokémon copies a foe's Ability.     III     0     5     0
054     Truant     The Pokémon can't attack on consecutive turns.     III     2     0     1
163     Turboblaze     Moves can be used regardless of Abilities.     V     2     0     0
109     Unaware     Ignores any change in stats by the foe.     IV     0     4     3
084     Unburden     Raises Speed if a held item is used.     IV     0     5     7
127     Unnerve     Prevents opposing Pokémon from eating held Berries.     V     0     4     15
162     Victory Star     Raises moves' accuracy to 1.1× for friendly Pokémon.     V     1     0     0
072     Vital Spirit     Prevents the Pokémon from falling asleep.     III     1     4     7
010     Volt Absorb     Restores HP if hit by an Electric-type move.     III     1     2     2
011     Water Absorb     Restores HP if hit by a Water-type move.     III     1     12     8
041     Water Veil     Prevents the Pokémon from getting a burn.     III     0     4     7
133     Weak Armor     Raises Speed and lowers Defense by one stage each upon being hit by any move.     V     0     1     15
073     White Smoke     Prevents the Pokémon’s stats from being lowered.     III     1     0     1
025     Wonder Guard     Only supereffective moves will hit.     III     1     0     0
147     Wonder Skin     Has a 50% chance of protecting against non-damaging moves that inflict major status ailments.     V     0     1     3
161     Zen Mode     Changes the Pokémon's shape when HP is halved.     V     0     0     1 """
main(data, data_en)
