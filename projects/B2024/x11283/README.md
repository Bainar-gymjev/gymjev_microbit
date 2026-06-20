# micro:bit Věštící koule

### Autor

Jakub Muselík

### Popis

Kód promění mikropočítač micro:bit v zábavnou rozhodovací kostku, která náhodně generuje nálady. Využívá k tomu tři vestavěné grafické symboly představující veselý, smutný a neutrální obličej. Po spuštění běží program v nekonečné smyčce a neustále hlídá změnu polohy zařízení. Celý proces výběru obsahuje krátkou časovou prodlevu, která simuluje přemýšlení počítače. Výsledná nálada je pokaždé dílem náhody díky integrovanému matematickému modulu `random`.

### Ovládání

Pro spuštění funkce stačí vzít micro:bit do ruky a rázně s ním zatřást. Pohybový senzor okamžitě zaznamená otřes, smaže displej a vybere nový symbol. Obrázek zůstane svítit na LED matici až do chvíle, než s deskou zatřeseš znovu.

