# Gruppe 1 - Lara Franke und Jannik Weisser - Optical Illusion
## Kurze Erklärung
Optische Illusion, bei welcher ein Gradientenbild erzeugt wird und ein Ausschnitt aus der Mitte nach links und rechts bewegt wird und scheinbar seine Farbe ändert. In Wirklichkeit ändert sich die Farbe jedoch nicht!
Das Programm wurde im Kurs Grafische Datenverarbeitung an der Hochschule Furtwangen in Medieninformatik Semester 4 erzeugt.

## Benötigte Ressourcen
Es wurde Python 3.9.7 verwendet mit den Modulen (über pip nachinstallieren) OpenCV (Version 4.5.3) und Numpy. Diese werden beim Start importiert. Das Programm wurde auf Debian (Linux) und Windows getestet.
## Code Erklärung
Nach dem import werden verschiedene Variablen wie die Bildgröße und die Größe des Ausschnitts, welcher bewegt werden soll, festgelegt. Diese können auch geändert werden. Allerdings findet keine Überprüfung der Werte statt, es sollten also sinnvolle Werte gewählt werden.

Danach wird ein Farbverlauf erstellt und den zu bewegenden Zwischenteil aus der Mitte des Bildes geladen.
Das Fenster zum Anzeigen wird erstellt und andere Variablen, welche zur Animation (Position, Right) und zum Erstellen des Videos gebraucht werden, initialisiert.

In einer Schleife (das Programm kann mit q beendet werden) wird der Ausschnitt aus der Mitte nach Rechts und Links bewegt. Ebenfalls wird in den Ecken oben der Ausschnitt aus der Mitte angezeigt, um die Illusion dauerhaft zu sehen. Nach dem ersten Durchlauf (Hin und Zurück) wird ein Video aus den bisherigen Bildern gespeichert.
Wenn der Ausschnitt aus der Mitte am Rand (einer Grenze: Border) angekommen ist, dreht er die Richtung automatisch um.