# Folder-Analyzer

Hallo Karsten,

hier einmal der Code für die Aufgabe.

Das tool kannst Du benutzen, indem Du der iterate_folder() function in folder_analyzer den Pfad zu dem Ordner gibst, den Du analysieren möchtest.
Das ganze liefert dann basierend auf der Struktur, die Du mir geschickt hattest, ein Dictionary mit den Keys passend zu den verschiedenen Klassentypen, deren Values jeweils eine Liste aus Instanzen der jeweiligen Klassen sind. 
Ich dachte mir, dass das praktisch wäre, wenn es mehrere Ordner gibt, die USD files der gleichen Klasse besitzen.

Um zum Beispiel die manifest() Methode bei einer StichClip instanz zu benutzen, hätte ich das so geschrieben: 

dict = iterate_folder(folder_path)
print(dict["StichClip"][0].manifest())

Liebe Grüße,

Robin :)
