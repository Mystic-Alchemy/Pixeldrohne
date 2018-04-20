import discord
import random
import pxldrn.adv.minigames
import pxldrn.adv.sysinfo
import pxldrn.adv.embed_data
import pxldrn.adv.eball


def zitate():
    öffnen = open("pxldrn/adv/config/zitate.txt", "r", encoding='utf-8')
    auswahl = öffnen.readlines()
    zitat = random.choice(auswahl)
    return zitat
    öffnen.close()


def schreiben(zitat):
    datei = open("pxldrn/adv/config/zitate.txt", "a", encoding='utf-8')
    datei.write("\n" + zitat)
    return "Dein Zitat `{0}` wurde der Liste hinzugefügt.".format(zitat)
    datei.close()


def coin():
    choice = random.randint(1, 13)
    if 1 <= choice <= 5:
        return '🌑'
    if choice == 6:
        return '🌟'
    if 7 <= choice <= 11:
        return '🌕'
    if choice == 12:
        return '💣'
    if choice == 13:
        return '💮'


def eightball(msg, length):
    count = len(msg)
    msgi = " ".join(msg)
    rmsg = pxldrn.adv.eball.eball(msgi, msg, length, count)
    return rmsg
