# Gruppe 1  - Lara Franke und Jannik Weisser - Face Detection 
## Kurze Erklärung
In einem Video sollen Gesichter erkannt werden und mit einem Rechteck markiert werde. 

## Benötigte Ressourcen
Es wurde Python 3.9.7 verwendet mit den Modulen (über pip nachinstallieren) OpenCV (Version 4.5.3) und Numpy. Das Programm wurde auf Windows (10.0.19043) getestet.

## Code Erklärung
Zuerst werden benötigte Module importiert und Variablen initialisiert. Und das Caffemodel für 300x300 dim geladen.
/
Danach wird das Video geladen in welchem die Gesichter erkannt werden sollen. Die Ergebnisse, wie viele Gesichter in jedem Fram erkannt werden, werden dann in eine Datei gespeichert die vorher initialisiert wird.
Um zu vergleichen ob die richtige Anzahl an Gesichtern durch die KI erkannt wurden, werden die Ergebnisse verglichen und dann vom Programm ausgegeben