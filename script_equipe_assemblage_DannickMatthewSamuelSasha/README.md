# Instruction
---
## Script_Flask.py
1. Naviguer dans le dossier en question :
``` cd ~monprojet ```

2. Ouvrire une environnement de travail:
``` srouce env/bin/activate ```

3. Ouvrire le serveur Flask
``` python3 ~Script_Flask.py ```

4. Allez dans le naviguater :
``` http://0.0.0.0:5000/{#moteur}/{#angle}```
"route" : la méthode que l'ont veut ouvrire dans le script pyton.

#### Exemple : 
 ```
# Ceci est la patern de l'URL que nous devons entrer dans l'URL du naviguateur
@app.route("/Entrer/<moteur>/<angle1>")
def une3_fonction(angle1=None, moteur=None):
	robot = ServoKit(channels=16)
  # Ici on indique quel moteur et quel angle nous voulons lui donner
	robot.servo[int(moteur)].angle = int(angle1)
	time.sleep(1)
	return render_template("index.html")
	return "string"
```

---
## Script_UtiliserTesterMoteurs.py
1. Naviguer dans le dossier en question
``` cd ~monprojet ```

2. Lancer le script
``` python3 Script_UtiliserTesterMoteurs.py ```

3. Entrer un angle
``` angle{#angle} ```
Il est seulement nécessaire d'entrer le chiffre

#### Exemple :
```
import time
from adafruit_servokit import ServoKit

inMoov = ServoKit(channels=16)

inMoov.servo[3].actuation_range = 180
inMoov.servo[3].set_pulse_width_range(556,2420)

# Ceci affiche le texte d'entrer
angDepart = int(input("angle"))
# Ceci vas chercher l'entrer par l'utilisateur et fait bouger le moteur a l'angle demandée.
inMoov.servo[3].angle = angDepart

print("connectez le servo au port 3 du module\n")

# Encienne boucle
#while True:
	#angle = int(input("angle: "))

while True:
# Ceci affiche le texte d'entrer
	ang = float(input("angle"))
  # Ceci vas chercher l'entrer par l'utilisateur et fait bouger le moteur a l'angle demandée.
	inMoov.servo[3].angle = ang
  ```
