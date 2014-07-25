# -*- coding: utf-8 -*- 
from app.models import Ability

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
        
        
        if len(row) > 3 and row[3] != "�":
            talent["out_fight"] = row[3].replace("\"", "\\\"")
        else:
            talent["out_fight"] = ""
        
        talents.append(talent)
    
    
    for talent in talents:
        namefr = talent["name"].strip().replace("�", "e").replace("�", "e").replace("�", "e").replace("�", "E").replace("�", "U").replace("-", "_").replace(" ", "_").replace(".", "").upper()
        name = talent["eng_name"].strip().replace("-", "_").replace(" ", "_").replace(".", "").upper()
        
        # Abilities.java
        # print '    {0} (R.string.ability_name_{1}, R.string.ability_infight_{1}, R.string.ability_outfight_{1}),'.format(name, name.lower())
        
        # Database
        Ability.objects.get_or_create(name="ability_name_{}".format(name.lower()),
                                      in_fight_description="ability_infight_{}".format(talent["in_fight"].replace("'", "\\'").strip()),
                                      out_fight_description="ability_outfight_{}".format(talent["out_fight"].replace("'", "\\'").strip()))
        
        # abilities.xml - fr
#         print "    <string name=\"ability_name_{}\">{}</string>".format(name.lower(), namefr)
#         print "    <string name=\"ability_infight_{}\">{}</string>".format(name.lower(), talent["in_fight"].replace("'", "\\'").strip())
#         print "    <string name=\"ability_outfight_{}\">{}</string>".format(name.lower(), talent["out_fight"].replace("'", "\\'").strip())
#         print ""
        
        # Ability name mapping
        
        print '"' + namefr + '": "' + name.upper() + '",'
        
    
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

main(data)
