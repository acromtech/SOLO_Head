# SOLO_Head

## Assembly
![Solo_Head](https://user-images.githubusercontent.com/103576080/176720313-73ced302-63ae-458b-936b-b461d0995bb6.png)

## Design Parts
| CAO | Print | Printing time | Name | Filament | Comment |
|:---:|:---:|---|---|---|---|
| <img src="https://user-images.githubusercontent.com/103576080/176712337-fcb16b7f-a679-4884-b101-5c17ccfe98c8.png" width="200"/> | <img src="https://user-images.githubusercontent.com/103576080/176708058-78d85a6b-77ac-4116-9104-041864b73865.png" width="200"/> | 9h | 1x Head_Top | ABS | 45° touching buildplate supports required (use soluble supports is better) |
| <img src="https://user-images.githubusercontent.com/103576080/176717110-486d1c79-e799-49ab-8438-1ed3e9d7ffc5.png" width="200"/> | | 1min | 1x Head_Joint | Neoprene | made with laser cutter machine |
| <img src="https://user-images.githubusercontent.com/103576080/176794802-b4d78cac-36d5-4579-a634-85427f4a29db.png" width="100"/> |<img src="" width="200"/>| ?min | 4x Camera_Spacer<br>4x CM4_Spacer<br>8x uDriver_Spacer | ABS | No support required |
| <img src="https://user-images.githubusercontent.com/103576080/176742165-355aa1c5-2903-4ab0-89ef-77ffb168ea4a.png" width="200"/> | <img src="https://user-images.githubusercontent.com/103576080/176703383-627a1979-0aec-4796-b0b4-fb14f6463fc0.png" width="200"/> | 1h | 1x Board_Mount | ABS | No support required |
| <img src="https://user-images.githubusercontent.com/103576080/176709893-309469c7-8986-41b5-afde-0cdcb62d7fd7.png" width="40"/> | <img src="https://user-images.githubusercontent.com/103576080/176702390-0295096c-01e5-4dd1-8b9a-963381cfda66.png" width="200"/> | 10min | 1x Bearing_Locker | ABS | No support required |
| <img src="https://user-images.githubusercontent.com/103576080/176714035-dad566cd-3d05-4768-a218-9158a1a16e61.png" width="200"/> | <img src="https://user-images.githubusercontent.com/103576080/176714904-20c3242e-bcdb-4bec-a5be-8248f9b6c007.png" width="200"/>| 2h | 1x Encoder_Mount | ABS | 45° touching buildplate supports required (use soluble supports is better) |
| <img src="https://user-images.githubusercontent.com/103576080/176708863-d3c989e0-e09b-4818-8285-16885a192a5f.png" height="70"/> | <img src="https://user-images.githubusercontent.com/103576080/176705812-a7254afc-4872-4458-ac21-198efc808fad.png" width="200"/> | 20min | 1x Encoder_Adaptator | ABS | No support required |
| <img src="https://user-images.githubusercontent.com/103576080/176712137-3ec55f86-b181-4a0f-926b-d82970593bb2.png" width="200"/> | <img src="https://user-images.githubusercontent.com/103576080/176711980-e22a1324-28d7-4df3-b85b-4aada3c72269.png" width="200"/> | 12h | 1x Head_Bottom | ABS | 45° touching buildplate supports required (use soluble supports is better) |
| <img src="https://user-images.githubusercontent.com/103576080/176712526-d6b4ff95-5b67-4812-afbc-280ccc3a95df.png" width="100"/> |<img src="https://user-images.githubusercontent.com/103576080/176718247-713f9b9c-eabd-4451-8c09-0b96006b3957.png" width="200"/>| ?min | 1x Head_Stand | ABS | No support required but print with soluble support is better |

Manque :
* Joint TPU oreilles (Cura + CAO)
* Entretoise Cura
* Temps Hand_Stand

## Generic Parts
| Screen | Reference | Link | Comment |
|:---:|---|---|---|
|<img src="https://user-images.githubusercontent.com/103576080/176797844-579fc894-cfb2-416d-bed2-819796a76146.png" width="100"/>|1x 6700-2RS ball bearing<br>Ø10xØ15x4mm|[123Roulement](https://www.123roulement.com/roulements-6700-2RS)|To link "Encoder_Mount" and "Encoder_Adaptator" design parts|
|<img src="https://user-images.githubusercontent.com/103576080/176797794-832c3a0f-43eb-40b4-b760-5a3c4f113e31.png" width="100"/>|8x TCHC M3x8 Screw|[Fixnvis](https://www.visseriefixations.fr/vis-a-six-pans-creux/tete-fraisee-hexagonale-creuse/inox-a4/tfhc-m3x8-inox-a4-ef-din-7991.html)|To link "Encoder_Mount" design part and the motor<br>To link "Encoder_Mount" and "Head_Bottom" design parts|
|<img src="https://user-images.githubusercontent.com/103576080/176797794-832c3a0f-43eb-40b4-b760-5a3c4f113e31.png" width="100"/>|4x TCHC M2.5x20 Screw|[Fixnvis](https://www.visseriefixations.fr/vis-a-six-pans-creux/tete-fraisee-hexagonale-creuse/inox-a4/tfhc-m2-5x20-inox-a4-din-7991.html)|To link "Board_Mount" with spacers and "Head_Bottom" design parts|
|<img src="https://user-images.githubusercontent.com/103576080/176798233-37725fd9-e9ad-492d-8506-0c2bc137f227.png" width="100"/>|1x AEDB-9140-A13 Broadcom Encoder|[RS](https://fr.rs-online.com/web/p/codeurs/7967806?cm_mmc=FR-PLA-DS3A-_-google-_-CSS_FR_FR_Automatisme_et_Controle_de_process_Whoop-_-(FR:Whoop!)+Codeurs-_-7967806&matchtype=&pla-371581285844&gclid=Cj0KCQjw4uaUBhC8ARIsANUuDjVO7Ht5YMR8SH6bczQU4esH6yAVaWhDGcGdfncjnVxadasoeFgfhUsaAsJuEALw_wcB&gclsrc=aw.ds)|/|
|<img src="https://user-images.githubusercontent.com/103576080/176798359-a442bc4f-9284-4650-9544-f3f09320328b.png" width="100"/>|1x GB4106 Tmotor motor|[Hexadrone](https://hexadrone.fr/gamme-gimbal-nacelle/509-moteur-brushless-nacelle-gb4106-tmotor-6971360351184.html)|/|

* Module camera
* Raspberry PI CM4
* Microphones LAAS
* uDriver LAAS

## Wires
* 1x Female/Male DF13 cable extension
* 1x Female/Male power cable extension

## Next Version
In the next version i should try to reduce mass of components. To
Pour être plus léger et garantir un aspet propre et esthétique il faut :
* suprimmer le joint néoprène : récupère le son + dur a metre en place pour peu d'ajout
* refaire un pied pour l'adapter au corps de SOLO
* trouver une idée pour intégrer les microphones de manière "design" et peu couteuse (vis + joint torique  le reste de la matière directement sur la tête de solo par exemple)
* clips rond pour simplifier l'impression
* moteur GB2208 ?
* Faire des entretoise intégrés dans la CAO Head_Top
