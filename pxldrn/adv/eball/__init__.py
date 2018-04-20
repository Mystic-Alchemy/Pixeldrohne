import keys
from pxldrn.adv.eball import choice_selection as response


def eball(msgi, msgl,  length=0, count=0):
    if length is 0 or count is 0:
        return "Ich weiß nicht was du von mir willst.\nDu musst mich schon was fragen."
    elif count < 3:
        return "Das ist ein bisschen wenig zu wenig, dass ich eine Antwort liefern kann"
    elif "?" not in msgl[-1]:
        return 'Ist das wirklich eine Frage? Ich sehe nämlich kein "?" am Ende.'
    else:
        ch_num = chooser(msgl, length, count)
        if ch_num is 0:
            result = choice(0, msgi)
        elif ch_num < 10:
            result = choice(1, msgi)
        elif ch_num < 20:
            result = choice(2, msgi)
        elif ch_num < 30:
            result = choice(3, msgi)
        elif ch_num < 40:
            result = choice(4, msgi)
        elif ch_num < 50:
            result = choice(5, msgi)
        elif ch_num < 60:
            result = choice(6, msgi)
        elif ch_num < 70:
            result = choice(7, msgi)
        elif ch_num < 80:
            result = choice(8, msgi)
        elif ch_num < 90:
            result = choice(9, msgi)
        elif ch_num < 100:
            result = choice(10, msgi)
        elif ch_num is 100:
            result = choice(11, msgi)
        else:
            result = choice(12, msgi)
        return str(result) + " " + str(ch_num)


def chooser(msg, length, count, base=0):
    for i in msg:
        form = len(i) - count
        base = base + form
    if base < 0:
        base = base * (-1)
        if base > 100:
            base = base - length
        return base
    elif base > 100:
        base = base - length
        return base
    else:
        return base


def blist(msg):
    pass


def choice(pos, msg):
    if any(i in msg.lower() for i in keys.blacklist):
        return blist(msg)
    elif pos is 0:
        return response.zero()
    elif pos is 1:
        return response.one()
    elif pos is 2:
        return response.two()
    elif pos is 3:
        return response.three()
    elif pos is 4:
        return response.four()
    elif pos is 5:
        return response.five()
    elif pos is 6:
        return response.six()
    elif pos is 7:
        return response.seven()
    elif pos is 8:
        return response.eight()
    elif pos is 9:
        return response.nine()
    elif pos is 10:
        return response.ten()
    elif pos is 11:
        return response.eleven()
    elif pos is 12:
        return response.twelve()
