#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os


def inst():
    y = "y"
    x = "x"
    ent = input("Tecle (y) para instalar ou (x) para cancelar: ")
    if(ent == y):
        #Inicialmente baixe os pré-requisitos para funcionamento do cliente SNX (execute como root):
       
        os.system("sudo apt-get install libpam0g:i386 libstdc++5 libx11-6:i386 libstdc++6:i386 libstdc++5:i386")
       
        #Instale a versão mais atualizada do Java JRE da Oracle (neste manual iremos contemplar a JRE8 – caso 
        # já possua o JRE instalado, desconsidere este passo):
       
        os.system("sudo add-apt-repository ppa:webupd8team/java")
        os.system("sudo apt-get update")#Atualize o Sistema;
        os.system("sudo apt-get install oracle-java8-installer")
        os.system("sudo apt-get install oracle-java8-set-default")
              
        #Instale o SNX
        os.system("chmod 777 snx_install_linux30.sh")
        os.system("sudo ./snx_install_linux30.sh")
        print("A instalação foi um sucesso")
    
    elif(ent == x):
        exit()

inst()
