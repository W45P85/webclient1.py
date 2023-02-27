# Entgegen der Datei "webserver.py" spricht hier ein Client mit dem Server.

import socket

# erstellt den Socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# verbindet sich mit Server 'localhost'
mysock.connect (('127.0.0.1'. 9000))
# holt sich den Inhalt der .txt Datei und codiert es in UTF-8
cmd = 'GET http://127.0.0.1/daniel.txt HTTP/1.0\r\n\r\n'.encode()
# sendet den GET-Befehl ab
mysock.send(cmd)

while True:
'''Wartet bis 512 Zeichen vorhanden sind und gibt diese Daten decodiert aus.
   Wenn keine Daten ankommen (if len(data) < 1:), wird die Verbindung beendet (break).'''
    data = mysock.recv(512)
    if len(data) < 1:
        break
    print(data.decpde(),end='')

mysock.clode()
