# Installation

1. Installer le driver pour permettre à la manette de communiquer avec le Pi:

   ``` sudo apt-get install xboxdrv ```

2. Installer le module pour lire les boutons de la manette:

   ```git clone https://github.com/FRC4564/Xbox```

3. Installer le module pour lire les boutons de la manette:

   ```git clone https://github.com/FRC4564/Xbox```

# Exécution

1. Ouvrir un terminal dans le fichier du projet et lancer Roscore:

   ```Roscore```

2. Ouvrir un autre terminal et lancer le listener:

   ```python listener.py```

3. Ouvrir un autre terminal et lancer le talker:

   ```python talker.py```

_Si le talker demande sudo pour trouver la manette, débranchez et rebranchez la manette et réexécutez le script_

# Instructions

Lorsque tous les scripts sont en cours d'exécution, les boutons A, X, Y ,B et RB permettent de bouger différents moteurs branchés sur les connecteurs GPIO 0 à 4 dans l'ordre énuméré. La gachette de droite permet de faire bouger les 5 moteurs en même temps. Pour bouger le moteur, il suffit d'appuyer sur l'un de 6 boutons et de bouger le stick analogique gauche vers le haut ou vers le bas. L'angle maximum est 180 degrés vers le haut et 0 vers le bas.

# Problèmes rencontrés

1. Utilisation de plusieurs versions de Python 

Le module Adafruit était seulement disponnible avec Python3 alors que Rospy utilisait Python. Nous devions donc exécuter le script du moteur avec une commande spéciale :  `subprocess.call(["sudo","python3","motor.py"])`

2. Problèmes de connexion de la manette

Le processus ne s'arrête pas par lui-même lorsque nous arrêtions notre scipt. Nous devions donc reconnecter notre manette à chaque exécution du script.







xbox.py
=======

Python class to support reading xbox 360 wired and wireless controller input under Linux.  Makes it easy to get real-time input from controller buttons, analog sticks and triggers.  Built and tested on RaspberryPi running Raspbian.

Requires that xboxdrv be installed first:

    sudo apt-get install xboxdrv

To test the driver, issue the following command and see if the controller inputs are recognized

    sudo xboxdrv --detach-kernel-driver

See http://pingus.seul.org/~grumbel/xboxdrv/ for details on xboxdrv

Download the python module and sample code with the following:

    wget https://raw.githubusercontent.com/FRC4564/Xbox/master/xbox.py
    wget https://raw.githubusercontent.com/FRC4564/Xbox/master/sample.py

You can run the sample code to see how the Joystick class works.

    sudo python sample.py

Example class usage:

    import xbox
    joy = xbox.Joystick()         #Initialize joystick
    
    if joy.A():                   #Test state of the A button (1=pressed, 0=not pressed)
        print 'A button pressed'
    x_axis   = joy.leftX()        #X-axis of the left stick (values -1.0 to 1.0)
    (x,y)    = joy.leftStick()    #Returns tuple containing left X and Y axes (values -1.0 to 1.0)
    trigger  = joy.rightTrigger() #Right trigger position (values 0 to 1.0)
    
    joy.close()                   #Cleanup before exit

Note:
Run your code with sudo privileges to allow xboxdrv the necessary control over USB devices.
If you want, you can provide your user account with the proper access, so you needn't use sudo.

First, add your user to the root group. Here's how to do this for the user ‘pi’

    sudo usermod -a -G root pi

Create a permissions file using the nano text editor.

    sudo nano /etc/udev/rules.d/55-permissions-uinput.rules

Enter the following rule and save your entry.

    KERNEL=="uinput", MODE="0660", GROUP="root"

Troubleshooting
---------------

I find that xboxdrv occasionally has trouble connecting to the controller.  You may see a USB device error or something similar.  Issuing the following command will detach and reconnect the controller.

    sudo xboxdrv --detach-kernel-driver
    
You should now be able to move the joysticks and press buttons to see the controller state display for all inputs.  Just press Ctrl-C to exit and then relaunch your python code that uses xbox.py.

If your wireless controller still won't connect, press the sync button on the controller and the receiver (both devices need to be powered).

Usage
-----

A good application for an XBox controller is for robot control.  Check out [Basic PiBot](https://github.com/FRC4564/BasicPiBot) for more details.
