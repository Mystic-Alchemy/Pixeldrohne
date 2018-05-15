import discord
import random
import pxldrn.adv.minigames
import pxldrn.adv.sysinfo
import pxldrn.adv.embed_data
import pxldrn.adv.eball
import pxldrn.adv.config


def capword(cap_list):
    r_list = []
    for i in cap_list:
        r_i = i.capitalize()
        r_list.append(r_i)
    r_string = " ".join(r_list)
    return r_string


def zitate():
    öffnen = open("pxldrn/adv/config/zitate.txt", "r", encoding='utf-8')
    auswahl = öffnen.readlines()
    zitat = random.choice(auswahl)
    öffnen.close()
    return zitat


def schreiben(zitat):
    datei = open("pxldrn/adv/config/zitate.txt", "a", encoding='utf-8')
    datei.write("\n" + zitat)
    datei.close()
    return "Dein Zitat `{0}` wurde der Liste hinzugefügt.".format(zitat)


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


def uptime(minutes, hours, days):
    if not days == 0:
        return 'Ich laufe schon für {} Tage, {} Stunden und {} Minuten.'.format(days, hours, minutes)
    elif not hours == 0:
        return 'Ich laufe schon für {} Stunden und {} Minuten.'.format(hours, minutes)
    elif not minutes == 0:
        return 'Ich laufe schon für {} Minuten.'.format(minutes)
    else:
        return "Ich bin noch nicht mal eine einzige Minute online."


def eightball(msg, length):
    count = len(msg)
    msgi = " ".join(msg)
    rmsg = pxldrn.adv.eball.eball(msgi, msg, length, count)
    return rmsg


def radio(radio_o):
    if radio_o == "iloveradio":
        return "http://stream01.iloveradio.de/iloveradio1.mp3"
    elif radio_o == "bayern1":
        return "http://br-br1-obb.cast.addradio.de/br/br1/obb/mp3/128/stream.mp3"
    elif radio_o == "antennebayern":
        return "http://mp3channels.webradio.antenne.de:80/antenne"
    elif radio_o == "radiogalaxy":
        return "http://fhin.4broadcast.de/galaxyin.mp3"
    elif radio_o == "youfm":
        return "http://hr-youfm-live.cast.addradio.de/hr/youfm/live/mp3/128/stream.mp3"
    elif radio_o == "planetradio":
        return "http://mp3.planetradio.de/planetradio/hqlivestream.mp3"
    elif radio_o == "rockantenne":
        return "http://mp3channels.webradio.antenne.de/rockantenne"
    elif radio_o == "random":
        return random.choice(pxldrn.adv.config.lists.random_radio)
    elif radio_o == "liste":
        return "RSL"
    elif radio_o == "dev.radio":
        return "NoStation"
    else:
        return "XTAB"