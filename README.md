# Series_prediction_via_RNN
Showcase my progress on developing an RNN. <br/>
A célom, hogy bemutassam az előrehaladásomat egy RNN alapú teszthálózat fejlesztésével.<br/>
Feladatom egy olyan rendszer megvalósítása, amely időben folyamatosan érkező adatok alapján predikciót tud hozni objektumok következő állapotáról. <br/>
Ez egy prototípus, melyben tesztelem az RNN nyújtotta lehetőségeket és kutatom az esetlegesen felmerülő nehézségeket egy egyszerű problémán keresztül. <br/>

## Prototípus feladata
<br/>
A prototípus feladata a következő: adott egy fix méretű adatkészlet( helyzetemben ez az első 10 pozitív egész szám), ezeket input formájában képes legyen feldolgozni. Az említett adatkészletre a továbbiakban mint egy számtani sorozatként tekintek.Belátható, hogy a szomszédos elemei közti külömbség állandó és az 1. <br/>
A prototípus sikeres, ha képes megtanulni ezt az egyszerű összefüggést és ha ez alapján képes valós, alapozott predikciót hozni.<br/>

## Program futtatása
<br/>
A program futtatásához szükség van a PyTorch(1.8.1) <br/>
A program a forrásmappából a python rnn.py parancsal futtatható. Meghívás után az expected_outcome.txt-hez hasonló kimenetre lehet számítani. <br/>

## Eredmények
<br/>
Az elfogadott felparaméterezés után a rendszer képes volt feldolgozni az adott inputokat és azokra egy azonos méretű outputtal válaszolni.<br/>
<br/>
![alt text](https://github.com/RichardVas/Series_prediction_via_RNN/blob/main/Pictures/newinputseq.png)
<br/>
Az eredmény a következő: A rendszer képes volt megtanulni az adott számtani sorozatot és a közte lévő összefüggéseket. A tanulás jelen esetben 3500 epochon át zajlott.<br/>
A tesztelésre meghívtam 4 példa predikciót. Látható, hogy képes folytatni a bemenet ként adott sorozatot és hogy minnél hoszabb a sorozat, annál biztosabb a predikcióban, de szinte mindig eredményre jut. <br/>
<br/>
![alt text](https://github.com/RichardVas/Series_prediction_via_RNN/blob/main/Pictures/expected_output.png)
<br/>

## Jövőbeli fejlesztések
<br/>
A hálózat protípusa sikeresen képes volt teljesíteni az általam elvárt követelményeket és tudta folytatni az adott sorozatot.<br/>
A jövőben tervem továbbfejleszteni jelenlegi hálózatomat, leginkább az alábbi pontok szerint.<br/>

⋅⋅* Képes legyen nagyobb dimenzióból is adatot fogadni.( leginkább 2D-s vektorokat)<br/>
⋅⋅* Nagyobb adatkészletét és komplexebb összefüggések megtanítása.<br/>
⋅⋅* Szélesebb körű, rugalmasabb felhasználás.<br/>
⋅⋅* A hálózat jelen konfigurációja nem feltétlenül pontos, a szükséges dimenzionalitások lepontosítása muszáj.<br/>
