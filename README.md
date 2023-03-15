# Feeder Backend

## In a Nutshell
"Feeder" is a webapplication that allows users to post, edit, and delete feeds. The app also offers the ability to post, edit, and delete comments on the feeds. With Feeder, users can share their thoughts and opinions, receive feedback from other users, and connect with others. The user interface is user-friendly and easy to navigate.

## Technologies
### Django
"Feeder" was developed using the Django technology. Django is a popular web framework that is widely used for building high-quality web applications quickly and efficiently. It provides a powerful and secure infrastructure for developing complex applications, and it is known for its scalability and flexibility. With Django, developers can easily create web applications with clean and maintainable code, making it a popular choice for building web applications. The use of Django in the development of "Feeder" ensures that the app is reliable, secure, and easy to maintain.


## Permissions
**Anonym User**
- No Permission

**Default User**
- Can read other feeds
- Can create Feeds
- Can update and delete own Feeds
- Can create Commentaries
- Can update and delete own Commentaries

**Verified User**
- All Default User Permissions
- Can create Feeds + can use more than 200 characters
- Can create Commentaries + can use more than 200 characters

**Moderator**
- All Verified User Permissions
- Can update and delete other Feeds
- Can update and delete other Commentaries
- Can warn verified and default users

**Admin**
- All Moderator Permissions
- Can verify and unverify other users
- Can give and remove moderator role to other users

## Setup
### Python
1. Besuche die offizielle Python-Website: https://www.python.org/downloads/
2. Scrolle nach unten zur "Stable Releases" Sektion und wähle die neueste Version von Python3 aus, die für dein Betriebssystem verfügbar ist.
3. Klicke auf den entsprechenden Download-Link, um das Installationspaket herunterzuladen.
4. Öffne das heruntergeladene Installationspaket.
5. Wähle die Option "Install Python 3.x" aus und klicke auf "Weiter".
6. Wähle das Zielverzeichnis für die Installation aus (der Standardpfad sollte in Ordnung sein) und klicke auf "Weiter".
7. Wähle die Komponenten aus, die du installieren möchtest. Für den Anfang empfehlen wir, alle Optionen auszuwählen. Klicke auf "Weiter".
8. Wähle "Add Python 3.x to PATH" aus und klicke auf "Installieren". Diese Option fügt Python zum Pfad hinzu, sodass du Python von der Befehlszeile aus aufrufen kannst.
9. Warte, bis die Installation abgeschlossen ist.
10. Überprüfe, ob Python korrekt installiert wurde, indem du die Eingabeaufforderung öffnest und den Befehl "python --version" eingibst. Die aktuelle Version von Python, die du installiert hast, sollte angezeigt werden.
Herzlichen Glückwunsch! Du hast Python3 erfolgreich auf deinem Computer installiert. Nun bist du bereit, Python-Programme zu schreiben und auszuführen.
