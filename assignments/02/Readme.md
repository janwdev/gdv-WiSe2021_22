# Gruppe 1 - Lara Franke und Jannik Weisser - Object counting
## Kurze Erklärung
In mehreren Bildern soll in vielen bunten Kaugummikugeln die Anzahl der Kugeln nach Farben getrennt festgestellt werden.\
Das Programm wurde im Kurs Grafische Datenverarbeitung an der Hochschule Furtwangen in Medieninformatik Semester 4 erzeugt.

## Benötigte Ressourcen
Es wurde Python 3.9.7 verwendet mit den Modulen (über pip nachinstallieren) OpenCV (Version 4.5.3). Das Programm wurde auf Windows getestet.

## Code Erklärung
Zuerst werden benötigte Module importiert und wichtige Variablen wie z.B. Farbwerte und richtige Anzahl der Kaugummikugeln definiert. Es folgen mehrere Funktionen für morphologische Operationen.
\
\
Nach Konvertierung des Bildes in den HSV-Farbraum wird eine Maske erstellt, damit das Bild nur noch Bereiche enthält, in welchen die Farbwerte in unserem definierten Bereich der jeweiligen Farbe liegt.\
Diese Maske wird je nach Farbe über verschiedene Morphologische Operationen angepasst, sodass danach nur noch Kugeln der Farbe im Bild zu sehen sind. Dann werden zu kleine Kugeln aussortiert und gefundene Kugeln in der richtigen Farbe gezählt. Die Ergebnisse der Zählung und die resultierenden Bilder werden anschließend ausgegeben.
\
\
Das Ganze wiederholt sich für alle definierten Farben und alle Bilder die im richtigen Ordner mit dem richtigen Namensschema liegen.