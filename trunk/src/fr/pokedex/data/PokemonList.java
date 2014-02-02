package fr.pokedex.data;

import java.util.ArrayList;
import java.util.HashMap;

@SuppressWarnings("serial")
public class PokemonList {
	
	public static void setEvolutions() {
        PokemonList.perName.get("Rattatac").evolutions = new Pokemon[]{PokemonList.perName.get("Rattata"),PokemonList.perName.get("Rattatac")};
        PokemonList.perName.get("Porygon-Z").evolutions = new Pokemon[]{PokemonList.perName.get("Porygon"),PokemonList.perName.get("Porygon2"),PokemonList.perName.get("Porygon-Z")};
        PokemonList.perName.get("Baggiguane").evolutions = new Pokemon[]{PokemonList.perName.get("Baggiguane"),PokemonList.perName.get("Baggaid")};
        PokemonList.perName.get("Noadkoko").evolutions = new Pokemon[]{PokemonList.perName.get("Noeunoeuf"),PokemonList.perName.get("Noadkoko")};
        PokemonList.perName.get("Gueriaigle").evolutions = new Pokemon[]{PokemonList.perName.get("Furaiglon"),PokemonList.perName.get("Gueriaigle")};
        PokemonList.perName.get("Polichombr").evolutions = new Pokemon[]{PokemonList.perName.get("Polichombr"),PokemonList.perName.get("Branette"),PokemonList.perName.get("Mega-Branette")};
        PokemonList.perName.get("Gaulet").evolutions = new Pokemon[]{PokemonList.perName.get("Trompignon"),PokemonList.perName.get("Gaulet")};
        PokemonList.perName.get("Hyporoi").evolutions = new Pokemon[]{PokemonList.perName.get("Hypotrempe"),PokemonList.perName.get("Hypocean"),PokemonList.perName.get("Hyporoi")};
        PokemonList.perName.get("Elekable").evolutions = new Pokemon[]{PokemonList.perName.get("Elekid"),PokemonList.perName.get("Elektek"),PokemonList.perName.get("Elekable")};
        PokemonList.perName.get("Roussil").evolutions = new Pokemon[]{PokemonList.perName.get("Feunnec"),PokemonList.perName.get("Roussil"),PokemonList.perName.get("Goupelin")};
        PokemonList.perName.get("Pashmilla").evolutions = new Pokemon[]{PokemonList.perName.get("Chinchidou"),PokemonList.perName.get("Pashmilla")};
        PokemonList.perName.get("Emolga").evolutions = new Pokemon[]{};
        PokemonList.perName.get("Grolem").evolutions = new Pokemon[]{PokemonList.perName.get("Racaillou"),PokemonList.perName.get("Gravalanch"),PokemonList.perName.get("Grolem")};
        PokemonList.perName.get("Cresselia").evolutions = new Pokemon[]{};
        PokemonList.perName.get("Flotoutan").evolutions = new Pokemon[]{PokemonList.perName.get("Flotajou"),PokemonList.perName.get("Flotoutan")};
        PokemonList.perName.get("Bekipan").evolutions = new Pokemon[]{PokemonList.perName.get("Goelise"),PokemonList.perName.get("Bekipan")};
        PokemonList.perName.get("Mateloutre").evolutions = new Pokemon[]{PokemonList.perName.get("Moustillon"),PokemonList.perName.get("Mateloutre"),PokemonList.perName.get("Clamiral")};
        PokemonList.perName.get("Dinoclier").evolutions = new Pokemon[]{PokemonList.perName.get("Dinoclier"),PokemonList.perName.get("Bastiodon")};
        PokemonList.perName.get("Absol").evolutions = new Pokemon[]{PokemonList.perName.get("Absol"),PokemonList.perName.get("Mega-Absol")};
        PokemonList.perName.get("Azurill").evolutions = new Pokemon[]{PokemonList.perName.get("Azurill"),PokemonList.perName.get("Marill"),PokemonList.perName.get("Azumarill")};
        PokemonList.perName.get("Apireine").evolutions = new Pokemon[]{PokemonList.perName.get("Apitrini"),PokemonList.perName.get("Apireine")};
        PokemonList.perName.get("Dracaufeu").evolutions = new Pokemon[]{PokemonList.perName.get("Salameche"),PokemonList.perName.get("Reptincel"),PokemonList.perName.get("Dracaufeu"),PokemonList.perName.get("Mega-Dracaufeu X"),PokemonList.perName.get("Mega-Dracaufeu Y")};
        PokemonList.perName.get("Solochi").evolutions = new Pokemon[]{PokemonList.perName.get("Solochi"),PokemonList.perName.get("Diamat"),PokemonList.perName.get("Trioxhydre")};
        PokemonList.perName.get("Motisma (Forme Tonte)").evolutions = new Pokemon[]{};
        PokemonList.perName.get("Volcaropod").evolutions = new Pokemon[]{PokemonList.perName.get("Limagma"),PokemonList.perName.get("Volcaropod")};
        PokemonList.perName.get("Boreas (Forme Totemique)").evolutions = new Pokemon[]{};
        PokemonList.perName.get("Meloetta (Forme Voix)").evolutions = new Pokemon[]{};
        PokemonList.perName.get("Snubbull").evolutions = new Pokemon[]{PokemonList.perName.get("Snubbull"),PokemonList.perName.get("Granbull")};
        PokemonList.perName.get("Sharpedo").evolutions = new Pokemon[]{PokemonList.perName.get("Carvanha"),PokemonList.perName.get("Sharpedo")};
        PokemonList.perName.get("Motisma (Forme Froid)").evolutions = new Pokemon[]{};
        PokemonList.perName.get("Mega-Mewtwo Y").evolutions = new Pokemon[]{PokemonList.perName.get("Mewtwo"),PokemonList.perName.get("Mega-Mewtwo X"),PokemonList.perName.get("Mega-Mewtwo Y")};
        PokemonList.perName.get("Tutafeh").evolutions = new Pokemon[]{PokemonList.perName.get("Tutafeh"),PokemonList.perName.get("Tutankafer")};
        PokemonList.perName.get("Noctunoir").evolutions = new Pokemon[]{PokemonList.perName.get("Skelenox"),PokemonList.perName.get("Teraclope"),PokemonList.perName.get("Noctunoir")};
        PokemonList.perName.get("Melodelfe").evolutions = new Pokemon[]{PokemonList.perName.get("Melo"),PokemonList.perName.get("Melofee"),PokemonList.perName.get("Melodelfe")};
        PokemonList.perName.get("Mega-Mewtwo X").evolutions = new Pokemon[]{PokemonList.perName.get("Mewtwo"),PokemonList.perName.get("Mega-Mewtwo X"),PokemonList.perName.get("Mega-Mewtwo Y")};
        PokemonList.perName.get("Celebi").evolutions = new Pokemon[]{};
        PokemonList.perName.get("Cocotine").evolutions = new Pokemon[]{PokemonList.perName.get("Fluvetin"),PokemonList.perName.get("Cocotine")};
        PokemonList.perName.get("Zorua").evolutions = new Pokemon[]{PokemonList.perName.get("Zorua"),PokemonList.perName.get("Zoroark")};
        PokemonList.perName.get("Mega-Elecsprint").evolutions = new Pokemon[]{PokemonList.perName.get("Dynavolt"),PokemonList.perName.get("Elecsprint"),PokemonList.perName.get("Mega-Elecsprint")};
        PokemonList.perName.get("Carabing").evolutions = new Pokemon[]{PokemonList.perName.get("Carabing"),PokemonList.perName.get("Lancargot")};
        PokemonList.perName.get("Okeoke").evolutions = new Pokemon[]{PokemonList.perName.get("Okeoke"),PokemonList.perName.get("Qulbutoke")};
        PokemonList.perName.get("Hypotrempe").evolutions = new Pokemon[]{PokemonList.perName.get("Hypotrempe"),PokemonList.perName.get("Hypocean"),PokemonList.perName.get("Hyporoi")};
        PokemonList.perName.get("Nymphali").evolutions = new Pokemon[]{PokemonList.perName.get("Evoli"),PokemonList.perName.get("Aquali"),PokemonList.perName.get("Voltali"),PokemonList.perName.get("Pyroli"),PokemonList.perName.get("Mentali"),PokemonList.perName.get("Noctali"),PokemonList.perName.get("Phyllali"),PokemonList.perName.get("Givrali"),PokemonList.perName.get("Nymphali")};
        PokemonList.perName.get("Venalgue").evolutions = new Pokemon[]{PokemonList.perName.get("Venalgue"),PokemonList.perName.get("Kravarech")};
        PokemonList.perName.get("Mega-Scarabrute").evolutions = new Pokemon[]{PokemonList.perName.get("Scarabrute"),PokemonList.perName.get("Mega-Scarabrute")};
        PokemonList.perName.get("Maraiste").evolutions = new Pokemon[]{PokemonList.perName.get("Axoloto"),PokemonList.perName.get("Maraiste")};
        PokemonList.perName.get("Mega-Florizarre").evolutions = new Pokemon[]{PokemonList.perName.get("Bulbizarre"),PokemonList.perName.get("Herbizarre"),PokemonList.perName.get("Florizarre"),PokemonList.perName.get("Mega-Florizarre")};
        PokemonList.perName.get("Papilusion").evolutions = new Pokemon[]{PokemonList.perName.get("Chenipan"),PokemonList.perName.get("Chrysacier"),PokemonList.perName.get("Papilusion")};
        PokemonList.perName.get("Charpenti").evolutions = new Pokemon[]{PokemonList.perName.get("Charpenti"),PokemonList.perName.get("Ouvrifier"),PokemonList.perName.get("Betochef")};
        PokemonList.perName.get("Doduo").evolutions = new Pokemon[]{PokemonList.perName.get("Doduo"),PokemonList.perName.get("Dodrio")};
        PokemonList.perName.get("Coatox").evolutions = new Pokemon[]{PokemonList.perName.get("Cradopaud"),PokemonList.perName.get("Coatox")};
        PokemonList.perName.get("Charmina").evolutions = new Pokemon[]{PokemonList.perName.get("Meditikka"),PokemonList.perName.get("Charmina"),PokemonList.perName.get("Mega-Charmina")};
        PokemonList.perName.get("Voltali").evolutions = new Pokemon[]{PokemonList.perName.get("Evoli"),PokemonList.perName.get("Aquali"),PokemonList.perName.get("Voltali"),PokemonList.perName.get("Pyroli"),PokemonList.perName.get("Mentali"),PokemonList.perName.get("Noctali"),PokemonList.perName.get("Phyllali"),PokemonList.perName.get("Givrali"),PokemonList.perName.get("Nymphali")};
        PokemonList.perName.get("Pitrouille (Taille Maxi)").evolutions = new Pokemon[]{};
        PokemonList.perName.get("Cheniselle (Cape Dechet)").evolutions = new Pokemon[]{};
        PokemonList.perName.get("Exagide (Forme Assaut)").evolutions = new Pokemon[]{};
        PokemonList.perName.get("Joliflor").evolutions = new Pokemon[]{PokemonList.perName.get("Mystherbe"),PokemonList.perName.get("Ortide"),PokemonList.perName.get("Rafflesia"),PokemonList.perName.get("Joliflor")};
        PokemonList.perName.get("Tarsal").evolutions = new Pokemon[]{PokemonList.perName.get("Tarsal"),PokemonList.perName.get("Kirlia"),PokemonList.perName.get("Gardevoir"),PokemonList.perName.get("Gallame"),PokemonList.perName.get("Mega-Gardevoir")};
        PokemonList.perName.get("Scalpion").evolutions = new Pokemon[]{PokemonList.perName.get("Scalpion"),PokemonList.perName.get("Scalproie")};
        PokemonList.perName.get("Galegon").evolutions = new Pokemon[]{PokemonList.perName.get("Galekid"),PokemonList.perName.get("Galegon"),PokemonList.perName.get("Galeking"),PokemonList.perName.get("Mega-Galeking")};
        PokemonList.perName.get("Smogogo").evolutions = new Pokemon[]{PokemonList.perName.get("Smogo"),PokemonList.perName.get("Smogogo")};
        PokemonList.perName.get("Baudrive").evolutions = new Pokemon[]{PokemonList.perName.get("Baudrive"),PokemonList.perName.get("Grodrive")};
        PokemonList.perName.get("Libegon").evolutions = new Pokemon[]{PokemonList.perName.get("Kraknoix"),PokemonList.perName.get("Vibraninf"),PokemonList.perName.get("Libegon")};
        PokemonList.perName.get("Pomdepik").evolutions = new Pokemon[]{PokemonList.perName.get("Pomdepik"),PokemonList.perName.get("Foretress")};
        PokemonList.perName.get("Korillon").evolutions = new Pokemon[]{PokemonList.perName.get("Korillon"),PokemonList.perName.get("Eoko")};
        PokemonList.perName.get("Boguerisse").evolutions = new Pokemon[]{PokemonList.perName.get("Marisson"),PokemonList.perName.get("Boguerisse"),PokemonList.perName.get("Blindepique")};
        PokemonList.perName.get("Mime Jr.").evolutions = new Pokemon[]{PokemonList.perName.get("Mime Jr."),PokemonList.perName.get("M. Mime")};
        PokemonList.perName.get("Queulorior").evolutions = new Pokemon[]{};
        PokemonList.perName.get("Ecremeuh").evolutions = new Pokemon[]{};
        PokemonList.perName.get("Lineon").evolutions = new Pokemon[]{PokemonList.perName.get("Zigzaton"),PokemonList.perName.get("Lineon")};
        PokemonList.perName.get("Osselait").evolutions = new Pokemon[]{PokemonList.perName.get("Osselait"),PokemonList.perName.get("Ossatueur")};
        PokemonList.perName.get("Castorno").evolutions = new Pokemon[]{PokemonList.perName.get("Keunotor"),PokemonList.perName.get("Castorno")};
        PokemonList.perName.get("Hypnomade").evolutions = new Pokemon[]{PokemonList.perName.get("Soporifik"),PokemonList.perName.get("Hypnomade")};
        PokemonList.perName.get("Lilia").evolutions = new Pokemon[]{PokemonList.perName.get("Lilia"),PokemonList.perName.get("Vacilys")};
        PokemonList.perName.get("Motisma (Forme Helice)").evolutions = new Pokemon[]{};
        PokemonList.perName.get("Kranidos").evolutions = new Pokemon[]{PokemonList.perName.get("Kranidos"),PokemonList.perName.get("Charkos")};
        PokemonList.perName.get("Mammochon").evolutions = new Pokemon[]{PokemonList.perName.get("Marcacrin"),PokemonList.perName.get("Cochignon"),PokemonList.perName.get("Mammochon")};
        PokemonList.perName.get("Moufouette").evolutions = new Pokemon[]{PokemonList.perName.get("Moufouette"),PokemonList.perName.get("Moufflair")};
        PokemonList.perName.get("Miasmax").evolutions = new Pokemon[]{PokemonList.perName.get("Miamiasme"),PokemonList.perName.get("Miasmax")};
        PokemonList.perName.get("Aflamanoir").evolutions = new Pokemon[]{};
        PokemonList.perName.get("Makuhita").evolutions = new Pokemon[]{PokemonList.perName.get("Makuhita"),PokemonList.perName.get("Hariyama")};
        PokemonList.perName.get("Cerfrousse").evolutions = new Pokemon[]{};
        PokemonList.perName.get("Alakazam").evolutions = new Pokemon[]{PokemonList.perName.get("Abra"),PokemonList.perName.get("Kadabra"),PokemonList.perName.get("Alakazam"),PokemonList.perName.get("Mega-Alakazam")};
        PokemonList.perName.get("Mega-Dracaufeu X").evolutions = new Pokemon[]{PokemonList.perName.get("Salameche"),PokemonList.perName.get("Reptincel"),PokemonList.perName.get("Dracaufeu"),PokemonList.perName.get("Mega-Dracaufeu X"),PokemonList.perName.get("Mega-Dracaufeu Y")};
        PokemonList.perName.get("Reptincel").evolutions = new Pokemon[]{PokemonList.perName.get("Salameche"),PokemonList.perName.get("Reptincel"),PokemonList.perName.get("Dracaufeu"),PokemonList.perName.get("Mega-Dracaufeu X"),PokemonList.perName.get("Mega-Dracaufeu Y")};
        PokemonList.perName.get("Carapagos").evolutions = new Pokemon[]{PokemonList.perName.get("Carapagos"),PokemonList.perName.get("Megapagos")};
        PokemonList.perName.get("Hypocean").evolutions = new Pokemon[]{PokemonList.perName.get("Hypotrempe"),PokemonList.perName.get("Hypocean"),PokemonList.perName.get("Hyporoi")};
        PokemonList.perName.get("Tortipouss").evolutions = new Pokemon[]{PokemonList.perName.get("Tortipouss"),PokemonList.perName.get("Boskara"),PokemonList.perName.get("Torterra")};
        PokemonList.perName.get("Stalgamin").evolutions = new Pokemon[]{PokemonList.perName.get("Stalgamin"),PokemonList.perName.get("Oniglali"),PokemonList.perName.get("Momartik")};
        PokemonList.perName.get("Lancargot").evolutions = new Pokemon[]{PokemonList.perName.get("Carabing"),PokemonList.perName.get("Lancargot")};
        PokemonList.perName.get("Chuchmur").evolutions = new Pokemon[]{PokemonList.perName.get("Chuchmur"),PokemonList.perName.get("Ramboum"),PokemonList.perName.get("Brouhabam")};
        PokemonList.perName.get("Motisma (Forme Normale)").evolutions = new Pokemon[]{};
        PokemonList.perName.get("Maganon").evolutions = new Pokemon[]{PokemonList.perName.get("Magby"),PokemonList.perName.get("Magmar"),PokemonList.perName.get("Maganon")};
        PokemonList.perName.get("Parecool").evolutions = new Pokemon[]{PokemonList.perName.get("Parecool"),PokemonList.perName.get("Vigoroth"),PokemonList.perName.get("Monaflemit")};
        PokemonList.perName.get("Wattouat").evolutions = new Pokemon[]{PokemonList.perName.get("Wattouat"),PokemonList.perName.get("Lainergie"),PokemonList.perName.get("Pharamp"),PokemonList.perName.get("Mega-Pharamp")};
        PokemonList.perName.get("Opermine").evolutions = new Pokemon[]{PokemonList.perName.get("Opermine"),PokemonList.perName.get("Golgopathe")};
        PokemonList.perName.get("Prinplouf").evolutions = new Pokemon[]{PokemonList.perName.get("Tiplouf"),PokemonList.perName.get("Prinplouf"),PokemonList.perName.get("Pingoleon")};
        PokemonList.perName.get("Anchwatt").evolutions = new Pokemon[]{PokemonList.perName.get("Anchwatt"),PokemonList.perName.get("Lamperoie"),PokemonList.perName.get("Ohmassacre")};
        PokemonList.perName.get("Posipi").evolutions = new Pokemon[]{};
        PokemonList.perName.get("Exagide (Forme Parade)").evolutions = new Pokemon[]{};
        PokemonList.perName.get("Elekid").evolutions = new Pokemon[]{PokemonList.perName.get("Elekid"),PokemonList.perName.get("Elektek"),PokemonList.perName.get("Elekable")};
        PokemonList.perName.get("Flambusard").evolutions = new Pokemon[]{PokemonList.perName.get("Passerouge"),PokemonList.perName.get("Braisillon"),PokemonList.perName.get("Flambusard")};
        PokemonList.perName.get("Balbuto").evolutions = new Pokemon[]{PokemonList.perName.get("Balbuto"),PokemonList.perName.get("Kaorine")};
        PokemonList.perName.get("Yanma").evolutions = new Pokemon[]{PokemonList.perName.get("Yanma"),PokemonList.perName.get("Yanmega")};
        PokemonList.perName.get("Poichigeon").evolutions = new Pokemon[]{PokemonList.perName.get("Poichigeon"),PokemonList.perName.get("Colombeau"),PokemonList.perName.get("Deflaisan")};
        PokemonList.perName.get("Lamperoie").evolutions = new Pokemon[]{PokemonList.perName.get("Anchwatt"),PokemonList.perName.get("Lamperoie"),PokemonList.perName.get("Ohmassacre")};
        PokemonList.perName.get("Kirlia").evolutions = new Pokemon[]{PokemonList.perName.get("Tarsal"),PokemonList.perName.get("Kirlia"),PokemonList.perName.get("Gardevoir"),PokemonList.perName.get("Gallame"),PokemonList.perName.get("Mega-Gardevoir")};
        PokemonList.perName.get("Couaneton").evolutions = new Pokemon[]{PokemonList.perName.get("Couaneton"),PokemonList.perName.get("Lakmecygne")};
        PokemonList.perName.get("Mystherbe").evolutions = new Pokemon[]{PokemonList.perName.get("Mystherbe"),PokemonList.perName.get("Ortide"),PokemonList.perName.get("Rafflesia"),PokemonList.perName.get("Joliflor")};
        PokemonList.perName.get("Metang").evolutions = new Pokemon[]{PokemonList.perName.get("Terhal"),PokemonList.perName.get("Metang"),PokemonList.perName.get("Metalosse")};
        PokemonList.perName.get("Tritosor").evolutions = new Pokemon[]{PokemonList.perName.get("Sancoki"),PokemonList.perName.get("Tritosor")};
        PokemonList.perName.get("Dracolosse").evolutions = new Pokemon[]{PokemonList.perName.get("Minidraco"),PokemonList.perName.get("Draco"),PokemonList.perName.get("Dracolosse")};
        PokemonList.perName.get("Fragilady").evolutions = new Pokemon[]{PokemonList.perName.get("Chlorobule"),PokemonList.perName.get("Fragilady")};
        PokemonList.perName.get("Genesect").evolutions = new Pokemon[]{};
        PokemonList.perName.get("Nidorino").evolutions = new Pokemon[]{PokemonList.perName.get("Nidoran M"),PokemonList.perName.get("Nidorino"),PokemonList.perName.get("Nidoking")};
        PokemonList.perName.get("Branette").evolutions = new Pokemon[]{PokemonList.perName.get("Polichombr"),PokemonList.perName.get("Branette"),PokemonList.perName.get("Mega-Branette")};
        PokemonList.perName.get("Nidorina").evolutions = new Pokemon[]{PokemonList.perName.get("Nidoran F"),PokemonList.perName.get("Nidorina"),PokemonList.perName.get("Nidoqueen")};
        PokemonList.perName.get("Rhinoferos").evolutions = new Pokemon[]{PokemonList.perName.get("Rhinocorne"),PokemonList.perName.get("Rhinoferos"),PokemonList.perName.get("Rhinastoc")};
        PokemonList.perName.get("Regigigas").evolutions = new Pokemon[]{};
        PokemonList.perName.get("Tentacruel").evolutions = new Pokemon[]{PokemonList.perName.get("Tentacool"),PokemonList.perName.get("Tentacruel")};
        PokemonList.perName.get("Chlorobule").evolutions = new Pokemon[]{PokemonList.perName.get("Chlorobule"),PokemonList.perName.get("Fragilady")};
        PokemonList.perName.get("Darumacho (Mode Daruma)").evolutions = new Pokemon[]{};
        PokemonList.perName.get("Ferosinge").evolutions = new Pokemon[]{PokemonList.perName.get("Ferosinge"),PokemonList.perName.get("Colossinge")};
        PokemonList.perName.get("Flagadoss").evolutions = new Pokemon[]{PokemonList.perName.get("Ramoloss"),PokemonList.perName.get("Flagadoss"),PokemonList.perName.get("Roigada")};
        PokemonList.perName.get("Crikzik").evolutions = new Pokemon[]{PokemonList.perName.get("Crikzik"),PokemonList.perName.get("Melokrik")};
        PokemonList.perName.get("Florges").evolutions = new Pokemon[]{PokemonList.perName.get("Flabebe"),PokemonList.perName.get("Floette"),PokemonList.perName.get("Florges")};
        PokemonList.perName.get("Scarabrute").evolutions = new Pokemon[]{PokemonList.perName.get("Scarabrute"),PokemonList.perName.get("Mega-Scarabrute")};
        PokemonList.perName.get("Mimigal").evolutions = new Pokemon[]{PokemonList.perName.get("Mimigal"),PokemonList.perName.get("Migalos")};
        PokemonList.perName.get("Dodrio").evolutions = new Pokemon[]{PokemonList.perName.get("Doduo"),PokemonList.perName.get("Dodrio")};
        PokemonList.perName.get("Pijako").evolutions = new Pokemon[]{};
        PokemonList.perName.get("Lepidonille").evolutions = new Pokemon[]{PokemonList.perName.get("Lepidonille"),PokemonList.perName.get("Peregrain"),PokemonList.perName.get("Prismillon")};
        PokemonList.perName.get("Bargantua").evolutions = new Pokemon[]{};
        PokemonList.perName.get("Chrysacier").evolutions = new Pokemon[]{PokemonList.perName.get("Chenipan"),PokemonList.perName.get("Chrysacier"),PokemonList.perName.get("Papilusion")};
        PokemonList.perName.get("Electrode").evolutions = new Pokemon[]{PokemonList.perName.get("Voltorbe"),PokemonList.perName.get("Electrode")};
        PokemonList.perName.get("Sorbebe").evolutions = new Pokemon[]{PokemonList.perName.get("Sorbebe"),PokemonList.perName.get("Sorboul"),PokemonList.perName.get("Sorbouboul")};
        PokemonList.perName.get("Givrali").evolutions = new Pokemon[]{PokemonList.perName.get("Evoli"),PokemonList.perName.get("Aquali"),PokemonList.perName.get("Voltali"),PokemonList.perName.get("Pyroli"),PokemonList.perName.get("Mentali"),PokemonList.perName.get("Noctali"),PokemonList.perName.get("Phyllali"),PokemonList.perName.get("Givrali"),PokemonList.perName.get("Nymphali")};
        PokemonList.perName.get("Gloupti").evolutions = new Pokemon[]{PokemonList.perName.get("Gloupti"),PokemonList.perName.get("Avaltout")};
        PokemonList.perName.get("Gringolem").evolutions = new Pokemon[]{PokemonList.perName.get("Gringolem"),PokemonList.perName.get("Golemastoc")};
        PokemonList.perName.get("Miamiasme").evolutions = new Pokemon[]{PokemonList.perName.get("Miamiasme"),PokemonList.perName.get("Miasmax")};
        PokemonList.perName.get("Togepi").evolutions = new Pokemon[]{PokemonList.perName.get("Togepi"),PokemonList.perName.get("Togetic"),PokemonList.perName.get("Togekiss")};
        PokemonList.perName.get("Corboss").evolutions = new Pokemon[]{PokemonList.perName.get("Cornebre"),PokemonList.perName.get("Corboss")};
        PokemonList.perName.get("Flamajou").evolutions = new Pokemon[]{PokemonList.perName.get("Flamajou"),PokemonList.perName.get("Flamoutan")};
        PokemonList.perName.get("Etourvol").evolutions = new Pokemon[]{PokemonList.perName.get("Etourmi"),PokemonList.perName.get("Etourvol"),PokemonList.perName.get("Etouraptor")};
        PokemonList.perName.get("Abo").evolutions = new Pokemon[]{PokemonList.perName.get("Abo"),PokemonList.perName.get("Arbok")};
        PokemonList.perName.get("Obalie").evolutions = new Pokemon[]{PokemonList.perName.get("Obalie"),PokemonList.perName.get("Phogleur"),PokemonList.perName.get("Kaimorse")};
        PokemonList.perName.get("Octillery").evolutions = new Pokemon[]{PokemonList.perName.get("Remoraid"),PokemonList.perName.get("Octillery")};
        PokemonList.perName.get("Feuillajou").evolutions = new Pokemon[]{PokemonList.perName.get("Feuillajou"),PokemonList.perName.get("Feuiloutan")};
        PokemonList.perName.get("Zygarde").evolutions = new Pokemon[]{};
        PokemonList.perName.get("Pikachu").evolutions = new Pokemon[]{PokemonList.perName.get("Pichu"),PokemonList.perName.get("Pikachu"),PokemonList.perName.get("Raichu")};
        PokemonList.perName.get("Zoroark").evolutions = new Pokemon[]{PokemonList.perName.get("Zorua"),PokemonList.perName.get("Zoroark")};
        PokemonList.perName.get("Mega-Mysdibule").evolutions = new Pokemon[]{PokemonList.perName.get("Mysdibule"),PokemonList.perName.get("Mega-Mysdibule")};
        PokemonList.perName.get("Nodulithe").evolutions = new Pokemon[]{PokemonList.perName.get("Nodulithe"),PokemonList.perName.get("Geolithe"),PokemonList.perName.get("Gigalithe")};
        PokemonList.perName.get("Rhinastoc").evolutions = new Pokemon[]{PokemonList.perName.get("Rhinocorne"),PokemonList.perName.get("Rhinoferos"),PokemonList.perName.get("Rhinastoc")};
        PokemonList.perName.get("Mega-Gardevoir").evolutions = new Pokemon[]{PokemonList.perName.get("Tarsal"),PokemonList.perName.get("Kirlia"),PokemonList.perName.get("Gardevoir"),PokemonList.perName.get("Gallame"),PokemonList.perName.get("Mega-Gardevoir")};
        PokemonList.perName.get("Mega-Brasegali").evolutions = new Pokemon[]{PokemonList.perName.get("Poussifeu"),PokemonList.perName.get("Galifeu"),PokemonList.perName.get("Brasegali"),PokemonList.perName.get("Mega-Brasegali")};
        PokemonList.perName.get("Grainipiot").evolutions = new Pokemon[]{PokemonList.perName.get("Grainipiot"),PokemonList.perName.get("Pifeuil"),PokemonList.perName.get("Tengalice")};
        PokemonList.perName.get("Qwilfish").evolutions = new Pokemon[]{};
        PokemonList.perName.get("Carchacrok").evolutions = new Pokemon[]{PokemonList.perName.get("Griknot"),PokemonList.perName.get("Carmache"),PokemonList.perName.get("Carchacrok"),PokemonList.perName.get("Mega-Carchacrok")};
        PokemonList.perName.get("Latios").evolutions = new Pokemon[]{};
        PokemonList.perName.get("Groret").evolutions = new Pokemon[]{PokemonList.perName.get("Spoink"),PokemonList.perName.get("Groret")};
        PokemonList.perName.get("Cheniselle (Cape Plante)").evolutions = new Pokemon[]{};
        PokemonList.perName.get("Oniglali").evolutions = new Pokemon[]{PokemonList.perName.get("Stalgamin"),PokemonList.perName.get("Oniglali"),PokemonList.perName.get("Momartik")};
        PokemonList.perName.get("Steelix").evolutions = new Pokemon[]{PokemonList.perName.get("Onix"),PokemonList.perName.get("Steelix")};
        PokemonList.perName.get("Crefollet").evolutions = new Pokemon[]{};
        PokemonList.perName.get("Electhor").evolutions = new Pokemon[]{};
        PokemonList.perName.get("Phanpy").evolutions = new Pokemon[]{PokemonList.perName.get("Phanpy"),PokemonList.perName.get("Donphan")};
        PokemonList.perName.get("Crehelf").evolutions = new Pokemon[]{};
        PokemonList.perName.get("Ortide").evolutions = new Pokemon[]{PokemonList.perName.get("Mystherbe"),PokemonList.perName.get("Ortide"),PokemonList.perName.get("Rafflesia"),PokemonList.perName.get("Joliflor")};
        PokemonList.perName.get("Metalosse").evolutions = new Pokemon[]{PokemonList.perName.get("Terhal"),PokemonList.perName.get("Metang"),PokemonList.perName.get("Metalosse")};
        PokemonList.perName.get("Azumarill").evolutions = new Pokemon[]{PokemonList.perName.get("Azurill"),PokemonList.perName.get("Marill"),PokemonList.perName.get("Azumarill")};
        PokemonList.perName.get("Kyogre").evolutions = new Pokemon[]{};
        PokemonList.perName.get("Mega-Branette").evolutions = new Pokemon[]{PokemonList.perName.get("Polichombr"),PokemonList.perName.get("Branette"),PokemonList.perName.get("Mega-Branette")};
        PokemonList.perName.get("Scorplane").evolutions = new Pokemon[]{PokemonList.perName.get("Scorplane"),PokemonList.perName.get("Scorvol")};
        PokemonList.perName.get("Chenipotte").evolutions = new Pokemon[]{PokemonList.perName.get("Chenipotte"),PokemonList.perName.get("Armulys"),PokemonList.perName.get("Blindalys"),PokemonList.perName.get("Charmillon"),PokemonList.perName.get("Papinox")};
        PokemonList.perName.get("Elektek").evolutions = new Pokemon[]{PokemonList.perName.get("Elekid"),PokemonList.perName.get("Elektek"),PokemonList.perName.get("Elekable")};
        PokemonList.perName.get("Vigoroth").evolutions = new Pokemon[]{PokemonList.perName.get("Parecool"),PokemonList.perName.get("Vigoroth"),PokemonList.perName.get("Monaflemit")};
        PokemonList.perName.get("Leveinard").evolutions = new Pokemon[]{PokemonList.perName.get("Ptiravi"),PokemonList.perName.get("Leveinard"),PokemonList.perName.get("Leuphorie")};
        PokemonList.perName.get("Fouinar").evolutions = new Pokemon[]{PokemonList.perName.get("Fouinette"),PokemonList.perName.get("Fouinar")};
        PokemonList.perName.get("Simularbre").evolutions = new Pokemon[]{PokemonList.perName.get("Manzai"),PokemonList.perName.get("Simularbre")};
        PokemonList.perName.get("Polagriffe").evolutions = new Pokemon[]{PokemonList.perName.get("Polarhume"),PokemonList.perName.get("Polagriffe")};
        PokemonList.perName.get("Maracachi").evolutions = new Pokemon[]{};
        PokemonList.perName.get("Dragmara").evolutions = new Pokemon[]{PokemonList.perName.get("Amagara"),PokemonList.perName.get("Dragmara")};
        PokemonList.perName.get("Insecateur").evolutions = new Pokemon[]{PokemonList.perName.get("Insecateur"),PokemonList.perName.get("Cizayox"),PokemonList.perName.get("Mega-Cizayox")};
        PokemonList.perName.get("Laporeille").evolutions = new Pokemon[]{PokemonList.perName.get("Laporeille"),PokemonList.perName.get("Lockpin")};
        PokemonList.perName.get("Hoot-hoot").evolutions = new Pokemon[]{};
        PokemonList.perName.get("Lokhlass").evolutions = new Pokemon[]{};
        PokemonList.perName.get("Spiritomb").evolutions = new Pokemon[]{};
        PokemonList.perName.get("Limagma").evolutions = new Pokemon[]{PokemonList.perName.get("Limagma"),PokemonList.perName.get("Volcaropod")};
        PokemonList.perName.get("Paras").evolutions = new Pokemon[]{PokemonList.perName.get("Paras"),PokemonList.perName.get("Parasect")};
        PokemonList.perName.get("Pyronille").evolutions = new Pokemon[]{PokemonList.perName.get("Pyronille"),PokemonList.perName.get("Pyrax")};
        PokemonList.perName.get("Symbios").evolutions = new Pokemon[]{};
        PokemonList.perName.get("Melo").evolutions = new Pokemon[]{PokemonList.perName.get("Melo"),PokemonList.perName.get("Melofee"),PokemonList.perName.get("Melodelfe")};
        PokemonList.perName.get("Lianaja").evolutions = new Pokemon[]{PokemonList.perName.get("Vipelierre"),PokemonList.perName.get("Lianaja"),PokemonList.perName.get("Majaspic")};
        PokemonList.perName.get("Arcko").evolutions = new Pokemon[]{PokemonList.perName.get("Arcko"),PokemonList.perName.get("Massko"),PokemonList.perName.get("Jungko")};
        PokemonList.perName.get("Archeomire").evolutions = new Pokemon[]{PokemonList.perName.get("Archeomire"),PokemonList.perName.get("Archeodong")};
        PokemonList.perName.get("Banshitrouye (Taille Normale)").evolutions = new Pokemon[]{};
        PokemonList.perName.get("Feuforeve").evolutions = new Pokemon[]{PokemonList.perName.get("Feuforeve"),PokemonList.perName.get("Magireve")};
        PokemonList.perName.get("Mega-Tortank").evolutions = new Pokemon[]{PokemonList.perName.get("Carapuce"),PokemonList.perName.get("Carabaffe"),PokemonList.perName.get("Tortank"),PokemonList.perName.get("Mega-Tortank")};
        PokemonList.perName.get("Venipatte").evolutions = new Pokemon[]{PokemonList.perName.get("Venipatte"),PokemonList.perName.get("Scobolide"),PokemonList.perName.get("Brutapode")};
        PokemonList.perName.get("Doudouvet").evolutions = new Pokemon[]{PokemonList.perName.get("Doudouvet"),PokemonList.perName.get("Farfaduvet")};
        PokemonList.perName.get("Lamantine").evolutions = new Pokemon[]{PokemonList.perName.get("Otaria"),PokemonList.perName.get("Lamantine")};
        PokemonList.perName.get("Parasect").evolutions = new Pokemon[]{PokemonList.perName.get("Paras"),PokemonList.perName.get("Parasect")};
        PokemonList.perName.get("Avaltout").evolutions = new Pokemon[]{PokemonList.perName.get("Gloupti"),PokemonList.perName.get("Avaltout")};
        PokemonList.perName.get("Voltorbe").evolutions = new Pokemon[]{PokemonList.perName.get("Voltorbe"),PokemonList.perName.get("Electrode")};
        PokemonList.perName.get("Magicarpe").evolutions = new Pokemon[]{PokemonList.perName.get("Magicarpe"),PokemonList.perName.get("Leviator"),PokemonList.perName.get("Mega-Leviator")};
        PokemonList.perName.get("Darumacho (Mode Normal)").evolutions = new Pokemon[]{};
        PokemonList.perName.get("Heledelle").evolutions = new Pokemon[]{PokemonList.perName.get("Nirondelle"),PokemonList.perName.get("Heledelle")};
        PokemonList.perName.get("Noacier").evolutions = new Pokemon[]{PokemonList.perName.get("Grindur"),PokemonList.perName.get("Noacier")};
        PokemonList.perName.get("Laggron").evolutions = new Pokemon[]{PokemonList.perName.get("Gobou"),PokemonList.perName.get("Flobio"),PokemonList.perName.get("Laggron")};
        PokemonList.perName.get("Gobou").evolutions = new Pokemon[]{PokemonList.perName.get("Gobou"),PokemonList.perName.get("Flobio"),PokemonList.perName.get("Laggron")};
        PokemonList.perName.get("Canarticho").evolutions = new Pokemon[]{};
        PokemonList.perName.get("Groudon").evolutions = new Pokemon[]{};
        PokemonList.perName.get("Blizzaroi").evolutions = new Pokemon[]{PokemonList.perName.get("Blizzi"),PokemonList.perName.get("Blizzaroi"),PokemonList.perName.get("Mega-Blizzaroi")};
        PokemonList.perName.get("Tournegrin").evolutions = new Pokemon[]{PokemonList.perName.get("Tournegrin"),PokemonList.perName.get("Heliatronc")};
        PokemonList.perName.get("Nidoqueen").evolutions = new Pokemon[]{PokemonList.perName.get("Nidoran F"),PokemonList.perName.get("Nidorina"),PokemonList.perName.get("Nidoqueen")};
        PokemonList.perName.get("Altaria").evolutions = new Pokemon[]{PokemonList.perName.get("Tylton"),PokemonList.perName.get("Altaria")};
        PokemonList.perName.get("Roucool").evolutions = new Pokemon[]{PokemonList.perName.get("Roucool"),PokemonList.perName.get("Roucoups"),PokemonList.perName.get("Roucarnage")};
        PokemonList.perName.get("Cradopaud").evolutions = new Pokemon[]{PokemonList.perName.get("Cradopaud"),PokemonList.perName.get("Coatox")};
        PokemonList.perName.get("Malosse").evolutions = new Pokemon[]{PokemonList.perName.get("Malosse"),PokemonList.perName.get("Demolosse"),PokemonList.perName.get("Mega-Demolosse")};
        PokemonList.perName.get("Vaututrice").evolutions = new Pokemon[]{PokemonList.perName.get("Vostourno"),PokemonList.perName.get("Vaututrice")};
        PokemonList.perName.get("Togekiss").evolutions = new Pokemon[]{PokemonList.perName.get("Togepi"),PokemonList.perName.get("Togetic"),PokemonList.perName.get("Togekiss")};
        PokemonList.perName.get("Tritonde").evolutions = new Pokemon[]{PokemonList.perName.get("Tritonde"),PokemonList.perName.get("Batracne"),PokemonList.perName.get("Crapustule")};
        PokemonList.perName.get("Moufflair").evolutions = new Pokemon[]{PokemonList.perName.get("Moufouette"),PokemonList.perName.get("Moufflair")};
        PokemonList.perName.get("Tiplouf").evolutions = new Pokemon[]{PokemonList.perName.get("Tiplouf"),PokemonList.perName.get("Prinplouf"),PokemonList.perName.get("Pingoleon")};
        PokemonList.perName.get("Lumivole").evolutions = new Pokemon[]{};
        PokemonList.perName.get("Carmache").evolutions = new Pokemon[]{PokemonList.perName.get("Griknot"),PokemonList.perName.get("Carmache"),PokemonList.perName.get("Carchacrok"),PokemonList.perName.get("Mega-Carchacrok")};
        PokemonList.perName.get("Cliticlic").evolutions = new Pokemon[]{PokemonList.perName.get("Tic"),PokemonList.perName.get("Clic"),PokemonList.perName.get("Cliticlic")};
        PokemonList.perName.get("Giratina (Forme Originelle)").evolutions = new Pokemon[]{};
        PokemonList.perName.get("Poussifeu").evolutions = new Pokemon[]{PokemonList.perName.get("Poussifeu"),PokemonList.perName.get("Galifeu"),PokemonList.perName.get("Brasegali"),PokemonList.perName.get("Mega-Brasegali")};
        PokemonList.perName.get("Limaspeed").evolutions = new Pokemon[]{PokemonList.perName.get("Escargaume"),PokemonList.perName.get("Limaspeed")};
        PokemonList.perName.get("Iguolta").evolutions = new Pokemon[]{PokemonList.perName.get("Galvaran"),PokemonList.perName.get("Iguolta")};
        PokemonList.perName.get("Cheniti").evolutions = new Pokemon[]{PokemonList.perName.get("Cheniti"),PokemonList.perName.get("Cheniselle"),PokemonList.perName.get("Papilord")};
        PokemonList.perName.get("Kapoera").evolutions = new Pokemon[]{PokemonList.perName.get("Debugant"),PokemonList.perName.get("Kicklee"),PokemonList.perName.get("Tygnon"),PokemonList.perName.get("Kapoera")};
        PokemonList.perName.get("Pachirisu").evolutions = new Pokemon[]{};
        PokemonList.perName.get("Marill").evolutions = new Pokemon[]{PokemonList.perName.get("Azurill"),PokemonList.perName.get("Marill"),PokemonList.perName.get("Azumarill")};
        PokemonList.perName.get("Mega-Lucario").evolutions = new Pokemon[]{PokemonList.perName.get("Riolu"),PokemonList.perName.get("Lucario"),PokemonList.perName.get("Mega-Lucario")};
        PokemonList.perName.get("Skitty").evolutions = new Pokemon[]{PokemonList.perName.get("Skitty"),PokemonList.perName.get("Delcatty")};
        PokemonList.perName.get("Abra").evolutions = new Pokemon[]{PokemonList.perName.get("Abra"),PokemonList.perName.get("Kadabra"),PokemonList.perName.get("Alakazam"),PokemonList.perName.get("Mega-Alakazam")};
        PokemonList.perName.get("Couverdure").evolutions = new Pokemon[]{PokemonList.perName.get("Larveyette"),PokemonList.perName.get("Couverdure"),PokemonList.perName.get("Manternel")};
        PokemonList.perName.get("Grodoudou").evolutions = new Pokemon[]{PokemonList.perName.get("Toudoudou"),PokemonList.perName.get("Rondoudou"),PokemonList.perName.get("Grodoudou")};
        PokemonList.perName.get("Ptyranidur").evolutions = new Pokemon[]{PokemonList.perName.get("Ptyranidur"),PokemonList.perName.get("Rexillius")};
        PokemonList.perName.get("Kecleon").evolutions = new Pokemon[]{};
        PokemonList.perName.get("Deoxys (Forme Vitesse)").evolutions = new Pokemon[]{};
        PokemonList.perName.get("Crustabri").evolutions = new Pokemon[]{PokemonList.perName.get("Kokiyas"),PokemonList.perName.get("Crustabri")};
        PokemonList.perName.get("Motisma (Forme Chaleur)").evolutions = new Pokemon[]{};
        PokemonList.perName.get("Galvaran").evolutions = new Pokemon[]{PokemonList.perName.get("Galvaran"),PokemonList.perName.get("Iguolta")};
        PokemonList.perName.get("Fluvetin").evolutions = new Pokemon[]{PokemonList.perName.get("Fluvetin"),PokemonList.perName.get("Cocotine")};
        PokemonList.perName.get("Haydaim").evolutions = new Pokemon[]{PokemonList.perName.get("Vivaldaim"),PokemonList.perName.get("Haydaim")};
        PokemonList.perName.get("Kyurem (Noir)").evolutions = new Pokemon[]{};
        PokemonList.perName.get("Hippopotas").evolutions = new Pokemon[]{PokemonList.perName.get("Hippopotas"),PokemonList.perName.get("Hippodocus")};
        PokemonList.perName.get("Giratina (Forme Alternative)").evolutions = new Pokemon[]{};
        PokemonList.perName.get("Coconfort").evolutions = new Pokemon[]{PokemonList.perName.get("Aspicot"),PokemonList.perName.get("Coconfort"),PokemonList.perName.get("Dardargnan")};
        PokemonList.perName.get("Noeunoeuf").evolutions = new Pokemon[]{PokemonList.perName.get("Noeunoeuf"),PokemonList.perName.get("Noadkoko")};
        PokemonList.perName.get("Zigzaton").evolutions = new Pokemon[]{PokemonList.perName.get("Zigzaton"),PokemonList.perName.get("Lineon")};
        PokemonList.perName.get("Rattata").evolutions = new Pokemon[]{PokemonList.perName.get("Rattata"),PokemonList.perName.get("Rattatac")};
        PokemonList.perName.get("Girafarig").evolutions = new Pokemon[]{};
        PokemonList.perName.get("Otaria").evolutions = new Pokemon[]{PokemonList.perName.get("Otaria"),PokemonList.perName.get("Lamantine")};
        PokemonList.perName.get("Granbull").evolutions = new Pokemon[]{PokemonList.perName.get("Snubbull"),PokemonList.perName.get("Granbull")};
        PokemonList.perName.get("Kabutops").evolutions = new Pokemon[]{PokemonList.perName.get("Kabuto"),PokemonList.perName.get("Kabutops")};
        PokemonList.perName.get("Ratentif").evolutions = new Pokemon[]{PokemonList.perName.get("Ratentif"),PokemonList.perName.get("Miradar")};
        PokemonList.perName.get("Cheniselle (Cape Sol)").evolutions = new Pokemon[]{};
        PokemonList.perName.get("Bulbizarre").evolutions = new Pokemon[]{PokemonList.perName.get("Bulbizarre"),PokemonList.perName.get("Herbizarre"),PokemonList.perName.get("Florizarre"),PokemonList.perName.get("Mega-Florizarre")};
        PokemonList.perName.get("Couafarel").evolutions = new Pokemon[]{};
        PokemonList.perName.get("Mega-Demolosse").evolutions = new Pokemon[]{PokemonList.perName.get("Malosse"),PokemonList.perName.get("Demolosse"),PokemonList.perName.get("Mega-Demolosse")};
        PokemonList.perName.get("Siderella").evolutions = new Pokemon[]{PokemonList.perName.get("Scrutella"),PokemonList.perName.get("Mesmerella"),PokemonList.perName.get("Siderella")};
        PokemonList.perName.get("Dedenne").evolutions = new Pokemon[]{};
        PokemonList.perName.get("Herbizarre").evolutions = new Pokemon[]{PokemonList.perName.get("Bulbizarre"),PokemonList.perName.get("Herbizarre"),PokemonList.perName.get("Florizarre"),PokemonList.perName.get("Mega-Florizarre")};
        PokemonList.perName.get("Lixy").evolutions = new Pokemon[]{PokemonList.perName.get("Lixy"),PokemonList.perName.get("Luxio"),PokemonList.perName.get("Luxray")};
        PokemonList.perName.get("Roucarnage").evolutions = new Pokemon[]{PokemonList.perName.get("Roucool"),PokemonList.perName.get("Roucoups"),PokemonList.perName.get("Roucarnage")};
        PokemonList.perName.get("Tarinor").evolutions = new Pokemon[]{PokemonList.perName.get("Tarinor"),PokemonList.perName.get("Tarinorme")};
        PokemonList.perName.get("Rapasdepic").evolutions = new Pokemon[]{PokemonList.perName.get("Piafabec"),PokemonList.perName.get("Rapasdepic")};
        PokemonList.perName.get("Embrylex").evolutions = new Pokemon[]{PokemonList.perName.get("Embrylex"),PokemonList.perName.get("Ymphect"),PokemonList.perName.get("Tyranocif"),PokemonList.perName.get("Mega-Tyranocif")};
        PokemonList.perName.get("Togetic").evolutions = new Pokemon[]{PokemonList.perName.get("Togepi"),PokemonList.perName.get("Togetic"),PokemonList.perName.get("Togekiss")};
        PokemonList.perName.get("Mega-Galeking").evolutions = new Pokemon[]{PokemonList.perName.get("Galekid"),PokemonList.perName.get("Galegon"),PokemonList.perName.get("Galeking"),PokemonList.perName.get("Mega-Galeking")};
        PokemonList.perName.get("Brouhabam").evolutions = new Pokemon[]{PokemonList.perName.get("Chuchmur"),PokemonList.perName.get("Ramboum"),PokemonList.perName.get("Brouhabam")};
        PokemonList.perName.get("Babimanta").evolutions = new Pokemon[]{PokemonList.perName.get("Babimanta"),PokemonList.perName.get("Demanta")};
        PokemonList.perName.get("Rhinolove").evolutions = new Pokemon[]{PokemonList.perName.get("Chovsourir"),PokemonList.perName.get("Rhinolove")};
        PokemonList.perName.get("Florizarre").evolutions = new Pokemon[]{PokemonList.perName.get("Bulbizarre"),PokemonList.perName.get("Herbizarre"),PokemonList.perName.get("Florizarre"),PokemonList.perName.get("Mega-Florizarre")};
        PokemonList.perName.get("Clamiral").evolutions = new Pokemon[]{PokemonList.perName.get("Moustillon"),PokemonList.perName.get("Mateloutre"),PokemonList.perName.get("Clamiral")};
        PokemonList.perName.get("Ronflex").evolutions = new Pokemon[]{PokemonList.perName.get("Goinfrex"),PokemonList.perName.get("Ronflex")};
        PokemonList.perName.get("Kyurem (Blanc)").evolutions = new Pokemon[]{};
        PokemonList.perName.get("Grotadmorv").evolutions = new Pokemon[]{PokemonList.perName.get("Tadmorv"),PokemonList.perName.get("Grotadmorv")};
        PokemonList.perName.get("Ptitard").evolutions = new Pokemon[]{PokemonList.perName.get("Ptitard"),PokemonList.perName.get("Tetarte"),PokemonList.perName.get("Tartard"),PokemonList.perName.get("Tarpaud")};
        PokemonList.perName.get("Mentali").evolutions = new Pokemon[]{PokemonList.perName.get("Evoli"),PokemonList.perName.get("Aquali"),PokemonList.perName.get("Voltali"),PokemonList.perName.get("Pyroli"),PokemonList.perName.get("Mentali"),PokemonList.perName.get("Noctali"),PokemonList.perName.get("Phyllali"),PokemonList.perName.get("Givrali"),PokemonList.perName.get("Nymphali")};
        PokemonList.perName.get("Betochef").evolutions = new Pokemon[]{PokemonList.perName.get("Charpenti"),PokemonList.perName.get("Ouvrifier"),PokemonList.perName.get("Betochef")};
        PokemonList.perName.get("Stari").evolutions = new Pokemon[]{};
        PokemonList.perName.get("Arkeapti").evolutions = new Pokemon[]{PokemonList.perName.get("Arkeapti"),PokemonList.perName.get("Aeropteryx")};
        PokemonList.perName.get("Crocorible").evolutions = new Pokemon[]{PokemonList.perName.get("Mascaiman"),PokemonList.perName.get("Escroco"),PokemonList.perName.get("Crocorible")};
        PokemonList.perName.get("Heatran").evolutions = new Pokemon[]{};
        PokemonList.perName.get("Ponyta").evolutions = new Pokemon[]{PokemonList.perName.get("Ponyta"),PokemonList.perName.get("Galopa")};
        PokemonList.perName.get("Crefadet").evolutions = new Pokemon[]{};
        PokemonList.perName.get("Escroco").evolutions = new Pokemon[]{PokemonList.perName.get("Mascaiman"),PokemonList.perName.get("Escroco"),PokemonList.perName.get("Crocorible")};
        PokemonList.perName.get("Hariyama").evolutions = new Pokemon[]{PokemonList.perName.get("Makuhita"),PokemonList.perName.get("Hariyama")};
        PokemonList.perName.get("Qulbutoke").evolutions = new Pokemon[]{PokemonList.perName.get("Okeoke"),PokemonList.perName.get("Qulbutoke")};
        PokemonList.perName.get("Staross").evolutions = new Pokemon[]{};
        PokemonList.perName.get("Hexagel").evolutions = new Pokemon[]{};
        PokemonList.perName.get("Lippouti").evolutions = new Pokemon[]{PokemonList.perName.get("Lippouti"),PokemonList.perName.get("Lippoutou")};
        PokemonList.perName.get("Bastiodon").evolutions = new Pokemon[]{PokemonList.perName.get("Dinoclier"),PokemonList.perName.get("Bastiodon")};
        PokemonList.perName.get("Peregrain").evolutions = new Pokemon[]{PokemonList.perName.get("Lepidonille"),PokemonList.perName.get("Peregrain"),PokemonList.perName.get("Prismillon")};
        PokemonList.perName.get("Carvanha").evolutions = new Pokemon[]{PokemonList.perName.get("Carvanha"),PokemonList.perName.get("Sharpedo")};
        PokemonList.perName.get("Pharamp").evolutions = new Pokemon[]{PokemonList.perName.get("Wattouat"),PokemonList.perName.get("Lainergie"),PokemonList.perName.get("Pharamp"),PokemonList.perName.get("Mega-Pharamp")};
        PokemonList.perName.get("Mega-Charmina").evolutions = new Pokemon[]{PokemonList.perName.get("Meditikka"),PokemonList.perName.get("Charmina"),PokemonList.perName.get("Mega-Charmina")};
        PokemonList.perName.get("Bouldeneu").evolutions = new Pokemon[]{PokemonList.perName.get("Saquedeneu"),PokemonList.perName.get("Bouldeneu")};
        PokemonList.perName.get("Heliatronc").evolutions = new Pokemon[]{PokemonList.perName.get("Tournegrin"),PokemonList.perName.get("Heliatronc")};
        PokemonList.perName.get("Gamblast").evolutions = new Pokemon[]{PokemonList.perName.get("Flingouste"),PokemonList.perName.get("Gamblast")};
        PokemonList.perName.get("Eoko").evolutions = new Pokemon[]{PokemonList.perName.get("Korillon"),PokemonList.perName.get("Eoko")};
        PokemonList.perName.get("Brutalibre").evolutions = new Pokemon[]{};
        PokemonList.perName.get("Furaiglon").evolutions = new Pokemon[]{PokemonList.perName.get("Furaiglon"),PokemonList.perName.get("Gueriaigle")};
        PokemonList.perName.get("Chevroum").evolutions = new Pokemon[]{PokemonList.perName.get("Cabriolaine"),PokemonList.perName.get("Chevroum")};
        PokemonList.perName.get("Flamoutan").evolutions = new Pokemon[]{PokemonList.perName.get("Flamajou"),PokemonList.perName.get("Flamoutan")};
        PokemonList.perName.get("Prismillon").evolutions = new Pokemon[]{PokemonList.perName.get("Lepidonille"),PokemonList.perName.get("Peregrain"),PokemonList.perName.get("Prismillon")};
        PokemonList.perName.get("Sonistrelle").evolutions = new Pokemon[]{PokemonList.perName.get("Sonistrelle"),PokemonList.perName.get("Bruyverne")};
        PokemonList.perName.get("Goupix").evolutions = new Pokemon[]{PokemonList.perName.get("Goupix"),PokemonList.perName.get("Feunard")};
        PokemonList.perName.get("Gravalanch").evolutions = new Pokemon[]{PokemonList.perName.get("Racaillou"),PokemonList.perName.get("Gravalanch"),PokemonList.perName.get("Grolem")};
        PokemonList.perName.get("Nostenfer").evolutions = new Pokemon[]{PokemonList.perName.get("Nosferapti"),PokemonList.perName.get("Nosferalto"),PokemonList.perName.get("Nostenfer")};
        PokemonList.perName.get("Chetiflor").evolutions = new Pokemon[]{PokemonList.perName.get("Chetiflor"),PokemonList.perName.get("Boustiflor"),PokemonList.perName.get("Empiflor")};
        PokemonList.perName.get("Motisma (Forme Lavage)").evolutions = new Pokemon[]{};
        PokemonList.perName.get("Lumineon").evolutions = new Pokemon[]{PokemonList.perName.get("Ecayon"),PokemonList.perName.get("Lumineon")};
        PokemonList.perName.get("Croaporal").evolutions = new Pokemon[]{PokemonList.perName.get("Grenousse"),PokemonList.perName.get("Croaporal"),PokemonList.perName.get("Amphinobi")};
        PokemonList.perName.get("Rhinocorne").evolutions = new Pokemon[]{PokemonList.perName.get("Rhinocorne"),PokemonList.perName.get("Rhinoferos"),PokemonList.perName.get("Rhinastoc")};
        PokemonList.perName.get("Leviator").evolutions = new Pokemon[]{PokemonList.perName.get("Magicarpe"),PokemonList.perName.get("Leviator"),PokemonList.perName.get("Mega-Leviator")};
        PokemonList.perName.get("Cryptero").evolutions = new Pokemon[]{};
        PokemonList.perName.get("Spoink").evolutions = new Pokemon[]{PokemonList.perName.get("Spoink"),PokemonList.perName.get("Groret")};
        PokemonList.perName.get("Dialga").evolutions = new Pokemon[]{};
        PokemonList.perName.get("Sabelette").evolutions = new Pokemon[]{PokemonList.perName.get("Sabelette"),PokemonList.perName.get("Sablaireau")};
        PokemonList.perName.get("Dynavolt").evolutions = new Pokemon[]{PokemonList.perName.get("Dynavolt"),PokemonList.perName.get("Elecsprint"),PokemonList.perName.get("Mega-Elecsprint")};
        PokemonList.perName.get("Pichu").evolutions = new Pokemon[]{PokemonList.perName.get("Pichu"),PokemonList.perName.get("Pikachu"),PokemonList.perName.get("Raichu")};
        PokemonList.perName.get("Terrakium").evolutions = new Pokemon[]{};
        PokemonList.perName.get("Amagara").evolutions = new Pokemon[]{PokemonList.perName.get("Amagara"),PokemonList.perName.get("Dragmara")};
        PokemonList.perName.get("Poissirene").evolutions = new Pokemon[]{PokemonList.perName.get("Poissirene"),PokemonList.perName.get("Poissoroy")};
        PokemonList.perName.get("Magby").evolutions = new Pokemon[]{PokemonList.perName.get("Magby"),PokemonList.perName.get("Magmar"),PokemonList.perName.get("Maganon")};
        PokemonList.perName.get("Farfaduvet").evolutions = new Pokemon[]{PokemonList.perName.get("Doudouvet"),PokemonList.perName.get("Farfaduvet")};
        PokemonList.perName.get("Lockpin").evolutions = new Pokemon[]{PokemonList.perName.get("Laporeille"),PokemonList.perName.get("Lockpin")};
        PokemonList.perName.get("Loupio").evolutions = new Pokemon[]{PokemonList.perName.get("Loupio"),PokemonList.perName.get("Lanturn")};
        PokemonList.perName.get("Elecsprint").evolutions = new Pokemon[]{PokemonList.perName.get("Dynavolt"),PokemonList.perName.get("Elecsprint"),PokemonList.perName.get("Mega-Elecsprint")};
        PokemonList.perName.get("Banshitrouye (Taille Ultra)").evolutions = new Pokemon[]{};
        PokemonList.perName.get("Keldeo").evolutions = new Pokemon[]{};
        PokemonList.perName.get("Jungko").evolutions = new Pokemon[]{PokemonList.perName.get("Arcko"),PokemonList.perName.get("Massko"),PokemonList.perName.get("Jungko")};
        PokemonList.perName.get("Boreas (Forme Avatar)").evolutions = new Pokemon[]{};
        PokemonList.perName.get("Registeel").evolutions = new Pokemon[]{};
        PokemonList.perName.get("Xatu").evolutions = new Pokemon[]{PokemonList.perName.get("Natu"),PokemonList.perName.get("Xatu")};
        PokemonList.perName.get("Skelenox").evolutions = new Pokemon[]{PokemonList.perName.get("Skelenox"),PokemonList.perName.get("Teraclope"),PokemonList.perName.get("Noctunoir")};
        PokemonList.perName.get("Etourmi").evolutions = new Pokemon[]{PokemonList.perName.get("Etourmi"),PokemonList.perName.get("Etourvol"),PokemonList.perName.get("Etouraptor")};
        PokemonList.perName.get("Aeromite").evolutions = new Pokemon[]{PokemonList.perName.get("Mimitoss"),PokemonList.perName.get("Aeromite")};
        PokemonList.perName.get("Tortank").evolutions = new Pokemon[]{PokemonList.perName.get("Carapuce"),PokemonList.perName.get("Carabaffe"),PokemonList.perName.get("Tortank"),PokemonList.perName.get("Mega-Tortank")};
        PokemonList.perName.get("Mega-Cizayox").evolutions = new Pokemon[]{PokemonList.perName.get("Insecateur"),PokemonList.perName.get("Cizayox"),PokemonList.perName.get("Mega-Cizayox")};
        PokemonList.perName.get("Minidraco").evolutions = new Pokemon[]{PokemonList.perName.get("Minidraco"),PokemonList.perName.get("Draco"),PokemonList.perName.get("Dracolosse")};
        PokemonList.perName.get("Trioxhydre").evolutions = new Pokemon[]{PokemonList.perName.get("Solochi"),PokemonList.perName.get("Diamat"),PokemonList.perName.get("Trioxhydre")};
        PokemonList.perName.get("Melofee").evolutions = new Pokemon[]{PokemonList.perName.get("Melo"),PokemonList.perName.get("Melofee"),PokemonList.perName.get("Melodelfe")};
        PokemonList.perName.get("Crabicoque").evolutions = new Pokemon[]{PokemonList.perName.get("Crabicoque"),PokemonList.perName.get("Crabaraque")};
        PokemonList.perName.get("Torterra").evolutions = new Pokemon[]{PokemonList.perName.get("Tortipouss"),PokemonList.perName.get("Boskara"),PokemonList.perName.get("Torterra")};
        PokemonList.perName.get("Rototaupe").evolutions = new Pokemon[]{PokemonList.perName.get("Rototaupe"),PokemonList.perName.get("Minotaupe")};
        PokemonList.perName.get("Ceribou").evolutions = new Pokemon[]{PokemonList.perName.get("Ceribou"),PokemonList.perName.get("Ceriflor")};
        PokemonList.perName.get("Keunotor").evolutions = new Pokemon[]{PokemonList.perName.get("Keunotor"),PokemonList.perName.get("Castorno")};
        PokemonList.perName.get("Nidoran F").evolutions = new Pokemon[]{PokemonList.perName.get("Nidoran F"),PokemonList.perName.get("Nidorina"),PokemonList.perName.get("Nidoqueen")};
        PokemonList.perName.get("Helionceau").evolutions = new Pokemon[]{PokemonList.perName.get("Helionceau"),PokemonList.perName.get("Nemelios")};
        PokemonList.perName.get("Entei").evolutions = new Pokemon[]{};
        PokemonList.perName.get("Nidoran M").evolutions = new Pokemon[]{PokemonList.perName.get("Nidoran M"),PokemonList.perName.get("Nidorino"),PokemonList.perName.get("Nidoking")};
        PokemonList.perName.get("Moustillon").evolutions = new Pokemon[]{PokemonList.perName.get("Moustillon"),PokemonList.perName.get("Mateloutre"),PokemonList.perName.get("Clamiral")};
        PokemonList.perName.get("Mygavolt").evolutions = new Pokemon[]{PokemonList.perName.get("Statitik"),PokemonList.perName.get("Mygavolt")};
        PokemonList.perName.get("Soporifik").evolutions = new Pokemon[]{PokemonList.perName.get("Soporifik"),PokemonList.perName.get("Hypnomade")};
        PokemonList.perName.get("Dimocles").evolutions = new Pokemon[]{PokemonList.perName.get("Monorpale"),PokemonList.perName.get("Dimocles"),PokemonList.perName.get("Exagide")};
        PokemonList.perName.get("Riolu").evolutions = new Pokemon[]{PokemonList.perName.get("Riolu"),PokemonList.perName.get("Lucario"),PokemonList.perName.get("Mega-Lucario")};
        PokemonList.perName.get("Aspicot").evolutions = new Pokemon[]{PokemonList.perName.get("Aspicot"),PokemonList.perName.get("Coconfort"),PokemonList.perName.get("Dardargnan")};
        PokemonList.perName.get("Marcacrin").evolutions = new Pokemon[]{PokemonList.perName.get("Marcacrin"),PokemonList.perName.get("Cochignon"),PokemonList.perName.get("Mammochon")};
        PokemonList.perName.get("Mysdibule").evolutions = new Pokemon[]{PokemonList.perName.get("Mysdibule"),PokemonList.perName.get("Mega-Mysdibule")};
        PokemonList.perName.get("Chartor").evolutions = new Pokemon[]{};
        PokemonList.perName.get("Minotaupe").evolutions = new Pokemon[]{PokemonList.perName.get("Rototaupe"),PokemonList.perName.get("Minotaupe")};
        PokemonList.perName.get("Maskadra").evolutions = new Pokemon[]{PokemonList.perName.get("Arakdo"),PokemonList.perName.get("Maskadra")};
        PokemonList.perName.get("Yanmega").evolutions = new Pokemon[]{PokemonList.perName.get("Yanma"),PokemonList.perName.get("Yanmega")};
        PokemonList.perName.get("Melokrik").evolutions = new Pokemon[]{PokemonList.perName.get("Crikzik"),PokemonList.perName.get("Melokrik")};
        PokemonList.perName.get("Scobolide").evolutions = new Pokemon[]{PokemonList.perName.get("Venipatte"),PokemonList.perName.get("Scobolide"),PokemonList.perName.get("Brutapode")};
        PokemonList.perName.get("Massko").evolutions = new Pokemon[]{PokemonList.perName.get("Arcko"),PokemonList.perName.get("Massko"),PokemonList.perName.get("Jungko")};
        PokemonList.perName.get("Brasegali").evolutions = new Pokemon[]{PokemonList.perName.get("Poussifeu"),PokemonList.perName.get("Galifeu"),PokemonList.perName.get("Brasegali"),PokemonList.perName.get("Mega-Brasegali")};
        PokemonList.perName.get("Sepiatroce").evolutions = new Pokemon[]{PokemonList.perName.get("Sepiatop"),PokemonList.perName.get("Sepiatroce")};
        PokemonList.perName.get("Vostourno").evolutions = new Pokemon[]{PokemonList.perName.get("Vostourno"),PokemonList.perName.get("Vaututrice")};
        PokemonList.perName.get("Ossatueur").evolutions = new Pokemon[]{PokemonList.perName.get("Osselait"),PokemonList.perName.get("Ossatueur")};
        PokemonList.perName.get("Cabriolaine").evolutions = new Pokemon[]{PokemonList.perName.get("Cabriolaine"),PokemonList.perName.get("Chevroum")};
        PokemonList.perName.get("Lombre").evolutions = new Pokemon[]{PokemonList.perName.get("Nenupiot"),PokemonList.perName.get("Lombre"),PokemonList.perName.get("Ludicolo")};
        PokemonList.perName.get("Apitrini").evolutions = new Pokemon[]{PokemonList.perName.get("Apitrini"),PokemonList.perName.get("Apireine")};
        PokemonList.perName.get("Nirondelle").evolutions = new Pokemon[]{PokemonList.perName.get("Nirondelle"),PokemonList.perName.get("Heledelle")};
        PokemonList.perName.get("Chinchidou").evolutions = new Pokemon[]{PokemonList.perName.get("Chinchidou"),PokemonList.perName.get("Pashmilla")};
        PokemonList.perName.get("Arceus").evolutions = new Pokemon[]{};
        PokemonList.perName.get("Mega-Ptera").evolutions = new Pokemon[]{PokemonList.perName.get("Ptera"),PokemonList.perName.get("Mega-Ptera")};
        PokemonList.perName.get("Kadabra").evolutions = new Pokemon[]{PokemonList.perName.get("Abra"),PokemonList.perName.get("Kadabra"),PokemonList.perName.get("Alakazam"),PokemonList.perName.get("Mega-Alakazam")};
        PokemonList.perName.get("Regirock").evolutions = new Pokemon[]{};
        PokemonList.perName.get("Deoxys (Forme Attaque)").evolutions = new Pokemon[]{};
        PokemonList.perName.get("Tarpaud").evolutions = new Pokemon[]{PokemonList.perName.get("Ptitard"),PokemonList.perName.get("Tetarte"),PokemonList.perName.get("Tartard"),PokemonList.perName.get("Tarpaud")};
        PokemonList.perName.get("Sapereau").evolutions = new Pokemon[]{PokemonList.perName.get("Sapereau"),PokemonList.perName.get("Excavarenne")};
        PokemonList.perName.get("Cacturne").evolutions = new Pokemon[]{PokemonList.perName.get("Cacnea"),PokemonList.perName.get("Cacturne")};
        PokemonList.perName.get("Raichu").evolutions = new Pokemon[]{PokemonList.perName.get("Pichu"),PokemonList.perName.get("Pikachu"),PokemonList.perName.get("Raichu")};
        PokemonList.perName.get("Poissoroy").evolutions = new Pokemon[]{PokemonList.perName.get("Poissirene"),PokemonList.perName.get("Poissoroy")};
        PokemonList.perName.get("Vibraninf").evolutions = new Pokemon[]{PokemonList.perName.get("Kraknoix"),PokemonList.perName.get("Vibraninf"),PokemonList.perName.get("Libegon")};
        PokemonList.perName.get("Vacilys").evolutions = new Pokemon[]{PokemonList.perName.get("Lilia"),PokemonList.perName.get("Vacilys")};
        PokemonList.perName.get("Vivaldaim").evolutions = new Pokemon[]{PokemonList.perName.get("Vivaldaim"),PokemonList.perName.get("Haydaim")};
        PokemonList.perName.get("Tadmorv").evolutions = new Pokemon[]{PokemonList.perName.get("Tadmorv"),PokemonList.perName.get("Grotadmorv")};
        PokemonList.perName.get("Zarbi").evolutions = new Pokemon[]{};
        PokemonList.perName.get("Galifeu").evolutions = new Pokemon[]{PokemonList.perName.get("Poussifeu"),PokemonList.perName.get("Galifeu"),PokemonList.perName.get("Brasegali"),PokemonList.perName.get("Mega-Brasegali")};
        PokemonList.perName.get("Dardargnan").evolutions = new Pokemon[]{PokemonList.perName.get("Aspicot"),PokemonList.perName.get("Coconfort"),PokemonList.perName.get("Dardargnan")};
        PokemonList.perName.get("Polarhume").evolutions = new Pokemon[]{PokemonList.perName.get("Polarhume"),PokemonList.perName.get("Polagriffe")};
        PokemonList.perName.get("Tylton").evolutions = new Pokemon[]{PokemonList.perName.get("Tylton"),PokemonList.perName.get("Altaria")};
        PokemonList.perName.get("Roitiflam").evolutions = new Pokemon[]{PokemonList.perName.get("Gruikui"),PokemonList.perName.get("Grotichon"),PokemonList.perName.get("Roitiflam")};
        PokemonList.perName.get("Manternel").evolutions = new Pokemon[]{PokemonList.perName.get("Larveyette"),PokemonList.perName.get("Couverdure"),PokemonList.perName.get("Manternel")};
        PokemonList.perName.get("Cornebre").evolutions = new Pokemon[]{PokemonList.perName.get("Cornebre"),PokemonList.perName.get("Corboss")};
        PokemonList.perName.get("Terhal").evolutions = new Pokemon[]{PokemonList.perName.get("Terhal"),PokemonList.perName.get("Metang"),PokemonList.perName.get("Metalosse")};
        PokemonList.perName.get("Shaofouine").evolutions = new Pokemon[]{PokemonList.perName.get("Kungfouine"),PokemonList.perName.get("Shaofouine")};
        PokemonList.perName.get("Papilord").evolutions = new Pokemon[]{PokemonList.perName.get("Cheniti"),PokemonList.perName.get("Cheniselle"),PokemonList.perName.get("Papilord")};
        PokemonList.perName.get("Fantominus").evolutions = new Pokemon[]{PokemonList.perName.get("Fantominus"),PokemonList.perName.get("Spectrum"),PokemonList.perName.get("Ectoplasma"),PokemonList.perName.get("Mega-Ectoplasma")};
        PokemonList.perName.get("Lakmecygne").evolutions = new Pokemon[]{PokemonList.perName.get("Couaneton"),PokemonList.perName.get("Lakmecygne")};
        PokemonList.perName.get("Kraknoix").evolutions = new Pokemon[]{PokemonList.perName.get("Kraknoix"),PokemonList.perName.get("Vibraninf"),PokemonList.perName.get("Libegon")};
        PokemonList.perName.get("Leuphorie").evolutions = new Pokemon[]{PokemonList.perName.get("Ptiravi"),PokemonList.perName.get("Leveinard"),PokemonList.perName.get("Leuphorie")};
        PokemonList.perName.get("Boskara").evolutions = new Pokemon[]{PokemonList.perName.get("Tortipouss"),PokemonList.perName.get("Boskara"),PokemonList.perName.get("Torterra")};
        PokemonList.perName.get("Charkos").evolutions = new Pokemon[]{PokemonList.perName.get("Kranidos"),PokemonList.perName.get("Charkos")};
        PokemonList.perName.get("Gigalithe").evolutions = new Pokemon[]{PokemonList.perName.get("Nodulithe"),PokemonList.perName.get("Geolithe"),PokemonList.perName.get("Gigalithe")};
        PokemonList.perName.get("Roucoups").evolutions = new Pokemon[]{PokemonList.perName.get("Roucool"),PokemonList.perName.get("Roucoups"),PokemonList.perName.get("Roucarnage")};
        PokemonList.perName.get("Ecayon").evolutions = new Pokemon[]{PokemonList.perName.get("Ecayon"),PokemonList.perName.get("Lumineon")};
        PokemonList.perName.get("Statitik").evolutions = new Pokemon[]{PokemonList.perName.get("Statitik"),PokemonList.perName.get("Mygavolt")};
        PokemonList.perName.get("Teraclope").evolutions = new Pokemon[]{PokemonList.perName.get("Skelenox"),PokemonList.perName.get("Teraclope"),PokemonList.perName.get("Noctunoir")};
        PokemonList.perName.get("Aquali").evolutions = new Pokemon[]{PokemonList.perName.get("Evoli"),PokemonList.perName.get("Aquali"),PokemonList.perName.get("Voltali"),PokemonList.perName.get("Pyroli"),PokemonList.perName.get("Mentali"),PokemonList.perName.get("Noctali"),PokemonList.perName.get("Phyllali"),PokemonList.perName.get("Givrali"),PokemonList.perName.get("Nymphali")};
        PokemonList.perName.get("Geolithe").evolutions = new Pokemon[]{PokemonList.perName.get("Nodulithe"),PokemonList.perName.get("Geolithe"),PokemonList.perName.get("Gigalithe")};
        PokemonList.perName.get("Draco").evolutions = new Pokemon[]{PokemonList.perName.get("Minidraco"),PokemonList.perName.get("Draco"),PokemonList.perName.get("Dracolosse")};
        PokemonList.perName.get("Magnezone").evolutions = new Pokemon[]{PokemonList.perName.get("Magneti"),PokemonList.perName.get("Magneton"),PokemonList.perName.get("Magnezone")};
        PokemonList.perName.get("Roselia").evolutions = new Pokemon[]{PokemonList.perName.get("Rozbouton"),PokemonList.perName.get("Roselia"),PokemonList.perName.get("Roserade")};
        PokemonList.perName.get("Monaflemit").evolutions = new Pokemon[]{PokemonList.perName.get("Parecool"),PokemonList.perName.get("Vigoroth"),PokemonList.perName.get("Monaflemit")};
        PokemonList.perName.get("Spinda").evolutions = new Pokemon[]{};
        PokemonList.perName.get("Tartard").evolutions = new Pokemon[]{PokemonList.perName.get("Ptitard"),PokemonList.perName.get("Tetarte"),PokemonList.perName.get("Tartard"),PokemonList.perName.get("Tarpaud")};
        PokemonList.perName.get("Palkia").evolutions = new Pokemon[]{};
        PokemonList.perName.get("Darumarond").evolutions = new Pokemon[]{PokemonList.perName.get("Darumarond"),PokemonList.perName.get("Darumacho")};
        PokemonList.perName.get("Munna").evolutions = new Pokemon[]{PokemonList.perName.get("Munna"),PokemonList.perName.get("Mushana")};
        PokemonList.perName.get("Tauros").evolutions = new Pokemon[]{};
        PokemonList.perName.get("Etouraptor").evolutions = new Pokemon[]{PokemonList.perName.get("Etourmi"),PokemonList.perName.get("Etourvol"),PokemonList.perName.get("Etouraptor")};
        PokemonList.perName.get("Frison").evolutions = new Pokemon[]{};
        PokemonList.perName.get("Raikou").evolutions = new Pokemon[]{};
        PokemonList.perName.get("Pingoleon").evolutions = new Pokemon[]{PokemonList.perName.get("Tiplouf"),PokemonList.perName.get("Prinplouf"),PokemonList.perName.get("Pingoleon")};
        PokemonList.perName.get("Hericendre").evolutions = new Pokemon[]{PokemonList.perName.get("Hericendre"),PokemonList.perName.get("Feurisson"),PokemonList.perName.get("Typhlosion")};
        PokemonList.perName.get("Arbok").evolutions = new Pokemon[]{PokemonList.perName.get("Abo"),PokemonList.perName.get("Arbok")};
        PokemonList.perName.get("Mesmerella").evolutions = new Pokemon[]{PokemonList.perName.get("Scrutella"),PokemonList.perName.get("Mesmerella"),PokemonList.perName.get("Siderella")};
        PokemonList.perName.get("Chimpenfeu").evolutions = new Pokemon[]{PokemonList.perName.get("Ouisticram"),PokemonList.perName.get("Chimpenfeu"),PokemonList.perName.get("Simiabraz")};
        PokemonList.perName.get("Psykokwak").evolutions = new Pokemon[]{PokemonList.perName.get("Psykokwak"),PokemonList.perName.get("Akwakwak")};
        PokemonList.perName.get("Boustiflor").evolutions = new Pokemon[]{PokemonList.perName.get("Chetiflor"),PokemonList.perName.get("Boustiflor"),PokemonList.perName.get("Empiflor")};
        PokemonList.perName.get("Porygon2").evolutions = new Pokemon[]{PokemonList.perName.get("Porygon"),PokemonList.perName.get("Porygon2"),PokemonList.perName.get("Porygon-Z")};
        PokemonList.perName.get("Kaimorse").evolutions = new Pokemon[]{PokemonList.perName.get("Obalie"),PokemonList.perName.get("Phogleur"),PokemonList.perName.get("Kaimorse")};
        PokemonList.perName.get("Akwakwak").evolutions = new Pokemon[]{PokemonList.perName.get("Psykokwak"),PokemonList.perName.get("Akwakwak")};
        PokemonList.perName.get("Tygnon").evolutions = new Pokemon[]{PokemonList.perName.get("Debugant"),PokemonList.perName.get("Kicklee"),PokemonList.perName.get("Tygnon"),PokemonList.perName.get("Kapoera")};
        PokemonList.perName.get("Goinfrex").evolutions = new Pokemon[]{PokemonList.perName.get("Goinfrex"),PokemonList.perName.get("Ronflex")};
        PokemonList.perName.get("Griknot").evolutions = new Pokemon[]{PokemonList.perName.get("Griknot"),PokemonList.perName.get("Carmache"),PokemonList.perName.get("Carchacrok"),PokemonList.perName.get("Mega-Carchacrok")};
        PokemonList.perName.get("Sucroquin").evolutions = new Pokemon[]{PokemonList.perName.get("Sucroquin"),PokemonList.perName.get("Cupcanaille")};
        PokemonList.perName.get("Escargaume").evolutions = new Pokemon[]{PokemonList.perName.get("Escargaume"),PokemonList.perName.get("Limaspeed")};
        PokemonList.perName.get("Monorpale").evolutions = new Pokemon[]{PokemonList.perName.get("Monorpale"),PokemonList.perName.get("Dimocles"),PokemonList.perName.get("Exagide")};
        PokemonList.perName.get("Goupelin").evolutions = new Pokemon[]{PokemonList.perName.get("Feunnec"),PokemonList.perName.get("Roussil"),PokemonList.perName.get("Goupelin")};
        PokemonList.perName.get("Tenefix").evolutions = new Pokemon[]{};
        PokemonList.perName.get("Mustebouee").evolutions = new Pokemon[]{PokemonList.perName.get("Mustebouee"),PokemonList.perName.get("Musteflott")};
        PokemonList.perName.get("Nosferalto").evolutions = new Pokemon[]{PokemonList.perName.get("Nosferapti"),PokemonList.perName.get("Nosferalto"),PokemonList.perName.get("Nostenfer")};
        PokemonList.perName.get("Judokrak").evolutions = new Pokemon[]{};
        PokemonList.perName.get("Relicanth").evolutions = new Pokemon[]{};
        PokemonList.perName.get("Mushana").evolutions = new Pokemon[]{PokemonList.perName.get("Munna"),PokemonList.perName.get("Mushana")};
        PokemonList.perName.get("Ptiravi").evolutions = new Pokemon[]{PokemonList.perName.get("Ptiravi"),PokemonList.perName.get("Leveinard"),PokemonList.perName.get("Leuphorie")};
        PokemonList.perName.get("Coquiperl").evolutions = new Pokemon[]{PokemonList.perName.get("Coquiperl"),PokemonList.perName.get("Serpang"),PokemonList.perName.get("Rosabyss")};
        PokemonList.perName.get("Ohmassacre").evolutions = new Pokemon[]{PokemonList.perName.get("Anchwatt"),PokemonList.perName.get("Lamperoie"),PokemonList.perName.get("Ohmassacre")};
        PokemonList.perName.get("Brocelome").evolutions = new Pokemon[]{PokemonList.perName.get("Brocelome"),PokemonList.perName.get("Desseliande")};
        PokemonList.perName.get("Rozbouton").evolutions = new Pokemon[]{PokemonList.perName.get("Rozbouton"),PokemonList.perName.get("Roselia"),PokemonList.perName.get("Roserade")};
        PokemonList.perName.get("Scalproie").evolutions = new Pokemon[]{PokemonList.perName.get("Scalpion"),PokemonList.perName.get("Scalproie")};
        PokemonList.perName.get("Phogleur").evolutions = new Pokemon[]{PokemonList.perName.get("Obalie"),PokemonList.perName.get("Phogleur"),PokemonList.perName.get("Kaimorse")};
        PokemonList.perName.get("Neitram").evolutions = new Pokemon[]{PokemonList.perName.get("Lewsor"),PokemonList.perName.get("Neitram")};
        PokemonList.perName.get("Chovsourir").evolutions = new Pokemon[]{PokemonList.perName.get("Chovsourir"),PokemonList.perName.get("Rhinolove")};
        PokemonList.perName.get("Musteflott").evolutions = new Pokemon[]{PokemonList.perName.get("Mustebouee"),PokemonList.perName.get("Musteflott")};
        PokemonList.perName.get("Insolourdo").evolutions = new Pokemon[]{};
        PokemonList.perName.get("Mega-Tyranocif").evolutions = new Pokemon[]{PokemonList.perName.get("Embrylex"),PokemonList.perName.get("Ymphect"),PokemonList.perName.get("Tyranocif"),PokemonList.perName.get("Mega-Tyranocif")};
        PokemonList.perName.get("Munja").evolutions = new Pokemon[]{PokemonList.perName.get("Ningale"),PokemonList.perName.get("Ninjask"),PokemonList.perName.get("Munja")};
        PokemonList.perName.get("Drakkarmin").evolutions = new Pokemon[]{};
        PokemonList.perName.get("Sorbouboul").evolutions = new Pokemon[]{PokemonList.perName.get("Sorbebe"),PokemonList.perName.get("Sorboul"),PokemonList.perName.get("Sorbouboul")};
        PokemonList.perName.get("Mega-Blizzaroi").evolutions = new Pokemon[]{PokemonList.perName.get("Blizzi"),PokemonList.perName.get("Blizzaroi"),PokemonList.perName.get("Mega-Blizzaroi")};
        PokemonList.perName.get("Zekrom").evolutions = new Pokemon[]{};
        PokemonList.perName.get("Remoraid").evolutions = new Pokemon[]{PokemonList.perName.get("Remoraid"),PokemonList.perName.get("Octillery")};
        PokemonList.perName.get("Mamanbo").evolutions = new Pokemon[]{};
        PokemonList.perName.get("Meios").evolutions = new Pokemon[]{PokemonList.perName.get("Nucleos"),PokemonList.perName.get("Meios"),PokemonList.perName.get("Symbios200e"),PokemonList.perName.get("Nucleos"),PokemonList.perName.get("Meios")};
        PokemonList.perName.get("Noctali").evolutions = new Pokemon[]{PokemonList.perName.get("Evoli"),PokemonList.perName.get("Aquali"),PokemonList.perName.get("Voltali"),PokemonList.perName.get("Pyroli"),PokemonList.perName.get("Mentali"),PokemonList.perName.get("Noctali"),PokemonList.perName.get("Phyllali"),PokemonList.perName.get("Givrali"),PokemonList.perName.get("Nymphali")};
        PokemonList.perName.get("Mega-Pharamp").evolutions = new Pokemon[]{PokemonList.perName.get("Wattouat"),PokemonList.perName.get("Lainergie"),PokemonList.perName.get("Pharamp"),PokemonList.perName.get("Mega-Pharamp")};
        PokemonList.perName.get("Ramoloss").evolutions = new Pokemon[]{PokemonList.perName.get("Ramoloss"),PokemonList.perName.get("Flagadoss"),PokemonList.perName.get("Roigada")};
        PokemonList.perName.get("Cupcanaille").evolutions = new Pokemon[]{PokemonList.perName.get("Sucroquin"),PokemonList.perName.get("Cupcanaille")};
        PokemonList.perName.get("Carabaffe").evolutions = new Pokemon[]{PokemonList.perName.get("Carapuce"),PokemonList.perName.get("Carabaffe"),PokemonList.perName.get("Tortank"),PokemonList.perName.get("Mega-Tortank")};
        PokemonList.perName.get("Barbicha").evolutions = new Pokemon[]{PokemonList.perName.get("Barloche"),PokemonList.perName.get("Barbicha")};
        PokemonList.perName.get("Colombeau").evolutions = new Pokemon[]{PokemonList.perName.get("Poichigeon"),PokemonList.perName.get("Colombeau"),PokemonList.perName.get("Deflaisan")};
        PokemonList.perName.get("Baggaid").evolutions = new Pokemon[]{PokemonList.perName.get("Baggiguane"),PokemonList.perName.get("Baggaid")};
        PokemonList.perName.get("Ramboum").evolutions = new Pokemon[]{PokemonList.perName.get("Chuchmur"),PokemonList.perName.get("Ramboum"),PokemonList.perName.get("Brouhabam")};
        PokemonList.perName.get("Kicklee").evolutions = new Pokemon[]{PokemonList.perName.get("Debugant"),PokemonList.perName.get("Kicklee"),PokemonList.perName.get("Tygnon"),PokemonList.perName.get("Kapoera")};
        PokemonList.perName.get("Teddiursa").evolutions = new Pokemon[]{PokemonList.perName.get("Teddiursa"),PokemonList.perName.get("Ursaring")};
        PokemonList.perName.get("Karaclee").evolutions = new Pokemon[]{};
        PokemonList.perName.get("Serpang").evolutions = new Pokemon[]{PokemonList.perName.get("Coquiperl"),PokemonList.perName.get("Serpang"),PokemonList.perName.get("Rosabyss")};
        PokemonList.perName.get("Porygon").evolutions = new Pokemon[]{PokemonList.perName.get("Porygon"),PokemonList.perName.get("Porygon2"),PokemonList.perName.get("Porygon-Z")};
        PokemonList.perName.get("Mastouffe").evolutions = new Pokemon[]{PokemonList.perName.get("Ponchiot"),PokemonList.perName.get("Ponchien"),PokemonList.perName.get("Mastouffe")};
        PokemonList.perName.get("Pyrax").evolutions = new Pokemon[]{PokemonList.perName.get("Pyronille"),PokemonList.perName.get("Pyrax")};
        PokemonList.perName.get("Majaspic").evolutions = new Pokemon[]{PokemonList.perName.get("Vipelierre"),PokemonList.perName.get("Lianaja"),PokemonList.perName.get("Majaspic")};
        PokemonList.perName.get("Blindalys").evolutions = new Pokemon[]{PokemonList.perName.get("Chenipotte"),PokemonList.perName.get("Armulys"),PokemonList.perName.get("Blindalys"),PokemonList.perName.get("Charmillon"),PokemonList.perName.get("Papinox")};
        PokemonList.perName.get("Nenupiot").evolutions = new Pokemon[]{PokemonList.perName.get("Nenupiot"),PokemonList.perName.get("Lombre"),PokemonList.perName.get("Ludicolo")};
        PokemonList.perName.get("Foretress").evolutions = new Pokemon[]{PokemonList.perName.get("Pomdepik"),PokemonList.perName.get("Foretress")};
        PokemonList.perName.get("Mimitoss").evolutions = new Pokemon[]{PokemonList.perName.get("Mimitoss"),PokemonList.perName.get("Aeromite")};
        PokemonList.perName.get("Lippoutou").evolutions = new Pokemon[]{PokemonList.perName.get("Lippouti"),PokemonList.perName.get("Lippoutou")};
        PokemonList.perName.get("Negapi").evolutions = new Pokemon[]{};
        PokemonList.perName.get("Mega-Leviator").evolutions = new Pokemon[]{PokemonList.perName.get("Magicarpe"),PokemonList.perName.get("Leviator"),PokemonList.perName.get("Mega-Leviator")};
        PokemonList.perName.get("Mega-Dracaufeu Y").evolutions = new Pokemon[]{PokemonList.perName.get("Salameche"),PokemonList.perName.get("Reptincel"),PokemonList.perName.get("Dracaufeu"),PokemonList.perName.get("Mega-Dracaufeu X"),PokemonList.perName.get("Mega-Dracaufeu Y")};
        PokemonList.perName.get("Colimucus").evolutions = new Pokemon[]{PokemonList.perName.get("Mucuscule"),PokemonList.perName.get("Colimucus"),PokemonList.perName.get("Muplodocus")};
        PokemonList.perName.get("Ouisticram").evolutions = new Pokemon[]{PokemonList.perName.get("Ouisticram"),PokemonList.perName.get("Chimpenfeu"),PokemonList.perName.get("Simiabraz")};
        PokemonList.perName.get("Gruikui").evolutions = new Pokemon[]{PokemonList.perName.get("Gruikui"),PokemonList.perName.get("Grotichon"),PokemonList.perName.get("Roitiflam")};
        PokemonList.perName.get("Gallame").evolutions = new Pokemon[]{PokemonList.perName.get("Tarsal"),PokemonList.perName.get("Kirlia"),PokemonList.perName.get("Gardevoir"),PokemonList.perName.get("Gallame"),PokemonList.perName.get("Mega-Gardevoir")};
        PokemonList.perName.get("Flotajou").evolutions = new Pokemon[]{PokemonList.perName.get("Flotajou"),PokemonList.perName.get("Flotoutan")};
        PokemonList.perName.get("Pandespiegle").evolutions = new Pokemon[]{PokemonList.perName.get("Pandespiegle"),PokemonList.perName.get("Pandarbare")};
        PokemonList.perName.get("Muplodocus").evolutions = new Pokemon[]{PokemonList.perName.get("Mucuscule"),PokemonList.perName.get("Colimucus"),PokemonList.perName.get("Muplodocus")};
        PokemonList.perName.get("Blindepique").evolutions = new Pokemon[]{PokemonList.perName.get("Marisson"),PokemonList.perName.get("Boguerisse"),PokemonList.perName.get("Blindepique")};
        PokemonList.perName.get("Melancolux").evolutions = new Pokemon[]{PokemonList.perName.get("Funecire"),PokemonList.perName.get("Melancolux"),PokemonList.perName.get("Lugulabre")};
        PokemonList.perName.get("Viridium").evolutions = new Pokemon[]{};
        PokemonList.perName.get("Fouinette").evolutions = new Pokemon[]{PokemonList.perName.get("Fouinette"),PokemonList.perName.get("Fouinar")};
        PokemonList.perName.get("Desseliande").evolutions = new Pokemon[]{PokemonList.perName.get("Brocelome"),PokemonList.perName.get("Desseliande")};
        PokemonList.perName.get("Seviper").evolutions = new Pokemon[]{};
        PokemonList.perName.get("Germignon").evolutions = new Pokemon[]{PokemonList.perName.get("Germignon"),PokemonList.perName.get("Macronium"),PokemonList.perName.get("Meganium")};
        PokemonList.perName.get("Ponchiot").evolutions = new Pokemon[]{PokemonList.perName.get("Ponchiot"),PokemonList.perName.get("Ponchien"),PokemonList.perName.get("Mastouffe")};
        PokemonList.perName.get("Typhlosion").evolutions = new Pokemon[]{PokemonList.perName.get("Hericendre"),PokemonList.perName.get("Feurisson"),PokemonList.perName.get("Typhlosion")};
        PokemonList.perName.get("Demeteros (Forme Avatar)").evolutions = new Pokemon[]{};
        PokemonList.perName.get("Feunard").evolutions = new Pokemon[]{PokemonList.perName.get("Goupix"),PokemonList.perName.get("Feunard")};
        PokemonList.perName.get("Magneti").evolutions = new Pokemon[]{PokemonList.perName.get("Magneti"),PokemonList.perName.get("Magneton"),PokemonList.perName.get("Magnezone")};
        PokemonList.perName.get("Cobaltium").evolutions = new Pokemon[]{};
        PokemonList.perName.get("Persian").evolutions = new Pokemon[]{PokemonList.perName.get("Miaouss"),PokemonList.perName.get("Persian")};
        PokemonList.perName.get("Nidoking").evolutions = new Pokemon[]{PokemonList.perName.get("Nidoran M"),PokemonList.perName.get("Nidorino"),PokemonList.perName.get("Nidoking")};
        PokemonList.perName.get("Ninjask").evolutions = new Pokemon[]{PokemonList.perName.get("Ningale"),PokemonList.perName.get("Ninjask"),PokemonList.perName.get("Munja")};
        PokemonList.perName.get("Amphinobi").evolutions = new Pokemon[]{PokemonList.perName.get("Grenousse"),PokemonList.perName.get("Croaporal"),PokemonList.perName.get("Amphinobi")};
        PokemonList.perName.get("Nemelios").evolutions = new Pokemon[]{PokemonList.perName.get("Helionceau"),PokemonList.perName.get("Nemelios")};
        PokemonList.perName.get("Medhyena").evolutions = new Pokemon[]{PokemonList.perName.get("Medhyena"),PokemonList.perName.get("Grahyena")};
        PokemonList.perName.get("Evoli").evolutions = new Pokemon[]{PokemonList.perName.get("Evoli"),PokemonList.perName.get("Aquali"),PokemonList.perName.get("Voltali"),PokemonList.perName.get("Pyroli"),PokemonList.perName.get("Mentali"),PokemonList.perName.get("Noctali"),PokemonList.perName.get("Phyllali"),PokemonList.perName.get("Givrali"),PokemonList.perName.get("Nymphali")};
        PokemonList.perName.get("Barloche").evolutions = new Pokemon[]{PokemonList.perName.get("Barloche"),PokemonList.perName.get("Barbicha")};
        PokemonList.perName.get("Kabuto").evolutions = new Pokemon[]{PokemonList.perName.get("Kabuto"),PokemonList.perName.get("Kabutops")};
        PokemonList.perName.get("Grenousse").evolutions = new Pokemon[]{PokemonList.perName.get("Grenousse"),PokemonList.perName.get("Croaporal"),PokemonList.perName.get("Amphinobi")};
        PokemonList.perName.get("Kaorine").evolutions = new Pokemon[]{PokemonList.perName.get("Balbuto"),PokemonList.perName.get("Kaorine")};
        PokemonList.perName.get("Debugant").evolutions = new Pokemon[]{PokemonList.perName.get("Debugant"),PokemonList.perName.get("Kicklee"),PokemonList.perName.get("Tygnon"),PokemonList.perName.get("Kapoera")};
        PokemonList.perName.get("Ningale").evolutions = new Pokemon[]{PokemonList.perName.get("Ningale"),PokemonList.perName.get("Ninjask"),PokemonList.perName.get("Munja")};
        PokemonList.perName.get("Capidextre").evolutions = new Pokemon[]{PokemonList.perName.get("Capumain"),PokemonList.perName.get("Capidextre")};
        PokemonList.perName.get("Tic").evolutions = new Pokemon[]{PokemonList.perName.get("Tic"),PokemonList.perName.get("Clic"),PokemonList.perName.get("Cliticlic")};
        PokemonList.perName.get("Piafabec").evolutions = new Pokemon[]{PokemonList.perName.get("Piafabec"),PokemonList.perName.get("Rapasdepic")};
        PokemonList.perName.get("Camerupt").evolutions = new Pokemon[]{PokemonList.perName.get("Chamallot"),PokemonList.perName.get("Camerupt")};
        PokemonList.perName.get("Goelise").evolutions = new Pokemon[]{PokemonList.perName.get("Goelise"),PokemonList.perName.get("Bekipan")};
        PokemonList.perName.get("Funecire").evolutions = new Pokemon[]{PokemonList.perName.get("Funecire"),PokemonList.perName.get("Melancolux"),PokemonList.perName.get("Lugulabre")};
        PokemonList.perName.get("Golgopathe").evolutions = new Pokemon[]{PokemonList.perName.get("Opermine"),PokemonList.perName.get("Golgopathe")};
        PokemonList.perName.get("Reshiram").evolutions = new Pokemon[]{};
        PokemonList.perName.get("Excelangue").evolutions = new Pokemon[]{PokemonList.perName.get("Excelangue"),PokemonList.perName.get("Coudlangue")};
        PokemonList.perName.get("Tetarte").evolutions = new Pokemon[]{PokemonList.perName.get("Ptitard"),PokemonList.perName.get("Tetarte"),PokemonList.perName.get("Tartard"),PokemonList.perName.get("Tarpaud")};
        PokemonList.perName.get("Mega-Ectoplasma").evolutions = new Pokemon[]{PokemonList.perName.get("Fantominus"),PokemonList.perName.get("Spectrum"),PokemonList.perName.get("Ectoplasma"),PokemonList.perName.get("Mega-Ectoplasma")};
        PokemonList.perName.get("Flingouste").evolutions = new Pokemon[]{PokemonList.perName.get("Flingouste"),PokemonList.perName.get("Gamblast")};
        PokemonList.perName.get("Aligatueur").evolutions = new Pokemon[]{PokemonList.perName.get("Kaiminus"),PokemonList.perName.get("Crocrodil"),PokemonList.perName.get("Aligatueur")};
        PokemonList.perName.get("Magireve").evolutions = new Pokemon[]{PokemonList.perName.get("Feuforeve"),PokemonList.perName.get("Magireve")};
        PokemonList.perName.get("Luxray").evolutions = new Pokemon[]{PokemonList.perName.get("Lixy"),PokemonList.perName.get("Luxio"),PokemonList.perName.get("Luxray")};
        PokemonList.perName.get("Rosabyss").evolutions = new Pokemon[]{PokemonList.perName.get("Coquiperl"),PokemonList.perName.get("Serpang"),PokemonList.perName.get("Rosabyss")};
        PokemonList.perName.get("Galekid").evolutions = new Pokemon[]{PokemonList.perName.get("Galekid"),PokemonList.perName.get("Galegon"),PokemonList.perName.get("Galeking"),PokemonList.perName.get("Mega-Galeking")};
        PokemonList.perName.get("Ptera").evolutions = new Pokemon[]{PokemonList.perName.get("Ptera"),PokemonList.perName.get("Mega-Ptera")};
        PokemonList.perName.get("Galopa").evolutions = new Pokemon[]{PokemonList.perName.get("Ponyta"),PokemonList.perName.get("Galopa")};
        PokemonList.perName.get("Roigada").evolutions = new Pokemon[]{PokemonList.perName.get("Ramoloss"),PokemonList.perName.get("Flagadoss"),PokemonList.perName.get("Roigada")};
        PokemonList.perName.get("Jirachi").evolutions = new Pokemon[]{};
        PokemonList.perName.get("Pitrouille (Taille Mini)").evolutions = new Pokemon[]{};
        PokemonList.perName.get("Marisson").evolutions = new Pokemon[]{PokemonList.perName.get("Marisson"),PokemonList.perName.get("Boguerisse"),PokemonList.perName.get("Blindepique")};
        PokemonList.perName.get("Mascaiman").evolutions = new Pokemon[]{PokemonList.perName.get("Mascaiman"),PokemonList.perName.get("Escroco"),PokemonList.perName.get("Crocorible")};
        PokemonList.perName.get("Carapuce").evolutions = new Pokemon[]{PokemonList.perName.get("Carapuce"),PokemonList.perName.get("Carabaffe"),PokemonList.perName.get("Tortank"),PokemonList.perName.get("Mega-Tortank")};
        PokemonList.perName.get("Mangriff").evolutions = new Pokemon[]{};
        PokemonList.perName.get("Latias").evolutions = new Pokemon[]{};
        PokemonList.perName.get("Grahyena").evolutions = new Pokemon[]{PokemonList.perName.get("Medhyena"),PokemonList.perName.get("Grahyena")};
        PokemonList.perName.get("Lugia").evolutions = new Pokemon[]{};
        PokemonList.perName.get("Onix").evolutions = new Pokemon[]{PokemonList.perName.get("Onix"),PokemonList.perName.get("Steelix")};
        PokemonList.perName.get("Pyroli").evolutions = new Pokemon[]{PokemonList.perName.get("Evoli"),PokemonList.perName.get("Aquali"),PokemonList.perName.get("Voltali"),PokemonList.perName.get("Pyroli"),PokemonList.perName.get("Mentali"),PokemonList.perName.get("Noctali"),PokemonList.perName.get("Phyllali"),PokemonList.perName.get("Givrali"),PokemonList.perName.get("Nymphali")};
        PokemonList.perName.get("Magneton").evolutions = new Pokemon[]{PokemonList.perName.get("Magneti"),PokemonList.perName.get("Magneton"),PokemonList.perName.get("Magnezone")};
        PokemonList.perName.get("Incisache").evolutions = new Pokemon[]{PokemonList.perName.get("Coupenotte"),PokemonList.perName.get("Incisache"),PokemonList.perName.get("Tranchodon")};
        PokemonList.perName.get("Kokiyas").evolutions = new Pokemon[]{PokemonList.perName.get("Kokiyas"),PokemonList.perName.get("Crustabri")};
        PokemonList.perName.get("Racaillou").evolutions = new Pokemon[]{PokemonList.perName.get("Racaillou"),PokemonList.perName.get("Gravalanch"),PokemonList.perName.get("Grolem")};
        PokemonList.perName.get("Colhomard").evolutions = new Pokemon[]{PokemonList.perName.get("Ecrapince"),PokemonList.perName.get("Colhomard")};
        PokemonList.perName.get("Papinox").evolutions = new Pokemon[]{PokemonList.perName.get("Chenipotte"),PokemonList.perName.get("Armulys"),PokemonList.perName.get("Blindalys"),PokemonList.perName.get("Charmillon"),PokemonList.perName.get("Papinox")};
        PokemonList.perName.get("Manaphy").evolutions = new Pokemon[]{};
        PokemonList.perName.get("Crocrodil").evolutions = new Pokemon[]{PokemonList.perName.get("Kaiminus"),PokemonList.perName.get("Crocrodil"),PokemonList.perName.get("Aligatueur")};
        PokemonList.perName.get("Ectoplasma").evolutions = new Pokemon[]{PokemonList.perName.get("Fantominus"),PokemonList.perName.get("Spectrum"),PokemonList.perName.get("Ectoplasma"),PokemonList.perName.get("Mega-Ectoplasma")};
        PokemonList.perName.get("Nucleos").evolutions = new Pokemon[]{PokemonList.perName.get("Nucleos"),PokemonList.perName.get("Meios"),PokemonList.perName.get("Symbios200e"),PokemonList.perName.get("Nucleos"),PokemonList.perName.get("Meios")};
        PokemonList.perName.get("Vortente").evolutions = new Pokemon[]{};
        PokemonList.perName.get("Ecrapince").evolutions = new Pokemon[]{PokemonList.perName.get("Ecrapince"),PokemonList.perName.get("Colhomard")};
        PokemonList.perName.get("Coxyclaque").evolutions = new Pokemon[]{PokemonList.perName.get("Coxy"),PokemonList.perName.get("Coxyclaque")};
        PokemonList.perName.get("Lugulabre").evolutions = new Pokemon[]{PokemonList.perName.get("Funecire"),PokemonList.perName.get("Melancolux"),PokemonList.perName.get("Lugulabre")};
        PokemonList.perName.get("Moyade").evolutions = new Pokemon[]{PokemonList.perName.get("Viskuse"),PokemonList.perName.get("Moyade")};
        PokemonList.perName.get("Delcatty").evolutions = new Pokemon[]{PokemonList.perName.get("Skitty"),PokemonList.perName.get("Delcatty")};
        PokemonList.perName.get("Floette").evolutions = new Pokemon[]{PokemonList.perName.get("Flabebe"),PokemonList.perName.get("Floette"),PokemonList.perName.get("Florges")};
        PokemonList.perName.get("Tutankafer").evolutions = new Pokemon[]{PokemonList.perName.get("Tutafeh"),PokemonList.perName.get("Tutankafer")};
        PokemonList.perName.get("Meditikka").evolutions = new Pokemon[]{PokemonList.perName.get("Meditikka"),PokemonList.perName.get("Charmina"),PokemonList.perName.get("Mega-Charmina")};
        PokemonList.perName.get("Nanmeouie").evolutions = new Pokemon[]{};
        PokemonList.perName.get("Feunnec").evolutions = new Pokemon[]{PokemonList.perName.get("Feunnec"),PokemonList.perName.get("Roussil"),PokemonList.perName.get("Goupelin")};
        PokemonList.perName.get("Archeodong").evolutions = new Pokemon[]{PokemonList.perName.get("Archeomire"),PokemonList.perName.get("Archeodong")};
        PokemonList.perName.get("Axoloto").evolutions = new Pokemon[]{PokemonList.perName.get("Axoloto"),PokemonList.perName.get("Maraiste")};
        PokemonList.perName.get("Macronium").evolutions = new Pokemon[]{PokemonList.perName.get("Germignon"),PokemonList.perName.get("Macronium"),PokemonList.perName.get("Meganium")};
        PokemonList.perName.get("Rafflesia").evolutions = new Pokemon[]{PokemonList.perName.get("Mystherbe"),PokemonList.perName.get("Ortide"),PokemonList.perName.get("Rafflesia"),PokemonList.perName.get("Joliflor")};
        PokemonList.perName.get("Caratroc").evolutions = new Pokemon[]{};
        PokemonList.perName.get("Shaymin (Forme Celeste)").evolutions = new Pokemon[]{};
        PokemonList.perName.get("Ponchien").evolutions = new Pokemon[]{PokemonList.perName.get("Ponchiot"),PokemonList.perName.get("Ponchien"),PokemonList.perName.get("Mastouffe")};
        PokemonList.perName.get("Pifeuil").evolutions = new Pokemon[]{PokemonList.perName.get("Grainipiot"),PokemonList.perName.get("Pifeuil"),PokemonList.perName.get("Tengalice")};
        PokemonList.perName.get("Toudoudou").evolutions = new Pokemon[]{PokemonList.perName.get("Toudoudou"),PokemonList.perName.get("Rondoudou"),PokemonList.perName.get("Grodoudou")};
        PokemonList.perName.get("Sablaireau").evolutions = new Pokemon[]{PokemonList.perName.get("Sabelette"),PokemonList.perName.get("Sablaireau")};
        PokemonList.perName.get("Banshitrouye (Taille Mini)").evolutions = new Pokemon[]{};
        PokemonList.perName.get("Draby").evolutions = new Pokemon[]{PokemonList.perName.get("Draby"),PokemonList.perName.get("Drackhaus"),PokemonList.perName.get("Drattak")};
        PokemonList.perName.get("Rayquaza").evolutions = new Pokemon[]{};
        PokemonList.perName.get("Granivol").evolutions = new Pokemon[]{PokemonList.perName.get("Granivol"),PokemonList.perName.get("Floravol"),PokemonList.perName.get("Cotovol")};
        PokemonList.perName.get("Luxio").evolutions = new Pokemon[]{PokemonList.perName.get("Lixy"),PokemonList.perName.get("Luxio"),PokemonList.perName.get("Luxray")};
        PokemonList.perName.get("Ceriflor").evolutions = new Pokemon[]{PokemonList.perName.get("Ceribou"),PokemonList.perName.get("Ceriflor")};
        PokemonList.perName.get("Dimoret").evolutions = new Pokemon[]{PokemonList.perName.get("Farfuret"),PokemonList.perName.get("Dimoret")};
        PokemonList.perName.get("Amonita").evolutions = new Pokemon[]{PokemonList.perName.get("Amonita"),PokemonList.perName.get("Amonistar")};
        PokemonList.perName.get("Larveyette").evolutions = new Pokemon[]{PokemonList.perName.get("Larveyette"),PokemonList.perName.get("Couverdure"),PokemonList.perName.get("Manternel")};
        PokemonList.perName.get("Krabboss").evolutions = new Pokemon[]{PokemonList.perName.get("Krabby"),PokemonList.perName.get("Krabboss")};
        PokemonList.perName.get("Batracne").evolutions = new Pokemon[]{PokemonList.perName.get("Tritonde"),PokemonList.perName.get("Batracne"),PokemonList.perName.get("Crapustule")};
        PokemonList.perName.get("Tentacool").evolutions = new Pokemon[]{PokemonList.perName.get("Tentacool"),PokemonList.perName.get("Tentacruel")};
        PokemonList.perName.get("Hippodocus").evolutions = new Pokemon[]{PokemonList.perName.get("Hippopotas"),PokemonList.perName.get("Hippodocus")};
        PokemonList.perName.get("Wailmer").evolutions = new Pokemon[]{PokemonList.perName.get("Wailmer"),PokemonList.perName.get("Wailord")};
        PokemonList.perName.get("Magmar").evolutions = new Pokemon[]{PokemonList.perName.get("Magby"),PokemonList.perName.get("Magmar"),PokemonList.perName.get("Maganon")};
        PokemonList.perName.get("Caninos").evolutions = new Pokemon[]{PokemonList.perName.get("Caninos"),PokemonList.perName.get("Arcanin")};
        PokemonList.perName.get("Seleroc").evolutions = new Pokemon[]{};
        PokemonList.perName.get("Lucario").evolutions = new Pokemon[]{PokemonList.perName.get("Riolu"),PokemonList.perName.get("Lucario"),PokemonList.perName.get("Mega-Lucario")};
        PokemonList.perName.get("Machopeur").evolutions = new Pokemon[]{PokemonList.perName.get("Machoc"),PokemonList.perName.get("Machopeur"),PokemonList.perName.get("Mackogneur")};
        PokemonList.perName.get("Barpau").evolutions = new Pokemon[]{PokemonList.perName.get("Barpau"),PokemonList.perName.get("Milobellus")};
        PokemonList.perName.get("Armulys").evolutions = new Pokemon[]{PokemonList.perName.get("Chenipotte"),PokemonList.perName.get("Armulys"),PokemonList.perName.get("Blindalys"),PokemonList.perName.get("Charmillon"),PokemonList.perName.get("Papinox")};
        PokemonList.perName.get("Drascore").evolutions = new Pokemon[]{PokemonList.perName.get("Rapion"),PokemonList.perName.get("Drascore")};
        PokemonList.perName.get("Coudlangue").evolutions = new Pokemon[]{PokemonList.perName.get("Excelangue"),PokemonList.perName.get("Coudlangue")};
        PokemonList.perName.get("Tarinorme").evolutions = new Pokemon[]{PokemonList.perName.get("Tarinor"),PokemonList.perName.get("Tarinorme")};
        PokemonList.perName.get("Lovdisc").evolutions = new Pokemon[]{};
        PokemonList.perName.get("Saquedeneu").evolutions = new Pokemon[]{PokemonList.perName.get("Saquedeneu"),PokemonList.perName.get("Bouldeneu")};
        PokemonList.perName.get("Tengalice").evolutions = new Pokemon[]{PokemonList.perName.get("Grainipiot"),PokemonList.perName.get("Pifeuil"),PokemonList.perName.get("Tengalice")};
        PokemonList.perName.get("Golemastoc").evolutions = new Pokemon[]{PokemonList.perName.get("Gringolem"),PokemonList.perName.get("Golemastoc")};
        PokemonList.perName.get("Diamat").evolutions = new Pokemon[]{PokemonList.perName.get("Solochi"),PokemonList.perName.get("Diamat"),PokemonList.perName.get("Trioxhydre")};
        PokemonList.perName.get("Phyllali").evolutions = new Pokemon[]{PokemonList.perName.get("Evoli"),PokemonList.perName.get("Aquali"),PokemonList.perName.get("Voltali"),PokemonList.perName.get("Pyroli"),PokemonList.perName.get("Mentali"),PokemonList.perName.get("Noctali"),PokemonList.perName.get("Phyllali"),PokemonList.perName.get("Givrali"),PokemonList.perName.get("Nymphali")};
        PokemonList.perName.get("Mistigrix").evolutions = new Pokemon[]{PokemonList.perName.get("Psystigri"),PokemonList.perName.get("Mistigrix")};
        PokemonList.perName.get("Grotichon").evolutions = new Pokemon[]{PokemonList.perName.get("Gruikui"),PokemonList.perName.get("Grotichon"),PokemonList.perName.get("Roitiflam")};
        PokemonList.perName.get("Tropius").evolutions = new Pokemon[]{};
        PokemonList.perName.get("Salameche").evolutions = new Pokemon[]{PokemonList.perName.get("Salameche"),PokemonList.perName.get("Reptincel"),PokemonList.perName.get("Dracaufeu"),PokemonList.perName.get("Mega-Dracaufeu X"),PokemonList.perName.get("Mega-Dracaufeu Y")};
        PokemonList.perName.get("Victini").evolutions = new Pokemon[]{};
        PokemonList.perName.get("Ymphect").evolutions = new Pokemon[]{PokemonList.perName.get("Embrylex"),PokemonList.perName.get("Ymphect"),PokemonList.perName.get("Tyranocif"),PokemonList.perName.get("Mega-Tyranocif")};
        PokemonList.perName.get("Artikodin").evolutions = new Pokemon[]{};
        PokemonList.perName.get("Phione").evolutions = new Pokemon[]{};
        PokemonList.perName.get("Miaouss").evolutions = new Pokemon[]{PokemonList.perName.get("Miaouss"),PokemonList.perName.get("Persian")};
        PokemonList.perName.get("Braisillon").evolutions = new Pokemon[]{PokemonList.perName.get("Passerouge"),PokemonList.perName.get("Braisillon"),PokemonList.perName.get("Flambusard")};
        PokemonList.perName.get("Migalos").evolutions = new Pokemon[]{PokemonList.perName.get("Mimigal"),PokemonList.perName.get("Migalos")};
        PokemonList.perName.get("Manzai").evolutions = new Pokemon[]{PokemonList.perName.get("Manzai"),PokemonList.perName.get("Simularbre")};
        PokemonList.perName.get("Nosferapti").evolutions = new Pokemon[]{PokemonList.perName.get("Nosferapti"),PokemonList.perName.get("Nosferalto"),PokemonList.perName.get("Nostenfer")};
        PokemonList.perName.get("Arakdo").evolutions = new Pokemon[]{PokemonList.perName.get("Arakdo"),PokemonList.perName.get("Maskadra")};
        PokemonList.perName.get("Kaiminus").evolutions = new Pokemon[]{PokemonList.perName.get("Kaiminus"),PokemonList.perName.get("Crocrodil"),PokemonList.perName.get("Aligatueur")};
        PokemonList.perName.get("Charmillon").evolutions = new Pokemon[]{PokemonList.perName.get("Chenipotte"),PokemonList.perName.get("Armulys"),PokemonList.perName.get("Blindalys"),PokemonList.perName.get("Charmillon"),PokemonList.perName.get("Papinox")};
        PokemonList.perName.get("Zebibron").evolutions = new Pokemon[]{PokemonList.perName.get("Zebibron"),PokemonList.perName.get("Zeblitz")};
        PokemonList.perName.get("Coupenotte").evolutions = new Pokemon[]{PokemonList.perName.get("Coupenotte"),PokemonList.perName.get("Incisache"),PokemonList.perName.get("Tranchodon")};
        PokemonList.perName.get("Muciole").evolutions = new Pokemon[]{};
        PokemonList.perName.get("Cizayox").evolutions = new Pokemon[]{PokemonList.perName.get("Insecateur"),PokemonList.perName.get("Cizayox"),PokemonList.perName.get("Mega-Cizayox")};
        PokemonList.perName.get("Triopikeur").evolutions = new Pokemon[]{PokemonList.perName.get("Taupiqueur"),PokemonList.perName.get("Triopikeur")};
        PokemonList.perName.get("Floravol").evolutions = new Pokemon[]{PokemonList.perName.get("Granivol"),PokemonList.perName.get("Floravol"),PokemonList.perName.get("Cotovol")};
        PokemonList.perName.get("Ouvrifier").evolutions = new Pokemon[]{PokemonList.perName.get("Charpenti"),PokemonList.perName.get("Ouvrifier"),PokemonList.perName.get("Betochef")};
        PokemonList.perName.get("Darkrai").evolutions = new Pokemon[]{};
        PokemonList.perName.get("Mew").evolutions = new Pokemon[]{};
        PokemonList.perName.get("Grindur").evolutions = new Pokemon[]{PokemonList.perName.get("Grindur"),PokemonList.perName.get("Noacier")};
        PokemonList.perName.get("Balignon").evolutions = new Pokemon[]{PokemonList.perName.get("Balignon"),PokemonList.perName.get("Chapignon")};
        PokemonList.perName.get("Kravarech").evolutions = new Pokemon[]{PokemonList.perName.get("Venalgue"),PokemonList.perName.get("Kravarech")};
        PokemonList.perName.get("Chaglam").evolutions = new Pokemon[]{PokemonList.perName.get("Chaglam"),PokemonList.perName.get("Chaffreux")};
        PokemonList.perName.get("Xerneas").evolutions = new Pokemon[]{};
        PokemonList.perName.get("Cadoizo").evolutions = new Pokemon[]{};
        PokemonList.perName.get("Mega-Kangourex").evolutions = new Pokemon[]{PokemonList.perName.get("Kangourex"),PokemonList.perName.get("Mega-Kangourex")};
        PokemonList.perName.get("Chapignon").evolutions = new Pokemon[]{PokemonList.perName.get("Balignon"),PokemonList.perName.get("Chapignon")};
        PokemonList.perName.get("Lanturn").evolutions = new Pokemon[]{PokemonList.perName.get("Loupio"),PokemonList.perName.get("Lanturn")};
        PokemonList.perName.get("Simiabraz").evolutions = new Pokemon[]{PokemonList.perName.get("Ouisticram"),PokemonList.perName.get("Chimpenfeu"),PokemonList.perName.get("Simiabraz")};
        PokemonList.perName.get("Bruyverne").evolutions = new Pokemon[]{PokemonList.perName.get("Sonistrelle"),PokemonList.perName.get("Bruyverne")};
        PokemonList.perName.get("Mucuscule").evolutions = new Pokemon[]{PokemonList.perName.get("Mucuscule"),PokemonList.perName.get("Colimucus"),PokemonList.perName.get("Muplodocus")};
        PokemonList.perName.get("Chaffreux").evolutions = new Pokemon[]{PokemonList.perName.get("Chaglam"),PokemonList.perName.get("Chaffreux")};
        PokemonList.perName.get("Aeropteryx").evolutions = new Pokemon[]{PokemonList.perName.get("Arkeapti"),PokemonList.perName.get("Aeropteryx")};
        PokemonList.perName.get("Farfuret").evolutions = new Pokemon[]{PokemonList.perName.get("Farfuret"),PokemonList.perName.get("Dimoret")};
        PokemonList.perName.get("Cotovol").evolutions = new Pokemon[]{PokemonList.perName.get("Granivol"),PokemonList.perName.get("Floravol"),PokemonList.perName.get("Cotovol")};
        PokemonList.perName.get("Rondoudou").evolutions = new Pokemon[]{PokemonList.perName.get("Toudoudou"),PokemonList.perName.get("Rondoudou"),PokemonList.perName.get("Grodoudou")};
        PokemonList.perName.get("Sorboul").evolutions = new Pokemon[]{PokemonList.perName.get("Sorbebe"),PokemonList.perName.get("Sorboul"),PokemonList.perName.get("Sorbouboul")};
        PokemonList.perName.get("Amonistar").evolutions = new Pokemon[]{PokemonList.perName.get("Amonita"),PokemonList.perName.get("Amonistar")};
        PokemonList.perName.get("Clic").evolutions = new Pokemon[]{PokemonList.perName.get("Tic"),PokemonList.perName.get("Clic"),PokemonList.perName.get("Cliticlic")};
        PokemonList.perName.get("Meganium").evolutions = new Pokemon[]{PokemonList.perName.get("Germignon"),PokemonList.perName.get("Macronium"),PokemonList.perName.get("Meganium")};
        PokemonList.perName.get("Deoxys (Forme Defense)").evolutions = new Pokemon[]{};
        PokemonList.perName.get("Viskuse").evolutions = new Pokemon[]{PokemonList.perName.get("Viskuse"),PokemonList.perName.get("Moyade")};
        PokemonList.perName.get("Metamorph").evolutions = new Pokemon[]{};
        PokemonList.perName.get("Kangourex").evolutions = new Pokemon[]{PokemonList.perName.get("Kangourex"),PokemonList.perName.get("Mega-Kangourex")};
        PokemonList.perName.get("Pitrouille (Taille Normale)").evolutions = new Pokemon[]{};
        PokemonList.perName.get("Wailord").evolutions = new Pokemon[]{PokemonList.perName.get("Wailmer"),PokemonList.perName.get("Wailord")};
        PokemonList.perName.get("Colossinge").evolutions = new Pokemon[]{PokemonList.perName.get("Ferosinge"),PokemonList.perName.get("Colossinge")};
        PokemonList.perName.get("Yveltal").evolutions = new Pokemon[]{};
        PokemonList.perName.get("Fulguris (Forme Totemique)").evolutions = new Pokemon[]{};
        PokemonList.perName.get("Corayon").evolutions = new Pokemon[]{};
        PokemonList.perName.get("Mackogneur").evolutions = new Pokemon[]{PokemonList.perName.get("Machoc"),PokemonList.perName.get("Machopeur"),PokemonList.perName.get("Mackogneur")};
        PokemonList.perName.get("Rapion").evolutions = new Pokemon[]{PokemonList.perName.get("Rapion"),PokemonList.perName.get("Drascore")};
        PokemonList.perName.get("Feuiloutan").evolutions = new Pokemon[]{PokemonList.perName.get("Feuillajou"),PokemonList.perName.get("Feuiloutan")};
        PokemonList.perName.get("Ursaring").evolutions = new Pokemon[]{PokemonList.perName.get("Teddiursa"),PokemonList.perName.get("Ursaring")};
        PokemonList.perName.get("Anorith").evolutions = new Pokemon[]{PokemonList.perName.get("Anorith"),PokemonList.perName.get("Armaldo")};
        PokemonList.perName.get("Vipelierre").evolutions = new Pokemon[]{PokemonList.perName.get("Vipelierre"),PokemonList.perName.get("Lianaja"),PokemonList.perName.get("Majaspic")};
        PokemonList.perName.get("Gardevoir").evolutions = new Pokemon[]{PokemonList.perName.get("Tarsal"),PokemonList.perName.get("Kirlia"),PokemonList.perName.get("Gardevoir"),PokemonList.perName.get("Gallame"),PokemonList.perName.get("Mega-Gardevoir")};
        PokemonList.perName.get("Scarhino").evolutions = new Pokemon[]{PokemonList.perName.get("Scarhino"),PokemonList.perName.get("Mega-Scarhino")};
        PokemonList.perName.get("Demolosse").evolutions = new Pokemon[]{PokemonList.perName.get("Malosse"),PokemonList.perName.get("Demolosse"),PokemonList.perName.get("Mega-Demolosse")};
        PokemonList.perName.get("Crapustule").evolutions = new Pokemon[]{PokemonList.perName.get("Tritonde"),PokemonList.perName.get("Batracne"),PokemonList.perName.get("Crapustule")};
        PokemonList.perName.get("Crabaraque").evolutions = new Pokemon[]{PokemonList.perName.get("Crabicoque"),PokemonList.perName.get("Crabaraque")};
        PokemonList.perName.get("Tranchodon").evolutions = new Pokemon[]{PokemonList.perName.get("Coupenotte"),PokemonList.perName.get("Incisache"),PokemonList.perName.get("Tranchodon")};
        PokemonList.perName.get("Mewtwo").evolutions = new Pokemon[]{PokemonList.perName.get("Mewtwo"),PokemonList.perName.get("Mega-Mewtwo X"),PokemonList.perName.get("Mega-Mewtwo Y")};
        PokemonList.perName.get("Feurisson").evolutions = new Pokemon[]{PokemonList.perName.get("Hericendre"),PokemonList.perName.get("Feurisson"),PokemonList.perName.get("Typhlosion")};
        PokemonList.perName.get("Galeking").evolutions = new Pokemon[]{PokemonList.perName.get("Galekid"),PokemonList.perName.get("Galegon"),PokemonList.perName.get("Galeking"),PokemonList.perName.get("Mega-Galeking")};
        PokemonList.perName.get("Miradar").evolutions = new Pokemon[]{PokemonList.perName.get("Ratentif"),PokemonList.perName.get("Miradar")};
        PokemonList.perName.get("Tyranocif").evolutions = new Pokemon[]{PokemonList.perName.get("Embrylex"),PokemonList.perName.get("Ymphect"),PokemonList.perName.get("Tyranocif"),PokemonList.perName.get("Mega-Tyranocif")};
        PokemonList.perName.get("Scorvol").evolutions = new Pokemon[]{PokemonList.perName.get("Scorplane"),PokemonList.perName.get("Scorvol")};
        PokemonList.perName.get("Demanta").evolutions = new Pokemon[]{PokemonList.perName.get("Babimanta"),PokemonList.perName.get("Demanta")};
        PokemonList.perName.get("Solaroc").evolutions = new Pokemon[]{};
        PokemonList.perName.get("Passerouge").evolutions = new Pokemon[]{PokemonList.perName.get("Passerouge"),PokemonList.perName.get("Braisillon"),PokemonList.perName.get("Flambusard")};
        PokemonList.perName.get("Mega-Scarhino").evolutions = new Pokemon[]{PokemonList.perName.get("Scarhino"),PokemonList.perName.get("Mega-Scarhino")};
        PokemonList.perName.get("Flobio").evolutions = new Pokemon[]{PokemonList.perName.get("Gobou"),PokemonList.perName.get("Flobio"),PokemonList.perName.get("Laggron")};
        PokemonList.perName.get("Cochignon").evolutions = new Pokemon[]{PokemonList.perName.get("Marcacrin"),PokemonList.perName.get("Cochignon"),PokemonList.perName.get("Mammochon")};
        PokemonList.perName.get("Roserade").evolutions = new Pokemon[]{PokemonList.perName.get("Rozbouton"),PokemonList.perName.get("Roselia"),PokemonList.perName.get("Roserade")};
        PokemonList.perName.get("Chamallot").evolutions = new Pokemon[]{PokemonList.perName.get("Chamallot"),PokemonList.perName.get("Camerupt")};
        PokemonList.perName.get("Chacripan").evolutions = new Pokemon[]{PokemonList.perName.get("Chacripan"),PokemonList.perName.get("Leopardus")};
        PokemonList.perName.get("Psystigri").evolutions = new Pokemon[]{PokemonList.perName.get("Psystigri"),PokemonList.perName.get("Mistigrix")};
        PokemonList.perName.get("Scrutella").evolutions = new Pokemon[]{PokemonList.perName.get("Scrutella"),PokemonList.perName.get("Mesmerella"),PokemonList.perName.get("Siderella")};
        PokemonList.perName.get("Kungfouine").evolutions = new Pokemon[]{PokemonList.perName.get("Kungfouine"),PokemonList.perName.get("Shaofouine")};
        PokemonList.perName.get("Momartik").evolutions = new Pokemon[]{PokemonList.perName.get("Stalgamin"),PokemonList.perName.get("Oniglali"),PokemonList.perName.get("Momartik")};
        PokemonList.perName.get("Leopardus").evolutions = new Pokemon[]{PokemonList.perName.get("Chacripan"),PokemonList.perName.get("Leopardus")};
        PokemonList.perName.get("Ho-Oh").evolutions = new Pokemon[]{};
        PokemonList.perName.get("Krabby").evolutions = new Pokemon[]{PokemonList.perName.get("Krabby"),PokemonList.perName.get("Krabboss")};
        PokemonList.perName.get("Suicune").evolutions = new Pokemon[]{};
        PokemonList.perName.get("Zeblitz").evolutions = new Pokemon[]{PokemonList.perName.get("Zebibron"),PokemonList.perName.get("Zeblitz")};
        PokemonList.perName.get("Excavarenne").evolutions = new Pokemon[]{PokemonList.perName.get("Sapereau"),PokemonList.perName.get("Excavarenne")};
        PokemonList.perName.get("Donphan").evolutions = new Pokemon[]{PokemonList.perName.get("Phanpy"),PokemonList.perName.get("Donphan")};
        PokemonList.perName.get("Grelacon").evolutions = new Pokemon[]{PokemonList.perName.get("Grelacon"),PokemonList.perName.get("Seracrawl")};
        PokemonList.perName.get("Pitrouille (Taille Ultra)").evolutions = new Pokemon[]{};
        PokemonList.perName.get("Blizzi").evolutions = new Pokemon[]{PokemonList.perName.get("Blizzi"),PokemonList.perName.get("Blizzaroi"),PokemonList.perName.get("Mega-Blizzaroi")};
        PokemonList.perName.get("Mega-Absol").evolutions = new Pokemon[]{PokemonList.perName.get("Absol"),PokemonList.perName.get("Mega-Absol")};
        PokemonList.perName.get("Strassie").evolutions = new Pokemon[]{};
        PokemonList.perName.get("Trousselin").evolutions = new Pokemon[]{};
        PokemonList.perName.get("Morpheo").evolutions = new Pokemon[]{};
        PokemonList.perName.get("Airmure").evolutions = new Pokemon[]{};
        PokemonList.perName.get("M. Mime").evolutions = new Pokemon[]{PokemonList.perName.get("Mime Jr."),PokemonList.perName.get("M. Mime")};
        PokemonList.perName.get("Natu").evolutions = new Pokemon[]{PokemonList.perName.get("Natu"),PokemonList.perName.get("Xatu")};
        PokemonList.perName.get("Lainergie").evolutions = new Pokemon[]{PokemonList.perName.get("Wattouat"),PokemonList.perName.get("Lainergie"),PokemonList.perName.get("Pharamp"),PokemonList.perName.get("Mega-Pharamp")};
        PokemonList.perName.get("Mega-Carchacrok").evolutions = new Pokemon[]{PokemonList.perName.get("Griknot"),PokemonList.perName.get("Carmache"),PokemonList.perName.get("Carchacrok"),PokemonList.perName.get("Mega-Carchacrok")};
        PokemonList.perName.get("Coxy").evolutions = new Pokemon[]{PokemonList.perName.get("Coxy"),PokemonList.perName.get("Coxyclaque")};
        PokemonList.perName.get("Shaymin (Forme Terrestre)").evolutions = new Pokemon[]{};
        PokemonList.perName.get("Banshitrouye (Taille Maxi)").evolutions = new Pokemon[]{};
        PokemonList.perName.get("Cacnea").evolutions = new Pokemon[]{PokemonList.perName.get("Cacnea"),PokemonList.perName.get("Cacturne")};
        PokemonList.perName.get("Smogo").evolutions = new Pokemon[]{PokemonList.perName.get("Smogo"),PokemonList.perName.get("Smogogo")};
        PokemonList.perName.get("Arcanin").evolutions = new Pokemon[]{PokemonList.perName.get("Caninos"),PokemonList.perName.get("Arcanin")};
        PokemonList.perName.get("Milobellus").evolutions = new Pokemon[]{PokemonList.perName.get("Barpau"),PokemonList.perName.get("Milobellus")};
        PokemonList.perName.get("Taupiqueur").evolutions = new Pokemon[]{PokemonList.perName.get("Taupiqueur"),PokemonList.perName.get("Triopikeur")};
        PokemonList.perName.get("Capumain").evolutions = new Pokemon[]{PokemonList.perName.get("Capumain"),PokemonList.perName.get("Capidextre")};
        PokemonList.perName.get("Fulguris (Forme Avatar)").evolutions = new Pokemon[]{};
        PokemonList.perName.get("Machoc").evolutions = new Pokemon[]{PokemonList.perName.get("Machoc"),PokemonList.perName.get("Machopeur"),PokemonList.perName.get("Mackogneur")};
        PokemonList.perName.get("Ludicolo").evolutions = new Pokemon[]{PokemonList.perName.get("Nenupiot"),PokemonList.perName.get("Lombre"),PokemonList.perName.get("Ludicolo")};
        PokemonList.perName.get("Noarfang").evolutions = new Pokemon[]{PokemonList.perName.get("Hoothoot"),PokemonList.perName.get("Noarfang")};
        PokemonList.perName.get("Meloetta (Forme Danse)").evolutions = new Pokemon[]{};
        PokemonList.perName.get("Sepiatop").evolutions = new Pokemon[]{PokemonList.perName.get("Sepiatop"),PokemonList.perName.get("Sepiatroce")};
        PokemonList.perName.get("Fermite").evolutions = new Pokemon[]{};
        PokemonList.perName.get("Regice").evolutions = new Pokemon[]{};
        PokemonList.perName.get("Armaldo").evolutions = new Pokemon[]{PokemonList.perName.get("Anorith"),PokemonList.perName.get("Armaldo")};
        PokemonList.perName.get("Lewsor").evolutions = new Pokemon[]{PokemonList.perName.get("Lewsor"),PokemonList.perName.get("Neitram")};
        PokemonList.perName.get("Sancoki").evolutions = new Pokemon[]{PokemonList.perName.get("Sancoki"),PokemonList.perName.get("Tritosor")};
        PokemonList.perName.get("Demeteros (Forme Totemique)").evolutions = new Pokemon[]{};
        PokemonList.perName.get("Trompignon").evolutions = new Pokemon[]{PokemonList.perName.get("Trompignon"),PokemonList.perName.get("Gaulet")};
        PokemonList.perName.get("Empiflor").evolutions = new Pokemon[]{PokemonList.perName.get("Chetiflor"),PokemonList.perName.get("Boustiflor"),PokemonList.perName.get("Empiflor")};
        PokemonList.perName.get("Drackhaus").evolutions = new Pokemon[]{PokemonList.perName.get("Draby"),PokemonList.perName.get("Drackhaus"),PokemonList.perName.get("Drattak")};
        PokemonList.perName.get("Chenipan").evolutions = new Pokemon[]{PokemonList.perName.get("Chenipan"),PokemonList.perName.get("Chrysacier"),PokemonList.perName.get("Papilusion")};
        PokemonList.perName.get("Limonde").evolutions = new Pokemon[]{};
        PokemonList.perName.get("Grodrive").evolutions = new Pokemon[]{PokemonList.perName.get("Baudrive"),PokemonList.perName.get("Grodrive")};
        PokemonList.perName.get("Flabebe").evolutions = new Pokemon[]{PokemonList.perName.get("Flabebe"),PokemonList.perName.get("Floette"),PokemonList.perName.get("Florges")};
        PokemonList.perName.get("Mega-Alakazam").evolutions = new Pokemon[]{PokemonList.perName.get("Abra"),PokemonList.perName.get("Kadabra"),PokemonList.perName.get("Alakazam"),PokemonList.perName.get("Mega-Alakazam")};
        PokemonList.perName.get("Brutapode").evolutions = new Pokemon[]{PokemonList.perName.get("Venipatte"),PokemonList.perName.get("Scobolide"),PokemonList.perName.get("Brutapode")};
        PokemonList.perName.get("Deoxys (Forme de Base)").evolutions = new Pokemon[]{};
        PokemonList.perName.get("Megapagos").evolutions = new Pokemon[]{PokemonList.perName.get("Carapagos"),PokemonList.perName.get("Megapagos")};
        PokemonList.perName.get("Deflaisan").evolutions = new Pokemon[]{PokemonList.perName.get("Poichigeon"),PokemonList.perName.get("Colombeau"),PokemonList.perName.get("Deflaisan")};
        PokemonList.perName.get("Spectrum").evolutions = new Pokemon[]{PokemonList.perName.get("Fantominus"),PokemonList.perName.get("Spectrum"),PokemonList.perName.get("Ectoplasma"),PokemonList.perName.get("Mega-Ectoplasma")};
        PokemonList.perName.get("Pandarbare").evolutions = new Pokemon[]{PokemonList.perName.get("Pandespiegle"),PokemonList.perName.get("Pandarbare")};
        PokemonList.perName.get("Rexillius").evolutions = new Pokemon[]{PokemonList.perName.get("Ptyranidur"),PokemonList.perName.get("Rexillius")};
        PokemonList.perName.get("Sulfura").evolutions = new Pokemon[]{};
        PokemonList.perName.get("Drattak").evolutions = new Pokemon[]{PokemonList.perName.get("Draby"),PokemonList.perName.get("Drackhaus"),PokemonList.perName.get("Drattak")};
        PokemonList.perName.get("Seracrawl").evolutions = new Pokemon[]{PokemonList.perName.get("Grelacon"),PokemonList.perName.get("Seracrawl")};
	}

    public static HashMap<String, Pokemon> perName = new HashMap<String, Pokemon>() {{
        ArrayList<Talent> talents;

        talents = new ArrayList<Talent>(){{this.add(Talent.CRAN);this.add(Talent.FUITE);this.add(Talent.AGITATION);}};
        this.put("Rattatac", new Pokemon("Rattatac", 20, Type.NORMAL, Type.NONE, talents, 55, 81, 60, 50, 70, 97));

        talents = new ArrayList<Talent>(){{this.add(Talent.TELECHARGE);this.add(Talent.ADAPTABILITE);this.add(Talent.ANALYSTE);}};
        this.put("Porygon-Z", new Pokemon("Porygon-Z", 474, Type.PSY, Type.NONE, talents, 85, 80, 70, 135, 75, 90));

        talents = new ArrayList<Talent>(){{this.add(Talent.MUE);this.add(Talent.IMPUDENCE);this.add(Talent.INTIMIDATION);}};
        this.put("Baggiguane", new Pokemon("Baggiguane", 559, Type.TENEBRE, Type.COMBAT, talents, 50, 75, 70, 35, 70, 48));

        talents = new ArrayList<Talent>(){{this.add(Talent.CHLOROPHYLE);this.add(Talent.RECOLTE);}};
        this.put("Noadkoko", new Pokemon("Noadkoko", 103, Type.PLANTE, Type.PSY, talents, 95, 95, 85, 125, 65, 55));

        talents = new ArrayList<Talent>(){{this.add(Talent.REGARD_VIF);this.add(Talent.SANS_LIMITE);this.add(Talent.ACHARNE);}};
        this.put("Gueriaigle", new Pokemon("Gueriaigle", 628, Type.NORMAL, Type.VOL, talents, 100, 123, 75, 57, 75, 80));

        talents = new ArrayList<Talent>(){{this.add(Talent.INSOMNIA);this.add(Talent.FOUILLE);this.add(Talent.CORPS_MAUDIT);}};
        this.put("Polichombr", new Pokemon("Polichombr", 353, Type.SPECTRE, Type.NONE, talents, 44, 75, 35, 63, 33, 45));

        talents = new ArrayList<Talent>(){{this.add(Talent.POSE_SPORE);this.add(Talent.REGE_FORCE);}};
        this.put("Gaulet", new Pokemon("Gaulet", 591, Type.PLANTE, Type.POISON, talents, 114, 85, 70, 85, 80, 30));

        talents = new ArrayList<Talent>(){{this.add(Talent.GLISSADE);this.add(Talent.SNIPER);this.add(Talent.MOITEUR);}};
        this.put("Hyporoi", new Pokemon("Hyporoi", 230, Type.EAU, Type.DRAGON, talents, 75, 95, 95, 95, 95, 85));

        talents = new ArrayList<Talent>(){{this.add(Talent.MOTORISE);this.add(Talent.ESPRIT_VITAL);}};
        this.put("Elekable", new Pokemon("Elekable", 466, Type.ELECTRIQUE, Type.NONE, talents, 75, 123, 67, 95, 85, 95));

        talents = new ArrayList<Talent>(){{this.add(Talent.BRASIER);this.add(Talent.MAGICIEN);}};
        this.put("Roussil", new Pokemon("Roussil", 654, Type.FEU, Type.NONE, talents, 59, 59, 58, 90, 70, 73));

        talents = new ArrayList<Talent>(){{this.add(Talent.JOLI_SOURIRE);this.add(Talent.TECHNICIEN);this.add(Talent.MULTI_COUPS);}};
        this.put("Pashmilla", new Pokemon("Pashmilla", 573, Type.NORMAL, Type.NONE, talents, 75, 95, 60, 65, 60, 115));

        talents = new ArrayList<Talent>(){{this.add(Talent.STATIK);this.add(Talent.MOTORISE);}};
        this.put("Emolga", new Pokemon("Emolga", 587, Type.ELECTRIQUE, Type.VOL, talents, 55, 75, 60, 75, 60, 103));

        talents = new ArrayList<Talent>(){{this.add(Talent.TETE_DE_ROC);this.add(Talent.FERMETE);}};
        this.put("Grolem", new Pokemon("Grolem", 76, Type.ROCHE, Type.SOL, talents, 80, 110, 130, 55, 65, 45));

        talents = new ArrayList<Talent>(){{this.add(Talent.LEVITATION);}};
        this.put("Cresselia", new Pokemon("Cresselia", 488, Type.PSY, Type.NONE, talents, 120, 70, 120, 75, 130, 85));

        talents = new ArrayList<Talent>(){{this.add(Talent.GLOUTONNERIE);this.add(Talent.TORRENT);}};
        this.put("Flotoutan", new Pokemon("Flotoutan", 516, Type.EAU, Type.NONE, talents, 75, 98, 63, 98, 63, 101));

        talents = new ArrayList<Talent>(){{this.add(Talent.REGARD_VIF);this.add(Talent.CUVETTE);}};
        this.put("Bekipan", new Pokemon("Bekipan", 279, Type.EAU, Type.VOL, talents, 60, 50, 100, 85, 70, 65));

        talents = new ArrayList<Talent>(){{this.add(Talent.TORRENT);this.add(Talent.COQUE_ARMURE);}};
        this.put("Mateloutre", new Pokemon("Mateloutre", 502, Type.EAU, Type.NONE, talents, 75, 75, 60, 83, 60, 60));

        talents = new ArrayList<Talent>(){{this.add(Talent.FERMETE);this.add(Talent.ANTI_BRUIT);}};
        this.put("Dinoclier", new Pokemon("Dinoclier", 410, Type.ROCHE, Type.ACIER, talents, 30, 42, 118, 42, 88, 30));

        talents = new ArrayList<Talent>(){{this.add(Talent.PRESSION);this.add(Talent.CHANCEUX);this.add(Talent.COEUR_NOBLE);}};
        this.put("Absol", new Pokemon("Absol", 359, Type.TENEBRE, Type.NONE, talents, 65, 130, 60, 75, 60, 75));

        talents = new ArrayList<Talent>(){{this.add(Talent.ISOGRAISSE);this.add(Talent.COLOFORCE);this.add(Talent.HERBIVORE);}};
        this.put("Azurill", new Pokemon("Azurill", 298, Type.NORMAL, Type.NONE, talents, 50, 20, 40, 20, 40, 20));

        talents = new ArrayList<Talent>(){{this.add(Talent.PRESSION);this.add(Talent.TENSION);}};
        this.put("Apireine", new Pokemon("Apireine", 416, Type.INSECTE, Type.VOL, talents, 70, 80, 102, 80, 102, 40));

        talents = new ArrayList<Talent>(){{this.add(Talent.BRASIER);this.add(Talent.FORCE_SOLEIL);}};
        this.put("Dracaufeu", new Pokemon("Dracaufeu", 6, Type.FEU, Type.VOL, talents, 78, 84, 78, 109, 85, 100));

        talents = new ArrayList<Talent>(){{this.add(Talent.AGITATION);}};
        this.put("Solochi", new Pokemon("Solochi", 633, Type.TENEBRE, Type.DRAGON, talents, 52, 65, 50, 45, 50, 38));

        talents = new ArrayList<Talent>(){{this.add(Talent.LEVITATION);}};
        this.put("Motisma (Forme Tonte)", new Pokemon("Motisma (Forme Tonte)", 479, Type.ELECTRIQUE, Type.SPECTRE, talents, 50, 65, 107, 105, 107, 86));

        talents = new ArrayList<Talent>(){{this.add(Talent.ARMUMAGMA);this.add(Talent.CORPS_ARDENT);this.add(Talent.ARMUROUILLEE);}};
        this.put("Volcaropod", new Pokemon("Volcaropod", 219, Type.FEU, Type.ROCHE, talents, 50, 50, 120, 80, 80, 30));

        talents = new ArrayList<Talent>(){{this.add(Talent.FARCEUR);this.add(Talent.ACHARNE);}};
        this.put("Boreas (Forme Totemique)", new Pokemon("Boreas (Forme Totemique)", 641, Type.VOL, Type.NONE, talents, 79, 100, 80, 110, 90, 121));

        talents = new ArrayList<Talent>(){{this.add(Talent.SERENITE);}};
        this.put("Meloetta (Forme Voix)", new Pokemon("Meloetta (Forme Voix)", 648, Type.NORMAL, Type.PSY, talents, 100, 77, 77, 128, 128, 90));

        talents = new ArrayList<Talent>(){{this.add(Talent.FUITE);this.add(Talent.INTIMIDATION);this.add(Talent.PHOBIQUE);}};
        this.put("Snubbull", new Pokemon("Snubbull", 209, Type.NORMAL, Type.NONE, talents, 60, 80, 50, 40, 40, 30));

        talents = new ArrayList<Talent>(){{this.add(Talent.PEAU_DURE);}};
        this.put("Sharpedo", new Pokemon("Sharpedo", 319, Type.EAU, Type.TENEBRE, talents, 70, 120, 40, 95, 40, 95));

        talents = new ArrayList<Talent>(){{this.add(Talent.LEVITATION);}};
        this.put("Motisma (Forme Froid)", new Pokemon("Motisma (Forme Froid)", 479, Type.ELECTRIQUE, Type.SPECTRE, talents, 50, 65, 107, 105, 107, 86));

        talents = new ArrayList<Talent>(){{this.add(Talent.INSOMNIA);}};
        this.put("Mega-Mewtwo Y", new Pokemon("Mega-Mewtwo Y", 150, Type.PSY, Type.NONE, talents, 106, 150, 70, 194, 120, 140));

        talents = new ArrayList<Talent>(){{this.add(Talent.MOMIE);}};
        this.put("Tutafeh", new Pokemon("Tutafeh", 562, Type.SPECTRE, Type.NONE, talents, 38, 30, 85, 55, 65, 30));

        talents = new ArrayList<Talent>(){{this.add(Talent.PRESSION);}};
        this.put("Noctunoir", new Pokemon("Noctunoir", 477, Type.SPECTRE, Type.NONE, talents, 45, 100, 135, 65, 135, 45));

        talents = new ArrayList<Talent>(){{this.add(Talent.JOLI_SOURIRE);this.add(Talent.GARDE_MAGIK);this.add(Talent.INCONSCIENT);}};
        this.put("Melodelfe", new Pokemon("Melodelfe", 36, Type.NORMAL, Type.NONE, talents, 95, 70, 73, 85, 90, 60));

        talents = new ArrayList<Talent>(){{this.add(Talent.IMPASSIBLE);}};
        this.put("Mega-Mewtwo X", new Pokemon("Mega-Mewtwo X", 150, Type.PSY, Type.COMBAT, talents, 106, 190, 100, 154, 100, 130));

        talents = new ArrayList<Talent>(){{this.add(Talent.MEDIC_NATURE);}};
        this.put("Celebi", new Pokemon("Celebi", 251, Type.PSY, Type.PLANTE, talents, 100, 100, 100, 100, 100, 100));

        talents = new ArrayList<Talent>(){{this.add(Talent.COEUR_SOIN);this.add(Talent.AROMA_VOILE);}};
        this.put("Cocotine", new Pokemon("Cocotine", 683, Type.FEE, Type.NONE, talents, 100, 65, 75, 95, 90, 30));

        talents = new ArrayList<Talent>(){{this.add(Talent.ILLUSION);}};
        this.put("Zorua", new Pokemon("Zorua", 570, Type.TENEBRE, Type.NONE, talents, 40, 65, 40, 80, 40, 65));

        talents = new ArrayList<Talent>(){{this.add(Talent.INTIMIDATION);}};
        this.put("Mega-Elecsprint", new Pokemon("Mega-Elecsprint", 310, Type.ELECTRIQUE, Type.NONE, talents, 70, 75, 80, 135, 80, 135));

        talents = new ArrayList<Talent>(){{this.add(Talent.ESSAIM);this.add(Talent.MUE);this.add(Talent.ANNULE_GARDE);}};
        this.put("Carabing", new Pokemon("Carabing", 588, Type.INSECTE, Type.NONE, talents, 50, 75, 45, 40, 45, 60));

        talents = new ArrayList<Talent>(){{this.add(Talent.MARQUE_OMBRE);this.add(Talent.TELEPATHE);}};
        this.put("Okeoke", new Pokemon("Okeoke", 360, Type.PSY, Type.NONE, talents, 95, 23, 48, 23, 48, 23));

        talents = new ArrayList<Talent>(){{this.add(Talent.GLISSADE);this.add(Talent.SNIPER);this.add(Talent.MOITEUR);}};
        this.put("Hypotrempe", new Pokemon("Hypotrempe", 116, Type.EAU, Type.NONE, talents, 30, 40, 70, 70, 25, 60));

        talents = new ArrayList<Talent>(){{this.add(Talent.JOLI_SOURIRE);this.add(Talent.PEAU_FEERIQUE);}};
        this.put("Nymphali", new Pokemon("Nymphali", 700, Type.FEE, Type.NONE, talents, 95, 65, 65, 110, 130, 60));

        talents = new ArrayList<Talent>(){{this.add(Talent.POINT_POISON);this.add(Talent.TOXITOUCHE);}};
        this.put("Venalgue", new Pokemon("Venalgue", 690, Type.POISON, Type.EAU, talents, 50, 60, 60, 60, 60, 30));

        talents = new ArrayList<Talent>(){{this.add(Talent.PEAU_CELESTE);}};
        this.put("Mega-Scarabrute", new Pokemon("Mega-Scarabrute", 127, Type.INSECTE, Type.VOL, talents, 65, 155, 120, 65, 90, 105));

        talents = new ArrayList<Talent>(){{this.add(Talent.ABSORB_EAU);this.add(Talent.MOITEUR);this.add(Talent.INCONSCIENT);}};
        this.put("Maraiste", new Pokemon("Maraiste", 195, Type.EAU, Type.SOL, talents, 95, 85, 85, 65, 65, 35));

        talents = new ArrayList<Talent>(){{this.add(Talent.ISOGRAISSE);}};
        this.put("Mega-Florizarre", new Pokemon("Mega-Florizarre", 3, Type.PLANTE, Type.POISON, talents, 80, 100, 123, 122, 120, 80));

        talents = new ArrayList<Talent>(){{this.add(Talent.OEIL_COMPOSE);this.add(Talent.LENTITEINTEE);}};
        this.put("Papilusion", new Pokemon("Papilusion", 12, Type.INSECTE, Type.VOL, talents, 60, 45, 50, 80, 80, 70));

        talents = new ArrayList<Talent>(){{this.add(Talent.CRAN);this.add(Talent.SANS_LIMITE);this.add(Talent.POING_DE_FER);}};
        this.put("Charpenti", new Pokemon("Charpenti", 532, Type.COMBAT, Type.NONE, talents, 75, 80, 55, 25, 35, 35));

        talents = new ArrayList<Talent>(){{this.add(Talent.FUITE);this.add(Talent.MATINAL);this.add(Talent.PIED_CONFUS);}};
        this.put("Doduo", new Pokemon("Doduo", 84, Type.NORMAL, Type.VOL, talents, 35, 85, 45, 35, 35, 75));

        talents = new ArrayList<Talent>(){{this.add(Talent.ANTICIPATION);this.add(Talent.PEAU_SECHE);this.add(Talent.TOXITOUCHE);}};
        this.put("Coatox", new Pokemon("Coatox", 454, Type.POISON, Type.COMBAT, talents, 83, 106, 65, 86, 65, 85));

        talents = new ArrayList<Talent>(){{this.add(Talent.FORCE_PURE);this.add(Talent.TELEPATHE);}};
        this.put("Charmina", new Pokemon("Charmina", 308, Type.COMBAT, Type.PSY, talents, 60, 60, 75, 60, 75, 80));

        talents = new ArrayList<Talent>(){{this.add(Talent.ABSORB_VOLT);this.add(Talent.PIED_VELOCE);}};
        this.put("Voltali", new Pokemon("Voltali", 135, Type.ELECTRIQUE, Type.NONE, talents, 65, 65, 60, 110, 95, 130));

        talents = new ArrayList<Talent>(){{this.add(Talent.RAMASSAGE);this.add(Talent.FOUILLE);this.add(Talent.INSOMNIA);}};
        this.put("Pitrouille (Taille Maxi)", new Pokemon("Pitrouille (Taille Maxi)", 710, Type.SPECTRE, Type.PLANTE, talents, 54, 66, 70, 44, 55, 51));

        talents = new ArrayList<Talent>(){{this.add(Talent.ANTICIPATION);this.add(Talent.ENVELOCAPE);}};
        this.put("Cheniselle (Cape Dechet)", new Pokemon("Cheniselle (Cape Dechet)", 413, Type.INSECTE, Type.NONE, talents, 60, 69, 95, 69, 95, 36));

        talents = new ArrayList<Talent>(){{this.add(Talent.DECLIC_TACTIQUE);}};
        this.put("Exagide (Forme Assaut)", new Pokemon("Exagide (Forme Assaut)", 681, Type.ACIER, Type.SPECTRE, talents, 60, 150, 50, 150, 50, 60));

        talents = new ArrayList<Talent>(){{this.add(Talent.CHLOROPHYLE);this.add(Talent.COEUR_SOIN);}};
        this.put("Joliflor", new Pokemon("Joliflor", 182, Type.PLANTE, Type.NONE, talents, 75, 80, 85, 90, 100, 50));

        talents = new ArrayList<Talent>(){{this.add(Talent.SYNCHRO);this.add(Talent.CALQUE);this.add(Talent.TELEPATHE);}};
        this.put("Tarsal", new Pokemon("Tarsal", 280, Type.PSY, Type.NONE, talents, 28, 25, 25, 45, 35, 40));

        talents = new ArrayList<Talent>(){{this.add(Talent.ATTENTION);this.add(Talent.ACHARNE);this.add(Talent.PRESSION);}};
        this.put("Scalpion", new Pokemon("Scalpion", 624, Type.ACIER, Type.TENEBRE, talents, 45, 85, 70, 40, 40, 60));

        talents = new ArrayList<Talent>(){{this.add(Talent.FERMETE);this.add(Talent.TETE_DE_ROC);this.add(Talent.HEAVY_METAL);}};
        this.put("Galegon", new Pokemon("Galegon", 305, Type.ACIER, Type.ROCHE, talents, 60, 90, 140, 50, 50, 40));

        talents = new ArrayList<Talent>(){{this.add(Talent.LEVITATION);}};
        this.put("Smogogo", new Pokemon("Smogogo", 110, Type.POISON, Type.NONE, talents, 65, 90, 120, 85, 70, 60));

        talents = new ArrayList<Talent>(){{this.add(Talent.BOOM_FINAL);this.add(Talent.DELESTAGE);this.add(Talent.RAGE_BRULURE);}};
        this.put("Baudrive", new Pokemon("Baudrive", 425, Type.SPECTRE, Type.VOL, talents, 90, 50, 34, 60, 44, 70));

        talents = new ArrayList<Talent>(){{this.add(Talent.LEVITATION);}};
        this.put("Libegon", new Pokemon("Libegon", 330, Type.SOL, Type.DRAGON, talents, 80, 100, 80, 80, 80, 100));

        talents = new ArrayList<Talent>(){{this.add(Talent.FERMETE);this.add(Talent.ENVELOCAPE);}};
        this.put("Pomdepik", new Pokemon("Pomdepik", 204, Type.INSECTE, Type.NONE, talents, 50, 65, 90, 35, 35, 15));

        talents = new ArrayList<Talent>(){{this.add(Talent.LEVITATION);}};
        this.put("Korillon", new Pokemon("Korillon", 433, Type.PSY, Type.NONE, talents, 45, 30, 50, 65, 50, 45));

        talents = new ArrayList<Talent>(){{this.add(Talent.ENGRAIS);this.add(Talent.PARE_BALLES);}};
        this.put("Boguerisse", new Pokemon("Boguerisse", 651, Type.PLANTE, Type.NONE, talents, 54, 79, 101, 50, 50, 52));

        talents = new ArrayList<Talent>(){{this.add(Talent.ANTI_BRUIT);this.add(Talent.FILTRE);this.add(Talent.TECHNICIEN);}};
        this.put("Mime Jr.", new Pokemon("Mime Jr.", 439, Type.PSY, Type.NONE, talents, 20, 25, 45, 70, 90, 60));

        talents = new ArrayList<Talent>(){{this.add(Talent.TECHNICIEN);this.add(Talent.TEMPO_PERSO);this.add(Talent.LUNATIQUE);}};
        this.put("Queulorior", new Pokemon("Queulorior", 235, Type.NORMAL, Type.NONE, talents, 55, 20, 35, 20, 45, 75));

        talents = new ArrayList<Talent>(){{this.add(Talent.ISOGRAISSE);this.add(Talent.QUERELLEUR);this.add(Talent.HERBIVORE);}};
        this.put("Ecremeuh", new Pokemon("Ecremeuh", 241, Type.NORMAL, Type.NONE, talents, 95, 80, 105, 40, 70, 100));

        talents = new ArrayList<Talent>(){{this.add(Talent.RAMASSAGE);this.add(Talent.GLOUTONNERIE);this.add(Talent.PIED_VELOCE);}};
        this.put("Lineon", new Pokemon("Lineon", 264, Type.NORMAL, Type.NONE, talents, 78, 70, 61, 50, 61, 100));

        talents = new ArrayList<Talent>(){{this.add(Talent.TETE_DE_ROC);this.add(Talent.PARATONNERRE);this.add(Talent.ARMURBASTON);}};
        this.put("Osselait", new Pokemon("Osselait", 104, Type.SOL, Type.NONE, talents, 50, 50, 95, 40, 50, 35));

        talents = new ArrayList<Talent>(){{this.add(Talent.INCONSCIENT);this.add(Talent.SIMPLE);this.add(Talent.LUNATIQUE);}};
        this.put("Castorno", new Pokemon("Castorno", 400, Type.NORMAL, Type.EAU, talents, 79, 85, 60, 55, 60, 71));

        talents = new ArrayList<Talent>(){{this.add(Talent.INSOMNIA);this.add(Talent.PREDICTION);this.add(Talent.ATTENTION);}};
        this.put("Hypnomade", new Pokemon("Hypnomade", 97, Type.PSY, Type.NONE, talents, 85, 73, 70, 73, 115, 67));

        talents = new ArrayList<Talent>(){{this.add(Talent.VENTOUSE);this.add(Talent.LAVABO);}};
        this.put("Lilia", new Pokemon("Lilia", 345, Type.ROCHE, Type.PLANTE, talents, 66, 41, 77, 61, 87, 23));

        talents = new ArrayList<Talent>(){{this.add(Talent.LEVITATION);}};
        this.put("Motisma (Forme Helice)", new Pokemon("Motisma (Forme Helice)", 479, Type.ELECTRIQUE, Type.SPECTRE, talents, 50, 65, 107, 105, 107, 86));

        talents = new ArrayList<Talent>(){{this.add(Talent.BRISE_MOULE);this.add(Talent.SANS_LIMITE);}};
        this.put("Kranidos", new Pokemon("Kranidos", 408, Type.ROCHE, Type.NONE, talents, 67, 125, 40, 30, 30, 58));

        talents = new ArrayList<Talent>(){{this.add(Talent.BENET);this.add(Talent.RIDEAU_NEIGE);this.add(Talent.ISOGRAISSE);}};
        this.put("Mammochon", new Pokemon("Mammochon", 473, Type.GLACE, Type.SOL, talents, 110, 130, 80, 70, 60, 80));

        talents = new ArrayList<Talent>(){{this.add(Talent.PUANTEUR);this.add(Talent.BOOM_FINAL);}};
        this.put("Moufouette", new Pokemon("Moufouette", 434, Type.POISON, Type.TENEBRE, talents, 63, 63, 47, 41, 41, 74));

        talents = new ArrayList<Talent>(){{this.add(Talent.PUANTEUR);this.add(Talent.ARMUROUILLEE);this.add(Talent.BOOM_FINAL);}};
        this.put("Miasmax", new Pokemon("Miasmax", 569, Type.POISON, Type.NONE, talents, 80, 95, 82, 60, 82, 75));

        talents = new ArrayList<Talent>(){{this.add(Talent.GLOUTONNERIE);this.add(Talent.TORCHE);this.add(Talent.ECRAN_FUMEE);}};
        this.put("Aflamanoir", new Pokemon("Aflamanoir", 631, Type.FEU, Type.NONE, talents, 85, 97, 66, 105, 66, 65));

        talents = new ArrayList<Talent>(){{this.add(Talent.ISOGRAISSE);this.add(Talent.CRAN);this.add(Talent.SANS_LIMITE);}};
        this.put("Makuhita", new Pokemon("Makuhita", 296, Type.COMBAT, Type.NONE, talents, 72, 60, 30, 20, 30, 25));

        talents = new ArrayList<Talent>(){{this.add(Talent.INTIMIDATION);this.add(Talent.FOUILLE);this.add(Talent.HERBIVORE);}};
        this.put("Cerfrousse", new Pokemon("Cerfrousse", 234, Type.NORMAL, Type.NONE, talents, 73, 95, 62, 85, 65, 85));

        talents = new ArrayList<Talent>(){{this.add(Talent.SYNCHRO);this.add(Talent.ATTENTION);this.add(Talent.GARDE_MAGIK);}};
        this.put("Alakazam", new Pokemon("Alakazam", 65, Type.PSY, Type.NONE, talents, 55, 50, 45, 135, 85, 120));

        talents = new ArrayList<Talent>(){{this.add(Talent.GRIFFE_DURE);}};
        this.put("Mega-Dracaufeu X", new Pokemon("Mega-Dracaufeu X", 6, Type.FEU, Type.DRAGON, talents, 78, 130, 111, 130, 85, 100));

        talents = new ArrayList<Talent>(){{this.add(Talent.BRASIER);this.add(Talent.FORCE_SOLEIL);}};
        this.put("Reptincel", new Pokemon("Reptincel", 5, Type.FEU, Type.NONE, talents, 58, 64, 58, 80, 65, 80));

        talents = new ArrayList<Talent>(){{this.add(Talent.SOLIDE_ROC);this.add(Talent.FERMETE);this.add(Talent.GLISSADE);}};
        this.put("Carapagos", new Pokemon("Carapagos", 564, Type.EAU, Type.ROCHE, talents, 54, 78, 103, 53, 45, 22));

        talents = new ArrayList<Talent>(){{this.add(Talent.POINT_POISON);this.add(Talent.SNIPER);this.add(Talent.MOITEUR);}};
        this.put("Hypocean", new Pokemon("Hypocean", 117, Type.EAU, Type.NONE, talents, 55, 65, 95, 95, 45, 85));

        talents = new ArrayList<Talent>(){{this.add(Talent.ENGRAIS);this.add(Talent.COQUE_ARMURE);}};
        this.put("Tortipouss", new Pokemon("Tortipouss", 387, Type.PLANTE, Type.NONE, talents, 55, 68, 64, 45, 55, 31));

        talents = new ArrayList<Talent>(){{this.add(Talent.ATTENTION);this.add(Talent.CORPS_GEL);this.add(Talent.LUNATIQUE);}};
        this.put("Stalgamin", new Pokemon("Stalgamin", 361, Type.GLACE, Type.NONE, talents, 50, 50, 50, 50, 50, 50));

        talents = new ArrayList<Talent>(){{this.add(Talent.ESSAIM);this.add(Talent.COQUE_ARMURE);this.add(Talent.ENVELOCAPE);}};
        this.put("Lancargot", new Pokemon("Lancargot", 589, Type.INSECTE, Type.ACIER, talents, 70, 135, 105, 60, 105, 20));

        talents = new ArrayList<Talent>(){{this.add(Talent.ANTI_BRUIT);this.add(Talent.PHOBIQUE);}};
        this.put("Chuchmur", new Pokemon("Chuchmur", 293, Type.NORMAL, Type.NONE, talents, 64, 51, 23, 51, 23, 28));

        talents = new ArrayList<Talent>(){{this.add(Talent.LEVITATION);}};
        this.put("Motisma (Forme Normale)", new Pokemon("Motisma (Forme Normale)", 479, Type.ELECTRIQUE, Type.SPECTRE, talents, 50, 50, 77, 95, 77, 91));

        talents = new ArrayList<Talent>(){{this.add(Talent.CORPS_ARDENT);this.add(Talent.ESPRIT_VITAL);}};
        this.put("Maganon", new Pokemon("Maganon", 467, Type.FEU, Type.NONE, talents, 75, 95, 67, 125, 95, 83));

        talents = new ArrayList<Talent>(){{this.add(Talent.ABSENTEISME);}};
        this.put("Parecool", new Pokemon("Parecool", 287, Type.NORMAL, Type.NONE, talents, 60, 60, 60, 35, 35, 30));

        talents = new ArrayList<Talent>(){{this.add(Talent.STATIK);}};
        this.put("Wattouat", new Pokemon("Wattouat", 179, Type.ELECTRIQUE, Type.NONE, talents, 55, 40, 40, 65, 45, 35));

        talents = new ArrayList<Talent>(){{this.add(Talent.SNIPER);this.add(Talent.GRIFFE_DURE);this.add(Talent.PICKPOCKET);}};
        this.put("Opermine", new Pokemon("Opermine", 688, Type.ROCHE, Type.EAU, talents, 50, 95, 95, 30, 80, 60));

        talents = new ArrayList<Talent>(){{this.add(Talent.TORRENT);this.add(Talent.ACHARNE);}};
        this.put("Prinplouf", new Pokemon("Prinplouf", 394, Type.EAU, Type.NONE, talents, 64, 66, 68, 81, 76, 50));

        talents = new ArrayList<Talent>(){{this.add(Talent.LEVITATION);}};
        this.put("Anchwatt", new Pokemon("Anchwatt", 602, Type.ELECTRIQUE, Type.NONE, talents, 35, 55, 40, 45, 40, 60));

        talents = new ArrayList<Talent>(){{this.add(Talent.PLUS);this.add(Talent.PARATONNERRE);}};
        this.put("Posipi", new Pokemon("Posipi", 311, Type.ELECTRIQUE, Type.NONE, talents, 60, 50, 40, 85, 75, 95));

        talents = new ArrayList<Talent>(){{this.add(Talent.DECLIC_TACTIQUE);}};
        this.put("Exagide (Forme Parade)", new Pokemon("Exagide (Forme Parade)", 681, Type.ACIER, Type.SPECTRE, talents, 60, 50, 150, 50, 150, 60));

        talents = new ArrayList<Talent>(){{this.add(Talent.STATIK);this.add(Talent.ESPRIT_VITAL);}};
        this.put("Elekid", new Pokemon("Elekid", 239, Type.ELECTRIQUE, Type.NONE, talents, 45, 63, 37, 65, 55, 95));

        talents = new ArrayList<Talent>(){{this.add(Talent.CORPS_ARDENT);this.add(Talent.AILES_BOURRASQUE);}};
        this.put("Flambusard", new Pokemon("Flambusard", 663, Type.FEU, Type.VOL, talents, 78, 81, 71, 74, 69, 126));

        talents = new ArrayList<Talent>(){{this.add(Talent.LEVITATION);}};
        this.put("Balbuto", new Pokemon("Balbuto", 343, Type.SOL, Type.PSY, talents, 40, 40, 55, 40, 70, 55));

        talents = new ArrayList<Talent>(){{this.add(Talent.OEIL_COMPOSE);this.add(Talent.TURBO);this.add(Talent.FOUILLE);}};
        this.put("Yanma", new Pokemon("Yanma", 193, Type.INSECTE, Type.VOL, talents, 65, 65, 45, 75, 45, 95));

        talents = new ArrayList<Talent>(){{this.add(Talent.COEUR_DE_COQ);this.add(Talent.CHANCEUX);this.add(Talent.RIVALITE);}};
        this.put("Poichigeon", new Pokemon("Poichigeon", 519, Type.NORMAL, Type.VOL, talents, 50, 55, 50, 36, 30, 43));

        talents = new ArrayList<Talent>(){{this.add(Talent.LEVITATION);}};
        this.put("Lamperoie", new Pokemon("Lamperoie", 603, Type.ELECTRIQUE, Type.NONE, talents, 65, 85, 70, 75, 70, 40));

        talents = new ArrayList<Talent>(){{this.add(Talent.SYNCHRO);this.add(Talent.CALQUE);this.add(Talent.TELEPATHE);}};
        this.put("Kirlia", new Pokemon("Kirlia", 281, Type.PSY, Type.NONE, talents, 38, 35, 35, 65, 55, 50));

        talents = new ArrayList<Talent>(){{this.add(Talent.REGARD_VIF);this.add(Talent.COEUR_DE_COQ);this.add(Talent.HYDRATATION);}};
        this.put("Couaneton", new Pokemon("Couaneton", 580, Type.EAU, Type.VOL, talents, 62, 44, 50, 44, 50, 55));

        talents = new ArrayList<Talent>(){{this.add(Talent.CHLOROPHYLE);this.add(Talent.FUITE);}};
        this.put("Mystherbe", new Pokemon("Mystherbe", 43, Type.PLANTE, Type.POISON, talents, 45, 50, 55, 75, 65, 30));

        talents = new ArrayList<Talent>(){{this.add(Talent.CORPS_SAIN);this.add(Talent.LIGHT_METAL);}};
        this.put("Metang", new Pokemon("Metang", 375, Type.ACIER, Type.PSY, talents, 60, 75, 100, 55, 80, 50));

        talents = new ArrayList<Talent>(){{this.add(Talent.GLUE);this.add(Talent.LAVABO);this.add(Talent.FORCE_SABLE);}};
        this.put("Tritosor", new Pokemon("Tritosor", 423, Type.EAU, Type.SOL, talents, 111, 83, 68, 92, 82, 39));

        talents = new ArrayList<Talent>(){{this.add(Talent.ATTENTION);this.add(Talent.MULTIECAILLE);}};
        this.put("Dracolosse", new Pokemon("Dracolosse", 149, Type.DRAGON, Type.VOL, talents, 91, 134, 95, 100, 100, 80));

        talents = new ArrayList<Talent>(){{this.add(Talent.CHLOROPHYLE);this.add(Talent.TEMPO_PERSO);this.add(Talent.FEUIL_GARDE);}};
        this.put("Fragilady", new Pokemon("Fragilady", 549, Type.PLANTE, Type.NONE, talents, 70, 60, 75, 110, 75, 90));

        talents = new ArrayList<Talent>(){{this.add(Talent.TELECHARGE);}};
        this.put("Genesect", new Pokemon("Genesect", 649, Type.INSECTE, Type.ACIER, talents, 71, 120, 95, 120, 95, 99));

        talents = new ArrayList<Talent>(){{this.add(Talent.POINT_POISON);this.add(Talent.RIVALITE);this.add(Talent.AGITATION);}};
        this.put("Nidorino", new Pokemon("Nidorino", 33, Type.POISON, Type.NONE, talents, 61, 72, 57, 55, 55, 65));

        talents = new ArrayList<Talent>(){{this.add(Talent.INSOMNIA);this.add(Talent.FOUILLE);this.add(Talent.CORPS_MAUDIT);}};
        this.put("Branette", new Pokemon("Branette", 354, Type.SPECTRE, Type.NONE, talents, 64, 115, 65, 83, 63, 65));

        talents = new ArrayList<Talent>(){{this.add(Talent.POINT_POISON);this.add(Talent.RIVALITE);this.add(Talent.AGITATION);}};
        this.put("Nidorina", new Pokemon("Nidorina", 30, Type.POISON, Type.NONE, talents, 70, 62, 67, 55, 55, 56));

        talents = new ArrayList<Talent>(){{this.add(Talent.PARATONNERRE);this.add(Talent.TETE_DE_ROC);this.add(Talent.TEMERAIRE);}};
        this.put("Rhinoferos", new Pokemon("Rhinoferos", 112, Type.SOL, Type.ROCHE, talents, 105, 130, 120, 45, 45, 40));

        talents = new ArrayList<Talent>(){{this.add(Talent.DEBUT_CALME);}};
        this.put("Regigigas", new Pokemon("Regigigas", 486, Type.NORMAL, Type.NONE, talents, 110, 160, 110, 80, 110, 100));

        talents = new ArrayList<Talent>(){{this.add(Talent.CORPS_SAIN);this.add(Talent.SUINTEMENT);this.add(Talent.CUVETTE);}};
        this.put("Tentacruel", new Pokemon("Tentacruel", 73, Type.EAU, Type.POISON, talents, 80, 70, 65, 80, 120, 100));

        talents = new ArrayList<Talent>(){{this.add(Talent.CHLOROPHYLE);this.add(Talent.TEMPO_PERSO);this.add(Talent.FEUIL_GARDE);}};
        this.put("Chlorobule", new Pokemon("Chlorobule", 548, Type.PLANTE, Type.NONE, talents, 45, 35, 50, 70, 50, 30));

        talents = new ArrayList<Talent>(){{this.add(Talent.SANS_LIMITE);this.add(Talent.MODE_TRANSE);}};
        this.put("Darumacho (Mode Daruma)", new Pokemon("Darumacho (Mode Daruma)", 555, Type.FEU, Type.NONE, talents, 105, 30, 105, 140, 105, 55));

        talents = new ArrayList<Talent>(){{this.add(Talent.ESPRIT_VITAL);this.add(Talent.COLERIQUE);this.add(Talent.ACHARNE);}};
        this.put("Ferosinge", new Pokemon("Ferosinge", 56, Type.COMBAT, Type.NONE, talents, 40, 80, 35, 35, 45, 70));

        talents = new ArrayList<Talent>(){{this.add(Talent.BENET);this.add(Talent.TEMPO_PERSO);this.add(Talent.REGE_FORCE);}};
        this.put("Flagadoss", new Pokemon("Flagadoss", 80, Type.EAU, Type.PSY, talents, 95, 75, 110, 100, 80, 30));

        talents = new ArrayList<Talent>(){{this.add(Talent.MUE);this.add(Talent.FUITE);}};
        this.put("Crikzik", new Pokemon("Crikzik", 401, Type.INSECTE, Type.NONE, talents, 37, 25, 41, 25, 41, 25));

        talents = new ArrayList<Talent>(){{this.add(Talent.FLORA_VOILE);this.add(Talent.SYMBIOSIS);}};
        this.put("Florges", new Pokemon("Florges", 671, Type.FEE, Type.NONE, talents, 78, 65, 68, 112, 154, 75));

        talents = new ArrayList<Talent>(){{this.add(Talent.HYPER_CUTTER);this.add(Talent.BRISE_MOULE);this.add(Talent.IMPUDENCE);}};
        this.put("Scarabrute", new Pokemon("Scarabrute", 127, Type.INSECTE, Type.NONE, talents, 65, 125, 100, 55, 70, 85));

        talents = new ArrayList<Talent>(){{this.add(Talent.ESSAIM);this.add(Talent.INSOMNIA);this.add(Talent.SNIPER);}};
        this.put("Mimigal", new Pokemon("Mimigal", 167, Type.INSECTE, Type.POISON, talents, 40, 60, 40, 40, 40, 30));

        talents = new ArrayList<Talent>(){{this.add(Talent.FUITE);this.add(Talent.MATINAL);this.add(Talent.PIED_CONFUS);}};
        this.put("Dodrio", new Pokemon("Dodrio", 85, Type.NORMAL, Type.VOL, talents, 60, 110, 70, 60, 60, 100));

        talents = new ArrayList<Talent>(){{this.add(Talent.OEIL_COMPOSE);this.add(Talent.PIED_CONFUS);this.add(Talent.COEUR_DE_COQ);}};
        this.put("Pijako", new Pokemon("Pijako", 441, Type.NORMAL, Type.VOL, talents, 76, 65, 45, 92, 42, 91));

        talents = new ArrayList<Talent>(){{this.add(Talent.OEIL_COMPOSE);this.add(Talent.ECRAN_POUDRE);this.add(Talent.GARDE_AMIE);}};
        this.put("Lepidonille", new Pokemon("Lepidonille", 664, Type.INSECTE, Type.NONE, talents, 38, 35, 40, 27, 25, 35));

        talents = new ArrayList<Talent>(){{this.add(Talent.TEMERAIRE);this.add(Talent.ADAPTABILITE);this.add(Talent.BRISE_MOULE);}};
        this.put("Bargantua", new Pokemon("Bargantua", 550, Type.EAU, Type.NONE, talents, 70, 92, 65, 80, 55, 98));

        talents = new ArrayList<Talent>(){{this.add(Talent.MUE);}};
        this.put("Chrysacier", new Pokemon("Chrysacier", 11, Type.INSECTE, Type.NONE, talents, 50, 20, 55, 25, 25, 30));

        talents = new ArrayList<Talent>(){{this.add(Talent.ANTI_BRUIT);this.add(Talent.STATIK);this.add(Talent.BOOM_FINAL);}};
        this.put("Electrode", new Pokemon("Electrode", 101, Type.ELECTRIQUE, Type.NONE, talents, 60, 50, 70, 80, 80, 140));

        talents = new ArrayList<Talent>(){{this.add(Talent.CORPS_GEL);this.add(Talent.ARMUROUILLEE);}};
        this.put("Sorbebe", new Pokemon("Sorbebe", 582, Type.GLACE, Type.NONE, talents, 36, 50, 50, 65, 60, 44));

        talents = new ArrayList<Talent>(){{this.add(Talent.RIDEAU_NEIGE);this.add(Talent.CORPS_GEL);}};
        this.put("Givrali", new Pokemon("Givrali", 471, Type.GLACE, Type.NONE, talents, 65, 60, 110, 130, 95, 65));

        talents = new ArrayList<Talent>(){{this.add(Talent.SUINTEMENT);this.add(Talent.GLUE);this.add(Talent.GLOUTONNERIE);}};
        this.put("Gloupti", new Pokemon("Gloupti", 316, Type.POISON, Type.NONE, talents, 70, 43, 53, 43, 53, 40));

        talents = new ArrayList<Talent>(){{this.add(Talent.POING_DE_FER);this.add(Talent.MALADRESSE);this.add(Talent.ANNULE_GARDE);}};
        this.put("Gringolem", new Pokemon("Gringolem", 622, Type.SOL, Type.SPECTRE, talents, 59, 74, 50, 35, 50, 35));

        talents = new ArrayList<Talent>(){{this.add(Talent.PUANTEUR);this.add(Talent.GLUE);this.add(Talent.BOOM_FINAL);}};
        this.put("Miamiasme", new Pokemon("Miamiasme", 568, Type.POISON, Type.NONE, talents, 50, 50, 62, 40, 62, 65));

        talents = new ArrayList<Talent>(){{this.add(Talent.SERENITE);this.add(Talent.AGITATION);this.add(Talent.CHANCEUX);}};
        this.put("Togepi", new Pokemon("Togepi", 175, Type.NORMAL, Type.NONE, talents, 35, 20, 65, 40, 65, 20));

        talents = new ArrayList<Talent>(){{this.add(Talent.INSOMNIA);this.add(Talent.CHANCEUX);this.add(Talent.IMPUDENCE);}};
        this.put("Corboss", new Pokemon("Corboss", 430, Type.TENEBRE, Type.VOL, talents, 100, 125, 52, 105, 52, 71));

        talents = new ArrayList<Talent>(){{this.add(Talent.GLOUTONNERIE);this.add(Talent.BRASIER);}};
        this.put("Flamajou", new Pokemon("Flamajou", 513, Type.FEU, Type.NONE, talents, 50, 53, 48, 53, 48, 64));

        talents = new ArrayList<Talent>(){{this.add(Talent.INTIMIDATION);this.add(Talent.TEMERAIRE);}};
        this.put("Etourvol", new Pokemon("Etourvol", 397, Type.NORMAL, Type.VOL, talents, 55, 75, 50, 40, 40, 80));

        talents = new ArrayList<Talent>(){{this.add(Talent.INTIMIDATION);this.add(Talent.MUE);this.add(Talent.TENSION);}};
        this.put("Abo", new Pokemon("Abo", 23, Type.POISON, Type.NONE, talents, 35, 60, 44, 40, 54, 55));

        talents = new ArrayList<Talent>(){{this.add(Talent.ISOGRAISSE);this.add(Talent.CORPS_GEL);this.add(Talent.BENET);}};
        this.put("Obalie", new Pokemon("Obalie", 363, Type.GLACE, Type.EAU, talents, 70, 40, 50, 55, 50, 25));

        talents = new ArrayList<Talent>(){{this.add(Talent.VENTOUSE);this.add(Talent.SNIPER);this.add(Talent.LUNATIQUE);}};
        this.put("Octillery", new Pokemon("Octillery", 224, Type.EAU, Type.NONE, talents, 75, 105, 75, 105, 75, 45));

        talents = new ArrayList<Talent>(){{this.add(Talent.GLOUTONNERIE);this.add(Talent.ENGRAIS);}};
        this.put("Feuillajou", new Pokemon("Feuillajou", 511, Type.PLANTE, Type.NONE, talents, 50, 53, 48, 53, 48, 64));

        talents = new ArrayList<Talent>(){{this.add(Talent.AURA_INVERSEE);}};
        this.put("Zygarde", new Pokemon("Zygarde", 718, Type.DRAGON, Type.SOL, talents, 108, 100, 121, 81, 95, 95));

        talents = new ArrayList<Talent>(){{this.add(Talent.STATIK);}};
        this.put("Pikachu", new Pokemon("Pikachu", 25, Type.ELECTRIQUE, Type.NONE, talents, 35, 55, 30, 50, 40, 90));

        talents = new ArrayList<Talent>(){{this.add(Talent.ILLUSION);}};
        this.put("Zoroark", new Pokemon("Zoroark", 571, Type.TENEBRE, Type.NONE, talents, 60, 105, 60, 120, 60, 105));

        talents = new ArrayList<Talent>(){{this.add(Talent.COLOFORCE);}};
        this.put("Mega-Mysdibule", new Pokemon("Mega-Mysdibule", 303, Type.ACIER, Type.FEE, talents, 50, 105, 125, 55, 95, 50));

        talents = new ArrayList<Talent>(){{this.add(Talent.FERMETE);this.add(Talent.FORCE_SABLE);}};
        this.put("Nodulithe", new Pokemon("Nodulithe", 524, Type.ROCHE, Type.NONE, talents, 55, 75, 85, 25, 25, 15));

        talents = new ArrayList<Talent>(){{this.add(Talent.PARATONNERRE);this.add(Talent.SOLIDE_ROC);this.add(Talent.TEMERAIRE);}};
        this.put("Rhinastoc", new Pokemon("Rhinastoc", 464, Type.SOL, Type.ROCHE, talents, 115, 140, 130, 55, 55, 40));

        talents = new ArrayList<Talent>(){{this.add(Talent.PEAU_FEERIQUE);}};
        this.put("Mega-Gardevoir", new Pokemon("Mega-Gardevoir", 282, Type.PSY, Type.FEE, talents, 68, 85, 65, 165, 135, 100));

        talents = new ArrayList<Talent>(){{this.add(Talent.TURBO);}};
        this.put("Mega-Brasegali", new Pokemon("Mega-Brasegali", 257, Type.FEU, Type.COMBAT, talents, 80, 160, 80, 130, 80, 100));

        talents = new ArrayList<Talent>(){{this.add(Talent.CHLOROPHYLE);this.add(Talent.MATINAL);this.add(Talent.PICKPOCKET);}};
        this.put("Grainipiot", new Pokemon("Grainipiot", 273, Type.PLANTE, Type.NONE, talents, 40, 40, 50, 30, 30, 30));

        talents = new ArrayList<Talent>(){{this.add(Talent.GLISSADE);this.add(Talent.POINT_POISON);this.add(Talent.INTIMIDATION);}};
        this.put("Qwilfish", new Pokemon("Qwilfish", 211, Type.EAU, Type.POISON, talents, 65, 95, 75, 55, 55, 85));

        talents = new ArrayList<Talent>(){{this.add(Talent.VOILE_SABLE);this.add(Talent.PEAU_DURE);}};
        this.put("Carchacrok", new Pokemon("Carchacrok", 445, Type.DRAGON, Type.SOL, talents, 108, 130, 95, 80, 85, 102));

        talents = new ArrayList<Talent>(){{this.add(Talent.LEVITATION);}};
        this.put("Latios", new Pokemon("Latios", 381, Type.DRAGON, Type.PSY, talents, 80, 90, 80, 130, 110, 110));

        talents = new ArrayList<Talent>(){{this.add(Talent.ISOGRAISSE);this.add(Talent.TEMPO_PERSO);this.add(Talent.GLOUTONNERIE);}};
        this.put("Groret", new Pokemon("Groret", 326, Type.PSY, Type.NONE, talents, 80, 45, 65, 90, 110, 80));

        talents = new ArrayList<Talent>(){{this.add(Talent.ANTICIPATION);this.add(Talent.ENVELOCAPE);}};
        this.put("Cheniselle (Cape Plante)", new Pokemon("Cheniselle (Cape Plante)", 413, Type.INSECTE, Type.NONE, talents, 60, 59, 85, 79, 105, 36));

        talents = new ArrayList<Talent>(){{this.add(Talent.ATTENTION);this.add(Talent.CORPS_GEL);this.add(Talent.LUNATIQUE);}};
        this.put("Oniglali", new Pokemon("Oniglali", 362, Type.GLACE, Type.NONE, talents, 80, 80, 80, 80, 80, 80));

        talents = new ArrayList<Talent>(){{this.add(Talent.TETE_DE_ROC);this.add(Talent.FERMETE);this.add(Talent.SANS_LIMITE);}};
        this.put("Steelix", new Pokemon("Steelix", 208, Type.ACIER, Type.SOL, talents, 75, 85, 200, 55, 65, 30));

        talents = new ArrayList<Talent>(){{this.add(Talent.LEVITATION);}};
        this.put("Crefollet", new Pokemon("Crefollet", 481, Type.PSY, Type.NONE, talents, 80, 105, 105, 105, 105, 80));

        talents = new ArrayList<Talent>(){{this.add(Talent.PRESSION);}};
        this.put("Electhor", new Pokemon("Electhor", 145, Type.ELECTRIQUE, Type.VOL, talents, 90, 90, 85, 125, 90, 100));

        talents = new ArrayList<Talent>(){{this.add(Talent.RAMASSAGE);this.add(Talent.VOILE_SABLE);}};
        this.put("Phanpy", new Pokemon("Phanpy", 231, Type.SOL, Type.NONE, talents, 90, 60, 60, 40, 40, 40));

        talents = new ArrayList<Talent>(){{this.add(Talent.LEVITATION);}};
        this.put("Crehelf", new Pokemon("Crehelf", 480, Type.PSY, Type.NONE, talents, 75, 75, 130, 75, 130, 95));

        talents = new ArrayList<Talent>(){{this.add(Talent.CHLOROPHYLE);}};
        this.put("Ortide", new Pokemon("Ortide", 44, Type.PLANTE, Type.POISON, talents, 60, 65, 70, 85, 75, 40));

        talents = new ArrayList<Talent>(){{this.add(Talent.CORPS_SAIN);this.add(Talent.LIGHT_METAL);}};
        this.put("Metalosse", new Pokemon("Metalosse", 376, Type.ACIER, Type.PSY, talents, 80, 135, 130, 95, 90, 70));

        talents = new ArrayList<Talent>(){{this.add(Talent.ISOGRAISSE);this.add(Talent.COLOFORCE);this.add(Talent.HERBIVORE);}};
        this.put("Azumarill", new Pokemon("Azumarill", 184, Type.EAU, Type.NONE, talents, 100, 50, 80, 50, 80, 50));

        talents = new ArrayList<Talent>(){{this.add(Talent.CRACHIN);}};
        this.put("Kyogre", new Pokemon("Kyogre", 382, Type.EAU, Type.NONE, talents, 100, 100, 90, 150, 140, 90));

        talents = new ArrayList<Talent>(){{this.add(Talent.FARCEUR);}};
        this.put("Mega-Branette", new Pokemon("Mega-Branette", 354, Type.SPECTRE, Type.NONE, talents, 64, 165, 75, 93, 83, 75));

        talents = new ArrayList<Talent>(){{this.add(Talent.VOILE_SABLE);this.add(Talent.HYPER_CUTTER);this.add(Talent.VACCIN);}};
        this.put("Scorplane", new Pokemon("Scorplane", 207, Type.SOL, Type.VOL, talents, 65, 75, 105, 35, 65, 85));

        talents = new ArrayList<Talent>(){{this.add(Talent.ECRAN_POUDRE);this.add(Talent.FUITE);}};
        this.put("Chenipotte", new Pokemon("Chenipotte", 265, Type.INSECTE, Type.NONE, talents, 45, 45, 35, 20, 30, 20));

        talents = new ArrayList<Talent>(){{this.add(Talent.STATIK);this.add(Talent.ESPRIT_VITAL);}};
        this.put("Elektek", new Pokemon("Elektek", 125, Type.ELECTRIQUE, Type.NONE, talents, 65, 83, 57, 95, 85, 105));

        talents = new ArrayList<Talent>(){{this.add(Talent.ESPRIT_VITAL);}};
        this.put("Vigoroth", new Pokemon("Vigoroth", 288, Type.NORMAL, Type.NONE, talents, 80, 80, 80, 55, 55, 90));

        talents = new ArrayList<Talent>(){{this.add(Talent.MEDIC_NATURE);this.add(Talent.SERENITE);this.add(Talent.COEUR_SOIN);}};
        this.put("Leveinard", new Pokemon("Leveinard", 113, Type.NORMAL, Type.NONE, talents, 250, 5, 5, 35, 105, 50));

        talents = new ArrayList<Talent>(){{this.add(Talent.FUITE);this.add(Talent.REGARD_VIF);this.add(Talent.FOUILLE);}};
        this.put("Fouinar", new Pokemon("Fouinar", 162, Type.NORMAL, Type.NONE, talents, 85, 76, 64, 45, 55, 90));

        talents = new ArrayList<Talent>(){{this.add(Talent.FERMETE);this.add(Talent.TETE_DE_ROC);this.add(Talent.PHOBIQUE);}};
        this.put("Simularbre", new Pokemon("Simularbre", 185, Type.ROCHE, Type.NONE, talents, 70, 100, 115, 30, 65, 30));

        talents = new ArrayList<Talent>(){{this.add(Talent.RIDEAU_NEIGE);this.add(Talent.GLISSADE);}};
        this.put("Polagriffe", new Pokemon("Polagriffe", 614, Type.GLACE, Type.NONE, talents, 95, 110, 80, 70, 80, 50));

        talents = new ArrayList<Talent>(){{this.add(Talent.ABSORB_EAU);this.add(Talent.CHLOROPHYLE);this.add(Talent.LAVABO);}};
        this.put("Maracachi", new Pokemon("Maracachi", 556, Type.PLANTE, Type.NONE, talents, 75, 86, 67, 106, 67, 60));

        talents = new ArrayList<Talent>(){{this.add(Talent.PEAU_GELEE);this.add(Talent.ALERTE_NEIGE);}};
        this.put("Dragmara", new Pokemon("Dragmara", 699, Type.ROCHE, Type.GLACE, talents, 123, 77, 72, 99, 92, 58));

        talents = new ArrayList<Talent>(){{this.add(Talent.ESSAIM);this.add(Talent.TECHNICIEN);this.add(Talent.IMPASSIBLE);}};
        this.put("Insecateur", new Pokemon("Insecateur", 123, Type.INSECTE, Type.VOL, talents, 70, 110, 80, 55, 80, 105));

        talents = new ArrayList<Talent>(){{this.add(Talent.FUITE);this.add(Talent.MALADRESSE);this.add(Talent.ECHAUFFEMENT);}};
        this.put("Laporeille", new Pokemon("Laporeille", 427, Type.NORMAL, Type.NONE, talents, 55, 66, 44, 44, 56, 85));

        talents = new ArrayList<Talent>(){{this.add(Talent.INSOMNIA);this.add(Talent.REGARD_VIF);this.add(Talent.LENTITEINTEE);}};
        this.put("Hoot-hoot", new Pokemon("Hoot-hoot", 163, Type.NORMAL, Type.VOL, talents, 60, 30, 30, 36, 56, 50));

        talents = new ArrayList<Talent>(){{this.add(Talent.ABSORB_EAU);this.add(Talent.COQUE_ARMURE);this.add(Talent.HYDRATATION);}};
        this.put("Lokhlass", new Pokemon("Lokhlass", 131, Type.EAU, Type.GLACE, talents, 130, 85, 80, 85, 95, 60));

        talents = new ArrayList<Talent>(){{this.add(Talent.PRESSION);this.add(Talent.INFILTRATION);}};
        this.put("Spiritomb", new Pokemon("Spiritomb", 442, Type.SPECTRE, Type.TENEBRE, talents, 50, 92, 108, 92, 108, 35));

        talents = new ArrayList<Talent>(){{this.add(Talent.ARMUMAGMA);this.add(Talent.CORPS_ARDENT);this.add(Talent.ARMUROUILLEE);}};
        this.put("Limagma", new Pokemon("Limagma", 218, Type.FEU, Type.NONE, talents, 40, 40, 40, 70, 40, 20));

        talents = new ArrayList<Talent>(){{this.add(Talent.POSE_SPORE);this.add(Talent.PEAU_SECHE);}};
        this.put("Paras", new Pokemon("Paras", 46, Type.INSECTE, Type.PLANTE, talents, 35, 70, 55, 45, 55, 25));

        talents = new ArrayList<Talent>(){{this.add(Talent.CORPS_ARDENT);this.add(Talent.ESSAIM);}};
        this.put("Pyronille", new Pokemon("Pyronille", 636, Type.INSECTE, Type.FEU, talents, 55, 85, 55, 50, 55, 60));

        talents = new ArrayList<Talent>(){{this.add(Talent.ENVELOCAPE);this.add(Talent.GARDE_MAGIK);this.add(Talent.REGE_FORCE);}};
        this.put("Symbios", new Pokemon("Symbios", 579, Type.PSY, Type.NONE, talents, 110, 65, 75, 125, 85, 30));

        talents = new ArrayList<Talent>(){{this.add(Talent.JOLI_SOURIRE);this.add(Talent.GARDE_MAGIK);this.add(Talent.GARDE_AMIE);}};
        this.put("Melo", new Pokemon("Melo", 173, Type.NORMAL, Type.NONE, talents, 50, 25, 28, 45, 55, 15));

        talents = new ArrayList<Talent>(){{this.add(Talent.ENGRAIS);this.add(Talent.CONTESTATION);}};
        this.put("Lianaja", new Pokemon("Lianaja", 496, Type.PLANTE, Type.NONE, talents, 60, 60, 75, 60, 75, 83));

        talents = new ArrayList<Talent>(){{this.add(Talent.ENGRAIS);this.add(Talent.DELESTAGE);}};
        this.put("Arcko", new Pokemon("Arcko", 252, Type.PLANTE, Type.NONE, talents, 40, 45, 35, 65, 55, 70));

        talents = new ArrayList<Talent>(){{this.add(Talent.LEVITATION);this.add(Talent.IGNIFUGE);this.add(Talent.HEAVY_METAL);}};
        this.put("Archeomire", new Pokemon("Archeomire", 436, Type.ACIER, Type.PSY, talents, 57, 24, 86, 24, 86, 23));

        talents = new ArrayList<Talent>(){{this.add(Talent.RAMASSAGE);this.add(Talent.FOUILLE);this.add(Talent.INSOMNIA);}};
        this.put("Banshitrouye (Taille Normale)", new Pokemon("Banshitrouye (Taille Normale)", 711, Type.SPECTRE, Type.PLANTE, talents, 65, 90, 122, 58, 75, 84));

        talents = new ArrayList<Talent>(){{this.add(Talent.LEVITATION);}};
        this.put("Feuforeve", new Pokemon("Feuforeve", 200, Type.SPECTRE, Type.NONE, talents, 60, 60, 60, 85, 85, 85));

        talents = new ArrayList<Talent>(){{this.add(Talent.MEGA_BLASTER);}};
        this.put("Mega-Tortank", new Pokemon("Mega-Tortank", 9, Type.EAU, Type.NONE, talents, 79, 103, 120, 135, 115, 78));

        talents = new ArrayList<Talent>(){{this.add(Talent.POINT_POISON);this.add(Talent.ESSAIM);this.add(Talent.PIED_VELOCE);}};
        this.put("Venipatte", new Pokemon("Venipatte", 543, Type.INSECTE, Type.POISON, talents, 30, 45, 59, 30, 39, 57));

        talents = new ArrayList<Talent>(){{this.add(Talent.FARCEUR);this.add(Talent.INFILTRATION);this.add(Talent.CHLOROPHYLE);}};
        this.put("Doudouvet", new Pokemon("Doudouvet", 546, Type.PLANTE, Type.NONE, talents, 40, 27, 60, 37, 50, 66));

        talents = new ArrayList<Talent>(){{this.add(Talent.ISOGRAISSE);this.add(Talent.HYDRATATION);this.add(Talent.CORPS_GEL);}};
        this.put("Lamantine", new Pokemon("Lamantine", 87, Type.EAU, Type.GLACE, talents, 90, 70, 80, 70, 95, 70));

        talents = new ArrayList<Talent>(){{this.add(Talent.POSE_SPORE);this.add(Talent.PEAU_SECHE);}};
        this.put("Parasect", new Pokemon("Parasect", 47, Type.INSECTE, Type.PLANTE, talents, 60, 95, 80, 60, 80, 30));

        talents = new ArrayList<Talent>(){{this.add(Talent.SUINTEMENT);this.add(Talent.GLUE);this.add(Talent.GLOUTONNERIE);}};
        this.put("Avaltout", new Pokemon("Avaltout", 317, Type.POISON, Type.NONE, talents, 100, 73, 83, 73, 83, 55));

        talents = new ArrayList<Talent>(){{this.add(Talent.ANTI_BRUIT);this.add(Talent.STATIK);this.add(Talent.BOOM_FINAL);}};
        this.put("Voltorbe", new Pokemon("Voltorbe", 100, Type.ELECTRIQUE, Type.NONE, talents, 40, 30, 50, 55, 55, 100));

        talents = new ArrayList<Talent>(){{this.add(Talent.GLISSADE);this.add(Talent.PHOBIQUE);}};
        this.put("Magicarpe", new Pokemon("Magicarpe", 129, Type.EAU, Type.NONE, talents, 20, 10, 55, 15, 20, 80));

        talents = new ArrayList<Talent>(){{this.add(Talent.SANS_LIMITE);this.add(Talent.MODE_TRANSE);}};
        this.put("Darumacho (Mode Normal)", new Pokemon("Darumacho (Mode Normal)", 555, Type.FEU, Type.NONE, talents, 105, 140, 55, 30, 55, 95));

        talents = new ArrayList<Talent>(){{this.add(Talent.CRAN);this.add(Talent.QUERELLEUR);}};
        this.put("Heledelle", new Pokemon("Heledelle", 277, Type.NORMAL, Type.VOL, talents, 60, 85, 60, 50, 50, 125));

        talents = new ArrayList<Talent>(){{this.add(Talent.EPINE_DE_FER);}};
        this.put("Noacier", new Pokemon("Noacier", 598, Type.PLANTE, Type.ACIER, talents, 74, 94, 131, 54, 116, 20));

        talents = new ArrayList<Talent>(){{this.add(Talent.TORRENT);this.add(Talent.MOITEUR);}};
        this.put("Laggron", new Pokemon("Laggron", 260, Type.EAU, Type.SOL, talents, 100, 110, 90, 85, 90, 60));

        talents = new ArrayList<Talent>(){{this.add(Talent.TORRENT);this.add(Talent.MOITEUR);}};
        this.put("Gobou", new Pokemon("Gobou", 258, Type.EAU, Type.NONE, talents, 50, 70, 50, 50, 50, 40));

        talents = new ArrayList<Talent>(){{this.add(Talent.ATTENTION);this.add(Talent.REGARD_VIF);this.add(Talent.ACHARNE);}};
        this.put("Canarticho", new Pokemon("Canarticho", 83, Type.NORMAL, Type.VOL, talents, 52, 65, 55, 58, 62, 60));

        talents = new ArrayList<Talent>(){{this.add(Talent.SECHERESSE);}};
        this.put("Groudon", new Pokemon("Groudon", 383, Type.SOL, Type.NONE, talents, 100, 150, 140, 100, 90, 90));

        talents = new ArrayList<Talent>(){{this.add(Talent.ALERTE_NEIGE);this.add(Talent.ANTI_BRUIT);}};
        this.put("Blizzaroi", new Pokemon("Blizzaroi", 460, Type.PLANTE, Type.GLACE, talents, 90, 92, 75, 92, 85, 60));

        talents = new ArrayList<Talent>(){{this.add(Talent.CHLOROPHYLE);this.add(Talent.FORCE_SOLEIL);this.add(Talent.MATINAL);}};
        this.put("Tournegrin", new Pokemon("Tournegrin", 191, Type.PLANTE, Type.NONE, talents, 30, 30, 30, 30, 30, 30));

        talents = new ArrayList<Talent>(){{this.add(Talent.POINT_POISON);this.add(Talent.RIVALITE);this.add(Talent.SANS_LIMITE);}};
        this.put("Nidoqueen", new Pokemon("Nidoqueen", 31, Type.POISON, Type.SOL, talents, 90, 82, 87, 75, 85, 76));

        talents = new ArrayList<Talent>(){{this.add(Talent.MEDIC_NATURE);this.add(Talent.CIEL_GRIS);}};
        this.put("Altaria", new Pokemon("Altaria", 334, Type.DRAGON, Type.VOL, talents, 75, 70, 90, 70, 105, 80));

        talents = new ArrayList<Talent>(){{this.add(Talent.REGARD_VIF);this.add(Talent.PIED_CONFUS);this.add(Talent.COEUR_DE_COQ);}};
        this.put("Roucool", new Pokemon("Roucool", 16, Type.NORMAL, Type.VOL, talents, 40, 45, 40, 35, 35, 56));

        talents = new ArrayList<Talent>(){{this.add(Talent.ANTICIPATION);this.add(Talent.PEAU_SECHE);this.add(Talent.TOXITOUCHE);}};
        this.put("Cradopaud", new Pokemon("Cradopaud", 453, Type.POISON, Type.COMBAT, talents, 48, 61, 40, 61, 40, 50));

        talents = new ArrayList<Talent>(){{this.add(Talent.TORCHE);this.add(Talent.MATINAL);this.add(Talent.TENSION);}};
        this.put("Malosse", new Pokemon("Malosse", 228, Type.TENEBRE, Type.FEU, talents, 45, 60, 30, 80, 50, 65));

        talents = new ArrayList<Talent>(){{this.add(Talent.COEUR_DE_COQ);this.add(Talent.ENVELOCAPE);this.add(Talent.ARMUROUILLEE);}};
        this.put("Vaututrice", new Pokemon("Vaututrice", 630, Type.TENEBRE, Type.VOL, talents, 110, 65, 105, 55, 95, 80));

        talents = new ArrayList<Talent>(){{this.add(Talent.SERENITE);this.add(Talent.AGITATION);this.add(Talent.CHANCEUX);}};
        this.put("Togekiss", new Pokemon("Togekiss", 468, Type.NORMAL, Type.VOL, talents, 85, 50, 95, 120, 115, 80));

        talents = new ArrayList<Talent>(){{this.add(Talent.GLISSADE);this.add(Talent.HYDRATATION);this.add(Talent.ABSORB_EAU);}};
        this.put("Tritonde", new Pokemon("Tritonde", 535, Type.EAU, Type.NONE, talents, 50, 50, 40, 50, 40, 64));

        talents = new ArrayList<Talent>(){{this.add(Talent.PUANTEUR);this.add(Talent.BOOM_FINAL);}};
        this.put("Moufflair", new Pokemon("Moufflair", 435, Type.POISON, Type.TENEBRE, talents, 103, 93, 67, 71, 61, 84));

        talents = new ArrayList<Talent>(){{this.add(Talent.TORRENT);this.add(Talent.ACHARNE);}};
        this.put("Tiplouf", new Pokemon("Tiplouf", 393, Type.EAU, Type.NONE, talents, 53, 51, 53, 61, 56, 40));

        talents = new ArrayList<Talent>(){{this.add(Talent.BENET);this.add(Talent.LENTITEINTEE);this.add(Talent.FARCEUR);}};
        this.put("Lumivole", new Pokemon("Lumivole", 314, Type.INSECTE, Type.NONE, talents, 65, 47, 55, 73, 75, 85));

        talents = new ArrayList<Talent>(){{this.add(Talent.VOILE_SABLE);}};
        this.put("Carmache", new Pokemon("Carmache", 444, Type.DRAGON, Type.SOL, talents, 68, 90, 65, 50, 55, 82));

        talents = new ArrayList<Talent>(){{this.add(Talent.PLUS);this.add(Talent.MINUS);this.add(Talent.CORPS_SAIN);}};
        this.put("Cliticlic", new Pokemon("Cliticlic", 601, Type.ACIER, Type.NONE, talents, 60, 100, 115, 70, 85, 90));

        talents = new ArrayList<Talent>(){{this.add(Talent.LEVITATION);this.add(Talent.PRESSION);this.add(Talent.TELEPATHE);}};
        this.put("Giratina (Forme Originelle)", new Pokemon("Giratina (Forme Originelle)", 487, Type.SPECTRE, Type.DRAGON, talents, 150, 120, 100, 120, 100, 90));

        talents = new ArrayList<Talent>(){{this.add(Talent.BRASIER);this.add(Talent.TURBO);}};
        this.put("Poussifeu", new Pokemon("Poussifeu", 255, Type.FEU, Type.NONE, talents, 45, 60, 40, 70, 50, 45));

        talents = new ArrayList<Talent>(){{this.add(Talent.HYDRATATION);this.add(Talent.GLUE);this.add(Talent.DELESTAGE);}};
        this.put("Limaspeed", new Pokemon("Limaspeed", 617, Type.INSECTE, Type.NONE, talents, 80, 70, 40, 100, 60, 145));

        talents = new ArrayList<Talent>(){{this.add(Talent.PEAU_SECHE);this.add(Talent.VOILE_SABLE);this.add(Talent.FORCE_SOLEIL);}};
        this.put("Iguolta", new Pokemon("Iguolta", 695, Type.ELECTRIQUE, Type.NORMAL, talents, 62, 55, 52, 109, 94, 109));

        talents = new ArrayList<Talent>(){{this.add(Talent.MUE);this.add(Talent.ENVELOCAPE);}};
        this.put("Cheniti", new Pokemon("Cheniti", 412, Type.INSECTE, Type.NONE, talents, 40, 29, 45, 29, 45, 36));

        talents = new ArrayList<Talent>(){{this.add(Talent.INTIMIDATION);this.add(Talent.TECHNICIEN);this.add(Talent.IMPASSIBLE);}};
        this.put("Kapoera", new Pokemon("Kapoera", 237, Type.COMBAT, Type.NONE, talents, 50, 95, 95, 35, 110, 70));

        talents = new ArrayList<Talent>(){{this.add(Talent.FUITE);this.add(Talent.RAMASSAGE);this.add(Talent.ABSORB_VOLT);}};
        this.put("Pachirisu", new Pokemon("Pachirisu", 417, Type.ELECTRIQUE, Type.NONE, talents, 60, 45, 70, 45, 90, 95));

        talents = new ArrayList<Talent>(){{this.add(Talent.ISOGRAISSE);this.add(Talent.COLOFORCE);this.add(Talent.HERBIVORE);}};
        this.put("Marill", new Pokemon("Marill", 183, Type.EAU, Type.NONE, talents, 70, 20, 50, 20, 50, 40));

        talents = new ArrayList<Talent>(){{this.add(Talent.ADAPTABILITE);}};
        this.put("Mega-Lucario", new Pokemon("Mega-Lucario", 448, Type.ACIER, Type.COMBAT, talents, 70, 145, 88, 140, 70, 112));

        talents = new ArrayList<Talent>(){{this.add(Talent.JOLI_SOURIRE);this.add(Talent.NORMALISE);}};
        this.put("Skitty", new Pokemon("Skitty", 300, Type.NORMAL, Type.NONE, talents, 50, 45, 45, 35, 35, 50));

        talents = new ArrayList<Talent>(){{this.add(Talent.SYNCHRO);this.add(Talent.ATTENTION);this.add(Talent.GARDE_MAGIK);}};
        this.put("Abra", new Pokemon("Abra", 63, Type.PSY, Type.NONE, talents, 25, 20, 15, 105, 55, 90));

        talents = new ArrayList<Talent>(){{this.add(Talent.FEUIL_GARDE);this.add(Talent.CHLOROPHYLE);this.add(Talent.ENVELOCAPE);}};
        this.put("Couverdure", new Pokemon("Couverdure", 541, Type.INSECTE, Type.PLANTE, talents, 55, 63, 90, 50, 80, 42));

        talents = new ArrayList<Talent>(){{this.add(Talent.JOLI_SOURIRE);this.add(Talent.BATTANT);this.add(Talent.FOUILLE);}};
        this.put("Grodoudou", new Pokemon("Grodoudou", 40, Type.NORMAL, Type.NONE, talents, 140, 70, 45, 75, 50, 45));

        talents = new ArrayList<Talent>(){{this.add(Talent.PROGNATHE);}};
        this.put("Ptyranidur", new Pokemon("Ptyranidur", 696, Type.ROCHE, Type.DRAGON, talents, 58, 89, 77, 45, 45, 48));

        talents = new ArrayList<Talent>(){{this.add(Talent.DEGUISEMENT);this.add(Talent.PROTEEN);}};
        this.put("Kecleon", new Pokemon("Kecleon", 352, Type.NORMAL, Type.NONE, talents, 60, 90, 70, 60, 120, 40));

        talents = new ArrayList<Talent>(){{this.add(Talent.PRESSION);}};
        this.put("Deoxys (Forme Vitesse)", new Pokemon("Deoxys (Forme Vitesse)", 386, Type.PSY, Type.NONE, talents, 50, 95, 90, 95, 90, 180));

        talents = new ArrayList<Talent>(){{this.add(Talent.COQUE_ARMURE);this.add(Talent.MULTI_COUPS);this.add(Talent.ENVELOCAPE);}};
        this.put("Crustabri", new Pokemon("Crustabri", 91, Type.EAU, Type.GLACE, talents, 50, 95, 180, 85, 45, 70));

        talents = new ArrayList<Talent>(){{this.add(Talent.LEVITATION);}};
        this.put("Motisma (Forme Chaleur)", new Pokemon("Motisma (Forme Chaleur)", 479, Type.ELECTRIQUE, Type.SPECTRE, talents, 50, 65, 107, 105, 107, 86));

        talents = new ArrayList<Talent>(){{this.add(Talent.PEAU_SECHE);this.add(Talent.VOILE_SABLE);this.add(Talent.FORCE_SOLEIL);}};
        this.put("Galvaran", new Pokemon("Galvaran", 694, Type.ELECTRIQUE, Type.NORMAL, talents, 44, 38, 33, 61, 43, 70));

        talents = new ArrayList<Talent>(){{this.add(Talent.COEUR_SOIN);this.add(Talent.AROMA_VOILE);}};
        this.put("Fluvetin", new Pokemon("Fluvetin", 682, Type.FEE, Type.NONE, talents, 78, 52, 60, 63, 65, 23));

        talents = new ArrayList<Talent>(){{this.add(Talent.CHLOROPHYLE);this.add(Talent.HERBIVORE);this.add(Talent.SERENITE);}};
        this.put("Haydaim", new Pokemon("Haydaim", 586, Type.NORMAL, Type.PLANTE, talents, 80, 100, 70, 60, 70, 95));

        talents = new ArrayList<Talent>(){{this.add(Talent.PRESSION);}};
        this.put("Kyurem (Noir)", new Pokemon("Kyurem (Noir)", 646, Type.DRAGON, Type.GLACE, talents, 125, 170, 100, 120, 90, 95));

        talents = new ArrayList<Talent>(){{this.add(Talent.SABLE_VOLANT);this.add(Talent.FORCE_SABLE);}};
        this.put("Hippopotas", new Pokemon("Hippopotas", 449, Type.SOL, Type.NONE, talents, 68, 72, 78, 38, 42, 32));

        talents = new ArrayList<Talent>(){{this.add(Talent.LEVITATION);this.add(Talent.PRESSION);this.add(Talent.TELEPATHE);}};
        this.put("Giratina (Forme Alternative)", new Pokemon("Giratina (Forme Alternative)", 487, Type.SPECTRE, Type.DRAGON, talents, 150, 100, 120, 100, 120, 90));

        talents = new ArrayList<Talent>(){{this.add(Talent.MUE);}};
        this.put("Coconfort", new Pokemon("Coconfort", 14, Type.INSECTE, Type.POISON, talents, 45, 25, 50, 25, 25, 35));

        talents = new ArrayList<Talent>(){{this.add(Talent.CHLOROPHYLE);this.add(Talent.RECOLTE);}};
        this.put("Noeunoeuf", new Pokemon("Noeunoeuf", 102, Type.PLANTE, Type.PSY, talents, 60, 40, 80, 60, 45, 40));

        talents = new ArrayList<Talent>(){{this.add(Talent.RAMASSAGE);this.add(Talent.GLOUTONNERIE);this.add(Talent.PIED_VELOCE);}};
        this.put("Zigzaton", new Pokemon("Zigzaton", 263, Type.NORMAL, Type.NONE, talents, 38, 30, 41, 30, 41, 60));

        talents = new ArrayList<Talent>(){{this.add(Talent.CRAN);this.add(Talent.FUITE);this.add(Talent.AGITATION);}};
        this.put("Rattata", new Pokemon("Rattata", 19, Type.NORMAL, Type.NONE, talents, 30, 56, 35, 25, 35, 72));

        talents = new ArrayList<Talent>(){{this.add(Talent.ATTENTION);this.add(Talent.MATINAL);this.add(Talent.HERBIVORE);}};
        this.put("Girafarig", new Pokemon("Girafarig", 203, Type.NORMAL, Type.PSY, talents, 70, 80, 65, 90, 65, 85));

        talents = new ArrayList<Talent>(){{this.add(Talent.ISOGRAISSE);this.add(Talent.HYDRATATION);this.add(Talent.CORPS_GEL);}};
        this.put("Otaria", new Pokemon("Otaria", 86, Type.EAU, Type.NONE, talents, 65, 45, 55, 45, 70, 45));

        talents = new ArrayList<Talent>(){{this.add(Talent.PIED_VELOCE);this.add(Talent.INTIMIDATION);this.add(Talent.PHOBIQUE);}};
        this.put("Granbull", new Pokemon("Granbull", 210, Type.NORMAL, Type.NONE, talents, 90, 120, 75, 60, 60, 45));

        talents = new ArrayList<Talent>(){{this.add(Talent.GLISSADE);this.add(Talent.ARMURBASTON);this.add(Talent.ARMUROUILLEE);}};
        this.put("Kabutops", new Pokemon("Kabutops", 141, Type.ROCHE, Type.EAU, talents, 60, 115, 105, 65, 70, 80));

        talents = new ArrayList<Talent>(){{this.add(Talent.FUITE);this.add(Talent.REGARD_VIF);this.add(Talent.ANALYSTE);}};
        this.put("Ratentif", new Pokemon("Ratentif", 504, Type.NORMAL, Type.NONE, talents, 45, 55, 39, 35, 39, 42));

        talents = new ArrayList<Talent>(){{this.add(Talent.ANTICIPATION);this.add(Talent.ENVELOCAPE);}};
        this.put("Cheniselle (Cape Sol)", new Pokemon("Cheniselle (Cape Sol)", 413, Type.INSECTE, Type.NONE, talents, 60, 79, 105, 59, 85, 36));

        talents = new ArrayList<Talent>(){{this.add(Talent.ENGRAIS);this.add(Talent.CHLOROPHYLE);}};
        this.put("Bulbizarre", new Pokemon("Bulbizarre", 1, Type.PLANTE, Type.POISON, talents, 45, 49, 49, 65, 65, 45));

        talents = new ArrayList<Talent>(){{this.add(Talent.TOISON_EPAISSE);}};
        this.put("Couafarel", new Pokemon("Couafarel", 676, Type.NORMAL, Type.NONE, talents, 75, 80, 60, 65, 90, 102));

        talents = new ArrayList<Talent>(){{this.add(Talent.FORCE_SOLEIL);}};
        this.put("Mega-Demolosse", new Pokemon("Mega-Demolosse", 229, Type.TENEBRE, Type.FEU, talents, 75, 90, 90, 140, 90, 115));

        talents = new ArrayList<Talent>(){{this.add(Talent.FOUILLE);this.add(Talent.MARQUE_OMBRE);}};
        this.put("Siderella", new Pokemon("Siderella", 576, Type.PSY, Type.NONE, talents, 70, 55, 95, 95, 110, 65));

        talents = new ArrayList<Talent>(){{this.add(Talent.RAMASSAGE);this.add(Talent.BAJOUES);this.add(Talent.PLUS);}};
        this.put("Dedenne", new Pokemon("Dedenne", 702, Type.ELECTRIQUE, Type.FEE, talents, 67, 58, 57, 81, 67, 101));

        talents = new ArrayList<Talent>(){{this.add(Talent.ENGRAIS);this.add(Talent.CHLOROPHYLE);}};
        this.put("Herbizarre", new Pokemon("Herbizarre", 2, Type.PLANTE, Type.POISON, talents, 62, 62, 63, 80, 80, 60));

        talents = new ArrayList<Talent>(){{this.add(Talent.INTIMIDATION);this.add(Talent.RIVALITE);this.add(Talent.CRAN);}};
        this.put("Lixy", new Pokemon("Lixy", 403, Type.ELECTRIQUE, Type.NONE, talents, 45, 65, 34, 40, 34, 45));

        talents = new ArrayList<Talent>(){{this.add(Talent.REGARD_VIF);this.add(Talent.PIED_CONFUS);this.add(Talent.COEUR_DE_COQ);}};
        this.put("Roucarnage", new Pokemon("Roucarnage", 18, Type.NORMAL, Type.VOL, talents, 83, 80, 75, 70, 70, 91));

        talents = new ArrayList<Talent>(){{this.add(Talent.FERMETE);this.add(Talent.MAGNEPIEGE);this.add(Talent.FORCE_SABLE);}};
        this.put("Tarinor", new Pokemon("Tarinor", 299, Type.ROCHE, Type.NONE, talents, 30, 45, 135, 45, 90, 30));

        talents = new ArrayList<Talent>(){{this.add(Talent.REGARD_VIF);this.add(Talent.SNIPER);}};
        this.put("Rapasdepic", new Pokemon("Rapasdepic", 22, Type.NORMAL, Type.VOL, talents, 65, 90, 65, 61, 61, 100));

        talents = new ArrayList<Talent>(){{this.add(Talent.CRAN);}};
        this.put("Embrylex", new Pokemon("Embrylex", 246, Type.ROCHE, Type.SOL, talents, 50, 64, 50, 45, 50, 41));

        talents = new ArrayList<Talent>(){{this.add(Talent.SERENITE);this.add(Talent.AGITATION);this.add(Talent.CHANCEUX);}};
        this.put("Togetic", new Pokemon("Togetic", 176, Type.NORMAL, Type.VOL, talents, 55, 40, 85, 80, 105, 40));

        talents = new ArrayList<Talent>(){{this.add(Talent.FILTRE);}};
        this.put("Mega-Galeking", new Pokemon("Mega-Galeking", 306, Type.ACIER, Type.NONE, talents, 70, 140, 230, 60, 80, 50));

        talents = new ArrayList<Talent>(){{this.add(Talent.ANTI_BRUIT);this.add(Talent.QUERELLEUR);}};
        this.put("Brouhabam", new Pokemon("Brouhabam", 295, Type.NORMAL, Type.NONE, talents, 104, 91, 63, 91, 63, 68));

        talents = new ArrayList<Talent>(){{this.add(Talent.GLISSADE);this.add(Talent.ABSORB_EAU);}};
        this.put("Babimanta", new Pokemon("Babimanta", 458, Type.EAU, Type.VOL, talents, 45, 20, 50, 60, 120, 50));

        talents = new ArrayList<Talent>(){{this.add(Talent.INCONSCIENT);this.add(Talent.MALADRESSE);this.add(Talent.SIMPLE);}};
        this.put("Rhinolove", new Pokemon("Rhinolove", 528, Type.PSY, Type.VOL, talents, 67, 57, 55, 77, 55, 114));

        talents = new ArrayList<Talent>(){{this.add(Talent.ENGRAIS);this.add(Talent.CHLOROPHYLE);}};
        this.put("Florizarre", new Pokemon("Florizarre", 3, Type.PLANTE, Type.POISON, talents, 80, 82, 83, 100, 100, 80));

        talents = new ArrayList<Talent>(){{this.add(Talent.TORRENT);this.add(Talent.COQUE_ARMURE);}};
        this.put("Clamiral", new Pokemon("Clamiral", 503, Type.EAU, Type.NONE, talents, 95, 100, 85, 108, 70, 70));

        talents = new ArrayList<Talent>(){{this.add(Talent.VACCIN);this.add(Talent.ISOGRAISSE);this.add(Talent.GLOUTONNERIE);}};
        this.put("Ronflex", new Pokemon("Ronflex", 143, Type.NORMAL, Type.NONE, talents, 160, 110, 65, 65, 110, 30));

        talents = new ArrayList<Talent>(){{this.add(Talent.PRESSION);}};
        this.put("Kyurem (Blanc)", new Pokemon("Kyurem (Blanc)", 646, Type.DRAGON, Type.GLACE, talents, 125, 120, 90, 170, 100, 95));

        talents = new ArrayList<Talent>(){{this.add(Talent.PUANTEUR);this.add(Talent.GLUE);this.add(Talent.TOXITOUCHE);}};
        this.put("Grotadmorv", new Pokemon("Grotadmorv", 89, Type.POISON, Type.NONE, talents, 105, 105, 75, 65, 100, 50));

        talents = new ArrayList<Talent>(){{this.add(Talent.ABSORB_EAU);this.add(Talent.MOITEUR);this.add(Talent.GLISSADE);}};
        this.put("Ptitard", new Pokemon("Ptitard", 60, Type.EAU, Type.NONE, talents, 40, 50, 40, 40, 40, 90));

        talents = new ArrayList<Talent>(){{this.add(Talent.SYNCHRO);this.add(Talent.MIROIR_MAGIK);}};
        this.put("Mentali", new Pokemon("Mentali", 196, Type.PSY, Type.NONE, talents, 65, 65, 60, 130, 95, 110));

        talents = new ArrayList<Talent>(){{this.add(Talent.CRAN);this.add(Talent.SANS_LIMITE);this.add(Talent.POING_DE_FER);}};
        this.put("Betochef", new Pokemon("Betochef", 534, Type.COMBAT, Type.NONE, talents, 105, 140, 95, 55, 65, 45));

        talents = new ArrayList<Talent>(){{this.add(Talent.MEDIC_NATURE);this.add(Talent.LUMIATTIRANCE);this.add(Talent.ANALYSTE);}};
        this.put("Stari", new Pokemon("Stari", 120, Type.EAU, Type.NONE, talents, 30, 45, 55, 70, 55, 85));

        talents = new ArrayList<Talent>(){{this.add(Talent.DEFAITISTE);}};
        this.put("Arkeapti", new Pokemon("Arkeapti", 566, Type.ROCHE, Type.VOL, talents, 55, 112, 45, 74, 45, 70));

        talents = new ArrayList<Talent>(){{this.add(Talent.INTIMIDATION);this.add(Talent.IMPUDENCE);this.add(Talent.COLERIQUE);}};
        this.put("Crocorible", new Pokemon("Crocorible", 553, Type.SOL, Type.TENEBRE, talents, 95, 117, 70, 65, 70, 92));

        talents = new ArrayList<Talent>(){{this.add(Talent.TORCHE);this.add(Talent.CORPS_ARDENT);}};
        this.put("Heatran", new Pokemon("Heatran", 485, Type.FEU, Type.ACIER, talents, 91, 90, 106, 130, 106, 77));

        talents = new ArrayList<Talent>(){{this.add(Talent.FUITE);this.add(Talent.TORCHE);this.add(Talent.CORPS_ARDENT);}};
        this.put("Ponyta", new Pokemon("Ponyta", 77, Type.FEU, Type.NONE, talents, 50, 85, 55, 65, 65, 90));

        talents = new ArrayList<Talent>(){{this.add(Talent.LEVITATION);}};
        this.put("Crefadet", new Pokemon("Crefadet", 482, Type.PSY, Type.NONE, talents, 75, 125, 70, 125, 70, 115));

        talents = new ArrayList<Talent>(){{this.add(Talent.INTIMIDATION);this.add(Talent.IMPUDENCE);this.add(Talent.COLERIQUE);}};
        this.put("Escroco", new Pokemon("Escroco", 552, Type.SOL, Type.TENEBRE, talents, 60, 82, 45, 45, 45, 74));

        talents = new ArrayList<Talent>(){{this.add(Talent.ISOGRAISSE);this.add(Talent.CRAN);this.add(Talent.SANS_LIMITE);}};
        this.put("Hariyama", new Pokemon("Hariyama", 297, Type.COMBAT, Type.NONE, talents, 144, 120, 60, 40, 60, 50));

        talents = new ArrayList<Talent>(){{this.add(Talent.MARQUE_OMBRE);this.add(Talent.TELEPATHE);}};
        this.put("Qulbutoke", new Pokemon("Qulbutoke", 202, Type.PSY, Type.NONE, talents, 190, 33, 58, 33, 58, 33));

        talents = new ArrayList<Talent>(){{this.add(Talent.MEDIC_NATURE);this.add(Talent.LUMIATTIRANCE);this.add(Talent.ANALYSTE);}};
        this.put("Staross", new Pokemon("Staross", 121, Type.EAU, Type.PSY, talents, 60, 75, 85, 100, 85, 115));

        talents = new ArrayList<Talent>(){{this.add(Talent.LEVITATION);}};
        this.put("Hexagel", new Pokemon("Hexagel", 615, Type.GLACE, Type.NONE, talents, 70, 50, 30, 95, 135, 105));

        talents = new ArrayList<Talent>(){{this.add(Talent.BENET);this.add(Talent.PREDICTION);this.add(Talent.HYDRATATION);}};
        this.put("Lippouti", new Pokemon("Lippouti", 238, Type.GLACE, Type.PSY, talents, 45, 30, 15, 85, 65, 65));

        talents = new ArrayList<Talent>(){{this.add(Talent.FERMETE);this.add(Talent.ANTI_BRUIT);}};
        this.put("Bastiodon", new Pokemon("Bastiodon", 411, Type.ROCHE, Type.ACIER, talents, 60, 52, 168, 47, 138, 30));

        talents = new ArrayList<Talent>(){{this.add(Talent.MUE);this.add(Talent.GARDE_AMIE);}};
        this.put("Peregrain", new Pokemon("Peregrain", 665, Type.INSECTE, Type.NONE, talents, 45, 22, 60, 37, 30, 29));

        talents = new ArrayList<Talent>(){{this.add(Talent.PEAU_DURE);}};
        this.put("Carvanha", new Pokemon("Carvanha", 318, Type.EAU, Type.TENEBRE, talents, 45, 90, 20, 65, 20, 65));

        talents = new ArrayList<Talent>(){{this.add(Talent.STATIK);}};
        this.put("Pharamp", new Pokemon("Pharamp", 181, Type.ELECTRIQUE, Type.NONE, talents, 90, 75, 75, 115, 90, 55));

        talents = new ArrayList<Talent>(){{this.add(Talent.FORCE_PURE);}};
        this.put("Mega-Charmina", new Pokemon("Mega-Charmina", 308, Type.COMBAT, Type.PSY, talents, 60, 100, 85, 80, 85, 100));

        talents = new ArrayList<Talent>(){{this.add(Talent.CHLOROPHYLE);this.add(Talent.FEUIL_GARDE);this.add(Talent.REGE_FORCE);}};
        this.put("Bouldeneu", new Pokemon("Bouldeneu", 465, Type.PLANTE, Type.NONE, talents, 100, 100, 125, 110, 50, 50));

        talents = new ArrayList<Talent>(){{this.add(Talent.CHLOROPHYLE);this.add(Talent.FORCE_SOLEIL);this.add(Talent.MATINAL);}};
        this.put("Heliatronc", new Pokemon("Heliatronc", 192, Type.PLANTE, Type.NONE, talents, 75, 75, 55, 105, 85, 30));

        talents = new ArrayList<Talent>(){{this.add(Talent.MEGA_BLASTER);}};
        this.put("Gamblast", new Pokemon("Gamblast", 693, Type.EAU, Type.NONE, talents, 71, 73, 88, 120, 89, 59));

        talents = new ArrayList<Talent>(){{this.add(Talent.LEVITATION);}};
        this.put("Eoko", new Pokemon("Eoko", 358, Type.PSY, Type.NONE, talents, 65, 50, 70, 95, 80, 65));

        talents = new ArrayList<Talent>(){{this.add(Talent.ECHAUFFEMENT);this.add(Talent.DELESTAGE);this.add(Talent.BRISE_MOULE);}};
        this.put("Brutalibre", new Pokemon("Brutalibre", 701, Type.COMBAT, Type.VOL, talents, 70, 95, 80, 65, 70, 110));

        talents = new ArrayList<Talent>(){{this.add(Talent.REGARD_VIF);this.add(Talent.SANS_LIMITE);this.add(Talent.AGITATION);}};
        this.put("Furaiglon", new Pokemon("Furaiglon", 627, Type.NORMAL, Type.VOL, talents, 70, 83, 50, 37, 50, 60));

        talents = new ArrayList<Talent>(){{this.add(Talent.HERBIVORE);}};
        this.put("Chevroum", new Pokemon("Chevroum", 673, Type.PLANTE, Type.NONE, talents, 123, 100, 62, 97, 81, 68));

        talents = new ArrayList<Talent>(){{this.add(Talent.GLOUTONNERIE);this.add(Talent.BRASIER);}};
        this.put("Flamoutan", new Pokemon("Flamoutan", 514, Type.FEU, Type.NONE, talents, 75, 98, 63, 98, 63, 101));

        talents = new ArrayList<Talent>(){{this.add(Talent.OEIL_COMPOSE);this.add(Talent.ECRAN_POUDRE);this.add(Talent.GARDE_AMIE);}};
        this.put("Prismillon", new Pokemon("Prismillon", 666, Type.INSECTE, Type.VOL, talents, 80, 52, 50, 90, 50, 89));

        talents = new ArrayList<Talent>(){{this.add(Talent.FOUILLE);this.add(Talent.INFILTRATION);this.add(Talent.TELEPATHE);}};
        this.put("Sonistrelle", new Pokemon("Sonistrelle", 714, Type.VOL, Type.DRAGON, talents, 70, 60, 60, 82, 60, 97));

        talents = new ArrayList<Talent>(){{this.add(Talent.TORCHE);this.add(Talent.SECHERESSE);}};
        this.put("Goupix", new Pokemon("Goupix", 37, Type.FEU, Type.NONE, talents, 38, 41, 40, 50, 65, 65));

        talents = new ArrayList<Talent>(){{this.add(Talent.TETE_DE_ROC);this.add(Talent.FERMETE);}};
        this.put("Gravalanch", new Pokemon("Gravalanch", 75, Type.ROCHE, Type.SOL, talents, 55, 95, 115, 45, 45, 35));

        talents = new ArrayList<Talent>(){{this.add(Talent.ATTENTION);this.add(Talent.INFILTRATION);}};
        this.put("Nostenfer", new Pokemon("Nostenfer", 169, Type.POISON, Type.VOL, talents, 85, 90, 80, 70, 80, 130));

        talents = new ArrayList<Talent>(){{this.add(Talent.CHLOROPHYLE);this.add(Talent.GLOUTONNERIE);}};
        this.put("Chetiflor", new Pokemon("Chetiflor", 69, Type.PLANTE, Type.POISON, talents, 50, 75, 35, 70, 30, 40));

        talents = new ArrayList<Talent>(){{this.add(Talent.LEVITATION);}};
        this.put("Motisma (Forme Lavage)", new Pokemon("Motisma (Forme Lavage)", 479, Type.ELECTRIQUE, Type.SPECTRE, talents, 50, 65, 107, 105, 107, 86));

        talents = new ArrayList<Talent>(){{this.add(Talent.LAVABO);}};
        this.put("Lumineon", new Pokemon("Lumineon", 457, Type.EAU, Type.NONE, talents, 69, 69, 76, 69, 86, 91));

        talents = new ArrayList<Talent>(){{this.add(Talent.TORRENT);this.add(Talent.PROTEEN);}};
        this.put("Croaporal", new Pokemon("Croaporal", 657, Type.EAU, Type.NONE, talents, 54, 63, 52, 83, 56, 97));

        talents = new ArrayList<Talent>(){{this.add(Talent.PARATONNERRE);this.add(Talent.TETE_DE_ROC);this.add(Talent.TEMERAIRE);}};
        this.put("Rhinocorne", new Pokemon("Rhinocorne", 111, Type.SOL, Type.ROCHE, talents, 80, 85, 95, 30, 30, 25));

        talents = new ArrayList<Talent>(){{this.add(Talent.INTIMIDATION);this.add(Talent.IMPUDENCE);}};
        this.put("Leviator", new Pokemon("Leviator", 130, Type.EAU, Type.VOL, talents, 95, 125, 79, 60, 100, 81));

        talents = new ArrayList<Talent>(){{this.add(Talent.PEAU_MIRACLE);this.add(Talent.GARDE_MAGIK);this.add(Talent.LENTITEINTEE);}};
        this.put("Cryptero", new Pokemon("Cryptero", 561, Type.PSY, Type.VOL, talents, 72, 58, 80, 103, 80, 97));

        talents = new ArrayList<Talent>(){{this.add(Talent.ISOGRAISSE);this.add(Talent.TEMPO_PERSO);}};
        this.put("Spoink", new Pokemon("Spoink", 325, Type.PSY, Type.NONE, talents, 60, 25, 35, 70, 80, 60));

        talents = new ArrayList<Talent>(){{this.add(Talent.PRESSION);this.add(Talent.TELEPATHE);}};
        this.put("Dialga", new Pokemon("Dialga", 483, Type.ACIER, Type.DRAGON, talents, 100, 120, 120, 150, 100, 90));

        talents = new ArrayList<Talent>(){{this.add(Talent.VOILE_SABLE);this.add(Talent.BAIGNE_SABLE);}};
        this.put("Sabelette", new Pokemon("Sabelette", 27, Type.SOL, Type.NONE, talents, 50, 75, 85, 20, 30, 40));

        talents = new ArrayList<Talent>(){{this.add(Talent.PARATONNERRE);this.add(Talent.STATIK);}};
        this.put("Dynavolt", new Pokemon("Dynavolt", 309, Type.ELECTRIQUE, Type.NONE, talents, 40, 45, 40, 65, 40, 65));

        talents = new ArrayList<Talent>(){{this.add(Talent.STATIK);this.add(Talent.PARATONNERRE);}};
        this.put("Pichu", new Pokemon("Pichu", 172, Type.ELECTRIQUE, Type.NONE, talents, 20, 40, 15, 35, 35, 60));

        talents = new ArrayList<Talent>(){{this.add(Talent.COEUR_NOBLE);}};
        this.put("Terrakium", new Pokemon("Terrakium", 639, Type.ROCHE, Type.COMBAT, talents, 91, 129, 90, 72, 90, 108));

        talents = new ArrayList<Talent>(){{this.add(Talent.PEAU_GELEE);}};
        this.put("Amagara", new Pokemon("Amagara", 698, Type.ROCHE, Type.GLACE, talents, 77, 59, 50, 67, 63, 46));

        talents = new ArrayList<Talent>(){{this.add(Talent.GLISSADE);this.add(Talent.IGNIFU_VOILE);}};
        this.put("Poissirene", new Pokemon("Poissirene", 118, Type.EAU, Type.NONE, talents, 45, 67, 60, 35, 50, 63));

        talents = new ArrayList<Talent>(){{this.add(Talent.CORPS_ARDENT);this.add(Talent.ESPRIT_VITAL);}};
        this.put("Magby", new Pokemon("Magby", 240, Type.FEU, Type.NONE, talents, 45, 75, 37, 70, 55, 83));

        talents = new ArrayList<Talent>(){{this.add(Talent.FARCEUR);this.add(Talent.INFILTRATION);this.add(Talent.CHLOROPHYLE);}};
        this.put("Farfaduvet", new Pokemon("Farfaduvet", 547, Type.PLANTE, Type.NONE, talents, 60, 67, 85, 77, 75, 116));

        talents = new ArrayList<Talent>(){{this.add(Talent.JOLI_SOURIRE);this.add(Talent.MALADRESSE);this.add(Talent.ECHAUFFEMENT);}};
        this.put("Lockpin", new Pokemon("Lockpin", 428, Type.NORMAL, Type.NONE, talents, 65, 76, 84, 54, 96, 105));

        talents = new ArrayList<Talent>(){{this.add(Talent.ABSORB_VOLT);this.add(Talent.LUMIATTIRANCE);this.add(Talent.ABSORB_EAU);}};
        this.put("Loupio", new Pokemon("Loupio", 170, Type.EAU, Type.ELECTRIQUE, talents, 75, 38, 38, 56, 56, 67));

        talents = new ArrayList<Talent>(){{this.add(Talent.PARATONNERRE);this.add(Talent.STATIK);this.add(Talent.MINUS);}};
        this.put("Elecsprint", new Pokemon("Elecsprint", 310, Type.ELECTRIQUE, Type.NONE, talents, 70, 75, 60, 105, 60, 105));

        talents = new ArrayList<Talent>(){{this.add(Talent.RAMASSAGE);this.add(Talent.FOUILLE);this.add(Talent.INSOMNIA);}};
        this.put("Banshitrouye (Taille Ultra)", new Pokemon("Banshitrouye (Taille Ultra)", 711, Type.SPECTRE, Type.PLANTE, talents, 85, 100, 122, 58, 75, 54));

        talents = new ArrayList<Talent>(){{this.add(Talent.COEUR_NOBLE);}};
        this.put("Keldeo", new Pokemon("Keldeo", 647, Type.EAU, Type.COMBAT, talents, 91, 72, 90, 129, 90, 108));

        talents = new ArrayList<Talent>(){{this.add(Talent.ENGRAIS);this.add(Talent.DELESTAGE);}};
        this.put("Jungko", new Pokemon("Jungko", 254, Type.PLANTE, Type.NONE, talents, 70, 85, 65, 105, 85, 120));

        talents = new ArrayList<Talent>(){{this.add(Talent.FARCEUR);this.add(Talent.ACHARNE);}};
        this.put("Boreas (Forme Avatar)", new Pokemon("Boreas (Forme Avatar)", 641, Type.VOL, Type.NONE, talents, 79, 115, 70, 125, 80, 111));

        talents = new ArrayList<Talent>(){{this.add(Talent.CORPS_SAIN);this.add(Talent.LIGHT_METAL);}};
        this.put("Registeel", new Pokemon("Registeel", 379, Type.ACIER, Type.NONE, talents, 80, 75, 150, 75, 150, 50));

        talents = new ArrayList<Talent>(){{this.add(Talent.SYNCHRO);this.add(Talent.MATINAL);this.add(Talent.MIROIR_MAGIK);}};
        this.put("Xatu", new Pokemon("Xatu", 178, Type.PSY, Type.VOL, talents, 65, 75, 70, 95, 70, 95));

        talents = new ArrayList<Talent>(){{this.add(Talent.LEVITATION);}};
        this.put("Skelenox", new Pokemon("Skelenox", 355, Type.SPECTRE, Type.NONE, talents, 20, 40, 90, 30, 90, 25));

        talents = new ArrayList<Talent>(){{this.add(Talent.REGARD_VIF);}};
        this.put("Etourmi", new Pokemon("Etourmi", 396, Type.NORMAL, Type.VOL, talents, 40, 55, 30, 30, 30, 60));

        talents = new ArrayList<Talent>(){{this.add(Talent.ECRAN_POUDRE);this.add(Talent.LENTITEINTEE);}};
        this.put("Aeromite", new Pokemon("Aeromite", 49, Type.INSECTE, Type.POISON, talents, 70, 65, 60, 90, 75, 90));

        talents = new ArrayList<Talent>(){{this.add(Talent.TORRENT);this.add(Talent.CUVETTE);}};
        this.put("Tortank", new Pokemon("Tortank", 9, Type.EAU, Type.NONE, talents, 79, 83, 100, 85, 105, 78));

        talents = new ArrayList<Talent>(){{this.add(Talent.TECHNICIEN);}};
        this.put("Mega-Cizayox", new Pokemon("Mega-Cizayox", 212, Type.INSECTE, Type.ACIER, talents, 70, 150, 140, 65, 100, 75));

        talents = new ArrayList<Talent>(){{this.add(Talent.MUE);this.add(Talent.ECAILLE_SPECIALE);}};
        this.put("Minidraco", new Pokemon("Minidraco", 147, Type.DRAGON, Type.NONE, talents, 41, 64, 45, 50, 50, 50));

        talents = new ArrayList<Talent>(){{this.add(Talent.LEVITATION);}};
        this.put("Trioxhydre", new Pokemon("Trioxhydre", 635, Type.TENEBRE, Type.DRAGON, talents, 92, 105, 90, 125, 90, 98));

        talents = new ArrayList<Talent>(){{this.add(Talent.JOLI_SOURIRE);this.add(Talent.GARDE_MAGIK);this.add(Talent.GARDE_AMIE);}};
        this.put("Melofee", new Pokemon("Melofee", 35, Type.NORMAL, Type.NONE, talents, 70, 45, 48, 60, 65, 35));

        talents = new ArrayList<Talent>(){{this.add(Talent.FERMETE);this.add(Talent.COQUE_ARMURE);this.add(Talent.ARMUROUILLEE);}};
        this.put("Crabicoque", new Pokemon("Crabicoque", 557, Type.INSECTE, Type.ROCHE, talents, 50, 65, 85, 35, 35, 55));

        talents = new ArrayList<Talent>(){{this.add(Talent.ENGRAIS);this.add(Talent.COQUE_ARMURE);}};
        this.put("Torterra", new Pokemon("Torterra", 389, Type.PLANTE, Type.SOL, talents, 95, 109, 105, 75, 85, 56));

        talents = new ArrayList<Talent>(){{this.add(Talent.BAIGNE_SABLE);this.add(Talent.FORCE_SABLE);this.add(Talent.BRISE_MOULE);}};
        this.put("Rototaupe", new Pokemon("Rototaupe", 529, Type.SOL, Type.NONE, talents, 60, 85, 40, 30, 45, 68));

        talents = new ArrayList<Talent>(){{this.add(Talent.CHLOROPHYLE);}};
        this.put("Ceribou", new Pokemon("Ceribou", 420, Type.PLANTE, Type.NONE, talents, 45, 35, 45, 62, 53, 35));

        talents = new ArrayList<Talent>(){{this.add(Talent.SIMPLE);this.add(Talent.INCONSCIENT);this.add(Talent.LUNATIQUE);}};
        this.put("Keunotor", new Pokemon("Keunotor", 399, Type.NORMAL, Type.NONE, talents, 59, 45, 40, 35, 40, 31));

        talents = new ArrayList<Talent>(){{this.add(Talent.POINT_POISON);this.add(Talent.RIVALITE);this.add(Talent.AGITATION);}};
        this.put("Nidoran F", new Pokemon("Nidoran F", 29, Type.POISON, Type.NONE, talents, 55, 47, 52, 40, 40, 41));

        talents = new ArrayList<Talent>(){{this.add(Talent.TENSION);this.add(Talent.RIVALITE);this.add(Talent.IMPUDENCE);}};
        this.put("Helionceau", new Pokemon("Helionceau", 667, Type.FEU, Type.NORMAL, talents, 62, 50, 58, 73, 54, 72));

        talents = new ArrayList<Talent>(){{this.add(Talent.PRESSION);this.add(Talent.TORCHE);}};
        this.put("Entei", new Pokemon("Entei", 244, Type.FEU, Type.NONE, talents, 115, 115, 85, 90, 75, 100));

        talents = new ArrayList<Talent>(){{this.add(Talent.POINT_POISON);this.add(Talent.RIVALITE);this.add(Talent.AGITATION);}};
        this.put("Nidoran M", new Pokemon("Nidoran M", 32, Type.POISON, Type.NONE, talents, 46, 57, 40, 40, 40, 50));

        talents = new ArrayList<Talent>(){{this.add(Talent.TORRENT);this.add(Talent.COQUE_ARMURE);}};
        this.put("Moustillon", new Pokemon("Moustillon", 501, Type.EAU, Type.NONE, talents, 55, 55, 45, 63, 45, 45));

        talents = new ArrayList<Talent>(){{this.add(Talent.OEIL_COMPOSE);this.add(Talent.TENSION);this.add(Talent.ESSAIM);}};
        this.put("Mygavolt", new Pokemon("Mygavolt", 596, Type.INSECTE, Type.ELECTRIQUE, talents, 70, 77, 60, 97, 60, 108));

        talents = new ArrayList<Talent>(){{this.add(Talent.INSOMNIA);this.add(Talent.PREDICTION);this.add(Talent.ATTENTION);}};
        this.put("Soporifik", new Pokemon("Soporifik", 96, Type.PSY, Type.NONE, talents, 60, 48, 45, 43, 90, 42));

        talents = new ArrayList<Talent>(){{this.add(Talent.ANNULE_GARDE);}};
        this.put("Dimocles", new Pokemon("Dimocles", 680, Type.ACIER, Type.SPECTRE, talents, 59, 110, 150, 45, 49, 35));

        talents = new ArrayList<Talent>(){{this.add(Talent.ATTENTION);this.add(Talent.IMPASSIBLE);this.add(Talent.FARCEUR);}};
        this.put("Riolu", new Pokemon("Riolu", 447, Type.COMBAT, Type.NONE, talents, 40, 70, 40, 35, 40, 60));

        talents = new ArrayList<Talent>(){{this.add(Talent.ECRAN_POUDRE);this.add(Talent.FUITE);}};
        this.put("Aspicot", new Pokemon("Aspicot", 13, Type.INSECTE, Type.POISON, talents, 40, 35, 30, 20, 20, 50));

        talents = new ArrayList<Talent>(){{this.add(Talent.RIDEAU_NEIGE);}};
        this.put("Marcacrin", new Pokemon("Marcacrin", 220, Type.GLACE, Type.SOL, talents, 50, 50, 40, 30, 30, 50));

        talents = new ArrayList<Talent>(){{this.add(Talent.HYPER_CUTTER);this.add(Talent.INTIMIDATION);this.add(Talent.SANS_LIMITE);}};
        this.put("Mysdibule", new Pokemon("Mysdibule", 303, Type.ACIER, Type.NONE, talents, 50, 85, 85, 55, 55, 50));

        talents = new ArrayList<Talent>(){{this.add(Talent.ECRAN_FUMEE);this.add(Talent.COQUE_ARMURE);}};
        this.put("Chartor", new Pokemon("Chartor", 324, Type.FEU, Type.NONE, talents, 70, 85, 140, 85, 70, 20));

        talents = new ArrayList<Talent>(){{this.add(Talent.BAIGNE_SABLE);this.add(Talent.FORCE_SABLE);this.add(Talent.BRISE_MOULE);}};
        this.put("Minotaupe", new Pokemon("Minotaupe", 530, Type.SOL, Type.ACIER, talents, 110, 135, 60, 50, 65, 88));

        talents = new ArrayList<Talent>(){{this.add(Talent.INTIMIDATION);this.add(Talent.TENSION);}};
        this.put("Maskadra", new Pokemon("Maskadra", 284, Type.INSECTE, Type.VOL, talents, 70, 60, 62, 80, 82, 60));

        talents = new ArrayList<Talent>(){{this.add(Talent.TURBO);this.add(Talent.LENTITEINTEE);this.add(Talent.FOUILLE);}};
        this.put("Yanmega", new Pokemon("Yanmega", 469, Type.INSECTE, Type.VOL, talents, 86, 76, 86, 116, 56, 95));

        talents = new ArrayList<Talent>(){{this.add(Talent.ESSAIM);this.add(Talent.TECHNICIEN);}};
        this.put("Melokrik", new Pokemon("Melokrik", 402, Type.INSECTE, Type.NONE, talents, 77, 85, 51, 55, 51, 65));

        talents = new ArrayList<Talent>(){{this.add(Talent.POINT_POISON);this.add(Talent.ESSAIM);this.add(Talent.TURBO);}};
        this.put("Scobolide", new Pokemon("Scobolide", 544, Type.INSECTE, Type.POISON, talents, 40, 55, 99, 40, 79, 47));

        talents = new ArrayList<Talent>(){{this.add(Talent.ENGRAIS);this.add(Talent.DELESTAGE);}};
        this.put("Massko", new Pokemon("Massko", 253, Type.PLANTE, Type.NONE, talents, 50, 65, 45, 85, 65, 95));

        talents = new ArrayList<Talent>(){{this.add(Talent.BRASIER);this.add(Talent.TURBO);}};
        this.put("Brasegali", new Pokemon("Brasegali", 257, Type.FEU, Type.COMBAT, talents, 80, 120, 70, 110, 70, 80));

        talents = new ArrayList<Talent>(){{this.add(Talent.VENTOUSE);this.add(Talent.CONTESTATION);}};
        this.put("Sepiatroce", new Pokemon("Sepiatroce", 687, Type.TENEBRE, Type.PSY, talents, 86, 92, 88, 68, 73, 75));

        talents = new ArrayList<Talent>(){{this.add(Talent.COEUR_DE_COQ);this.add(Talent.ENVELOCAPE);this.add(Talent.ARMUROUILLEE);}};
        this.put("Vostourno", new Pokemon("Vostourno", 629, Type.TENEBRE, Type.VOL, talents, 70, 55, 75, 45, 65, 60));

        talents = new ArrayList<Talent>(){{this.add(Talent.TETE_DE_ROC);this.add(Talent.PARATONNERRE);this.add(Talent.ARMURBASTON);}};
        this.put("Ossatueur", new Pokemon("Ossatueur", 105, Type.SOL, Type.NONE, talents, 60, 80, 110, 50, 80, 45));

        talents = new ArrayList<Talent>(){{this.add(Talent.HERBIVORE);}};
        this.put("Cabriolaine", new Pokemon("Cabriolaine", 672, Type.PLANTE, Type.NONE, talents, 66, 65, 48, 62, 57, 52));

        talents = new ArrayList<Talent>(){{this.add(Talent.GLISSADE);this.add(Talent.CUVETTE);}};
        this.put("Lombre", new Pokemon("Lombre", 271, Type.EAU, Type.PLANTE, talents, 60, 50, 50, 60, 70, 50));

        talents = new ArrayList<Talent>(){{this.add(Talent.CHERCHE_MIEL);this.add(Talent.AGITATION);}};
        this.put("Apitrini", new Pokemon("Apitrini", 415, Type.INSECTE, Type.VOL, talents, 30, 30, 42, 30, 42, 70));

        talents = new ArrayList<Talent>(){{this.add(Talent.CRAN);this.add(Talent.QUERELLEUR);}};
        this.put("Nirondelle", new Pokemon("Nirondelle", 276, Type.NORMAL, Type.VOL, talents, 40, 55, 30, 30, 30, 85));

        talents = new ArrayList<Talent>(){{this.add(Talent.JOLI_SOURIRE);this.add(Talent.TECHNICIEN);this.add(Talent.MULTI_COUPS);}};
        this.put("Chinchidou", new Pokemon("Chinchidou", 572, Type.NORMAL, Type.NONE, talents, 55, 50, 40, 40, 40, 75));

        talents = new ArrayList<Talent>(){{this.add(Talent.MULTITYPE);}};
        this.put("Arceus", new Pokemon("Arceus", 493, Type.NORMAL, Type.NONE, talents, 120, 120, 120, 120, 120, 120));

        talents = new ArrayList<Talent>(){{this.add(Talent.GRIFFE_DURE);}};
        this.put("Mega-Ptera", new Pokemon("Mega-Ptera", 142, Type.ROCHE, Type.VOL, talents, 80, 135, 85, 70, 95, 150));

        talents = new ArrayList<Talent>(){{this.add(Talent.SYNCHRO);this.add(Talent.ATTENTION);this.add(Talent.GARDE_MAGIK);}};
        this.put("Kadabra", new Pokemon("Kadabra", 64, Type.PSY, Type.NONE, talents, 40, 35, 30, 120, 70, 105));

        talents = new ArrayList<Talent>(){{this.add(Talent.CORPS_SAIN);this.add(Talent.FERMETE);}};
        this.put("Regirock", new Pokemon("Regirock", 377, Type.ROCHE, Type.NONE, talents, 80, 100, 200, 50, 100, 50));

        talents = new ArrayList<Talent>(){{this.add(Talent.PRESSION);}};
        this.put("Deoxys (Forme Attaque)", new Pokemon("Deoxys (Forme Attaque)", 386, Type.PSY, Type.NONE, talents, 50, 180, 20, 180, 20, 150));

        talents = new ArrayList<Talent>(){{this.add(Talent.ABSORB_EAU);this.add(Talent.MOITEUR);this.add(Talent.CRACHIN);}};
        this.put("Tarpaud", new Pokemon("Tarpaud", 186, Type.EAU, Type.NONE, talents, 90, 75, 75, 90, 100, 70));

        talents = new ArrayList<Talent>(){{this.add(Talent.RAMASSAGE);this.add(Talent.BAJOUES);this.add(Talent.COLOFORCE);}};
        this.put("Sapereau", new Pokemon("Sapereau", 659, Type.NORMAL, Type.NONE, talents, 38, 36, 38, 32, 36, 57));

        talents = new ArrayList<Talent>(){{this.add(Talent.VOILE_SABLE);this.add(Talent.ABSORB_EAU);}};
        this.put("Cacturne", new Pokemon("Cacturne", 332, Type.PLANTE, Type.TENEBRE, talents, 70, 115, 60, 115, 60, 55));

        talents = new ArrayList<Talent>(){{this.add(Talent.STATIK);this.add(Talent.PARATONNERRE);}};
        this.put("Raichu", new Pokemon("Raichu", 26, Type.ELECTRIQUE, Type.NONE, talents, 60, 90, 55, 90, 80, 100));

        talents = new ArrayList<Talent>(){{this.add(Talent.GLISSADE);this.add(Talent.IGNIFU_VOILE);this.add(Talent.PARATONNERRE);}};
        this.put("Poissoroy", new Pokemon("Poissoroy", 119, Type.EAU, Type.NONE, talents, 80, 92, 65, 65, 80, 68));

        talents = new ArrayList<Talent>(){{this.add(Talent.LEVITATION);}};
        this.put("Vibraninf", new Pokemon("Vibraninf", 329, Type.SOL, Type.DRAGON, talents, 50, 70, 50, 50, 50, 70));

        talents = new ArrayList<Talent>(){{this.add(Talent.VENTOUSE);this.add(Talent.LAVABO);}};
        this.put("Vacilys", new Pokemon("Vacilys", 346, Type.ROCHE, Type.PLANTE, talents, 86, 81, 97, 81, 107, 43));

        talents = new ArrayList<Talent>(){{this.add(Talent.CHLOROPHYLE);this.add(Talent.HERBIVORE);this.add(Talent.SERENITE);}};
        this.put("Vivaldaim", new Pokemon("Vivaldaim", 585, Type.NORMAL, Type.PLANTE, talents, 60, 60, 50, 40, 50, 75));

        talents = new ArrayList<Talent>(){{this.add(Talent.PUANTEUR);this.add(Talent.GLUE);this.add(Talent.TOXITOUCHE);}};
        this.put("Tadmorv", new Pokemon("Tadmorv", 88, Type.POISON, Type.NONE, talents, 80, 80, 50, 40, 50, 25));

        talents = new ArrayList<Talent>(){{this.add(Talent.LEVITATION);}};
        this.put("Zarbi", new Pokemon("Zarbi", 201, Type.PSY, Type.NONE, talents, 48, 72, 48, 72, 48, 48));

        talents = new ArrayList<Talent>(){{this.add(Talent.BRASIER);this.add(Talent.TURBO);}};
        this.put("Galifeu", new Pokemon("Galifeu", 256, Type.FEU, Type.COMBAT, talents, 60, 85, 60, 85, 60, 55));

        talents = new ArrayList<Talent>(){{this.add(Talent.ESSAIM);this.add(Talent.SNIPER);}};
        this.put("Dardargnan", new Pokemon("Dardargnan", 15, Type.INSECTE, Type.POISON, talents, 65, 80, 40, 45, 80, 75));

        talents = new ArrayList<Talent>(){{this.add(Talent.RIDEAU_NEIGE);this.add(Talent.PHOBIQUE);}};
        this.put("Polarhume", new Pokemon("Polarhume", 613, Type.GLACE, Type.NONE, talents, 55, 70, 40, 60, 40, 40));

        talents = new ArrayList<Talent>(){{this.add(Talent.MEDIC_NATURE);this.add(Talent.CIEL_GRIS);}};
        this.put("Tylton", new Pokemon("Tylton", 333, Type.NORMAL, Type.VOL, talents, 45, 40, 60, 40, 75, 50));

        talents = new ArrayList<Talent>(){{this.add(Talent.BRASIER);this.add(Talent.TEMERAIRE);}};
        this.put("Roitiflam", new Pokemon("Roitiflam", 500, Type.FEU, Type.COMBAT, talents, 110, 123, 65, 100, 65, 65));

        talents = new ArrayList<Talent>(){{this.add(Talent.ESSAIM);this.add(Talent.CHLOROPHYLE);this.add(Talent.ENVELOCAPE);}};
        this.put("Manternel", new Pokemon("Manternel", 542, Type.INSECTE, Type.PLANTE, talents, 75, 103, 80, 70, 70, 92));

        talents = new ArrayList<Talent>(){{this.add(Talent.INSOMNIA);this.add(Talent.CHANCEUX);this.add(Talent.FARCEUR);}};
        this.put("Cornebre", new Pokemon("Cornebre", 198, Type.TENEBRE, Type.VOL, talents, 60, 85, 42, 85, 42, 91));

        talents = new ArrayList<Talent>(){{this.add(Talent.CORPS_SAIN);this.add(Talent.LIGHT_METAL);}};
        this.put("Terhal", new Pokemon("Terhal", 374, Type.ACIER, Type.PSY, talents, 40, 55, 80, 35, 60, 30));

        talents = new ArrayList<Talent>(){{this.add(Talent.REGE_FORCE);this.add(Talent.ATTENTION);this.add(Talent.TEMERAIRE);}};
        this.put("Shaofouine", new Pokemon("Shaofouine", 620, Type.COMBAT, Type.NONE, talents, 65, 125, 60, 95, 60, 105));

        talents = new ArrayList<Talent>(){{this.add(Talent.ESSAIM);this.add(Talent.LENTITEINTEE);}};
        this.put("Papilord", new Pokemon("Papilord", 414, Type.INSECTE, Type.VOL, talents, 70, 94, 50, 94, 50, 66));

        talents = new ArrayList<Talent>(){{this.add(Talent.LEVITATION);}};
        this.put("Fantominus", new Pokemon("Fantominus", 92, Type.SPECTRE, Type.POISON, talents, 30, 35, 30, 100, 35, 80));

        talents = new ArrayList<Talent>(){{this.add(Talent.REGARD_VIF);this.add(Talent.COEUR_DE_COQ);this.add(Talent.HYDRATATION);}};
        this.put("Lakmecygne", new Pokemon("Lakmecygne", 581, Type.EAU, Type.VOL, talents, 75, 87, 63, 87, 63, 98));

        talents = new ArrayList<Talent>(){{this.add(Talent.HYPER_CUTTER);this.add(Talent.PIEGE);this.add(Talent.SANS_LIMITE);}};
        this.put("Kraknoix", new Pokemon("Kraknoix", 328, Type.SOL, Type.NONE, talents, 45, 100, 45, 45, 45, 10));

        talents = new ArrayList<Talent>(){{this.add(Talent.MEDIC_NATURE);this.add(Talent.SERENITE);this.add(Talent.COEUR_SOIN);}};
        this.put("Leuphorie", new Pokemon("Leuphorie", 242, Type.NORMAL, Type.NONE, talents, 255, 10, 10, 75, 135, 55));

        talents = new ArrayList<Talent>(){{this.add(Talent.ENGRAIS);this.add(Talent.COQUE_ARMURE);}};
        this.put("Boskara", new Pokemon("Boskara", 388, Type.PLANTE, Type.NONE, talents, 75, 89, 85, 55, 65, 36));

        talents = new ArrayList<Talent>(){{this.add(Talent.BRISE_MOULE);this.add(Talent.SANS_LIMITE);}};
        this.put("Charkos", new Pokemon("Charkos", 409, Type.ROCHE, Type.NONE, talents, 97, 165, 60, 65, 50, 58));

        talents = new ArrayList<Talent>(){{this.add(Talent.FERMETE);this.add(Talent.FORCE_SABLE);}};
        this.put("Gigalithe", new Pokemon("Gigalithe", 526, Type.ROCHE, Type.NONE, talents, 85, 135, 130, 60, 70, 25));

        talents = new ArrayList<Talent>(){{this.add(Talent.REGARD_VIF);this.add(Talent.PIED_CONFUS);this.add(Talent.COEUR_DE_COQ);}};
        this.put("Roucoups", new Pokemon("Roucoups", 17, Type.NORMAL, Type.VOL, talents, 63, 60, 55, 50, 50, 71));

        talents = new ArrayList<Talent>(){{this.add(Talent.LAVABO);this.add(Talent.GLISSADE);this.add(Talent.IGNIFU_VOILE);}};
        this.put("Ecayon", new Pokemon("Ecayon", 456, Type.EAU, Type.NONE, talents, 49, 49, 56, 49, 61, 66));

        talents = new ArrayList<Talent>(){{this.add(Talent.OEIL_COMPOSE);this.add(Talent.TENSION);this.add(Talent.ESSAIM);}};
        this.put("Statitik", new Pokemon("Statitik", 595, Type.INSECTE, Type.ELECTRIQUE, talents, 50, 47, 50, 57, 50, 65));

        talents = new ArrayList<Talent>(){{this.add(Talent.PRESSION);}};
        this.put("Teraclope", new Pokemon("Teraclope", 356, Type.SPECTRE, Type.NONE, talents, 40, 70, 130, 60, 130, 25));

        talents = new ArrayList<Talent>(){{this.add(Talent.ABSORB_EAU);this.add(Talent.HYDRATATION);}};
        this.put("Aquali", new Pokemon("Aquali", 134, Type.EAU, Type.NONE, talents, 130, 65, 60, 110, 95, 65));

        talents = new ArrayList<Talent>(){{this.add(Talent.FERMETE);this.add(Talent.FORCE_SABLE);}};
        this.put("Geolithe", new Pokemon("Geolithe", 525, Type.ROCHE, Type.NONE, talents, 70, 105, 105, 50, 40, 20));

        talents = new ArrayList<Talent>(){{this.add(Talent.MUE);this.add(Talent.ECAILLE_SPECIALE);}};
        this.put("Draco", new Pokemon("Draco", 148, Type.DRAGON, Type.NONE, talents, 61, 84, 65, 70, 70, 70));

        talents = new ArrayList<Talent>(){{this.add(Talent.FERMETE);this.add(Talent.MAGNEPIEGE);this.add(Talent.ANALYSTE);}};
        this.put("Magnezone", new Pokemon("Magnezone", 462, Type.ELECTRIQUE, Type.ACIER, talents, 70, 70, 115, 130, 90, 60));

        talents = new ArrayList<Talent>(){{this.add(Talent.MEDIC_NATURE);this.add(Talent.POINT_POISON);this.add(Talent.FEUIL_GARDE);}};
        this.put("Roselia", new Pokemon("Roselia", 315, Type.PLANTE, Type.POISON, talents, 50, 60, 45, 100, 80, 65));

        talents = new ArrayList<Talent>(){{this.add(Talent.ABSENTEISME);}};
        this.put("Monaflemit", new Pokemon("Monaflemit", 289, Type.NORMAL, Type.NONE, talents, 150, 160, 100, 95, 65, 100));

        talents = new ArrayList<Talent>(){{this.add(Talent.TEMPO_PERSO);this.add(Talent.PIED_CONFUS);this.add(Talent.CONTESTATION);}};
        this.put("Spinda", new Pokemon("Spinda", 327, Type.NORMAL, Type.NONE, talents, 60, 60, 60, 60, 60, 60));

        talents = new ArrayList<Talent>(){{this.add(Talent.ABSORB_EAU);this.add(Talent.MOITEUR);this.add(Talent.GLISSADE);}};
        this.put("Tartard", new Pokemon("Tartard", 62, Type.EAU, Type.COMBAT, talents, 90, 85, 95, 70, 90, 70));

        talents = new ArrayList<Talent>(){{this.add(Talent.PRESSION);this.add(Talent.TELEPATHE);}};
        this.put("Palkia", new Pokemon("Palkia", 484, Type.EAU, Type.DRAGON, talents, 90, 120, 100, 150, 120, 100));

        talents = new ArrayList<Talent>(){{this.add(Talent.AGITATION);this.add(Talent.ATTENTION);}};
        this.put("Darumarond", new Pokemon("Darumarond", 554, Type.FEU, Type.NONE, talents, 70, 90, 45, 15, 45, 50));

        talents = new ArrayList<Talent>(){{this.add(Talent.PREDICTION);this.add(Talent.SYNCHRO);this.add(Talent.TELEPATHE);}};
        this.put("Munna", new Pokemon("Munna", 517, Type.PSY, Type.NONE, talents, 76, 25, 45, 67, 55, 24));

        talents = new ArrayList<Talent>(){{this.add(Talent.INTIMIDATION);this.add(Talent.COLERIQUE);this.add(Talent.SANS_LIMITE);}};
        this.put("Tauros", new Pokemon("Tauros", 128, Type.NORMAL, Type.NONE, talents, 75, 100, 95, 40, 70, 110));

        talents = new ArrayList<Talent>(){{this.add(Talent.INTIMIDATION);this.add(Talent.TEMERAIRE);}};
        this.put("Etouraptor", new Pokemon("Etouraptor", 398, Type.NORMAL, Type.VOL, talents, 85, 120, 70, 50, 50, 100));

        talents = new ArrayList<Talent>(){{this.add(Talent.TEMERAIRE);this.add(Talent.HERBIVORE);this.add(Talent.ANTI_BRUIT);}};
        this.put("Frison", new Pokemon("Frison", 626, Type.NORMAL, Type.NONE, talents, 95, 110, 95, 40, 95, 55));

        talents = new ArrayList<Talent>(){{this.add(Talent.PRESSION);this.add(Talent.ABSORB_VOLT);}};
        this.put("Raikou", new Pokemon("Raikou", 243, Type.ELECTRIQUE, Type.NONE, talents, 90, 85, 75, 115, 100, 115));

        talents = new ArrayList<Talent>(){{this.add(Talent.TORRENT);this.add(Talent.ACHARNE);}};
        this.put("Pingoleon", new Pokemon("Pingoleon", 395, Type.EAU, Type.ACIER, talents, 84, 86, 88, 111, 101, 60));

        talents = new ArrayList<Talent>(){{this.add(Talent.BRASIER);this.add(Talent.TORCHE);}};
        this.put("Hericendre", new Pokemon("Hericendre", 155, Type.FEU, Type.NONE, talents, 39, 52, 43, 60, 50, 65));

        talents = new ArrayList<Talent>(){{this.add(Talent.INTIMIDATION);this.add(Talent.MUE);this.add(Talent.TENSION);}};
        this.put("Arbok", new Pokemon("Arbok", 24, Type.POISON, Type.NONE, talents, 60, 85, 69, 65, 79, 80));

        talents = new ArrayList<Talent>(){{this.add(Talent.FOUILLE);this.add(Talent.BATTANT);this.add(Talent.MARQUE_OMBRE);}};
        this.put("Mesmerella", new Pokemon("Mesmerella", 575, Type.PSY, Type.NONE, talents, 60, 45, 70, 75, 85, 55));

        talents = new ArrayList<Talent>(){{this.add(Talent.BRASIER);this.add(Talent.POING_DE_FER);}};
        this.put("Chimpenfeu", new Pokemon("Chimpenfeu", 391, Type.FEU, Type.COMBAT, talents, 64, 78, 52, 78, 52, 81));

        talents = new ArrayList<Talent>(){{this.add(Talent.MOITEUR);this.add(Talent.CIEL_GRIS);this.add(Talent.GLISSADE);}};
        this.put("Psykokwak", new Pokemon("Psykokwak", 54, Type.EAU, Type.NONE, talents, 50, 52, 48, 65, 50, 55));

        talents = new ArrayList<Talent>(){{this.add(Talent.CHLOROPHYLE);this.add(Talent.GLOUTONNERIE);}};
        this.put("Boustiflor", new Pokemon("Boustiflor", 70, Type.PLANTE, Type.POISON, talents, 65, 90, 50, 85, 45, 55));

        talents = new ArrayList<Talent>(){{this.add(Talent.CALQUE);this.add(Talent.TELECHARGE);this.add(Talent.ANALYSTE);}};
        this.put("Porygon2", new Pokemon("Porygon2", 233, Type.NORMAL, Type.NONE, talents, 85, 80, 90, 105, 95, 60));

        talents = new ArrayList<Talent>(){{this.add(Talent.ISOGRAISSE);this.add(Talent.CORPS_GEL);this.add(Talent.BENET);}};
        this.put("Kaimorse", new Pokemon("Kaimorse", 365, Type.GLACE, Type.EAU, talents, 110, 80, 90, 95, 90, 65));

        talents = new ArrayList<Talent>(){{this.add(Talent.MOITEUR);this.add(Talent.CIEL_GRIS);this.add(Talent.GLISSADE);}};
        this.put("Akwakwak", new Pokemon("Akwakwak", 55, Type.EAU, Type.NONE, talents, 80, 82, 78, 95, 80, 85));

        talents = new ArrayList<Talent>(){{this.add(Talent.REGARD_VIF);this.add(Talent.POING_DE_FER);this.add(Talent.ATTENTION);}};
        this.put("Tygnon", new Pokemon("Tygnon", 107, Type.COMBAT, Type.NONE, talents, 50, 105, 79, 35, 110, 76));

        talents = new ArrayList<Talent>(){{this.add(Talent.RAMASSAGE);this.add(Talent.ISOGRAISSE);this.add(Talent.GLOUTONNERIE);}};
        this.put("Goinfrex", new Pokemon("Goinfrex", 446, Type.NORMAL, Type.NONE, talents, 135, 85, 40, 40, 85, 5));

        talents = new ArrayList<Talent>(){{this.add(Talent.VOILE_SABLE);}};
        this.put("Griknot", new Pokemon("Griknot", 443, Type.DRAGON, Type.SOL, talents, 58, 70, 45, 40, 45, 42));

        talents = new ArrayList<Talent>(){{this.add(Talent.GLUCO_VOILE);this.add(Talent.DELESTAGE);}};
        this.put("Sucroquin", new Pokemon("Sucroquin", 684, Type.FEE, Type.NONE, talents, 62, 48, 66, 59, 57, 49));

        talents = new ArrayList<Talent>(){{this.add(Talent.HYDRATATION);this.add(Talent.COQUE_ARMURE);this.add(Talent.ENVELOCAPE);}};
        this.put("Escargaume", new Pokemon("Escargaume", 616, Type.INSECTE, Type.NONE, talents, 50, 40, 85, 40, 65, 25));

        talents = new ArrayList<Talent>(){{this.add(Talent.ANNULE_GARDE);}};
        this.put("Monorpale", new Pokemon("Monorpale", 679, Type.ACIER, Type.SPECTRE, talents, 40, 90, 130, 35, 30, 10));

        talents = new ArrayList<Talent>(){{this.add(Talent.BRASIER);this.add(Talent.MAGICIEN);}};
        this.put("Goupelin", new Pokemon("Goupelin", 655, Type.FEU, Type.PSY, talents, 75, 69, 72, 114, 100, 104));

        talents = new ArrayList<Talent>(){{this.add(Talent.REGARD_VIF);this.add(Talent.FREIN);this.add(Talent.FARCEUR);}};
        this.put("Tenefix", new Pokemon("Tenefix", 302, Type.TENEBRE, Type.SPECTRE, talents, 50, 75, 75, 65, 65, 50));

        talents = new ArrayList<Talent>(){{this.add(Talent.GLISSADE);}};
        this.put("Mustebouee", new Pokemon("Mustebouee", 418, Type.EAU, Type.NONE, talents, 55, 65, 35, 60, 30, 85));

        talents = new ArrayList<Talent>(){{this.add(Talent.ATTENTION);this.add(Talent.INFILTRATION);}};
        this.put("Nosferalto", new Pokemon("Nosferalto", 42, Type.POISON, Type.VOL, talents, 75, 80, 70, 65, 75, 90));

        talents = new ArrayList<Talent>(){{this.add(Talent.CRAN);this.add(Talent.ATTENTION);this.add(Talent.BRISE_MOULE);}};
        this.put("Judokrak", new Pokemon("Judokrak", 538, Type.COMBAT, Type.NONE, talents, 120, 100, 85, 30, 85, 45));

        talents = new ArrayList<Talent>(){{this.add(Talent.GLISSADE);this.add(Talent.TETE_DE_ROC);this.add(Talent.FERMETE);}};
        this.put("Relicanth", new Pokemon("Relicanth", 369, Type.EAU, Type.ROCHE, talents, 100, 90, 130, 45, 65, 55));

        talents = new ArrayList<Talent>(){{this.add(Talent.PREDICTION);this.add(Talent.SYNCHRO);this.add(Talent.TELEPATHE);}};
        this.put("Mushana", new Pokemon("Mushana", 518, Type.PSY, Type.NONE, talents, 116, 55, 85, 107, 95, 29));

        talents = new ArrayList<Talent>(){{this.add(Talent.MEDIC_NATURE);this.add(Talent.SERENITE);this.add(Talent.GARDE_AMIE);}};
        this.put("Ptiravi", new Pokemon("Ptiravi", 440, Type.NORMAL, Type.NONE, talents, 100, 5, 5, 15, 65, 30));

        talents = new ArrayList<Talent>(){{this.add(Talent.COQUE_ARMURE);this.add(Talent.PHOBIQUE);}};
        this.put("Coquiperl", new Pokemon("Coquiperl", 366, Type.EAU, Type.NONE, talents, 35, 64, 85, 74, 55, 32));

        talents = new ArrayList<Talent>(){{this.add(Talent.LEVITATION);}};
        this.put("Ohmassacre", new Pokemon("Ohmassacre", 604, Type.ELECTRIQUE, Type.NONE, talents, 85, 115, 80, 105, 80, 50));

        talents = new ArrayList<Talent>(){{this.add(Talent.MEDIC_NATURE);this.add(Talent.FOUILLE);this.add(Talent.RECOLTE);}};
        this.put("Brocelome", new Pokemon("Brocelome", 708, Type.SPECTRE, Type.PLANTE, talents, 43, 70, 48, 50, 60, 38));

        talents = new ArrayList<Talent>(){{this.add(Talent.MEDIC_NATURE);this.add(Talent.POINT_POISON);this.add(Talent.FEUIL_GARDE);}};
        this.put("Rozbouton", new Pokemon("Rozbouton", 406, Type.PLANTE, Type.NONE, talents, 40, 30, 35, 50, 70, 55));

        talents = new ArrayList<Talent>(){{this.add(Talent.ATTENTION);this.add(Talent.ACHARNE);this.add(Talent.PRESSION);}};
        this.put("Scalproie", new Pokemon("Scalproie", 625, Type.ACIER, Type.TENEBRE, talents, 65, 125, 100, 60, 70, 70));

        talents = new ArrayList<Talent>(){{this.add(Talent.ISOGRAISSE);this.add(Talent.CORPS_GEL);this.add(Talent.BENET);}};
        this.put("Phogleur", new Pokemon("Phogleur", 364, Type.GLACE, Type.EAU, talents, 90, 60, 70, 75, 70, 45));

        talents = new ArrayList<Talent>(){{this.add(Talent.TELEPATHE);this.add(Talent.SYNCHRO);this.add(Talent.ANALYSTE);}};
        this.put("Neitram", new Pokemon("Neitram", 606, Type.PSY, Type.NONE, talents, 75, 75, 75, 125, 95, 40));

        talents = new ArrayList<Talent>(){{this.add(Talent.INCONSCIENT);this.add(Talent.MALADRESSE);this.add(Talent.SIMPLE);}};
        this.put("Chovsourir", new Pokemon("Chovsourir", 527, Type.PSY, Type.VOL, talents, 55, 45, 43, 55, 43, 72));

        talents = new ArrayList<Talent>(){{this.add(Talent.GLISSADE);}};
        this.put("Musteflott", new Pokemon("Musteflott", 419, Type.EAU, Type.NONE, talents, 85, 105, 55, 85, 50, 115));

        talents = new ArrayList<Talent>(){{this.add(Talent.SERENITE);this.add(Talent.FUITE);this.add(Talent.PHOBIQUE);}};
        this.put("Insolourdo", new Pokemon("Insolourdo", 206, Type.NORMAL, Type.NONE, talents, 100, 70, 70, 65, 65, 45));

        talents = new ArrayList<Talent>(){{this.add(Talent.SABLE_VOLANT);}};
        this.put("Mega-Tyranocif", new Pokemon("Mega-Tyranocif", 248, Type.ROCHE, Type.TENEBRE, talents, 100, 164, 150, 95, 120, 71));

        talents = new ArrayList<Talent>(){{this.add(Talent.GARDE_MYSTIK);}};
        this.put("Munja", new Pokemon("Munja", 292, Type.INSECTE, Type.SPECTRE, talents, 1, 90, 45, 30, 30, 40));

        talents = new ArrayList<Talent>(){{this.add(Talent.PEAU_DURE);this.add(Talent.SANS_LIMITE);this.add(Talent.BRISE_MOULE);}};
        this.put("Drakkarmin", new Pokemon("Drakkarmin", 621, Type.DRAGON, Type.NONE, talents, 77, 120, 90, 60, 90, 48));

        talents = new ArrayList<Talent>(){{this.add(Talent.CORPS_GEL);this.add(Talent.ARMUROUILLEE);}};
        this.put("Sorbouboul", new Pokemon("Sorbouboul", 584, Type.GLACE, Type.NONE, talents, 71, 95, 85, 110, 95, 79));

        talents = new ArrayList<Talent>(){{this.add(Talent.ALERTE_NEIGE);}};
        this.put("Mega-Blizzaroi", new Pokemon("Mega-Blizzaroi", 460, Type.GLACE, Type.PLANTE, talents, 90, 132, 105, 132, 105, 30));

        talents = new ArrayList<Talent>(){{this.add(Talent.TERA_VOLTAGE);}};
        this.put("Zekrom", new Pokemon("Zekrom", 644, Type.DRAGON, Type.ELECTRIQUE, talents, 100, 150, 120, 120, 100, 90));

        talents = new ArrayList<Talent>(){{this.add(Talent.AGITATION);this.add(Talent.SNIPER);this.add(Talent.LUNATIQUE);}};
        this.put("Remoraid", new Pokemon("Remoraid", 223, Type.EAU, Type.NONE, talents, 35, 65, 35, 65, 35, 65));

        talents = new ArrayList<Talent>(){{this.add(Talent.HYDRATATION);this.add(Talent.COEUR_SOIN);this.add(Talent.REGE_FORCE);}};
        this.put("Mamanbo", new Pokemon("Mamanbo", 594, Type.EAU, Type.NONE, talents, 165, 75, 80, 40, 45, 65));

        talents = new ArrayList<Talent>(){{this.add(Talent.ENVELOCAPE);this.add(Talent.GARDE_MAGIK);this.add(Talent.REGE_FORCE);}};
        this.put("Meios", new Pokemon("Meios", 578, Type.PSY, Type.NONE, talents, 65, 40, 50, 125, 60, 30));

        talents = new ArrayList<Talent>(){{this.add(Talent.SYNCHRO);this.add(Talent.ATTENTION);}};
        this.put("Noctali", new Pokemon("Noctali", 197, Type.TENEBRE, Type.NONE, talents, 95, 65, 110, 60, 130, 65));

        talents = new ArrayList<Talent>(){{this.add(Talent.BRISE_MOULE);}};
        this.put("Mega-Pharamp", new Pokemon("Mega-Pharamp", 181, Type.ELECTRIQUE, Type.DRAGON, talents, 90, 95, 105, 165, 110, 45));

        talents = new ArrayList<Talent>(){{this.add(Talent.BENET);this.add(Talent.TEMPO_PERSO);this.add(Talent.REGE_FORCE);}};
        this.put("Ramoloss", new Pokemon("Ramoloss", 79, Type.EAU, Type.PSY, talents, 90, 65, 65, 40, 40, 15));

        talents = new ArrayList<Talent>(){{this.add(Talent.GLUCO_VOILE);this.add(Talent.DELESTAGE);}};
        this.put("Cupcanaille", new Pokemon("Cupcanaille", 685, Type.FEE, Type.NONE, talents, 82, 80, 86, 85, 75, 72));

        talents = new ArrayList<Talent>(){{this.add(Talent.TORRENT);this.add(Talent.CUVETTE);}};
        this.put("Carabaffe", new Pokemon("Carabaffe", 8, Type.EAU, Type.NONE, talents, 59, 63, 80, 65, 80, 58));

        talents = new ArrayList<Talent>(){{this.add(Talent.BENET);this.add(Talent.ANTICIPATION);this.add(Talent.HYDRATATION);}};
        this.put("Barbicha", new Pokemon("Barbicha", 340, Type.EAU, Type.SOL, talents, 110, 78, 73, 76, 71, 60));

        talents = new ArrayList<Talent>(){{this.add(Talent.COEUR_DE_COQ);this.add(Talent.CHANCEUX);this.add(Talent.RIVALITE);}};
        this.put("Colombeau", new Pokemon("Colombeau", 520, Type.NORMAL, Type.VOL, talents, 62, 77, 62, 50, 42, 65));

        talents = new ArrayList<Talent>(){{this.add(Talent.MUE);this.add(Talent.IMPUDENCE);this.add(Talent.INTIMIDATION);}};
        this.put("Baggaid", new Pokemon("Baggaid", 560, Type.TENEBRE, Type.COMBAT, talents, 65, 90, 115, 45, 115, 58));

        talents = new ArrayList<Talent>(){{this.add(Talent.ANTI_BRUIT);this.add(Talent.QUERELLEUR);}};
        this.put("Ramboum", new Pokemon("Ramboum", 294, Type.NORMAL, Type.NONE, talents, 84, 71, 43, 71, 43, 48));

        talents = new ArrayList<Talent>(){{this.add(Talent.ECHAUFFEMENT);this.add(Talent.TEMERAIRE);this.add(Talent.DELESTAGE);}};
        this.put("Kicklee", new Pokemon("Kicklee", 106, Type.COMBAT, Type.NONE, talents, 50, 120, 53, 35, 110, 87));

        talents = new ArrayList<Talent>(){{this.add(Talent.RAMASSAGE);this.add(Talent.PIED_VELOCE);this.add(Talent.CHERCHE_MIEL);}};
        this.put("Teddiursa", new Pokemon("Teddiursa", 216, Type.NORMAL, Type.NONE, talents, 60, 80, 50, 50, 50, 40));

        talents = new ArrayList<Talent>(){{this.add(Talent.FERMETE);this.add(Talent.ATTENTION);this.add(Talent.BRISE_MOULE);}};
        this.put("Karaclee", new Pokemon("Karaclee", 539, Type.COMBAT, Type.NONE, talents, 75, 125, 75, 30, 75, 85));

        talents = new ArrayList<Talent>(){{this.add(Talent.GLISSADE);this.add(Talent.IGNIFU_VOILE);}};
        this.put("Serpang", new Pokemon("Serpang", 367, Type.EAU, Type.NONE, talents, 55, 104, 105, 94, 75, 52));

        talents = new ArrayList<Talent>(){{this.add(Talent.CALQUE);this.add(Talent.TELECHARGE);this.add(Talent.ANALYSTE);}};
        this.put("Porygon", new Pokemon("Porygon", 137, Type.NORMAL, Type.NONE, talents, 65, 60, 70, 85, 75, 40));

        talents = new ArrayList<Talent>(){{this.add(Talent.INTIMIDATION);this.add(Talent.BAIGNE_SABLE);this.add(Talent.QUERELLEUR);}};
        this.put("Mastouffe", new Pokemon("Mastouffe", 508, Type.NORMAL, Type.NONE, talents, 85, 100, 90, 45, 90, 80));

        talents = new ArrayList<Talent>(){{this.add(Talent.CORPS_ARDENT);this.add(Talent.ESSAIM);}};
        this.put("Pyrax", new Pokemon("Pyrax", 637, Type.INSECTE, Type.FEU, talents, 85, 60, 65, 135, 105, 100));

        talents = new ArrayList<Talent>(){{this.add(Talent.ENGRAIS);this.add(Talent.CONTESTATION);}};
        this.put("Majaspic", new Pokemon("Majaspic", 497, Type.PLANTE, Type.NONE, talents, 75, 75, 95, 75, 95, 113));

        talents = new ArrayList<Talent>(){{this.add(Talent.MUE);}};
        this.put("Blindalys", new Pokemon("Blindalys", 268, Type.INSECTE, Type.NONE, talents, 50, 35, 55, 25, 25, 15));

        talents = new ArrayList<Talent>(){{this.add(Talent.GLISSADE);this.add(Talent.CUVETTE);}};
        this.put("Nenupiot", new Pokemon("Nenupiot", 270, Type.EAU, Type.PLANTE, talents, 40, 30, 30, 40, 50, 30));

        talents = new ArrayList<Talent>(){{this.add(Talent.FERMETE);this.add(Talent.ENVELOCAPE);}};
        this.put("Foretress", new Pokemon("Foretress", 205, Type.INSECTE, Type.ACIER, talents, 75, 90, 140, 60, 60, 40));

        talents = new ArrayList<Talent>(){{this.add(Talent.OEIL_COMPOSE);this.add(Talent.LENTITEINTEE);this.add(Talent.FUITE);}};
        this.put("Mimitoss", new Pokemon("Mimitoss", 48, Type.INSECTE, Type.POISON, talents, 60, 55, 50, 40, 55, 45));

        talents = new ArrayList<Talent>(){{this.add(Talent.BENET);this.add(Talent.PREDICTION);this.add(Talent.PEAU_SECHE);}};
        this.put("Lippoutou", new Pokemon("Lippoutou", 124, Type.GLACE, Type.PSY, talents, 65, 50, 35, 115, 95, 95));

        talents = new ArrayList<Talent>(){{this.add(Talent.MINUS);}};
        this.put("Negapi", new Pokemon("Negapi", 312, Type.ELECTRIQUE, Type.NONE, talents, 60, 40, 50, 75, 85, 95));

        talents = new ArrayList<Talent>(){{this.add(Talent.BRISE_MOULE);}};
        this.put("Mega-Leviator", new Pokemon("Mega-Leviator", 130, Type.EAU, Type.TENEBRE, talents, 95, 155, 109, 70, 130, 81));

        talents = new ArrayList<Talent>(){{this.add(Talent.SECHERESSE);}};
        this.put("Mega-Dracaufeu Y", new Pokemon("Mega-Dracaufeu Y", 6, Type.FEU, Type.VOL, talents, 78, 104, 78, 159, 115, 100));

        talents = new ArrayList<Talent>(){{this.add(Talent.HYDRATATION);this.add(Talent.HERBIVORE);this.add(Talent.POISSEUX);}};
        this.put("Colimucus", new Pokemon("Colimucus", 705, Type.DRAGON, Type.NONE, talents, 50, 70, 50, 90, 120, 65));

        talents = new ArrayList<Talent>(){{this.add(Talent.BRASIER);this.add(Talent.POING_DE_FER);}};
        this.put("Ouisticram", new Pokemon("Ouisticram", 390, Type.FEU, Type.NONE, talents, 44, 58, 44, 58, 44, 61));

        talents = new ArrayList<Talent>(){{this.add(Talent.BRASIER);this.add(Talent.ISOGRAISSE);}};
        this.put("Gruikui", new Pokemon("Gruikui", 498, Type.FEU, Type.NONE, talents, 65, 63, 45, 45, 45, 45));

        talents = new ArrayList<Talent>(){{this.add(Talent.IMPASSIBLE);}};
        this.put("Gallame", new Pokemon("Gallame", 475, Type.PSY, Type.COMBAT, talents, 68, 125, 65, 65, 115, 80));

        talents = new ArrayList<Talent>(){{this.add(Talent.GLOUTONNERIE);this.add(Talent.TORRENT);}};
        this.put("Flotajou", new Pokemon("Flotajou", 515, Type.EAU, Type.NONE, talents, 50, 53, 48, 53, 48, 64));

        talents = new ArrayList<Talent>(){{this.add(Talent.BRISE_MOULE);this.add(Talent.POING_DE_FER);this.add(Talent.QUERELLEUR);}};
        this.put("Pandespiegle", new Pokemon("Pandespiegle", 674, Type.COMBAT, Type.NONE, talents, 67, 82, 62, 46, 48, 43));

        talents = new ArrayList<Talent>(){{this.add(Talent.HYDRATATION);this.add(Talent.HERBIVORE);this.add(Talent.POISSEUX);}};
        this.put("Muplodocus", new Pokemon("Muplodocus", 706, Type.DRAGON, Type.NONE, talents, 90, 100, 70, 110, 150, 80));

        talents = new ArrayList<Talent>(){{this.add(Talent.ENGRAIS);this.add(Talent.PARE_BALLES);}};
        this.put("Blindepique", new Pokemon("Blindepique", 652, Type.PLANTE, Type.COMBAT, talents, 88, 107, 122, 74, 75, 64));

        talents = new ArrayList<Talent>(){{this.add(Talent.TORCHE);this.add(Talent.CORPS_ARDENT);this.add(Talent.INFILTRATION);}};
        this.put("Melancolux", new Pokemon("Melancolux", 608, Type.SPECTRE, Type.FEU, talents, 60, 40, 60, 95, 60, 55));

        talents = new ArrayList<Talent>(){{this.add(Talent.COEUR_NOBLE);}};
        this.put("Viridium", new Pokemon("Viridium", 640, Type.PLANTE, Type.COMBAT, talents, 91, 90, 72, 90, 129, 108));

        talents = new ArrayList<Talent>(){{this.add(Talent.FUITE);this.add(Talent.REGARD_VIF);this.add(Talent.FOUILLE);}};
        this.put("Fouinette", new Pokemon("Fouinette", 161, Type.NORMAL, Type.NONE, talents, 35, 46, 34, 35, 45, 20));

        talents = new ArrayList<Talent>(){{this.add(Talent.MEDIC_NATURE);this.add(Talent.FOUILLE);this.add(Talent.RECOLTE);}};
        this.put("Desseliande", new Pokemon("Desseliande", 709, Type.SPECTRE, Type.PLANTE, talents, 85, 110, 76, 65, 82, 56));

        talents = new ArrayList<Talent>(){{this.add(Talent.MUE);this.add(Talent.INFILTRATION);}};
        this.put("Seviper", new Pokemon("Seviper", 336, Type.POISON, Type.NONE, talents, 73, 100, 60, 100, 60, 65));

        talents = new ArrayList<Talent>(){{this.add(Talent.ENGRAIS);this.add(Talent.FEUIL_GARDE);}};
        this.put("Germignon", new Pokemon("Germignon", 152, Type.PLANTE, Type.NONE, talents, 45, 49, 65, 49, 65, 45));

        talents = new ArrayList<Talent>(){{this.add(Talent.ESPRIT_VITAL);this.add(Talent.RAMASSAGE);this.add(Talent.FUITE);}};
        this.put("Ponchiot", new Pokemon("Ponchiot", 506, Type.NORMAL, Type.NONE, talents, 45, 60, 45, 25, 45, 55));

        talents = new ArrayList<Talent>(){{this.add(Talent.BRASIER);this.add(Talent.TORCHE);}};
        this.put("Typhlosion", new Pokemon("Typhlosion", 157, Type.FEU, Type.NONE, talents, 78, 84, 78, 109, 85, 100));

        talents = new ArrayList<Talent>(){{this.add(Talent.FORCE_SABLE);this.add(Talent.SANS_LIMITE);}};
        this.put("Demeteros (Forme Avatar)", new Pokemon("Demeteros (Forme Avatar)", 645, Type.SOL, Type.VOL, talents, 89, 125, 90, 115, 80, 101));

        talents = new ArrayList<Talent>(){{this.add(Talent.TORCHE);this.add(Talent.SECHERESSE);}};
        this.put("Feunard", new Pokemon("Feunard", 38, Type.FEU, Type.NONE, talents, 73, 76, 75, 81, 100, 100));

        talents = new ArrayList<Talent>(){{this.add(Talent.MAGNEPIEGE);this.add(Talent.FERMETE);this.add(Talent.ANALYSTE);}};
        this.put("Magneti", new Pokemon("Magneti", 81, Type.ELECTRIQUE, Type.ACIER, talents, 25, 35, 70, 95, 55, 45));

        talents = new ArrayList<Talent>(){{this.add(Talent.COEUR_NOBLE);}};
        this.put("Cobaltium", new Pokemon("Cobaltium", 638, Type.ACIER, Type.COMBAT, talents, 91, 90, 129, 90, 72, 108));

        talents = new ArrayList<Talent>(){{this.add(Talent.ECHAUFFEMENT);this.add(Talent.TECHNICIEN);this.add(Talent.TENSION);}};
        this.put("Persian", new Pokemon("Persian", 53, Type.NORMAL, Type.NONE, talents, 65, 70, 60, 65, 65, 115));

        talents = new ArrayList<Talent>(){{this.add(Talent.POINT_POISON);this.add(Talent.RIVALITE);this.add(Talent.SANS_LIMITE);}};
        this.put("Nidoking", new Pokemon("Nidoking", 34, Type.POISON, Type.SOL, talents, 81, 92, 77, 85, 75, 85));

        talents = new ArrayList<Talent>(){{this.add(Talent.TURBO);this.add(Talent.INFILTRATION);}};
        this.put("Ninjask", new Pokemon("Ninjask", 291, Type.INSECTE, Type.VOL, talents, 61, 90, 45, 50, 50, 160));

        talents = new ArrayList<Talent>(){{this.add(Talent.TORRENT);this.add(Talent.PROTEEN);}};
        this.put("Amphinobi", new Pokemon("Amphinobi", 658, Type.EAU, Type.TENEBRE, talents, 72, 95, 67, 103, 71, 122));

        talents = new ArrayList<Talent>(){{this.add(Talent.RIVALITE);this.add(Talent.TENSION);this.add(Talent.IMPUDENCE);}};
        this.put("Nemelios", new Pokemon("Nemelios", 668, Type.FEU, Type.NORMAL, talents, 86, 68, 72, 109, 66, 106));

        talents = new ArrayList<Talent>(){{this.add(Talent.FUITE);this.add(Talent.PIED_VELOCE);this.add(Talent.PHOBIQUE);}};
        this.put("Medhyena", new Pokemon("Medhyena", 261, Type.TENEBRE, Type.NONE, talents, 35, 55, 35, 30, 30, 35));

        talents = new ArrayList<Talent>(){{this.add(Talent.FUITE);this.add(Talent.ADAPTABILITE);this.add(Talent.ANTICIPATION);}};
        this.put("Evoli", new Pokemon("Evoli", 133, Type.NORMAL, Type.NONE, talents, 55, 55, 50, 45, 65, 55));

        talents = new ArrayList<Talent>(){{this.add(Talent.BENET);this.add(Talent.ANTICIPATION);this.add(Talent.HYDRATATION);}};
        this.put("Barloche", new Pokemon("Barloche", 339, Type.EAU, Type.SOL, talents, 50, 48, 43, 46, 41, 60));

        talents = new ArrayList<Talent>(){{this.add(Talent.GLISSADE);this.add(Talent.ARMURBASTON);this.add(Talent.ARMUROUILLEE);}};
        this.put("Kabuto", new Pokemon("Kabuto", 140, Type.ROCHE, Type.EAU, talents, 30, 80, 90, 55, 45, 55));

        talents = new ArrayList<Talent>(){{this.add(Talent.TORRENT);this.add(Talent.PROTEEN);}};
        this.put("Grenousse", new Pokemon("Grenousse", 656, Type.EAU, Type.NONE, talents, 37, 53, 49, 66, 50, 70));

        talents = new ArrayList<Talent>(){{this.add(Talent.LEVITATION);}};
        this.put("Kaorine", new Pokemon("Kaorine", 344, Type.SOL, Type.PSY, talents, 60, 70, 105, 70, 120, 75));

        talents = new ArrayList<Talent>(){{this.add(Talent.CRAN);this.add(Talent.IMPASSIBLE);this.add(Talent.ESPRIT_VITAL);}};
        this.put("Debugant", new Pokemon("Debugant", 236, Type.COMBAT, Type.NONE, talents, 35, 35, 35, 35, 35, 35));

        talents = new ArrayList<Talent>(){{this.add(Talent.OEIL_COMPOSE);}};
        this.put("Ningale", new Pokemon("Ningale", 290, Type.INSECTE, Type.SOL, talents, 31, 45, 90, 30, 30, 40));

        talents = new ArrayList<Talent>(){{this.add(Talent.RAMASSAGE);this.add(Talent.TECHNICIEN);this.add(Talent.MULTI_COUPS);}};
        this.put("Capidextre", new Pokemon("Capidextre", 424, Type.NORMAL, Type.NONE, talents, 75, 100, 66, 60, 66, 115));

        talents = new ArrayList<Talent>(){{this.add(Talent.PLUS);this.add(Talent.MINUS);this.add(Talent.CORPS_SAIN);}};
        this.put("Tic", new Pokemon("Tic", 599, Type.ACIER, Type.NONE, talents, 40, 55, 70, 45, 60, 30));

        talents = new ArrayList<Talent>(){{this.add(Talent.REGARD_VIF);this.add(Talent.SNIPER);}};
        this.put("Piafabec", new Pokemon("Piafabec", 21, Type.NORMAL, Type.VOL, talents, 40, 60, 30, 31, 31, 70));

        talents = new ArrayList<Talent>(){{this.add(Talent.ARMUMAGMA);this.add(Talent.SOLIDE_ROC);this.add(Talent.COLERIQUE);}};
        this.put("Camerupt", new Pokemon("Camerupt", 323, Type.FEU, Type.SOL, talents, 70, 100, 70, 105, 75, 40));

        talents = new ArrayList<Talent>(){{this.add(Talent.REGARD_VIF);this.add(Talent.CUVETTE);}};
        this.put("Goelise", new Pokemon("Goelise", 278, Type.EAU, Type.VOL, talents, 40, 30, 30, 55, 30, 85));

        talents = new ArrayList<Talent>(){{this.add(Talent.TORCHE);this.add(Talent.CORPS_ARDENT);this.add(Talent.MARQUE_OMBRE);}};
        this.put("Funecire", new Pokemon("Funecire", 607, Type.SPECTRE, Type.FEU, talents, 50, 30, 55, 65, 55, 20));

        talents = new ArrayList<Talent>(){{this.add(Talent.SNIPER);this.add(Talent.GRIFFE_DURE);this.add(Talent.PICKPOCKET);}};
        this.put("Golgopathe", new Pokemon("Golgopathe", 689, Type.ROCHE, Type.EAU, talents, 70, 115, 115, 50, 100, 80));

        talents = new ArrayList<Talent>(){{this.add(Talent.TURBOBRASIER);}};
        this.put("Reshiram", new Pokemon("Reshiram", 643, Type.DRAGON, Type.FEU, talents, 100, 120, 100, 150, 120, 90));

        talents = new ArrayList<Talent>(){{this.add(Talent.BENET);this.add(Talent.TEMPO_PERSO);this.add(Talent.CIEL_GRIS);}};
        this.put("Excelangue", new Pokemon("Excelangue", 108, Type.NORMAL, Type.NONE, talents, 90, 55, 75, 60, 75, 30));

        talents = new ArrayList<Talent>(){{this.add(Talent.ABSORB_EAU);this.add(Talent.MOITEUR);this.add(Talent.GLISSADE);}};
        this.put("Tetarte", new Pokemon("Tetarte", 61, Type.EAU, Type.NONE, talents, 65, 65, 65, 50, 50, 90));

        talents = new ArrayList<Talent>(){{this.add(Talent.MARQUE_OMBRE);}};
        this.put("Mega-Ectoplasma", new Pokemon("Mega-Ectoplasma", 94, Type.SPECTRE, Type.POISON, talents, 60, 65, 80, 170, 95, 130));

        talents = new ArrayList<Talent>(){{this.add(Talent.MEGA_BLASTER);}};
        this.put("Flingouste", new Pokemon("Flingouste", 692, Type.EAU, Type.NONE, talents, 50, 53, 62, 58, 63, 44));

        talents = new ArrayList<Talent>(){{this.add(Talent.TORRENT);this.add(Talent.SANS_LIMITE);}};
        this.put("Aligatueur", new Pokemon("Aligatueur", 160, Type.EAU, Type.NONE, talents, 85, 105, 100, 79, 83, 78));

        talents = new ArrayList<Talent>(){{this.add(Talent.LEVITATION);}};
        this.put("Magireve", new Pokemon("Magireve", 429, Type.SPECTRE, Type.NONE, talents, 60, 60, 60, 105, 105, 105));

        talents = new ArrayList<Talent>(){{this.add(Talent.RIVALITE);this.add(Talent.INTIMIDATION);this.add(Talent.CRAN);}};
        this.put("Luxray", new Pokemon("Luxray", 405, Type.ELECTRIQUE, Type.NONE, talents, 80, 120, 79, 95, 79, 70));

        talents = new ArrayList<Talent>(){{this.add(Talent.GLISSADE);this.add(Talent.HYDRATATION);}};
        this.put("Rosabyss", new Pokemon("Rosabyss", 368, Type.EAU, Type.NONE, talents, 55, 84, 105, 114, 75, 52));

        talents = new ArrayList<Talent>(){{this.add(Talent.FERMETE);this.add(Talent.TETE_DE_ROC);this.add(Talent.HEAVY_METAL);}};
        this.put("Galekid", new Pokemon("Galekid", 304, Type.ACIER, Type.ROCHE, talents, 50, 70, 100, 40, 40, 30));

        talents = new ArrayList<Talent>(){{this.add(Talent.TETE_DE_ROC);this.add(Talent.PRESSION);this.add(Talent.TENSION);}};
        this.put("Ptera", new Pokemon("Ptera", 142, Type.ROCHE, Type.VOL, talents, 80, 105, 65, 60, 75, 130));

        talents = new ArrayList<Talent>(){{this.add(Talent.FUITE);this.add(Talent.TORCHE);this.add(Talent.CORPS_ARDENT);}};
        this.put("Galopa", new Pokemon("Galopa", 78, Type.FEU, Type.NONE, talents, 65, 100, 70, 80, 80, 105));

        talents = new ArrayList<Talent>(){{this.add(Talent.BENET);this.add(Talent.TEMPO_PERSO);this.add(Talent.REGE_FORCE);}};
        this.put("Roigada", new Pokemon("Roigada", 199, Type.EAU, Type.PSY, talents, 95, 75, 80, 100, 110, 30));

        talents = new ArrayList<Talent>(){{this.add(Talent.SERENITE);}};
        this.put("Jirachi", new Pokemon("Jirachi", 385, Type.ACIER, Type.PSY, talents, 100, 100, 100, 100, 100, 100));

        talents = new ArrayList<Talent>(){{this.add(Talent.RAMASSAGE);this.add(Talent.FOUILLE);this.add(Talent.INSOMNIA);}};
        this.put("Pitrouille (Taille Mini)", new Pokemon("Pitrouille (Taille Mini)", 710, Type.SPECTRE, Type.PLANTE, talents, 44, 66, 70, 44, 55, 56));

        talents = new ArrayList<Talent>(){{this.add(Talent.ENGRAIS);this.add(Talent.PARE_BALLES);}};
        this.put("Marisson", new Pokemon("Marisson", 650, Type.PLANTE, Type.NONE, talents, 56, 64, 66, 50, 45, 38));

        talents = new ArrayList<Talent>(){{this.add(Talent.INTIMIDATION);this.add(Talent.IMPUDENCE);this.add(Talent.COLERIQUE);}};
        this.put("Mascaiman", new Pokemon("Mascaiman", 551, Type.SOL, Type.TENEBRE, talents, 50, 72, 35, 35, 35, 65));

        talents = new ArrayList<Talent>(){{this.add(Talent.TORRENT);this.add(Talent.CUVETTE);}};
        this.put("Carapuce", new Pokemon("Carapuce", 7, Type.EAU, Type.NONE, talents, 44, 48, 65, 50, 64, 43));

        talents = new ArrayList<Talent>(){{this.add(Talent.VACCIN);this.add(Talent.RAGE_POISON);}};
        this.put("Mangriff", new Pokemon("Mangriff", 335, Type.NORMAL, Type.NONE, talents, 73, 115, 60, 60, 60, 90));

        talents = new ArrayList<Talent>(){{this.add(Talent.LEVITATION);}};
        this.put("Latias", new Pokemon("Latias", 380, Type.DRAGON, Type.PSY, talents, 80, 80, 90, 110, 130, 110));

        talents = new ArrayList<Talent>(){{this.add(Talent.INTIMIDATION);this.add(Talent.PIED_VELOCE);this.add(Talent.IMPUDENCE);}};
        this.put("Grahyena", new Pokemon("Grahyena", 262, Type.TENEBRE, Type.NONE, talents, 70, 90, 70, 60, 60, 70));

        talents = new ArrayList<Talent>(){{this.add(Talent.PRESSION);this.add(Talent.MULTIECAILLE);}};
        this.put("Lugia", new Pokemon("Lugia", 249, Type.PSY, Type.VOL, talents, 106, 90, 130, 90, 154, 110));

        talents = new ArrayList<Talent>(){{this.add(Talent.TETE_DE_ROC);this.add(Talent.FERMETE);this.add(Talent.ARMUROUILLEE);}};
        this.put("Onix", new Pokemon("Onix", 95, Type.ROCHE, Type.SOL, talents, 35, 45, 160, 30, 45, 70));

        talents = new ArrayList<Talent>(){{this.add(Talent.TORCHE);this.add(Talent.CRAN);}};
        this.put("Pyroli", new Pokemon("Pyroli", 136, Type.FEU, Type.NONE, talents, 65, 130, 60, 95, 110, 65));

        talents = new ArrayList<Talent>(){{this.add(Talent.MAGNEPIEGE);this.add(Talent.FERMETE);this.add(Talent.ANALYSTE);}};
        this.put("Magneton", new Pokemon("Magneton", 82, Type.ELECTRIQUE, Type.ACIER, talents, 50, 60, 95, 120, 70, 70));

        talents = new ArrayList<Talent>(){{this.add(Talent.RIVALITE);this.add(Talent.BRISE_MOULE);this.add(Talent.TENSION);}};
        this.put("Incisache", new Pokemon("Incisache", 611, Type.DRAGON, Type.DRAGON, talents, 66, 117, 70, 40, 50, 67));

        talents = new ArrayList<Talent>(){{this.add(Talent.COQUE_ARMURE);this.add(Talent.MULTI_COUPS);this.add(Talent.ENVELOCAPE);}};
        this.put("Kokiyas", new Pokemon("Kokiyas", 90, Type.EAU, Type.NONE, talents, 30, 65, 100, 45, 25, 40));

        talents = new ArrayList<Talent>(){{this.add(Talent.TETE_DE_ROC);this.add(Talent.FERMETE);this.add(Talent.VOILE_SABLE);}};
        this.put("Racaillou", new Pokemon("Racaillou", 74, Type.ROCHE, Type.SOL, talents, 40, 80, 100, 30, 30, 20));

        talents = new ArrayList<Talent>(){{this.add(Talent.HYPER_CUTTER);this.add(Talent.COQUE_ARMURE);this.add(Talent.ADAPTABILITE);}};
        this.put("Colhomard", new Pokemon("Colhomard", 342, Type.EAU, Type.TENEBRE, talents, 63, 120, 85, 90, 55, 55));

        talents = new ArrayList<Talent>(){{this.add(Talent.ECRAN_POUDRE);}};
        this.put("Papinox", new Pokemon("Papinox", 269, Type.INSECTE, Type.POISON, talents, 60, 50, 70, 50, 90, 65));

        talents = new ArrayList<Talent>(){{this.add(Talent.HYDRATATION);}};
        this.put("Manaphy", new Pokemon("Manaphy", 490, Type.EAU, Type.NONE, talents, 100, 100, 100, 100, 100, 100));

        talents = new ArrayList<Talent>(){{this.add(Talent.TORRENT);this.add(Talent.SANS_LIMITE);}};
        this.put("Crocrodil", new Pokemon("Crocrodil", 159, Type.EAU, Type.NONE, talents, 65, 80, 80, 59, 63, 58));

        talents = new ArrayList<Talent>(){{this.add(Talent.LEVITATION);}};
        this.put("Ectoplasma", new Pokemon("Ectoplasma", 94, Type.SPECTRE, Type.POISON, talents, 60, 65, 60, 130, 75, 110));

        talents = new ArrayList<Talent>(){{this.add(Talent.ENVELOCAPE);this.add(Talent.GARDE_MAGIK);this.add(Talent.REGE_FORCE);}};
        this.put("Nucleos", new Pokemon("Nucleos", 577, Type.PSY, Type.NONE, talents, 45, 30, 40, 105, 50, 20));

        talents = new ArrayList<Talent>(){{this.add(Talent.LEVITATION);}};
        this.put("Vortente", new Pokemon("Vortente", 455, Type.PLANTE, Type.NONE, talents, 74, 100, 72, 90, 72, 46));

        talents = new ArrayList<Talent>(){{this.add(Talent.HYPER_CUTTER);this.add(Talent.COQUE_ARMURE);this.add(Talent.ADAPTABILITE);}};
        this.put("Ecrapince", new Pokemon("Ecrapince", 341, Type.EAU, Type.NONE, talents, 43, 80, 65, 50, 35, 35));

        talents = new ArrayList<Talent>(){{this.add(Talent.ESSAIM);this.add(Talent.MATINAL);this.add(Talent.POING_DE_FER);}};
        this.put("Coxyclaque", new Pokemon("Coxyclaque", 166, Type.INSECTE, Type.VOL, talents, 55, 35, 50, 55, 110, 85));

        talents = new ArrayList<Talent>(){{this.add(Talent.TORCHE);this.add(Talent.CORPS_ARDENT);this.add(Talent.MARQUE_OMBRE);}};
        this.put("Lugulabre", new Pokemon("Lugulabre", 609, Type.SPECTRE, Type.FEU, talents, 60, 55, 90, 145, 90, 80));

        talents = new ArrayList<Talent>(){{this.add(Talent.ABSORB_EAU);this.add(Talent.CORPS_MAUDIT);this.add(Talent.MOITEUR);}};
        this.put("Moyade", new Pokemon("Moyade", 593, Type.EAU, Type.SPECTRE, talents, 100, 60, 70, 85, 105, 60));

        talents = new ArrayList<Talent>(){{this.add(Talent.JOLI_SOURIRE);this.add(Talent.NORMALISE);}};
        this.put("Delcatty", new Pokemon("Delcatty", 301, Type.NORMAL, Type.NONE, talents, 70, 65, 65, 55, 55, 70));

        talents = new ArrayList<Talent>(){{this.add(Talent.FLORA_VOILE);this.add(Talent.SYMBIOSIS);}};
        this.put("Floette", new Pokemon("Floette", 670, Type.FEE, Type.NONE, talents, 58, 54, 52, 90, 116, 63));

        talents = new ArrayList<Talent>(){{this.add(Talent.MOMIE);}};
        this.put("Tutankafer", new Pokemon("Tutankafer", 563, Type.SPECTRE, Type.NONE, talents, 58, 50, 145, 95, 105, 30));

        talents = new ArrayList<Talent>(){{this.add(Talent.FORCE_PURE);this.add(Talent.TELEPATHE);}};
        this.put("Meditikka", new Pokemon("Meditikka", 307, Type.COMBAT, Type.PSY, talents, 30, 40, 55, 40, 55, 60));

        talents = new ArrayList<Talent>(){{this.add(Talent.COEUR_SOIN);this.add(Talent.REGE_FORCE);this.add(Talent.MALADRESSE);}};
        this.put("Nanmeouie", new Pokemon("Nanmeouie", 531, Type.NORMAL, Type.NONE, talents, 103, 60, 86, 60, 86, 50));

        talents = new ArrayList<Talent>(){{this.add(Talent.BRASIER);this.add(Talent.MAGICIEN);}};
        this.put("Feunnec", new Pokemon("Feunnec", 653, Type.FEU, Type.NONE, talents, 40, 45, 40, 62, 60, 60));

        talents = new ArrayList<Talent>(){{this.add(Talent.LEVITATION);this.add(Talent.IGNIFUGE);this.add(Talent.HEAVY_METAL);}};
        this.put("Archeodong", new Pokemon("Archeodong", 437, Type.ACIER, Type.PSY, talents, 67, 89, 116, 79, 116, 33));

        talents = new ArrayList<Talent>(){{this.add(Talent.ABSORB_EAU);this.add(Talent.MOITEUR);this.add(Talent.INCONSCIENT);}};
        this.put("Axoloto", new Pokemon("Axoloto", 194, Type.EAU, Type.SOL, talents, 55, 45, 45, 25, 25, 15));

        talents = new ArrayList<Talent>(){{this.add(Talent.ENGRAIS);this.add(Talent.FEUIL_GARDE);}};
        this.put("Macronium", new Pokemon("Macronium", 153, Type.PLANTE, Type.NONE, talents, 60, 62, 80, 63, 80, 60));

        talents = new ArrayList<Talent>(){{this.add(Talent.CHLOROPHYLE);}};
        this.put("Rafflesia", new Pokemon("Rafflesia", 45, Type.PLANTE, Type.POISON, talents, 75, 80, 85, 100, 90, 50));

        talents = new ArrayList<Talent>(){{this.add(Talent.FERMETE);this.add(Talent.GLOUTONNERIE);this.add(Talent.CONTESTATION);}};
        this.put("Caratroc", new Pokemon("Caratroc", 213, Type.INSECTE, Type.ROCHE, talents, 20, 10, 230, 10, 230, 5));

        talents = new ArrayList<Talent>(){{this.add(Talent.MEDIC_NATURE);}};
        this.put("Shaymin (Forme Celeste)", new Pokemon("Shaymin (Forme Celeste)", 492, Type.PLANTE, Type.NONE, talents, 100, 103, 75, 120, 75, 127));

        talents = new ArrayList<Talent>(){{this.add(Talent.INTIMIDATION);this.add(Talent.BAIGNE_SABLE);this.add(Talent.QUERELLEUR);}};
        this.put("Ponchien", new Pokemon("Ponchien", 507, Type.NORMAL, Type.NONE, talents, 65, 80, 65, 35, 65, 60));

        talents = new ArrayList<Talent>(){{this.add(Talent.CHLOROPHYLE);this.add(Talent.MATINAL);this.add(Talent.PICKPOCKET);}};
        this.put("Pifeuil", new Pokemon("Pifeuil", 274, Type.PLANTE, Type.TENEBRE, talents, 70, 70, 40, 60, 40, 60));

        talents = new ArrayList<Talent>(){{this.add(Talent.JOLI_SOURIRE);this.add(Talent.BATTANT);this.add(Talent.GARDE_AMIE);}};
        this.put("Toudoudou", new Pokemon("Toudoudou", 174, Type.NORMAL, Type.NONE, talents, 90, 30, 15, 40, 20, 15));

        talents = new ArrayList<Talent>(){{this.add(Talent.VOILE_SABLE);this.add(Talent.BAIGNE_SABLE);}};
        this.put("Sablaireau", new Pokemon("Sablaireau", 28, Type.SOL, Type.NONE, talents, 75, 100, 110, 45, 55, 65));

        talents = new ArrayList<Talent>(){{this.add(Talent.RAMASSAGE);this.add(Talent.FOUILLE);this.add(Talent.INSOMNIA);}};
        this.put("Banshitrouye (Taille Mini)", new Pokemon("Banshitrouye (Taille Mini)", 711, Type.SPECTRE, Type.PLANTE, talents, 55, 85, 122, 58, 75, 99));

        talents = new ArrayList<Talent>(){{this.add(Talent.TETE_DE_ROC);this.add(Talent.SANS_LIMITE);}};
        this.put("Draby", new Pokemon("Draby", 371, Type.DRAGON, Type.NONE, talents, 45, 75, 60, 40, 30, 50));

        talents = new ArrayList<Talent>(){{this.add(Talent.AIR_LOCK);}};
        this.put("Rayquaza", new Pokemon("Rayquaza", 384, Type.DRAGON, Type.VOL, talents, 105, 150, 90, 150, 90, 95));

        talents = new ArrayList<Talent>(){{this.add(Talent.CHLOROPHYLE);this.add(Talent.FEUIL_GARDE);this.add(Talent.INFILTRATION);}};
        this.put("Granivol", new Pokemon("Granivol", 187, Type.PLANTE, Type.VOL, talents, 35, 35, 40, 35, 55, 50));

        talents = new ArrayList<Talent>(){{this.add(Talent.INTIMIDATION);this.add(Talent.RIVALITE);this.add(Talent.CRAN);}};
        this.put("Luxio", new Pokemon("Luxio", 404, Type.ELECTRIQUE, Type.NONE, talents, 60, 85, 49, 60, 49, 60));

        talents = new ArrayList<Talent>(){{this.add(Talent.DON_FLORAL);}};
        this.put("Ceriflor", new Pokemon("Ceriflor", 421, Type.PLANTE, Type.NONE, talents, 70, 60, 70, 87, 78, 85));

        talents = new ArrayList<Talent>(){{this.add(Talent.PRESSION);this.add(Talent.PICKPOCKET);}};
        this.put("Dimoret", new Pokemon("Dimoret", 461, Type.TENEBRE, Type.GLACE, talents, 70, 120, 65, 45, 85, 125));

        talents = new ArrayList<Talent>(){{this.add(Talent.GLISSADE);this.add(Talent.COQUE_ARMURE);this.add(Talent.ARMUROUILLEE);}};
        this.put("Amonita", new Pokemon("Amonita", 138, Type.ROCHE, Type.EAU, talents, 35, 40, 100, 90, 55, 35));

        talents = new ArrayList<Talent>(){{this.add(Talent.ESSAIM);this.add(Talent.CHLOROPHYLE);this.add(Talent.ENVELOCAPE);}};
        this.put("Larveyette", new Pokemon("Larveyette", 540, Type.INSECTE, Type.PLANTE, talents, 45, 53, 70, 40, 60, 42));

        talents = new ArrayList<Talent>(){{this.add(Talent.HYPER_CUTTER);this.add(Talent.COQUE_ARMURE);this.add(Talent.SANS_LIMITE);}};
        this.put("Krabboss", new Pokemon("Krabboss", 99, Type.EAU, Type.NONE, talents, 55, 130, 115, 50, 50, 75));

        talents = new ArrayList<Talent>(){{this.add(Talent.GLISSADE);this.add(Talent.HYDRATATION);this.add(Talent.ABSORB_EAU);}};
        this.put("Batracne", new Pokemon("Batracne", 536, Type.EAU, Type.SOL, talents, 75, 65, 55, 65, 55, 69));

        talents = new ArrayList<Talent>(){{this.add(Talent.CORPS_SAIN);this.add(Talent.SUINTEMENT);this.add(Talent.CUVETTE);}};
        this.put("Tentacool", new Pokemon("Tentacool", 72, Type.EAU, Type.POISON, talents, 40, 40, 35, 50, 100, 70));

        talents = new ArrayList<Talent>(){{this.add(Talent.SABLE_VOLANT);this.add(Talent.FORCE_SABLE);}};
        this.put("Hippodocus", new Pokemon("Hippodocus", 450, Type.SOL, Type.NONE, talents, 108, 112, 118, 68, 72, 47));

        talents = new ArrayList<Talent>(){{this.add(Talent.IGNIFU_VOILE);this.add(Talent.BENET);}};
        this.put("Wailmer", new Pokemon("Wailmer", 320, Type.EAU, Type.NONE, talents, 130, 70, 35, 70, 35, 60));

        talents = new ArrayList<Talent>(){{this.add(Talent.CORPS_ARDENT);this.add(Talent.ESPRIT_VITAL);}};
        this.put("Magmar", new Pokemon("Magmar", 126, Type.FEU, Type.NONE, talents, 65, 95, 57, 100, 85, 93));

        talents = new ArrayList<Talent>(){{this.add(Talent.TORCHE);this.add(Talent.INTIMIDATION);}};
        this.put("Caninos", new Pokemon("Caninos", 58, Type.FEU, Type.NONE, talents, 55, 70, 45, 70, 50, 60));

        talents = new ArrayList<Talent>(){{this.add(Talent.LEVITATION);}};
        this.put("Seleroc", new Pokemon("Seleroc", 337, Type.ROCHE, Type.PSY, talents, 70, 55, 65, 95, 85, 70));

        talents = new ArrayList<Talent>(){{this.add(Talent.ATTENTION);this.add(Talent.IMPASSIBLE);this.add(Talent.COEUR_NOBLE);}};
        this.put("Lucario", new Pokemon("Lucario", 448, Type.COMBAT, Type.ACIER, talents, 70, 110, 70, 115, 70, 90));

        talents = new ArrayList<Talent>(){{this.add(Talent.CRAN);this.add(Talent.ANNULE_GARDE);this.add(Talent.IMPASSIBLE);}};
        this.put("Machopeur", new Pokemon("Machopeur", 67, Type.COMBAT, Type.NONE, talents, 80, 100, 70, 50, 60, 45));

        talents = new ArrayList<Talent>(){{this.add(Talent.GLISSADE);this.add(Talent.BENET);this.add(Talent.ADAPTABILITE);}};
        this.put("Barpau", new Pokemon("Barpau", 349, Type.EAU, Type.NONE, talents, 20, 15, 20, 10, 55, 80));

        talents = new ArrayList<Talent>(){{this.add(Talent.MUE);}};
        this.put("Armulys", new Pokemon("Armulys", 266, Type.INSECTE, Type.NONE, talents, 50, 35, 55, 25, 25, 15));

        talents = new ArrayList<Talent>(){{this.add(Talent.ARMURBASTON);this.add(Talent.SNIPER);this.add(Talent.REGARD_VIF);}};
        this.put("Drascore", new Pokemon("Drascore", 452, Type.POISON, Type.TENEBRE, talents, 70, 90, 110, 60, 75, 95));

        talents = new ArrayList<Talent>(){{this.add(Talent.BENET);this.add(Talent.TEMPO_PERSO);this.add(Talent.CIEL_GRIS);}};
        this.put("Coudlangue", new Pokemon("Coudlangue", 463, Type.NORMAL, Type.NONE, talents, 110, 85, 95, 80, 95, 50));

        talents = new ArrayList<Talent>(){{this.add(Talent.FERMETE);this.add(Talent.MAGNEPIEGE);this.add(Talent.FORCE_SABLE);}};
        this.put("Tarinorme", new Pokemon("Tarinorme", 476, Type.ROCHE, Type.ACIER, talents, 60, 55, 145, 75, 150, 40));

        talents = new ArrayList<Talent>(){{this.add(Talent.GLISSADE);this.add(Talent.HYDRATATION);}};
        this.put("Lovdisc", new Pokemon("Lovdisc", 370, Type.EAU, Type.NONE, talents, 43, 30, 55, 40, 65, 97));

        talents = new ArrayList<Talent>(){{this.add(Talent.CHLOROPHYLE);this.add(Talent.FEUIL_GARDE);this.add(Talent.REGE_FORCE);}};
        this.put("Saquedeneu", new Pokemon("Saquedeneu", 114, Type.PLANTE, Type.NONE, talents, 65, 55, 115, 100, 40, 60));

        talents = new ArrayList<Talent>(){{this.add(Talent.CHLOROPHYLE);this.add(Talent.MATINAL);this.add(Talent.PICKPOCKET);}};
        this.put("Tengalice", new Pokemon("Tengalice", 275, Type.PLANTE, Type.TENEBRE, talents, 90, 100, 60, 90, 60, 80));

        talents = new ArrayList<Talent>(){{this.add(Talent.POING_DE_FER);this.add(Talent.MALADRESSE);this.add(Talent.ANNULE_GARDE);}};
        this.put("Golemastoc", new Pokemon("Golemastoc", 623, Type.SOL, Type.SPECTRE, talents, 89, 124, 80, 55, 80, 55));

        talents = new ArrayList<Talent>(){{this.add(Talent.AGITATION);}};
        this.put("Diamat", new Pokemon("Diamat", 634, Type.TENEBRE, Type.DRAGON, talents, 72, 85, 70, 65, 70, 58));

        talents = new ArrayList<Talent>(){{this.add(Talent.FEUIL_GARDE);this.add(Talent.CHLOROPHYLE);}};
        this.put("Phyllali", new Pokemon("Phyllali", 470, Type.PLANTE, Type.NONE, talents, 65, 110, 130, 60, 65, 95));

        talents = new ArrayList<Talent>(){{this.add(Talent.REGARD_VIF);this.add(Talent.INFILTRATION);this.add(Talent.FARCEUR);this.add(Talent.BATTANT);}};
        this.put("Mistigrix", new Pokemon("Mistigrix", 678, Type.PSY, Type.NONE, talents, 74, 48, 76, 83, 81, 104));

        talents = new ArrayList<Talent>(){{this.add(Talent.BRASIER);this.add(Talent.ISOGRAISSE);}};
        this.put("Grotichon", new Pokemon("Grotichon", 499, Type.FEU, Type.COMBAT, talents, 90, 93, 55, 70, 55, 55));

        talents = new ArrayList<Talent>(){{this.add(Talent.CHLOROPHYLE);this.add(Talent.FORCE_SOLEIL);this.add(Talent.RECOLTE);}};
        this.put("Tropius", new Pokemon("Tropius", 357, Type.PLANTE, Type.VOL, talents, 99, 68, 83, 72, 87, 51));

        talents = new ArrayList<Talent>(){{this.add(Talent.POSE_SPORE);this.add(Talent.SOIN_POISON);this.add(Talent.TECHNICIEN);}};
        this.put("Chapignon", new Pokemon("Chapignon", 286, Type.PLANTE, Type.COMBAT, talents, 60, 130, 80, 60, 60, 70));

        talents = new ArrayList<Talent>(){{this.add(Talent.VICTORIEUX);}};
        this.put("Victini", new Pokemon("Victini", 494, Type.PSY, Type.FEU, talents, 100, 100, 100, 100, 100, 100));

        talents = new ArrayList<Talent>(){{this.add(Talent.MUE);}};
        this.put("Ymphect", new Pokemon("Ymphect", 247, Type.ROCHE, Type.SOL, talents, 70, 84, 70, 65, 70, 51));

        talents = new ArrayList<Talent>(){{this.add(Talent.PRESSION);this.add(Talent.RIDEAU_NEIGE);}};
        this.put("Artikodin", new Pokemon("Artikodin", 144, Type.GLACE, Type.VOL, talents, 90, 85, 100, 95, 125, 85));

        talents = new ArrayList<Talent>(){{this.add(Talent.HYDRATATION);}};
        this.put("Phione", new Pokemon("Phione", 489, Type.EAU, Type.NONE, talents, 80, 80, 80, 80, 80, 80));

        talents = new ArrayList<Talent>(){{this.add(Talent.RAMASSAGE);this.add(Talent.TECHNICIEN);this.add(Talent.TENSION);}};
        this.put("Miaouss", new Pokemon("Miaouss", 52, Type.NORMAL, Type.NONE, talents, 40, 45, 35, 40, 40, 90));

        talents = new ArrayList<Talent>(){{this.add(Talent.CORPS_ARDENT);this.add(Talent.AILES_BOURRASQUE);}};
        this.put("Braisillon", new Pokemon("Braisillon", 662, Type.FEU, Type.VOL, talents, 62, 73, 55, 56, 52, 84));

        talents = new ArrayList<Talent>(){{this.add(Talent.ESSAIM);this.add(Talent.INSOMNIA);this.add(Talent.SNIPER);}};
        this.put("Migalos", new Pokemon("Migalos", 168, Type.INSECTE, Type.POISON, talents, 70, 90, 70, 60, 60, 40));

        talents = new ArrayList<Talent>(){{this.add(Talent.TETE_DE_ROC);this.add(Talent.FERMETE);this.add(Talent.PHOBIQUE);}};
        this.put("Manzai", new Pokemon("Manzai", 438, Type.ROCHE, Type.NONE, talents, 50, 80, 95, 10, 45, 10));

        talents = new ArrayList<Talent>(){{this.add(Talent.ATTENTION);this.add(Talent.INFILTRATION);}};
        this.put("Nosferapti", new Pokemon("Nosferapti", 41, Type.POISON, Type.VOL, talents, 40, 45, 35, 30, 40, 55));

        talents = new ArrayList<Talent>(){{this.add(Talent.GLISSADE);this.add(Talent.CUVETTE);}};
        this.put("Arakdo", new Pokemon("Arakdo", 283, Type.INSECTE, Type.EAU, talents, 40, 30, 32, 50, 52, 65));

        talents = new ArrayList<Talent>(){{this.add(Talent.TORRENT);this.add(Talent.SANS_LIMITE);}};
        this.put("Kaiminus", new Pokemon("Kaiminus", 158, Type.EAU, Type.NONE, talents, 50, 65, 64, 44, 48, 43));

        talents = new ArrayList<Talent>(){{this.add(Talent.ESSAIM);this.add(Talent.RIVALITE);}};
        this.put("Charmillon", new Pokemon("Charmillon", 267, Type.INSECTE, Type.VOL, talents, 60, 70, 50, 90, 50, 65));

        talents = new ArrayList<Talent>(){{this.add(Talent.PARATONNERRE);this.add(Talent.MOTORISE);this.add(Talent.HERBIVORE);}};
        this.put("Zebibron", new Pokemon("Zebibron", 522, Type.ELECTRIQUE, Type.NONE, talents, 45, 60, 32, 50, 32, 76));

        talents = new ArrayList<Talent>(){{this.add(Talent.RIVALITE);this.add(Talent.BRISE_MOULE);this.add(Talent.TENSION);}};
        this.put("Coupenotte", new Pokemon("Coupenotte", 610, Type.DRAGON, Type.NONE, talents, 46, 87, 60, 30, 40, 57));

        talents = new ArrayList<Talent>(){{this.add(Talent.LUMIATTIRANCE);this.add(Talent.ESSAIM);this.add(Talent.FARCEUR);}};
        this.put("Muciole", new Pokemon("Muciole", 313, Type.INSECTE, Type.NONE, talents, 65, 73, 55, 47, 75, 85));

        talents = new ArrayList<Talent>(){{this.add(Talent.ESSAIM);this.add(Talent.TECHNICIEN);this.add(Talent.LIGHT_METAL);}};
        this.put("Cizayox", new Pokemon("Cizayox", 212, Type.INSECTE, Type.ACIER, talents, 70, 130, 100, 55, 80, 65));

        talents = new ArrayList<Talent>(){{this.add(Talent.VOILE_SABLE);this.add(Talent.PIEGE);this.add(Talent.FORCE_SABLE);}};
        this.put("Triopikeur", new Pokemon("Triopikeur", 51, Type.SOL, Type.NONE, talents, 35, 80, 50, 50, 70, 120));

        talents = new ArrayList<Talent>(){{this.add(Talent.CHLOROPHYLE);this.add(Talent.FEUIL_GARDE);this.add(Talent.INFILTRATION);}};
        this.put("Floravol", new Pokemon("Floravol", 188, Type.PLANTE, Type.VOL, talents, 55, 45, 50, 45, 65, 80));

        talents = new ArrayList<Talent>(){{this.add(Talent.CRAN);this.add(Talent.SANS_LIMITE);this.add(Talent.POING_DE_FER);}};
        this.put("Ouvrifier", new Pokemon("Ouvrifier", 533, Type.COMBAT, Type.NONE, talents, 85, 105, 85, 40, 50, 40));

        talents = new ArrayList<Talent>(){{this.add(Talent.MAUVAIS_REVE);}};
        this.put("Darkrai", new Pokemon("Darkrai", 491, Type.TENEBRE, Type.NONE, talents, 70, 90, 90, 135, 90, 125));

        talents = new ArrayList<Talent>(){{this.add(Talent.SYNCHRO);}};
        this.put("Mew", new Pokemon("Mew", 151, Type.PSY, Type.NONE, talents, 100, 100, 100, 100, 100, 100));

        talents = new ArrayList<Talent>(){{this.add(Talent.EPINE_DE_FER);}};
        this.put("Grindur", new Pokemon("Grindur", 597, Type.PLANTE, Type.ACIER, talents, 44, 50, 91, 24, 86, 10));

        talents = new ArrayList<Talent>(){{this.add(Talent.POSE_SPORE);this.add(Talent.SOIN_POISON);this.add(Talent.PIED_VELOCE);}};
        this.put("Balignon", new Pokemon("Balignon", 285, Type.PLANTE, Type.NONE, talents, 60, 40, 60, 40, 60, 35));

        talents = new ArrayList<Talent>(){{this.add(Talent.POINT_POISON);this.add(Talent.TOXITOUCHE);}};
        this.put("Kravarech", new Pokemon("Kravarech", 691, Type.POISON, Type.DRAGON, talents, 65, 75, 90, 97, 123, 44));

        talents = new ArrayList<Talent>(){{this.add(Talent.ECHAUFFEMENT);this.add(Talent.TEMPO_PERSO);this.add(Talent.REGARD_VIF);}};
        this.put("Chaglam", new Pokemon("Chaglam", 431, Type.NORMAL, Type.NONE, talents, 49, 55, 42, 42, 37, 85));

        talents = new ArrayList<Talent>(){{this.add(Talent.AURA_FEERIQUE);}};
        this.put("Xerneas", new Pokemon("Xerneas", 716, Type.FEE, Type.NONE, talents, 126, 131, 95, 131, 98, 99));

        talents = new ArrayList<Talent>(){{this.add(Talent.ESPRIT_VITAL);this.add(Talent.AGITATION);}};
        this.put("Cadoizo", new Pokemon("Cadoizo", 225, Type.GLACE, Type.VOL, talents, 45, 55, 45, 65, 45, 75));

        talents = new ArrayList<Talent>(){{this.add(Talent.AMOUR_FILIAL);}};
        this.put("Mega-Kangourex", new Pokemon("Mega-Kangourex", 115, Type.NORMAL, Type.NONE, talents, 105, 125, 100, 60, 100, 100));

        talents = new ArrayList<Talent>(){{this.add(Talent.BRASIER);this.add(Talent.FORCE_SOLEIL);}};
        this.put("Salameche", new Pokemon("Salameche", 4, Type.FEU, Type.NONE, talents, 39, 52, 43, 60, 40, 65));

        talents = new ArrayList<Talent>(){{this.add(Talent.ABSORB_VOLT);this.add(Talent.LUMIATTIRANCE);this.add(Talent.ABSORB_EAU);}};
        this.put("Lanturn", new Pokemon("Lanturn", 171, Type.EAU, Type.ELECTRIQUE, talents, 125, 58, 58, 76, 76, 67));

        talents = new ArrayList<Talent>(){{this.add(Talent.BRASIER);this.add(Talent.POING_DE_FER);}};
        this.put("Simiabraz", new Pokemon("Simiabraz", 392, Type.FEU, Type.COMBAT, talents, 76, 104, 71, 104, 71, 108));

        talents = new ArrayList<Talent>(){{this.add(Talent.FOUILLE);this.add(Talent.INFILTRATION);this.add(Talent.TELEPATHE);}};
        this.put("Bruyverne", new Pokemon("Bruyverne", 715, Type.VOL, Type.DRAGON, talents, 85, 70, 80, 97, 80, 123));

        talents = new ArrayList<Talent>(){{this.add(Talent.HYDRATATION);this.add(Talent.HERBIVORE);this.add(Talent.POISSEUX);}};
        this.put("Mucuscule", new Pokemon("Mucuscule", 704, Type.DRAGON, Type.NONE, talents, 40, 50, 30, 70, 100, 45));

        talents = new ArrayList<Talent>(){{this.add(Talent.ISOGRAISSE);this.add(Talent.TEMPO_PERSO);this.add(Talent.ACHARNE);}};
        this.put("Chaffreux", new Pokemon("Chaffreux", 432, Type.NORMAL, Type.NONE, talents, 71, 82, 64, 64, 59, 112));

        talents = new ArrayList<Talent>(){{this.add(Talent.DEFAITISTE);}};
        this.put("Aeropteryx", new Pokemon("Aeropteryx", 567, Type.ROCHE, Type.VOL, talents, 75, 140, 65, 112, 65, 110));

        talents = new ArrayList<Talent>(){{this.add(Talent.ATTENTION);this.add(Talent.REGARD_VIF);this.add(Talent.PICKPOCKET);}};
        this.put("Farfuret", new Pokemon("Farfuret", 215, Type.TENEBRE, Type.GLACE, talents, 55, 95, 55, 35, 75, 115));

        talents = new ArrayList<Talent>(){{this.add(Talent.CHLOROPHYLE);this.add(Talent.FEUIL_GARDE);this.add(Talent.INFILTRATION);}};
        this.put("Cotovol", new Pokemon("Cotovol", 189, Type.PLANTE, Type.VOL, talents, 75, 55, 70, 55, 85, 110));

        talents = new ArrayList<Talent>(){{this.add(Talent.JOLI_SOURIRE);this.add(Talent.BATTANT);this.add(Talent.GARDE_AMIE);}};
        this.put("Rondoudou", new Pokemon("Rondoudou", 39, Type.NORMAL, Type.NONE, talents, 115, 45, 20, 45, 25, 20));

        talents = new ArrayList<Talent>(){{this.add(Talent.CORPS_GEL);this.add(Talent.ARMUROUILLEE);}};
        this.put("Sorboul", new Pokemon("Sorboul", 583, Type.GLACE, Type.NONE, talents, 51, 65, 65, 80, 75, 59));

        talents = new ArrayList<Talent>(){{this.add(Talent.GLISSADE);this.add(Talent.COQUE_ARMURE);this.add(Talent.ARMUROUILLEE);}};
        this.put("Amonistar", new Pokemon("Amonistar", 139, Type.ROCHE, Type.EAU, talents, 70, 60, 125, 115, 70, 55));

        talents = new ArrayList<Talent>(){{this.add(Talent.PLUS);this.add(Talent.MINUS);this.add(Talent.CORPS_SAIN);}};
        this.put("Clic", new Pokemon("Clic", 600, Type.ACIER, Type.NONE, talents, 60, 80, 95, 70, 85, 50));

        talents = new ArrayList<Talent>(){{this.add(Talent.ENGRAIS);this.add(Talent.FEUIL_GARDE);}};
        this.put("Meganium", new Pokemon("Meganium", 154, Type.PLANTE, Type.NONE, talents, 80, 82, 100, 83, 100, 80));

        talents = new ArrayList<Talent>(){{this.add(Talent.PRESSION);}};
        this.put("Deoxys (Forme Defense)", new Pokemon("Deoxys (Forme Defense)", 386, Type.PSY, Type.NONE, talents, 50, 70, 160, 70, 160, 90));

        talents = new ArrayList<Talent>(){{this.add(Talent.ABSORB_EAU);this.add(Talent.CORPS_MAUDIT);this.add(Talent.MOITEUR);}};
        this.put("Viskuse", new Pokemon("Viskuse", 592, Type.EAU, Type.SPECTRE, talents, 55, 40, 50, 65, 85, 40));

        talents = new ArrayList<Talent>(){{this.add(Talent.ECHAUFFEMENT);this.add(Talent.IMPOSTEUR);}};
        this.put("Metamorph", new Pokemon("Metamorph", 132, Type.NORMAL, Type.NONE, talents, 48, 48, 48, 48, 48, 48));

        talents = new ArrayList<Talent>(){{this.add(Talent.MATINAL);this.add(Talent.QUERELLEUR);this.add(Talent.ATTENTION);}};
        this.put("Kangourex", new Pokemon("Kangourex", 115, Type.NORMAL, Type.NONE, talents, 105, 95, 80, 40, 80, 90));

        talents = new ArrayList<Talent>(){{this.add(Talent.RAMASSAGE);this.add(Talent.FOUILLE);this.add(Talent.INSOMNIA);}};
        this.put("Pitrouille (Taille Normale)", new Pokemon("Pitrouille (Taille Normale)", 710, Type.SPECTRE, Type.PLANTE, talents, 49, 66, 70, 44, 55, 51));

        talents = new ArrayList<Talent>(){{this.add(Talent.IGNIFU_VOILE);this.add(Talent.BENET);}};
        this.put("Wailord", new Pokemon("Wailord", 321, Type.EAU, Type.NONE, talents, 170, 90, 45, 90, 45, 60));

        talents = new ArrayList<Talent>(){{this.add(Talent.ESPRIT_VITAL);this.add(Talent.COLERIQUE);this.add(Talent.ACHARNE);}};
        this.put("Colossinge", new Pokemon("Colossinge", 57, Type.COMBAT, Type.NONE, talents, 65, 105, 60, 60, 70, 95));

        talents = new ArrayList<Talent>(){{this.add(Talent.AURA_TENEBREUSE);}};
        this.put("Yveltal", new Pokemon("Yveltal", 717, Type.TENEBRE, Type.VOL, talents, 126, 131, 95, 131, 98, 99));

        talents = new ArrayList<Talent>(){{this.add(Talent.FARCEUR);this.add(Talent.ACHARNE);}};
        this.put("Fulguris (Forme Totemique)", new Pokemon("Fulguris (Forme Totemique)", 642, Type.ELECTRIQUE, Type.VOL, talents, 79, 105, 70, 145, 80, 101));

        talents = new ArrayList<Talent>(){{this.add(Talent.AGITATION);this.add(Talent.MEDIC_NATURE);}};
        this.put("Corayon", new Pokemon("Corayon", 222, Type.EAU, Type.ROCHE, talents, 55, 55, 85, 65, 85, 35));

        talents = new ArrayList<Talent>(){{this.add(Talent.CRAN);this.add(Talent.ANNULE_GARDE);this.add(Talent.IMPASSIBLE);}};
        this.put("Mackogneur", new Pokemon("Mackogneur", 68, Type.COMBAT, Type.NONE, talents, 90, 130, 80, 65, 85, 55));

        talents = new ArrayList<Talent>(){{this.add(Talent.ARMURBASTON);this.add(Talent.SNIPER);this.add(Talent.REGARD_VIF);}};
        this.put("Rapion", new Pokemon("Rapion", 451, Type.POISON, Type.INSECTE, talents, 40, 50, 90, 30, 55, 65));

        talents = new ArrayList<Talent>(){{this.add(Talent.GLOUTONNERIE);this.add(Talent.ENGRAIS);}};
        this.put("Feuiloutan", new Pokemon("Feuiloutan", 512, Type.PLANTE, Type.NONE, talents, 75, 98, 63, 98, 63, 101));

        talents = new ArrayList<Talent>(){{this.add(Talent.CRAN);this.add(Talent.PIED_VELOCE);this.add(Talent.TENSION);}};
        this.put("Ursaring", new Pokemon("Ursaring", 217, Type.NORMAL, Type.NONE, talents, 90, 130, 75, 75, 75, 55));

        talents = new ArrayList<Talent>(){{this.add(Talent.ARMURBASTON);this.add(Talent.GLISSADE);}};
        this.put("Anorith", new Pokemon("Anorith", 347, Type.ROCHE, Type.INSECTE, talents, 45, 95, 50, 40, 50, 75));

        talents = new ArrayList<Talent>(){{this.add(Talent.ENGRAIS);this.add(Talent.CONTESTATION);}};
        this.put("Vipelierre", new Pokemon("Vipelierre", 495, Type.PLANTE, Type.NONE, talents, 45, 45, 55, 45, 55, 63));

        talents = new ArrayList<Talent>(){{this.add(Talent.SYNCHRO);this.add(Talent.CALQUE);this.add(Talent.TELEPATHE);}};
        this.put("Gardevoir", new Pokemon("Gardevoir", 282, Type.PSY, Type.NONE, talents, 68, 65, 65, 125, 115, 80));

        talents = new ArrayList<Talent>(){{this.add(Talent.CRAN);this.add(Talent.ESSAIM);this.add(Talent.IMPUDENCE);}};
        this.put("Scarhino", new Pokemon("Scarhino", 214, Type.INSECTE, Type.COMBAT, talents, 80, 125, 75, 40, 95, 85));

        talents = new ArrayList<Talent>(){{this.add(Talent.TORCHE);this.add(Talent.MATINAL);this.add(Talent.TENSION);}};
        this.put("Demolosse", new Pokemon("Demolosse", 229, Type.TENEBRE, Type.FEU, talents, 75, 90, 50, 110, 80, 95));

        talents = new ArrayList<Talent>(){{this.add(Talent.GLISSADE);this.add(Talent.TOXITOUCHE);this.add(Talent.ABSORB_EAU);}};
        this.put("Crapustule", new Pokemon("Crapustule", 537, Type.EAU, Type.SOL, talents, 105, 85, 75, 85, 75, 74));

        talents = new ArrayList<Talent>(){{this.add(Talent.FERMETE);this.add(Talent.COQUE_ARMURE);this.add(Talent.ARMUROUILLEE);}};
        this.put("Crabaraque", new Pokemon("Crabaraque", 558, Type.INSECTE, Type.ROCHE, talents, 70, 95, 125, 65, 75, 45));

        talents = new ArrayList<Talent>(){{this.add(Talent.RIVALITE);this.add(Talent.BRISE_MOULE);this.add(Talent.TENSION);}};
        this.put("Tranchodon", new Pokemon("Tranchodon", 612, Type.DRAGON, Type.NONE, talents, 76, 147, 90, 60, 70, 97));

        talents = new ArrayList<Talent>(){{this.add(Talent.PRESSION);this.add(Talent.TENSION);}};
        this.put("Mewtwo", new Pokemon("Mewtwo", 150, Type.PSY, Type.NONE, talents, 106, 110, 90, 154, 90, 130));

        talents = new ArrayList<Talent>(){{this.add(Talent.BRASIER);this.add(Talent.TORCHE);}};
        this.put("Feurisson", new Pokemon("Feurisson", 156, Type.FEU, Type.NONE, talents, 58, 64, 58, 80, 65, 80));

        talents = new ArrayList<Talent>(){{this.add(Talent.FERMETE);this.add(Talent.TETE_DE_ROC);this.add(Talent.HEAVY_METAL);}};
        this.put("Galeking", new Pokemon("Galeking", 306, Type.ACIER, Type.ROCHE, talents, 70, 110, 180, 60, 60, 50));

        talents = new ArrayList<Talent>(){{this.add(Talent.LUMIATTIRANCE);this.add(Talent.REGARD_VIF);this.add(Talent.ANALYSTE);}};
        this.put("Miradar", new Pokemon("Miradar", 505, Type.NORMAL, Type.NONE, talents, 60, 85, 69, 60, 69, 77));

        talents = new ArrayList<Talent>(){{this.add(Talent.SABLE_VOLANT);this.add(Talent.TENSION);}};
        this.put("Tyranocif", new Pokemon("Tyranocif", 248, Type.ROCHE, Type.TENEBRE, talents, 100, 134, 110, 95, 100, 61));

        talents = new ArrayList<Talent>(){{this.add(Talent.HYPER_CUTTER);this.add(Talent.VOILE_SABLE);this.add(Talent.SOIN_POISON);}};
        this.put("Scorvol", new Pokemon("Scorvol", 472, Type.SOL, Type.VOL, talents, 75, 95, 125, 45, 75, 95));

        talents = new ArrayList<Talent>(){{this.add(Talent.GLISSADE);this.add(Talent.ABSORB_EAU);}};
        this.put("Demanta", new Pokemon("Demanta", 226, Type.EAU, Type.VOL, talents, 65, 40, 70, 80, 140, 70));

        talents = new ArrayList<Talent>(){{this.add(Talent.LEVITATION);}};
        this.put("Solaroc", new Pokemon("Solaroc", 338, Type.ROCHE, Type.PSY, talents, 70, 95, 85, 55, 65, 70));

        talents = new ArrayList<Talent>(){{this.add(Talent.COEUR_DE_COQ);this.add(Talent.AILES_BOURRASQUE);}};
        this.put("Passerouge", new Pokemon("Passerouge", 661, Type.NORMAL, Type.VOL, talents, 45, 50, 43, 40, 38, 62));

        talents = new ArrayList<Talent>(){{this.add(Talent.MULTI_COUPS);}};
        this.put("Mega-Scarhino", new Pokemon("Mega-Scarhino", 214, Type.INSECTE, Type.COMBAT, talents, 80, 185, 115, 40, 105, 75));

        talents = new ArrayList<Talent>(){{this.add(Talent.TORRENT);this.add(Talent.MOITEUR);}};
        this.put("Flobio", new Pokemon("Flobio", 259, Type.EAU, Type.SOL, talents, 70, 85, 70, 60, 70, 50));

        talents = new ArrayList<Talent>(){{this.add(Talent.RIDEAU_NEIGE);}};
        this.put("Cochignon", new Pokemon("Cochignon", 221, Type.GLACE, Type.SOL, talents, 100, 100, 80, 60, 60, 50));

        talents = new ArrayList<Talent>(){{this.add(Talent.MEDIC_NATURE);this.add(Talent.POINT_POISON);this.add(Talent.TECHNICIEN);}};
        this.put("Roserade", new Pokemon("Roserade", 407, Type.PLANTE, Type.POISON, talents, 60, 70, 55, 125, 105, 90));

        talents = new ArrayList<Talent>(){{this.add(Talent.BENET);this.add(Talent.SIMPLE);}};
        this.put("Chamallot", new Pokemon("Chamallot", 322, Type.FEU, Type.SOL, talents, 60, 60, 40, 65, 45, 35));

        talents = new ArrayList<Talent>(){{this.add(Talent.ECHAUFFEMENT);this.add(Talent.DELESTAGE);this.add(Talent.FARCEUR);}};
        this.put("Chacripan", new Pokemon("Chacripan", 509, Type.TENEBRE, Type.NONE, talents, 41, 50, 37, 50, 37, 66));

        talents = new ArrayList<Talent>(){{this.add(Talent.INFILTRATION);this.add(Talent.REGARD_VIF);this.add(Talent.TEMPO_PERSO);}};
        this.put("Psystigri", new Pokemon("Psystigri", 677, Type.PSY, Type.NONE, talents, 60, 22, 62, 72, 72, 95));

        talents = new ArrayList<Talent>(){{this.add(Talent.FOUILLE);this.add(Talent.BATTANT);this.add(Talent.MARQUE_OMBRE);}};
        this.put("Scrutella", new Pokemon("Scrutella", 574, Type.PSY, Type.NONE, talents, 45, 30, 50, 55, 65, 45));

        talents = new ArrayList<Talent>(){{this.add(Talent.REGE_FORCE);this.add(Talent.ATTENTION);this.add(Talent.TEMERAIRE);}};
        this.put("Kungfouine", new Pokemon("Kungfouine", 619, Type.COMBAT, Type.NONE, talents, 45, 85, 50, 55, 50, 65));

        talents = new ArrayList<Talent>(){{this.add(Talent.RIDEAU_NEIGE);this.add(Talent.CORPS_MAUDIT);}};
        this.put("Momartik", new Pokemon("Momartik", 478, Type.GLACE, Type.SPECTRE, talents, 70, 80, 70, 80, 70, 110));

        talents = new ArrayList<Talent>(){{this.add(Talent.ECHAUFFEMENT);this.add(Talent.DELESTAGE);this.add(Talent.FARCEUR);}};
        this.put("Leopardus", new Pokemon("Leopardus", 510, Type.TENEBRE, Type.NONE, talents, 64, 88, 50, 88, 50, 106));

        talents = new ArrayList<Talent>(){{this.add(Talent.PRESSION);this.add(Talent.REGE_FORCE);}};
        this.put("Ho-Oh", new Pokemon("Ho-Oh", 250, Type.FEU, Type.VOL, talents, 106, 130, 90, 110, 154, 90));

        talents = new ArrayList<Talent>(){{this.add(Talent.HYPER_CUTTER);this.add(Talent.COQUE_ARMURE);this.add(Talent.SANS_LIMITE);}};
        this.put("Krabby", new Pokemon("Krabby", 98, Type.EAU, Type.NONE, talents, 30, 105, 90, 25, 25, 50));

        talents = new ArrayList<Talent>(){{this.add(Talent.PRESSION);this.add(Talent.ABSORB_EAU);}};
        this.put("Suicune", new Pokemon("Suicune", 245, Type.EAU, Type.NONE, talents, 100, 75, 115, 90, 115, 85));

        talents = new ArrayList<Talent>(){{this.add(Talent.PARATONNERRE);this.add(Talent.MOTORISE);this.add(Talent.HERBIVORE);}};
        this.put("Zeblitz", new Pokemon("Zeblitz", 523, Type.ELECTRIQUE, Type.NONE, talents, 75, 100, 63, 80, 63, 116));

        talents = new ArrayList<Talent>(){{this.add(Talent.BAJOUES);this.add(Talent.RAMASSAGE);this.add(Talent.COLOFORCE);}};
        this.put("Excavarenne", new Pokemon("Excavarenne", 660, Type.NORMAL, Type.SOL, talents, 85, 56, 77, 50, 77, 78));

        talents = new ArrayList<Talent>(){{this.add(Talent.FERMETE);this.add(Talent.VOILE_SABLE);}};
        this.put("Donphan", new Pokemon("Donphan", 232, Type.SOL, Type.NONE, talents, 90, 120, 120, 60, 60, 50));

        talents = new ArrayList<Talent>(){{this.add(Talent.TEMPO_PERSO);this.add(Talent.CORPS_GEL);this.add(Talent.FERMETE);}};
        this.put("Grelacon", new Pokemon("Grelacon", 712, Type.GLACE, Type.NONE, talents, 55, 69, 85, 32, 35, 28));

        talents = new ArrayList<Talent>(){{this.add(Talent.RAMASSAGE);this.add(Talent.FOUILLE);this.add(Talent.INSOMNIA);}};
        this.put("Pitrouille (Taille Ultra)", new Pokemon("Pitrouille (Taille Ultra)", 710, Type.SPECTRE, Type.PLANTE, talents, 59, 66, 70, 44, 55, 41));

        talents = new ArrayList<Talent>(){{this.add(Talent.ALERTE_NEIGE);this.add(Talent.ANTI_BRUIT);}};
        this.put("Blizzi", new Pokemon("Blizzi", 459, Type.PLANTE, Type.GLACE, talents, 60, 62, 50, 62, 60, 40));

        talents = new ArrayList<Talent>(){{this.add(Talent.MIROIR_MAGIK);}};
        this.put("Mega-Absol", new Pokemon("Mega-Absol", 359, Type.TENEBRE, Type.NONE, talents, 65, 150, 60, 115, 60, 115));

        talents = new ArrayList<Talent>(){{this.add(Talent.CORPS_SAIN);this.add(Talent.FERMETE);}};
        this.put("Strassie", new Pokemon("Strassie", 703, Type.ROCHE, Type.FEE, talents, 50, 50, 150, 50, 150, 50));

        talents = new ArrayList<Talent>(){{this.add(Talent.FARCEUR);this.add(Talent.MAGICIEN);}};
        this.put("Trousselin", new Pokemon("Trousselin", 707, Type.ACIER, Type.FEE, talents, 57, 80, 91, 80, 87, 75));

        talents = new ArrayList<Talent>(){{this.add(Talent.METEO);}};
        this.put("Morpheo", new Pokemon("Morpheo", 351, Type.NORMAL, Type.NONE, talents, 70, 70, 70, 70, 70, 70));

        talents = new ArrayList<Talent>(){{this.add(Talent.FERMETE);this.add(Talent.REGARD_VIF);this.add(Talent.ARMUROUILLEE);}};
        this.put("Airmure", new Pokemon("Airmure", 227, Type.ACIER, Type.VOL, talents, 65, 80, 140, 40, 70, 70));

        talents = new ArrayList<Talent>(){{this.add(Talent.ANTI_BRUIT);this.add(Talent.FILTRE);this.add(Talent.TECHNICIEN);}};
        this.put("M. Mime", new Pokemon("M. Mime", 122, Type.PSY, Type.NONE, talents, 40, 45, 65, 100, 120, 90));

        talents = new ArrayList<Talent>(){{this.add(Talent.SYNCHRO);this.add(Talent.MATINAL);this.add(Talent.MIROIR_MAGIK);}};
        this.put("Natu", new Pokemon("Natu", 177, Type.PSY, Type.VOL, talents, 40, 50, 45, 70, 45, 70));

        talents = new ArrayList<Talent>(){{this.add(Talent.STATIK);}};
        this.put("Lainergie", new Pokemon("Lainergie", 180, Type.ELECTRIQUE, Type.NONE, talents, 70, 55, 55, 80, 60, 45));

        talents = new ArrayList<Talent>(){{this.add(Talent.FORCE_SABLE);}};
        this.put("Mega-Carchacrok", new Pokemon("Mega-Carchacrok", 445, Type.DRAGON, Type.SOL, talents, 108, 170, 115, 120, 95, 92));

        talents = new ArrayList<Talent>(){{this.add(Talent.ESSAIM);this.add(Talent.MATINAL);this.add(Talent.PHOBIQUE);}};
        this.put("Coxy", new Pokemon("Coxy", 165, Type.INSECTE, Type.VOL, talents, 40, 20, 30, 40, 80, 55));

        talents = new ArrayList<Talent>(){{this.add(Talent.MEDIC_NATURE);}};
        this.put("Shaymin (Forme Terrestre)", new Pokemon("Shaymin (Forme Terrestre)", 492, Type.PLANTE, Type.NONE, talents, 100, 100, 100, 100, 100, 100));

        talents = new ArrayList<Talent>(){{this.add(Talent.RAMASSAGE);this.add(Talent.FOUILLE);this.add(Talent.INSOMNIA);}};
        this.put("Banshitrouye (Taille Maxi)", new Pokemon("Banshitrouye (Taille Maxi)", 711, Type.SPECTRE, Type.PLANTE, talents, 75, 95, 122, 58, 75, 69));

        talents = new ArrayList<Talent>(){{this.add(Talent.VOILE_SABLE);this.add(Talent.ABSORB_EAU);}};
        this.put("Cacnea", new Pokemon("Cacnea", 331, Type.PLANTE, Type.NONE, talents, 50, 85, 40, 85, 40, 35));

        talents = new ArrayList<Talent>(){{this.add(Talent.LEVITATION);}};
        this.put("Smogo", new Pokemon("Smogo", 109, Type.POISON, Type.NONE, talents, 40, 65, 95, 60, 45, 35));

        talents = new ArrayList<Talent>(){{this.add(Talent.INTIMIDATION);this.add(Talent.TORCHE);this.add(Talent.COEUR_NOBLE);}};
        this.put("Arcanin", new Pokemon("Arcanin", 59, Type.FEU, Type.NONE, talents, 90, 110, 80, 100, 80, 95));

        talents = new ArrayList<Talent>(){{this.add(Talent.ECAILLE_SPECIALE);this.add(Talent.BATTANT);this.add(Talent.JOLI_SOURIRE);}};
        this.put("Milobellus", new Pokemon("Milobellus", 350, Type.EAU, Type.NONE, talents, 95, 60, 79, 100, 125, 81));

        talents = new ArrayList<Talent>(){{this.add(Talent.VOILE_SABLE);this.add(Talent.PIEGE);this.add(Talent.FORCE_SABLE);}};
        this.put("Taupiqueur", new Pokemon("Taupiqueur", 50, Type.SOL, Type.NONE, talents, 10, 55, 25, 35, 45, 95));

        talents = new ArrayList<Talent>(){{this.add(Talent.FUITE);this.add(Talent.RAMASSAGE);this.add(Talent.MULTI_COUPS);}};
        this.put("Capumain", new Pokemon("Capumain", 190, Type.NORMAL, Type.NONE, talents, 55, 70, 55, 40, 55, 85));

        talents = new ArrayList<Talent>(){{this.add(Talent.FARCEUR);this.add(Talent.ACHARNE);}};
        this.put("Fulguris (Forme Avatar)", new Pokemon("Fulguris (Forme Avatar)", 642, Type.ELECTRIQUE, Type.VOL, talents, 79, 115, 70, 125, 80, 111));

        talents = new ArrayList<Talent>(){{this.add(Talent.CRAN);this.add(Talent.ANNULE_GARDE);this.add(Talent.IMPASSIBLE);}};
        this.put("Machoc", new Pokemon("Machoc", 66, Type.COMBAT, Type.NONE, talents, 70, 80, 50, 35, 35, 35));

        talents = new ArrayList<Talent>(){{this.add(Talent.GLISSADE);this.add(Talent.CUVETTE);}};
        this.put("Ludicolo", new Pokemon("Ludicolo", 272, Type.EAU, Type.PLANTE, talents, 80, 70, 70, 90, 100, 70));

        talents = new ArrayList<Talent>(){{this.add(Talent.INSOMNIA);this.add(Talent.REGARD_VIF);this.add(Talent.LENTITEINTEE);}};
        this.put("Noarfang", new Pokemon("Noarfang", 164, Type.NORMAL, Type.VOL, talents, 100, 50, 50, 76, 96, 70));

        talents = new ArrayList<Talent>(){{this.add(Talent.SERENITE);}};
        this.put("Meloetta (Forme Danse)", new Pokemon("Meloetta (Forme Danse)", 648, Type.NORMAL, Type.PSY, talents, 100, 128, 90, 77, 77, 128));

        talents = new ArrayList<Talent>(){{this.add(Talent.VENTOUSE);this.add(Talent.CONTESTATION);this.add(Talent.INFILTRATION);}};
        this.put("Sepiatop", new Pokemon("Sepiatop", 686, Type.TENEBRE, Type.PSY, talents, 53, 54, 53, 37, 46, 45));

        talents = new ArrayList<Talent>(){{this.add(Talent.ESSAIM);this.add(Talent.AGITATION);this.add(Talent.ABSENTEISME);}};
        this.put("Fermite", new Pokemon("Fermite", 632, Type.INSECTE, Type.ACIER, talents, 58, 109, 112, 48, 48, 109));

        talents = new ArrayList<Talent>(){{this.add(Talent.CORPS_SAIN);this.add(Talent.CORPS_GEL);}};
        this.put("Regice", new Pokemon("Regice", 378, Type.GLACE, Type.NONE, talents, 80, 50, 100, 100, 200, 50));

        talents = new ArrayList<Talent>(){{this.add(Talent.ARMURBASTON);this.add(Talent.GLISSADE);}};
        this.put("Armaldo", new Pokemon("Armaldo", 348, Type.ROCHE, Type.INSECTE, talents, 75, 125, 100, 70, 80, 45));

        talents = new ArrayList<Talent>(){{this.add(Talent.TELEPATHE);this.add(Talent.SYNCHRO);this.add(Talent.ANALYSTE);}};
        this.put("Lewsor", new Pokemon("Lewsor", 605, Type.PSY, Type.NONE, talents, 55, 55, 55, 85, 55, 30));

        talents = new ArrayList<Talent>(){{this.add(Talent.GLUE);this.add(Talent.LAVABO);this.add(Talent.FORCE_SABLE);}};
        this.put("Sancoki", new Pokemon("Sancoki", 422, Type.EAU, Type.NONE, talents, 76, 48, 48, 57, 62, 34));

        talents = new ArrayList<Talent>(){{this.add(Talent.FORCE_SABLE);this.add(Talent.SANS_LIMITE);}};
        this.put("Demeteros (Forme Totemique)", new Pokemon("Demeteros (Forme Totemique)", 645, Type.SOL, Type.VOL, talents, 89, 145, 90, 105, 80, 91));

        talents = new ArrayList<Talent>(){{this.add(Talent.POSE_SPORE);this.add(Talent.REGE_FORCE);}};
        this.put("Trompignon", new Pokemon("Trompignon", 590, Type.PLANTE, Type.POISON, talents, 69, 55, 45, 55, 55, 15));

        talents = new ArrayList<Talent>(){{this.add(Talent.CHLOROPHYLE);this.add(Talent.GLOUTONNERIE);}};
        this.put("Empiflor", new Pokemon("Empiflor", 71, Type.PLANTE, Type.POISON, talents, 80, 105, 65, 100, 60, 70));

        talents = new ArrayList<Talent>(){{this.add(Talent.TETE_DE_ROC);this.add(Talent.ENVELOCAPE);}};
        this.put("Drackhaus", new Pokemon("Drackhaus", 372, Type.DRAGON, Type.NONE, talents, 65, 95, 100, 60, 50, 50));

        talents = new ArrayList<Talent>(){{this.add(Talent.ECRAN_POUDRE);this.add(Talent.FUITE);}};
        this.put("Chenipan", new Pokemon("Chenipan", 10, Type.INSECTE, Type.NONE, talents, 45, 30, 35, 20, 20, 45));

        talents = new ArrayList<Talent>(){{this.add(Talent.STATIK);this.add(Talent.ECHAUFFEMENT);this.add(Talent.VOILE_SABLE);}};
        this.put("Limonde", new Pokemon("Limonde", 618, Type.ELECTRIQUE, Type.SOL, talents, 109, 66, 84, 81, 99, 32));

        talents = new ArrayList<Talent>(){{this.add(Talent.BOOM_FINAL);this.add(Talent.DELESTAGE);this.add(Talent.RAGE_BRULURE);}};
        this.put("Grodrive", new Pokemon("Grodrive", 426, Type.SPECTRE, Type.VOL, talents, 150, 80, 44, 90, 54, 80));

        talents = new ArrayList<Talent>(){{this.add(Talent.FLORA_VOILE);this.add(Talent.SYMBIOSIS);}};
        this.put("Flabebe", new Pokemon("Flabebe", 669, Type.FEE, Type.NONE, talents, 44, 38, 39, 61, 79, 42));

        talents = new ArrayList<Talent>(){{this.add(Talent.CALQUE);}};
        this.put("Mega-Alakazam", new Pokemon("Mega-Alakazam", 65, Type.PSY, Type.NONE, talents, 55, 50, 65, 175, 95, 150));

        talents = new ArrayList<Talent>(){{this.add(Talent.POINT_POISON);this.add(Talent.ESSAIM);this.add(Talent.PIED_VELOCE);}};
        this.put("Brutapode", new Pokemon("Brutapode", 545, Type.INSECTE, Type.POISON, talents, 60, 90, 89, 55, 69, 112));

        talents = new ArrayList<Talent>(){{this.add(Talent.PRESSION);}};
        this.put("Deoxys (Forme de Base)", new Pokemon("Deoxys (Forme de Base)", 386, Type.PSY, Type.NONE, talents, 50, 150, 50, 150, 50, 150));

        talents = new ArrayList<Talent>(){{this.add(Talent.SOLIDE_ROC);this.add(Talent.FERMETE);this.add(Talent.GLISSADE);}};
        this.put("Megapagos", new Pokemon("Megapagos", 565, Type.EAU, Type.ROCHE, talents, 74, 108, 133, 83, 65, 32));

        talents = new ArrayList<Talent>(){{this.add(Talent.CHANCEUX);this.add(Talent.COEUR_DE_COQ);this.add(Talent.RIVALITE);}};
        this.put("Deflaisan", new Pokemon("Deflaisan", 521, Type.NORMAL, Type.VOL, talents, 80, 105, 80, 65, 55, 93));

        talents = new ArrayList<Talent>(){{this.add(Talent.LEVITATION);}};
        this.put("Spectrum", new Pokemon("Spectrum", 93, Type.SPECTRE, Type.POISON, talents, 45, 50, 45, 115, 55, 95));

        talents = new ArrayList<Talent>(){{this.add(Talent.POING_DE_FER);this.add(Talent.BRISE_MOULE);this.add(Talent.QUERELLEUR);}};
        this.put("Pandarbare", new Pokemon("Pandarbare", 675, Type.COMBAT, Type.TENEBRE, talents, 95, 124, 78, 69, 71, 58));

        talents = new ArrayList<Talent>(){{this.add(Talent.PROGNATHE);}};
        this.put("Rexillius", new Pokemon("Rexillius", 697, Type.ROCHE, Type.DRAGON, talents, 82, 121, 119, 69, 59, 71));

        talents = new ArrayList<Talent>(){{this.add(Talent.PRESSION);this.add(Talent.CORPS_ARDENT);}};
        this.put("Sulfura", new Pokemon("Sulfura", 146, Type.FEU, Type.VOL, talents, 90, 100, 90, 125, 85, 90));

        talents = new ArrayList<Talent>(){{this.add(Talent.INTIMIDATION);this.add(Talent.IMPUDENCE);}};
        this.put("Drattak", new Pokemon("Drattak", 373, Type.DRAGON, Type.VOL, talents, 95, 135, 80, 110, 80, 100));

        talents = new ArrayList<Talent>(){{this.add(Talent.TEMPO_PERSO);this.add(Talent.CORPS_GEL);this.add(Talent.FERMETE);}};
        this.put("Seracrawl", new Pokemon("Seracrawl", 713, Type.GLACE, Type.NONE, talents, 95, 117, 184, 44, 46, 28));
    }};
}
