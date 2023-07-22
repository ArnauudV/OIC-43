#-----------------------------------------------------
# Auteur: Arnaud V
# Date: 19 Juin 2023
# Description: Ce programme permet de calculer une date de naissance parmi le million de decimales de PI, puis de d'afficher le jour de naissance correspondant. 
# Ensuite, il permet de calculer la somme des 20 premieres decimales de PI et aussi des 144 premieres. 
#-----------------------------------------------------

import streamlit as st
from mpmath import mp
import datetime

# On configure mpmath pour obtenir 1 000 000 de décimales de Pi.
mp.dps = 1000000 
pi_decimals = str(mp.pi)

# On convertit pi_decimals en une chaîne qui contient seulement les chiffres
pi_digits = pi_decimals.replace('.', '')

st.title('Jouons avec PI')

birthdate = st.text_input("Veuillez entrer votre date de naissance au format (JJMMAA):")

# Si l'utilisateur a bien entré une date de naissance.
if birthdate:
    # Vérifier si la date de naissance existe dans PI.
    if birthdate in pi_digits:
        st.write("Votre date de naissance se trouve dans les premiers un million de décimales de PI!")

        # Conversion de la date de naissance en date et affichage du jour correspondant
        birth_date = datetime.datetime.strptime(birthdate, "%d%m%y")
        st.write(f"Le jour de la semaine correspondant à votre date de naissance est : {birth_date.strftime('%A')}")
    else:
        st.write("Votre date de naissance ne se trouve pas dans les premiers un million de décimales de PI.")

# Sommes des 20 premières décimales
st.write(f"La somme des 20 premières décimales de PI est {sum(int(i) for i in pi_digits[:20])}")

# Sommes des 12^2 premières décimales
st.write(f"La somme des 144 premières décimales de PI est {sum(int(i) for i in pi_digits[:144])}")

# Ajout de la vidéo youtube
st.write("La somme de tous les nombres entiers naturels est -1/12, voici une vidéo qui explique cela :")
st.video('https://www.youtube.com/watch?v=GnZQOb9YNV4')

