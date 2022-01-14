# Gruppe 1  - Lara Franke und Jannik Weisser - Face Detection 
## Kurze Erklärung
In einem Video sollen Gesichter erkannt werden und mit einem Rechteck markiert werden. 

## Benötigte Ressourcen
Es wurde Python 3.9.7 verwendet mit den Modulen (über pip nachinstallieren) OpenCV (Version 4.5.3) und Numpy (Version 1.21.2). Das Programm wurde auf Windows (10.0.19043) getestet.

## Code Erklärung
Zuerst werden benötigte Module importiert, Variablen initialisiert und das Caffemodel geladen.
\
Danach wird das Video geladen in welchem die Gesichter erkannt werden sollen. Die Ergebnisse, wie viele Gesichter in jedem Frame erkannt werden sollen, werden aus einer vorher angelegten Datei gelesen. Diese Zahl wird mit den tatsächlich erkannten Gesichtern verglichen. Wenn das Ergebnis übereinstimmt wird die Anzahl der richtig erkannten Frames erhöht, aus welcher sich später eine Prozentzahl errechnet, wie viel Prozent der verarbeiteten Frames richtig erkannt wurden. Diese wird mit ein paar Anmerkungen in eine Datei geschrieben.
\
Um die erkannten Gesichter wird ein Rechteck mit Prozentanzahl der Wahrscheinlichkeit eines Gesichtes gezeichnet.
\
Wenn man will (Variable im Code auf True) kann man das Ergebnisvideo mit den Rechtecken um die Gesichter speichern.

## Model
In dem Programm wurde das Caffemodel verwendet. Caffe verarbeitet und speichert Daten in Blobs.