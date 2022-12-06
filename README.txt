Du må installere MAMP for å kunne kjøre en lokal MySQL server (det er bare den man trenger, man trenger ikke Mac, Apache og PHP).
Man kan leste ned MAMP fra denne nettsiden (https://www.mamp.info/en/windows/).
Du må deretter gå inn på MAMP -> Preferences, og deretter velge port 3306 for MySQL (denne porten bruker jeg i programmet mitt).

NB! Kjør MAMP før du gjør steget under.
Deretter må du lage en database ved å åpne database.sql filen, fjerne kommentaren fra #CREATE DATABASE BANKSYSTEM; og kjøre filen. 
Det kan hende at du må åpne og kjøre filen i MySQL Workbench (også en app som du må laste ned). 

Deretter må du installere driveren for MySQL Connector i Python. 
Bruk denne lenken og bruk pip install kommandoen som står på nettsiden (https://www.w3schools.com/python/python_mysql_getstarted.asp).
NB! Du kommer sikkert til å ha en annen Python versjon enn den de bruker på guiden, og derfor kommer du sikkert til å ha en annen path enn den som er spesifisert i guiden.

For å kunne kjøre koden trenger du å åpne root-directoryen til all koden (det er der hovedprogrammet ligger) i for eksempel Visual Studio Code.
Dersom du ikke gjør det kan du få en feilmelding. 
Kjør hovedprogrammet. 

Dersom alt fungerer, så skal alt være fine fint og du skal ikke få feil i framtiden.