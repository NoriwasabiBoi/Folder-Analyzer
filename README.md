# Folder-Analyzer

Hallo Karsten,

anbei findest Du den Code für die Aufgabe.

Das Tool kannst Du ganz einfach nutzen, indem Du der Funktion iterate_folder() aus folder_analyzer den Pfad zu dem Ordner übergibst, den Du analysieren möchtest.
Die Funktion liefert dann, basierend auf der Struktur, die Du mir geschickt hattest, ein Dictionary zurück. Die Keys entsprechen dabei den verschiedenen Klassentypen, und die Values sind jeweils Listen mit Instanzen der jeweiligen Klassen.
Ich fand das sinnvoll, gerade wenn es mehrere Ordner gibt, die USD-Dateien der gleichen Klasse enthalten, und die Klassen sortiert nach Typ vorliegen.

Möchtest Du beispielsweise die manifest()-Methode einer StichClip-Instanz aufrufen, kannst Du das so machen:

folder_data = iterate_folder(folder_path)
print(folder_data["StichClip"][0].manifest())

Viele Grüße
Robin :)
