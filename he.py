import discord

hilfe = discord.Embed(
    title="Erklärung der Hilfe",
    color=0xad1457,
    description='Um die einzelnen Teile der Hilfe aufzurufen einfach mit "p.help <argument>" '
                'auf diese Nachricht reagieren\n\nMögliche Argumente sind:'
)
hilfe.set_author(
            name="Pixeldrohne",
            icon_url="https://static-cdn.jtvnw.net/jtv_user_pictures/5aa94e1433d8041e-profile_image-300x300.png",
            url="https://twitch.tv/pixelwerfer"
)
hilfe.set_footer(
    text='Dieser Bot ist in aktiver Entwicklung, fast täglich gibt es neues Zeug.',
    icon_url="https://static-cdn.jtvnw.net/jtv_user_pictures/5aa94e1433d8041e-profile_image-300x300.png"
)
hilfe.set_thumbnail(
    url="https://static-cdn.jtvnw.net/jtv_user_pictures/5aa94e1433d8041e-profile_image-300x300.png"
)
hilfe.add_field(
    name="komplett",
    value="Ruft die gesamte Hilfe ab"
)
