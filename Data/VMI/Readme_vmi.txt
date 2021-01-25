Samuli Launiainen 30.8.2016


Tiedostot vmi11.csv ja vmi12.csv (pilkkueroteltu) sisältävät seuraavat poimitut muuttujat VMI-maastotiedoston kuviotietueesta:


Katso folderissa olevat .sas-koodit joita käy ilmi muuttujanimi-sar. vastaavuus VMI-tietueessa, kts. Arton pdf-tietuekuvaukset.

Muuttujien tulkinta (==selkokielistys) pitää tehdä VMI12-maasto-oppaan mukaan.


invtun;
lohy-lohx;
koeala;
kuvio;
kunta; #MML kuntakoodi
koealankorkeus; #dm, a.sl.
lamposumma; #dd degC
framaa; # 1 forest, 2 other wooded land, 3 other land, 4 other land with tree cover
maaluokka; #1 metsämaa, 2 kitumaa, 3 joutomaa, 4 muu metsätalousmaa, 5 maatalousmaa, 6 rakennettu maa, 7 liikenneväylät, 8 voimansiirtolinjat, A sisävesi B merivesi C koealaan kuulumaton kuvio
entinenmaaluokka;
paatyyppi; 1 kangas, 2 korpi, 3 räme, 4 avosuo
kasvupaikkat; # 1 lehdot, 2 lehtomaiset kankaat, 3 tuoreet kankaat, 4 kuivahkot kankaat, 5 kuivat kankaat, 6 karukkomaat, 7 kalliomaat, 8 lakimetsät, T tunturikoivikot, A avotunturit
kasvuplisa; # 0 ei lisämäärettä, 1 ohutturpeisuus, 2 talvikkityypin kangas
suotyy; #AIDOT TYYPIT: 1 lehtokorpi, 2 ruohokorpi, 3 kangaskorpi, 4 mustikkakorpi, 5 puolukkakorpi, 6 pallosarakorpi, 7 korpiräme, 8 pallosararäme, 9 kangasräme, 10 isovarpuräme, 11 rahkaräme, 
		#SEKATYYPIT: 12 vars. lettokorpi, 13 koivulettokorpi, 14 ruoh. sarakorpi
		#15 vars. sarakorpi, 16 vars. lettoräme, 17 ruoh sararäme, 18 vars. sararäme, 19 tupasvillasararäme, 20 lyhytkorsiräme, 21 tupasvillaräme, 22 keidasräme
		#AVOSUOT: 23 vars. letto, 24 rimpiletto, 25 ruoh. saraneva, 26 ruoh. rimpineva, 27 vars. saraneva, 28 vars. rimpineva, 29 lyhytkorsikalvakkaneva, 30 lyhytkorsineva, 31 rahkaneva
turvekangas; # 1 ruohoturvekangas RhTg, 2 mustikkaturvekangas I MtKg(I), 3 mustikkaturvekangas II MtKg(II), 4 puolukkaturvekangas PtKg(I), 5 puolukkaturvekangas PtKg(II), 6 varputurvekangas Vatkg, 7 jäkäläturvekangas Jätkg
ojitustilanne; # 0 ojittamaton kangas tai suo, 1 ojitettu kangas, 2 ojikko (ojituksen vaikutus ei havaittavissa kasvillisuudessa), 3 muuttuma (vaikutus selvä, aluskasvillisuutta leimaa alkup. suotyyppi), 4 turvekangas
tehtyojitus; # 0 ei oijitusta, 1 uudisojitus, 2 ojien perkaus, 3 täydennysojitus, 4 muu kuin metsäojitus, 5 ojien tukkiminen
ojitusaika; #- ei toimenpiteitä, 1 arviointivuonna, 1 -1v, 2 -2v, 3 - 3v ... 50 -50v tai enemmän
ojitustarve; #0 ei ehdotusta, 1 uudisojitus, 2 ojien perkaus, 3 täydennysojitus
ojienkunto; # - ojittamaton, 1 hyvä, 2 tyydyttävä, 3 välttävä, 4 huono
veroluokka; #0 IA lehto ja lehtomainen kangas pl. talvikkityyppi, 1 IB tuore kangas ja lehtomainen talvikkityyppi, 2 II kuivahko kangas ja kunttaantunut puolukka-mustikkatyyppi, 3 III kuiva ja karukkokangas, 
				kunttaantunut paksusammal, luonnont. korpi, 4 IV metsämaan luonnontil. räme tai korpi
veroluokkatarkennus; #0 ei muutosta, 1 kallioperän läheisyys, kivisyys, 2 soistuneisuus, vetisyys, 3 kunttaisuus, 4 sijainti, 5 Muu ominaisuus, 6 luonnontil. suon tai ojikon veroluokan nosto, 7 muuttuma suo veroluokan vastaavuus
orgkerroslaatu; #0 hyvin ohut <1cm, 1 kangashumus, 2 mullas, 3 multa, 4 turve, 5 kangashumus turvekerroksen pinnassa, 6 turvemulta
orgkerrospaksuus; #cm, tarkkuus 1cm paitsi kun >30cm niin 5cm
maalaji; #0 orgaaninen, 1 kallio, 2 kivikko,louhikko, 3 moreeni, 4 lajittunut	
raekoko; #0 orgaaninen,kallio,kivikko, 1 hieno, 2 keskikarkea, 3 karkea
maaperanpaksuus; # 1 <10cm, 210-30cm, 3 >30cm
jaksoja; # 0 eri-ikäisrakenteinen, 1 yksijaksoinen, 2 kaksijaksoinen, 3 kolmijaksoinen
kehitysluokka; #vallitsevan jakson kehitysluokka 1 aukea uudistusala, 2 pieni taimikko, 3 varttunut taimikko, 4 nuori kasv. metsikkö, 5 vart. kasvatusmetsikkö
vallitsevapl; #0 puuton, 1 mänty, 2 kuusi, 3 rauduskoivu, 4 hieskoivu, 5 haapa, 6 tervaleppä, 8 pihlaja, 9 raita, A1-A0 havupuulajeja (kts. opas), B1-B0 lehtipuulajeja
ppa; #m2 ha-1
runkoluku; #ha-1
keskilpm; #cm
keskipituus; #dm
rinnankorkeusika;	#vuotta
alikasvoskehitysluokka; 
alikasvospl;	
alikasvosppa;
ylispuutkehitysluokka; 
ylispuutpl;
ylispuutppa;
maanpinnankasittely; #0 ei toimenpiteitä, 1 äestys, 2 laikutus, 3 auraus, säätöauraus, 4 mätästys, 5 ojitusmätästys, 6 kulotus
viljely; #0 ei tehty, 
muutoimenpide;
maanpinnankasittelyehdotus;
maanpinnankasittelyaika;
viljelyaika;
muutoimenpideaikainvtun;

