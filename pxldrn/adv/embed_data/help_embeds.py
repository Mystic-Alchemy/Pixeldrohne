import discord


def intro():
    hilfe = discord.Embed(
        title="Erklärung der Hilfe",
        color=0xad1457,
        description='Um die einzelnen Teile der Hilfe aufzurufen, einfach mit "p.help <argument>" '
                    'auf diese Nachricht reagieren.\n\nMögliche Argumente sind:'
    )
    hilfe.set_author(
        name="Pixeldrohne",
        icon_url="https://www.mystic-alchemy.com/wp-content/uploads/2018/05/avatar.jpg",
        url="https://twitch.tv/pixelwerfer"
    )
    hilfe.set_footer(
        text='Um mehr Informationen über den Autor dieses Bots zu erhalten: p.about',
        icon_url="https://www.mystic-alchemy.com/wp-content/uploads/2018/05/avatar.jpg"
    )
    hilfe.set_thumbnail(
        url="https://www.mystic-alchemy.com/wp-content/uploads/2018/05/avatar.jpg"
    )
    hilfe.add_field(
        name="musik",
        value="Ruft die Hilfe für die Musik ab."
    )
    hilfe.add_field(
        name="spiele",
        value="Ruft die Minigames ab"
    )
    hilfe.add_field(
        name="allgemein",
        value="Ruft die Befehle ab, die in keiner\n anderen Kategorie ihren Platz haben."
    )
    return hilfe


def primary():
    allgemein = discord.Embed(
        title="Allgemeine Befehle",
        color=0xad1457,
        description="Alle Befehle, die keine spezielle Kategorie haben."
    )
    return allgemein


def music():
    musik = discord.Embed(
        title="Kategorie: Musik",
        color=0xad1457,
        description="Alle Befehle des Bots, die mit dem Abspielen von Musik zu tun haben."
    )
    musik.add_field(
        name="p.join",
        value="Holt den Bot in den Sprachkanal, in dem du auch bist."
    )
    musik.add_field(
        name="p.leave",
        value="Lässt den Bot den Sprachkanal verlassen."
    )
    musik.add_field(
        name="p.play <yt-link>",
        value="Lässt den Bot ein Lied oder eine Playlist abspielen.\n**Achtung:** Bei Liedern aus einer"
              " Playlist wird die gesamte Playlist ab dem gewünschten Lied abgespielt."
    )
    musik.add_field(
        name="p.pause/p.resume",
        value="Pausiert/setzt das aktuelle Lied fort."
    )
    musik.add_field(
        name="p.stop",
        value="Hält das Lied komplett an."
    )
    musik.add_field(
        name="p.volume",
        value="Passt die Lautstärke in Prozent an. Werte von 0 bis 100 möglich."
    )
    return musik


def minigames():
    mini = discord.Embed(
        title="Kategorie: Spiele",
        color=0xad1457,
        description="Alle Befehle des Bots, die mit Spielen zu tun haben."
    )
    mini.add_field(
        name="p.ssp <wahl>",
        value="Schere, Stein, Papier\ngegen die Drohne."
    )
    mini.add_field(
        name="p.coin",
        value="Der gute alte Münzwurf."
    )
    return mini
