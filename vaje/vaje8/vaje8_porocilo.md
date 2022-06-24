# Vaje 8

**Ime:** Tomaž Tratnik
**Datum:** 7.4.2022

# Uvod
Na vajah smo reševali naloge na tablo in odgovarjali na vprašanja zastavljena na spletni učilnici.

# Vprašanja

**Ponovitev Primovega algoritma (vhod, izhod, ideja algoritma, časovna zahtevnost)**
Vhod Primovega algoritma je obtežen graf. Izhod je vpeto poddrevo grafa, katerega vsota povezav je minimalna (poveže vsa vozlišča z n-1 povezavami). Ideja: na začetku izberemo eno vozlišče in ga dodamo v drevo. Nato ponavljamo. dokler niso vsa vozlišča v drevesu: izberemo najcenejšo povezavo robno povezavo (začne na vozlišču znotraj drevesa, konča zunaj) in jo dodamo v drevo. Časovna zahtevnost algoritma je O(|V|^2) (ali O((|V| + |E|)log|E|) z uporabo prioritetne vrste).

**Simulacija Primovega algoritma na grafu:**
![Simulacija Primovega algoritma na podanem grafu](prim.jpg)

**Pokaži, da je MVD enolično, če so vse uteži. v grafu različne. Namig: protislovje**
Recimo. da smo že poiskali eno MVD grafa. Če i želeli, da obstaja še kako, bi morali pri vsaj enem vozlišču spremeniti povezavo, ki ga povezuje z drevesom. Ta nova povezava, bi imela ceno, ki je večja ali enaka prejšnji. Ker pa so vse povezave v drevesu različne, bi bila cena nove povezave večja, zato to ne bi bilo več MVD.

**Kako bi poiskal najdražje vpeto drevo?**
V primovem algoritmu bi namesto najmanjše ihodne povezave iskali največjo izhodno povezavo.

**Naj bo T MVD in T' drevo najkrajših razdalj od vozlišča s do vseh ostalih. Vsaki uteži sedaj prištejemo 1. Ali se T in T' spremenita?**
T se ne bi spremenil, ker se pri iskanju najcenejše izhodne povezave ne bi nič spremenilo. T' bi se pa lahko spremenil, lahko pa tudi ne.

**Recimo, da imamo utežen graf G in njegovo MVD T (eno izmed možnih). Sedaj določeni povezavi e spremenimo utež. Opiši čim bolj učinkovit algoritem, ki popravi T.**
Če ta utež ni v MVD, ne naredimo nič. Če je znotraj grafa, bo povezovala eno vozlišče, ki je list drevesa, in njenga očeta. Preveriti moramo, ali bi lahko list povezali z drevesom s kako povezavo, ki je cenejša od trenutne spremenjene. Če lahko, jo zamenjamo z najcenejšo izmed teh.


