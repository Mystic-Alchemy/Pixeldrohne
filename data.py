import dataset
import random
import discord

db = dataset.connect('sqlite:///bot.db')
userdb = db['daten']


def nachrichten(mid):
    db.begin()
    try:
        userid = userdb.find_one(userid=mid)
        if userid is None:
            userdb.upsert(dict(userid=mid, nachrichten=0, lvl=0, xp=0, pixel=0), ['userid'])
            db.commit()
        else:
            messages = dict(userid=mid, nachrichten=userid['nachrichten'] + 1)
            userdb.upsert(messages, ['userid'])
            db.commit()
    except:
        db.rollback()


def xp(mid, length):
    db.begin()
    if length > 250:
        exp = random.randint(50, 75)
    elif length > 100:
        exp = random.randint(30, 50)
    else:
        exp = random.randint(10, 30)
    try:
        userid = userdb.find_one(userid=mid)
        if userid is None:
            userdb.upsert(dict(userid=mid, nachrichten=0, lvl=0, xp=0, pixel=0), ['userid'])
            db.commit()
        else:
            exp = exp + userid['xp']
            messages = dict(userid=mid, xp=exp)
            userdb.upsert(messages, ['userid'])
            db.commit()
    except:
        db.rollback()


def level(mid, name):

    return embed
