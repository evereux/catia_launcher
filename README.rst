==============
CATIA Launcher
==============

About
-----

CATIA Launcher is a PySide2 (PyQT) application that will launch CATIA V5.
It's purpose is for company's that might have several CATIA installations
configured to suit a clients / projects requirements.

To use CATIA launcher the CATIA shortcut .lnk files need to all be in the same
network accessible location.

.. image:: images/picture.jpeg


Get CATIA Launcher
------------------

Clone from github::
    git clone https://github.com/evereux/catia_launcher.git

Download from github https://github.com/evereux/catia_launcher/archive/master.zip


Requirements
------------

* Python 3.5 >
* See requirements.txt


Install Requirements
--------------------

pip install -r requirements.txt

First Run
---------

Upon first running the application the user is prompted for the path
of the location to the folder containing the CATIA shortcut links. This
will then create a config.json file. These shortcut links are then used
to generate the menu options within the application.

Once done, run the application again.

::
    python run.py