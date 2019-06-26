# This fle is for people who do not have pygame
import subprocess

import sys

import get_pip

import os



def install(package):

    subprocess.call([sys.executable, "-m", "pip", "install", package])



try:

    print("[GAME] Trying to import pygame")

    import pygame

except:

    print("[EXCEPTION] Pygame not installed")



    try:

        print("[GAME] Trying to install pygame via pip")

        import pip

        install("pygame")

        print("[GAME] Pygame has been installed")

    except:

        print("[EXCEPTION] Pip not installed on system")
        quit()


    #test
    import pygame

