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
    elif radio_o == "oe3":
        return "http://mp3stream7.apasf.apa.at:8000"
    elif radio_o == "krone":
        return "http://raj.krone.at:80/kronehit-ultra-hd.aac"
    elif radio_o == "vgm":
        return "http://radio.vgmradio.com:8040/stream"
    elif radio_o == "bbc1":
        return "http://bbcmedia.ic.llnwd.net/stream/bbcmedia_radio1_mf_p"
    elif radio_o == "bbc2":
        return "http://bbcmedia.ic.llnwd.net/stream/bbcmedia_radio2_mf_p"
    elif radio_o == "bbc3":
        return "http://bbcmedia.ic.llnwd.net/stream/bbcmedia_radio3_mf_p"
    elif radio_o == "bollywood":
        return "http://us2.internet-radio.com:8281/live"
    elif radio_o == "bigb-k":
        return "http://64.71.79.181:8040/"
    elif radio_o == "bigb-j":
        return "http://64.71.79.181:8018/"
    elif radio_o == "ibiza":
        return "http://ibizaglobalradio.streaming-pro.com:8024/"
    elif radio_o == "random":
        return random.choice(pxldrn.adv.config.lists.random_radio)
    elif radio_o == "liste":
        return "RSL"
    elif radio_o == "dev.radio":
        return "NoStation"
    else:
        return "XTAB"