Samuli Launiainen 30.8.2016


Tiedostot vmi11.csv ja vmi12.csv (pilkkueroteltu) sis�lt�v�t seuraavat poimitut muuttujat VMI-maastotiedoston kuviotietueesta:


Katso folderissa olevat .sas-koodit joita k�y ilmi muuttujanimi-sar. vastaavuus VMI-tietueessa, kts. Arton pdf-tietuekuvaukset.

Muuttujien tulkinta (==selkokielistys) pit�� tehd� VMI12-maasto-oppaan mukaan.


invtun;
lohy-lohx;
koeala;
kuvio;
kunta; #MML kuntakoodi
koealankorkeus; #dm, a.sl.
lamposumma; #dd degC
framaa; # 1 forest, 2 other wooded land, 3 other land, 4 other land with tree cover
maaluokka; #1 mets�maa, 2 kitumaa, 3 joutomaa, 4 muu mets�talousmaa, 5 maatalousmaa, 6 rakennettu maa, 7 liikennev�yl�t, 8 voimansiirtolinjat, A sis�vesi B merivesi C koealaan kuulumaton kuvio
entinenmaaluokka;
paatyyppi; 1 kangas, 2 korpi, 3 r�me, 4 avosuo
kasvupaikkat; # 1 lehdot, 2 lehtomaiset kankaat, 3 tuoreet kankaat, 4 kuivahkot kankaat, 5 kuivat kankaat, 6 karukkomaat, 7 kalliomaat, 8 lakimets�t, T tunturikoivikot, A avotunturit
kasvuplisa; # 0 ei lis�m��rett�, 1 ohutturpeisuus, 2 talvikkityypin kangas
suotyy; #AIDOT TYYPIT: 1 lehtokorpi, 2 ruohokorpi, 3 kangaskorpi, 4 mustikkakorpi, 5 puolukkakorpi, 6 pallosarakorpi, 7 korpir�me, 8 pallosarar�me, 9 kangasr�me, 10 isovarpur�me, 11 rahkar�me, 
		#SEKATYYPIT: 12 vars. lettokorpi, 13 koivulettokorpi, 14 ruoh. sarakorpi
		#15 vars. sarakorpi, 16 vars. lettor�me, 17 ruoh sarar�me, 18 vars. sarar�me, 19 tupasvillasarar�me, 20 lyhytkorsir�me, 21 tupasvillar�me, 22 keidasr�me
		#AVOSUOT: 23 vars. letto, 24 rimpiletto, 25 ruoh. saraneva, 26 ruoh. rimpineva, 27 vars. saraneva, 28 vars. rimpineva, 29 lyhytkorsikalvakkaneva, 30 lyhytkorsineva, 31 rahkaneva
turvekangas; # 1 ruohoturvekangas RhTg, 2 mustikkaturvekangas I MtKg(I), 3 mustikkaturvekangas II MtKg(II), 4 puolukkaturvekangas PtKg(I), 5 puolukkaturvekangas PtKg(II), 6 varputurvekangas Vatkg, 7 j�k�l�turvekangas J�tkg
ojitustilanne; # 0 ojittamaton kangas tai suo, 1 ojitettu kangas, 2 ojikko (ojituksen vaikutus ei havaittavissa kasvillisuudessa), 3 muuttuma (vaikutus selv�, aluskasvillisuutta leimaa alkup. suotyyppi), 4 turvekangas
tehtyojitus; # 0 ei oijitusta, 1 uudisojitus, 2 ojien perkaus, 3 t�ydennysojitus, 4 muu kuin mets�ojitus, 5 ojien tukkiminen
ojitusaika; #- ei toimenpiteit�, 1 arviointivuonna, 1 -1v, 2 -2v, 3 - 3v ... 50 -50v tai enemm�n
ojitustarve; #0 ei ehdotusta, 1 uudisojitus, 2 ojien perkaus, 3 t�ydennysojitus
ojienkunto; # - ojittamaton, 1 hyv�, 2 tyydytt�v�, 3 v�ltt�v�, 4 huono
veroluokka; #0 IA lehto ja lehtomainen kangas pl. talvikkityyppi, 1 IB tuore kangas ja lehtomainen talvikkityyppi, 2 II kuivahko kangas ja kunttaantunut puolukka-mustikkatyyppi, 3 III kuiva ja karukkokangas, 
				kunttaantunut paksusammal, luonnont. korpi, 4 IV mets�maan luonnontil. r�me tai korpi
veroluokkatarkennus; #0 ei muutosta, 1 kallioper�n l�heisyys, kivisyys, 2 soistuneisuus, vetisyys, 3 kunttaisuus, 4 sijainti, 5 Muu ominaisuus, 6 luonnontil. suon tai ojikon veroluokan nosto, 7 muuttuma suo veroluokan vastaavuus
orgkerroslaatu; #0 hyvin ohut <1cm, 1 kangashumus, 2 mullas, 3 multa, 4 turve, 5 kangashumus turvekerroksen pinnassa, 6 turvemulta
orgkerrospaksuus; #cm, tarkkuus 1cm paitsi kun >30cm niin 5cm
maalaji; #0 orgaaninen, 1 kallio, 2 kivikko,louhikko, 3 moreeni, 4 lajittunut	
raekoko; #0 orgaaninen,kallio,kivikko, 1 hieno, 2 keskikarkea, 3 karkea
maaperanpaksuus; # 1 <10cm, 210-30cm, 3 >30cm
jaksoja; # 0 eri-ik�israkenteinen, 1 yksijaksoinen, 2 kaksijaksoinen, 3 kolmijaksoinen
kehitysluokka; #vallitsevan jakson kehitysluokka 1 aukea uudistusala, 2 pieni taimikko, 3 varttunut taimikko, 4 nuori kasv. metsikk�, 5 vart. kasvatusmetsikk�
vallitsevapl; #0 puuton, 1 m�nty, 2 kuusi, 3 rauduskoivu, 4 hieskoivu, 5 haapa, 6 tervalepp�, 8 pihlaja, 9 raita, A1-A0 havupuulajeja (kts. opas), B1-B0 lehtipuulajeja
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
maanpinnankasittely; #0 ei toimenpiteit�, 1 �estys, 2 laikutus, 3 auraus, s��t�auraus, 4 m�t�stys, 5 ojitusm�t�stys, 6 kulotus
viljely; #0 ei tehty, 
muutoimenpide;
maanpinnankasittelyehdotus;
maanpinnankasittelyaika;
viljelyaika;
muutoimenpideaikainvtun;

