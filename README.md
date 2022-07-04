# SOLO_Head

## Assembly
![Solo_Head](https://user-images.githubusercontent.com/103576080/177130169-ec60ade3-e996-42d8-83a8-933b70f49e77.png)
<br>*Note : Equations can be used to re-size head diameter*

## Design Parts
| CAO | Print | Printing time | Name | Filament | Comment |
|:---:|:---:|---|---|---|---|
| <img src="https://user-images.githubusercontent.com/103576080/176712337-fcb16b7f-a679-4884-b101-5c17ccfe98c8.png" width="200"/> | <img src="https://user-images.githubusercontent.com/103576080/176708058-78d85a6b-77ac-4116-9104-041864b73865.png" width="200"/> | 9h | 1x Head_Top | ABS | 45° touching buildplate supports required (use soluble supports is better) |
| <img src="https://user-images.githubusercontent.com/103576080/176717110-486d1c79-e799-49ab-8438-1ed3e9d7ffc5.png" width="200"/> | | 1min | 1x Head_Joint | Neoprene | made with laser cutter machine |
| <img src="https://user-images.githubusercontent.com/103576080/176862314-a833ad4c-af54-49c5-833c-99272ebb91ee.png" width="150"/> |<img src="https://user-images.githubusercontent.com/103576080/176862075-79e57878-b72c-42bb-916f-0094aff5a8ef.png" width="200"/>| 33min | 2x Microphone_Joint | TPU | 45° touching buildplate supports required (use soluble supports is better) |
| <img src="https://user-images.githubusercontent.com/103576080/176794802-b4d78cac-36d5-4579-a634-85427f4a29db.png" width="100"/> |<img src="https://user-images.githubusercontent.com/103576080/176850083-c576f7ef-48a2-48c7-a86a-bb910d2cc6de.png" width="200"/>| 20min | 4x Camera_Spacer<br>4x CM4_Spacer<br>8x uDriver_Spacer | ABS | No support required |
| <img src="https://user-images.githubusercontent.com/103576080/176742165-355aa1c5-2903-4ab0-89ef-77ffb168ea4a.png" width="200"/> | <img src="https://user-images.githubusercontent.com/103576080/176703383-627a1979-0aec-4796-b0b4-fb14f6463fc0.png" width="200"/> | 1h | 1x Board_Mount | ABS | No support required |
| <img src="https://user-images.githubusercontent.com/103576080/176709893-309469c7-8986-41b5-afde-0cdcb62d7fd7.png" width="40"/> | <img src="https://user-images.githubusercontent.com/103576080/176702390-0295096c-01e5-4dd1-8b9a-963381cfda66.png" width="200"/> | 10min | 1x Bearing_Locker | ABS | No support required |
| <img src="https://user-images.githubusercontent.com/103576080/177129301-58c5812a-bb35-498d-a1b7-18fe4050c6b5.png" width="120"/> | <img src="https://user-images.githubusercontent.com/103576080/177128546-d958930a-cb48-499c-8c96-3749d15eda0e.png" width="200"/>| 1h30 | 1x Encoder_Mount | ABS | No support required |
| <img src="https://user-images.githubusercontent.com/103576080/176708863-d3c989e0-e09b-4818-8285-16885a192a5f.png" height="70"/> | <img src="https://user-images.githubusercontent.com/103576080/176705812-a7254afc-4872-4458-ac21-198efc808fad.png" width="200"/> | 20min | 1x Encoder_Adaptator | ABS | No support required |
| <img src="https://user-images.githubusercontent.com/103576080/176712137-3ec55f86-b181-4a0f-926b-d82970593bb2.png" width="200"/> | <img src="https://user-images.githubusercontent.com/103576080/176711980-e22a1324-28d7-4df3-b85b-4aada3c72269.png" width="200"/> | 12h | 1x Head_Bottom | ABS | 45° touching buildplate supports required (use soluble supports is better) |
| <img src="https://user-images.githubusercontent.com/103576080/176712526-d6b4ff95-5b67-4812-afbc-280ccc3a95df.png" width="100"/> |<img src="https://user-images.githubusercontent.com/103576080/176718247-713f9b9c-eabd-4451-8c09-0b96006b3957.png" width="200"/>| 4h | 1x Head_Stand | ABS | No support required but print with soluble support is better |

## Generic Parts
| Screen | Reference | Link | Comment |
|:---:|---|---|---|
|<img src="https://user-images.githubusercontent.com/103576080/176797844-579fc894-cfb2-416d-bed2-819796a76146.png" width="100"/>|1x 6700-2RS ball bearing<br>Ø10xØ15x4mm|[123Roulement](https://www.123roulement.com/roulements-6700-2RS)|To link "Encoder_Mount" and "Encoder_Adaptator" design parts|
|<img src="https://user-images.githubusercontent.com/103576080/176797794-832c3a0f-43eb-40b4-b760-5a3c4f113e31.png" width="100"/>|8x TCHC M3x8 Screw|[Fixnvis](https://www.visseriefixations.fr/vis-a-six-pans-creux/tete-fraisee-hexagonale-creuse/inox-a4/tfhc-m3x8-inox-a4-ef-din-7991.html)|To link "Encoder_Mount" design part and the motor<br>To link "Encoder_Mount" and "Head_Bottom" design parts|
|<img src="https://user-images.githubusercontent.com/103576080/176797794-832c3a0f-43eb-40b4-b760-5a3c4f113e31.png" width="100"/>|4x TCHC M2.5x20 Screw|[Fixnvis](https://www.visseriefixations.fr/vis-a-six-pans-creux/tete-fraisee-hexagonale-creuse/inox-a4/tfhc-m2-5x20-inox-a4-din-7991.html)|To link "Board_Mount" with spacers and "Head_Bottom" design parts|
|<img src="https://user-images.githubusercontent.com/103576080/176798233-37725fd9-e9ad-492d-8506-0c2bc137f227.png" width="100"/>|1x AEDB-9140-A13 Broadcom Encoder|[RS](https://fr.rs-online.com/web/p/codeurs/7967806?cm_mmc=FR-PLA-DS3A-_-google-_-CSS_FR_FR_Automatisme_et_Controle_de_process_Whoop-_-(FR:Whoop!)+Codeurs-_-7967806&matchtype=&pla-371581285844&gclid=Cj0KCQjw4uaUBhC8ARIsANUuDjVO7Ht5YMR8SH6bczQU4esH6yAVaWhDGcGdfncjnVxadasoeFgfhUsaAsJuEALw_wcB&gclsrc=aw.ds)|/|
|<img src="https://user-images.githubusercontent.com/103576080/176798359-a442bc4f-9284-4650-9544-f3f09320328b.png" width="100"/>|1x GB4106 Tmotor motor|[Hexadrone](https://hexadrone.fr/gamme-gimbal-nacelle/509-moteur-brushless-nacelle-gb4106-tmotor-6971360351184.html)|/|
|<img src="https://user-images.githubusercontent.com/103576080/176842784-77394364-5e0e-40f2-8b64-3c60082c9e68.png" width="100"/>|1x Arducam 2MP Global Shutter OG02B10 Pivariety camera module |[Robotshop](https://www.robotshop.com/be/fr/module-camera-couleur-arducam-2mp-global-shutter-og02b10-pivariety.html)|/|
|<img src="https://user-images.githubusercontent.com/103576080/176843317-37360fd4-4d6f-4b6d-a5e9-b13ddcd80681.png" width="100"/>|1x ArduCam M12 camera lens (6pcs)|[Robotshop](https://www.robotshop.com/be/fr/kit-objectif-arducam-m12-pour-camera-hq-20-180deg-6pcs.html)|/|
|<img src="https://user-images.githubusercontent.com/103576080/176843642-893fac68-a70e-4d11-ba58-e1c68d599df5.png" width="100"/>|1x CM4 Raspberry Pi|[Kubii](https://www.kubii.fr/cartes-raspberry-pi/3086-raspberry-pi-compute-module-4-3272496302952.html)|/|
|<img src="https://user-images.githubusercontent.com/103576080/176862778-0e5930e9-1529-4630-b24c-e529fa6d2c24.png" width="100"/>|2x Microphone module|/|Electronic CAD are in the repository "hardware"|
|<img src="https://user-images.githubusercontent.com/103576080/176845495-7ff0f7b5-cc67-4a1c-92a4-e13cbe0bf7dc.png" width="100"/>|2x uDriver board||[ODRI repository](https://github.com/open-dynamic-robot-initiative/open_robot_actuator_hardware/blob/master/electronics/micro_driver_electronics/README.md#micro-driver-electronics)|
|<img src="https://user-images.githubusercontent.com/103576080/176851398-2c1e4fcf-01f7-4eec-a24b-85888b4bb1b5.png" width="100"/>|2x DF13-5S-1.25C Hirose connector|[RS components](https://fr.rs-online.com/web/p/boitiers-de-connecteurs-pour-circuits-imprimes/1113616)|To link uDriver and communication cables<br>To link CM4 Raspberry Pi and communication cables|
|<img src="https://user-images.githubusercontent.com/103576080/176852740-7b08fb74-c656-4ad4-bb7a-515ca463866d.png" width="100"/>|1x DF13-5P-1.25DS Hirose connector|[RS components](https://fr.rs-online.com/web/p/embases-circuits-imprimes/7793529)|To change encoder connector|
|<img src="https://user-images.githubusercontent.com/103576080/176853572-a5cc0f6f-79e0-48ae-bf69-0302304ad2c6.png" width="100"/>|1x RE-6619107 XT30U 2 mm Reely Male  connector|[Conrad](https://www.conrad.fr/p/reely-re-6619107-fiche-male-pour-batterie-xt30u-2-mm-femelle-doree-a-souder-1-pcs-2206369)|To link power cables to uDriver board|
|<img src="https://user-images.githubusercontent.com/103576080/176853753-42e9bae6-4886-4f0d-b6ce-645b94257f55.png" width="100"/>|1x RE-6619104 XT30U 2 mm Reely Female connector|[Conrad](https://www.conrad.fr/p/reely-re-6619107-fiche-male-pour-batterie-xt30u-2-mm-femelle-doree-a-souder-1-pcs-2206369)|To link power cables to power board (on SOLO body)|
|<img src="https://user-images.githubusercontent.com/103576080/176854897-fb1fb77d-83ea-403a-90d0-83c045a15dbe.png" width="100"/>|1x Kabeltronik 160110009-1 1mm² Black Power Wire|[Conrad](https://www.conrad.com/p/kabeltronik-160110009-1-strand-lify-1-x-1-mm-black-sold-per-metre-323735)|To power uDriver board|
|<img src="https://user-images.githubusercontent.com/103576080/176855303-628d6284-1070-4019-9bbd-e4c8d97d330e.png" width="100"/>|1x Kabeltronik 160110008 1mm² Red Power Wire|[Conrad](https://www.conrad.fr/p/fil-de-cablage-lify-kabeltronik-160110008-1-1-x-1-mm-rouge-marchandise-vendue-au-metre-323734)|To power uDriver board|
|<img src="https://user-images.githubusercontent.com/103576080/176855789-f24872d6-c92a-4998-93ae-22171cd41eba.png" width="100"/>|1x 10 way 3M 3302-10 100FT communication cables |[RS components](https://fr.rs-online.com/web/p/cables-en-nappe/1055281)|To link encoder and uDriver (5 way)<br>To link CM4 Raspberry Pi and uDriver (5 way)|
|<img src="https://user-images.githubusercontent.com/103576080/176863273-ad95b7d8-0026-4dc5-9add-4440e668f190.png" width="100"/>|1x DF13-2630SCF 0.12mm² Hirose DF13 Crimp Terminals|[RS components](https://fr.rs-online.com/web/p/cables-en-nappe/1055281)|To link communication cables with DF13-5S-1.25C Hirose connector|
|<img src="https://user-images.githubusercontent.com/103576080/176864595-ea0badd4-c492-4d3d-a5d5-04556ce603c5.png" width="100"/>|1x DF13-TB2630HC Hirose Crimping Tool for DF13 Crimp Terminals |[RS components](https://fr.rs-online.com/web/p/cables-en-nappe/1055281)|To link communication cables with DF13-5S-1.25C Hirose connector|

## Next Version (V7)
To reduce mass, clean print, and keep design apparence. I realize some modifications on the V6 design :
* Delete "Head_Joint" neoprene gasket and chamfer "Head_Bottom" and "Head_Top" parts to simplify the model and clean model surface.
* Design a new "Head_Stand" to link the SOLO's head to SOLO's body.
* Delete "Microphone_Joint" and integrate a screwing system on "Head_Bottom" to simplify the model. To limit microphone noise, generic O-rings are positioned on the screw.
* Upgrade clips shape to limit printing supports.

## Links
[Light BLDC Motor](https://github.com/acromtech/Light_BLDC_motor)<br>
[Light BLDC Driver](https://github.com/acromtech/Light-BLDC-controller)
