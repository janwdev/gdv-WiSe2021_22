# Gruppe 1 - Lara Franke und Jannik Weisser - Hybrid Imaging
## Kurze Erklärung
Zwei Bilder sollen so kombiniert werden, dass ein Hybridbild entsteht. Dabei werden 3 entsprechende Punkte händisch übereinandergemorpht, dass sie einander entsprechen. Dann werden aus einem Bild die tiefen und aus einem die hohen Frequenzen genommen und diese kombiniert, so dass bei Betrachtung von weit weg (kleines Bild) etwas anderes zu sehen ist, als bei Betrachtung von nahem.

## Benötigte Ressourcen
Es wurde Python 3.9.7 verwendet mit den Modulen (über pip nachinstallieren) OpenCV (Version 4.5.3). Das Programm wurde auf Windows (10.0.19043) getestet.

## Code Erklärung
Zuerst werden benötigte Module importiert und Variablen initialisiert. Dann folgen mehrere Funktion für Oberflächeninteraktionen und um Frequenzen aus dem Bild zu extrahieren.
 \
Es werden die Bilder geladen, angezeigt und weitere Variablen für die Oberfläche initialisiert. \
 \
In einer Schleife wird nun geprüft, ob auf den Ursprungsbildern jeweils 3 Punkte, welche auf den Bildern übereinandergelegt werden sollen, geklickt wurden. Ist das der Fall, werden die Bilder entsprechend übereinandergelegt und ein Hybridbild erzeugt, welches mit verschiedenen Reglern weiter angepasst werden kann. Damit der Effekt besser sichtbar wird, wird das Hybridbild zusätzlich in sehr klein und sehr groß angezeigt. Zwischenschritte sind hierbei die Erstellung eines Low- sowie High-Frequency Bildes. Alle Bilder werden angezeigt.