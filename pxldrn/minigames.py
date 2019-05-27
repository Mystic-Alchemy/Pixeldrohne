import random, discord, typing, asyncio, pxldrn.tools
from math import sqrt
from pxldrn.tools import MineSweeper
from discord.ext import commands


def to_lower(argument):
    return str(argument.lower())


class SchereSteinPapier(commands.Cog):

    def __init__(self, bot):

        self.bot = bot
        self.norm = ["schere", "stein", "papier"]
        self.ext = ["schere", "stein", "papier", "spock", "echse"]
        self.win_dict = {"schere": {"sieg": "papier", "verloren": "stein"},
                         "stein": {"sieg": "schere", "verloren": "papier"},
                         "papier": {"sieg": "stein", "verloren": "schere"}}
        self.win_dict_ext = {"schere": {"sieg": ["papier", "echse"], "verloren": ["stein", "spock"]},
                             "stein": {"sieg": ["schere", "echse"], "verloren": ["papier", "spock"]},
                             "papier": {"sieg": ["stein", "spock"], "verloren": ["schere", "echse"]},
                             "echse": {"sieg": ["papier", "spock"], "verloren": ["stein", "echse"]},
                             "spock": {"sieg": ["schere", "stein"], "verloren": ["papier", "echse"]}}

    async def ssp_embeds(self, ctx, status="n", bot=None, spieler=None):
        if status == "u":
            embed = discord.Embed(
                title="Wir haben das gleiche gewählt",
                description="Eigentlich hasse ich es ja, dass es auf ein Unentschieden rausläuft.",
                color=0xecde13
            )
            await ctx.send(embed=embed)
        elif status == "s":
            embed = discord.Embed(
                title="Du hast gewonnen.",
                description="😭 Ich habe verloren. 😭 Och menno! 😭 Ich wollte doch gewinnen. 😭",
                color=0x00ff00
            )
            embed.add_field(name="Bot", value=bot.capitalize())
            embed.add_field(name="Spieler", value=spieler.capitalize())
            await ctx.send(embed=embed)
        elif status == "v":
            embed = discord.Embed(
                title="Du hast verloren.",
                description="😁 Hihi, ich habe gewonnen. Aber keine Sorge du kannst dann vielleicht nächstes mal auch gewinnen. 😇",
                color=0xff0000
            )
            embed.add_field(name="Bot", value=bot.capitalize())
            embed.add_field(name="Spieler", value=spieler.capitalize())
            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(
                title="Huch, da ist was schiefgegangen.",
                description="Da ist wohl in meinem System was falsch gelaufen, na klasse."
            )

    @commands.group(name="ssp", case_insensitive=True)
    async def ssp(self, ctx):
        if ctx.invoked_subcommand is None:
            await ctx.send("Bitte nenne mir Schere Stein Papier oder -e um mit Echse und Spock zu spielen")

    @ssp.command(name="schere")
    async def schere(self, ctx):
        bot_choice = random.choice(self.norm)
        if bot_choice == "schere":
            await self.ssp_embeds(ctx, status="u", bot=bot_choice, spieler="schere")
        elif bot_choice in self.win_dict['schere']['sieg']:
            await self.ssp_embeds(ctx, status="s", bot=bot_choice, spieler="schere")
        elif bot_choice in self.win_dict['schere']['verloren']:
            await self.ssp_embeds(ctx, status="v", bot=bot_choice, spieler="schere")
        else:
            await self.ssp_embeds(ctx)

    @ssp.command(name="stein")
    async def stein(self, ctx):
        bot_choice = random.choice(self.norm)
        if bot_choice == "stein":
            await self.ssp_embeds(ctx, status="u", bot=bot_choice, spieler="stein")
        elif bot_choice in self.win_dict['stein']['sieg']:
            await self.ssp_embeds(ctx, status="s", bot=bot_choice, spieler="stein")
        elif bot_choice in self.win_dict['stein']['verloren']:
            await self.ssp_embeds(ctx, status="v", bot=bot_choice, spieler="stein")
        else:
            await self.ssp_embeds(ctx)

    @ssp.command(name="papier")
    async def papier(self, ctx):
        bot_choice = random.choice(self.norm)
        if bot_choice == "papier":
            await self.ssp_embeds(ctx, status="u", bot=bot_choice, spieler="papier")
        elif bot_choice in self.win_dict['papier']['sieg']:
            await self.ssp_embeds(ctx, status="s", bot=bot_choice, spieler="papier")
        elif bot_choice in self.win_dict['papier']['verloren']:
            await self.ssp_embeds(ctx, status="v", bot=bot_choice, spieler="papier")
        else:
            await self.ssp_embeds(ctx)

    @ssp.command(name="-e")
    async def extended(self, ctx, wahl: to_lower):
        if wahl not in self.ext:
            await ctx.send("Bitte wähle zwischen Schere, Stein, Papier, Echse oder Spock.")
        else:
            bot_choice = random.choice(self.ext)
            if bot_choice == wahl:
                await self.ssp_embeds(ctx, status="u", bot=bot_choice, spieler=wahl)
            elif bot_choice in self.win_dict_ext[wahl]['sieg']:
                await self.ssp_embeds(ctx, status="s", bot=bot_choice, spieler=wahl)
            elif bot_choice in self.win_dict_ext[wahl]['verloren']:
                await self.ssp_embeds(ctx, status="v", bot=bot_choice, spieler=wahl)
            else:
                await self.ssp_embeds(ctx)

    @extended.error
    async def extended_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("Bitte wähle zwischen Schere, Stein, Papier, Echse oder Spock.")


class Minesweeper(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="minesweeper")
    async def minesweeper(self, ctx, columns: typing.Union[int, str] = None, rows: typing.Optional[int] = None, bombs: typing.Union[int, str] = None, output: typing.Optional[str] = None):
        if columns is None:
            mine_help = discord.Embed(
                title="Minesweeper",
                description="Dieser Befehl ist ein Generator für Minesweeper Layouts.",
                colour=0x123456
            )
            mine_help.add_field(
                name=f"Aufbau | Generelle Form: {self.bot.command_prefix}minesweeper <x> <y> [bombs|tag]",
                value=f"Wenn du die Anzahl and Spalten (x) angibst musst du auch die Anzahl an Zeilen (y) angeben. Die Anzahl an Bomben ist optional, wenn man keinen Wert angibt, dann wird die Anzahl automatisch festgelegt."
                      f"Man kann auch das Tag `-v` oder `--visible` nutzen um das generierte Spiel nicht zu verdecken, dies sollte immer am Schluss stehen, kann aber auch mit angegeber Anzahl von Bomben genutzt werden."
            )
            mine_help.add_field(name="Wie man spielt.", value=f"Eine Hilfe wie man Minesweeper spielt ist mit `{self.bot.command_prefix}minesweeper help` aufrufbar.")
            mine_help.add_field(name="Tipp", value="Klicke auf 🇦 unter dieser Nachricht um ein zufälliges Spiel zu generieren.\n"
                                                   "Klicke auf 🇧 um die oben genannte Spielhilfe aufzurufen.")
            help_message = await ctx.send(embed=mine_help)
            await help_message.add_reaction("🇦")
            await help_message.add_reaction('🇧')

            def check(reaction, user):
                reaction_list = ["🇦", '🇧']
                return user == ctx.message.author and str(reaction.emoji) in reaction_list

            try:
                reaction, user = await self.bot.wait_for('reaction_add', timeout=30.0, check=check)
            except asyncio.TimeoutError:
                pass
            else:
                if str(reaction.emoji) == "🇦":
                    mines = MineSweeper(rows=random.randint(7, 12), columns=random.randint(7, 12), bombs=random.randint(12, 20))
                    mapped = await mines.map_builder()
                    await ctx.send(mapped)
                if str(reaction.emoji) == '🇧':
                    await ctx.send(embed=pxldrn.tools.minesweeper_spielhilfe)
        elif columns == "help" or columns == "hilfe":
            await ctx.send(embed=pxldrn.tools.minesweeper_spielhilfe)
        elif columns > 15 or rows > 13:
            await ctx.send("Die maximale Größe is 15x13")
        else:
            if bombs is None:
                tag = None
                if rows < 10 or columns < 10:
                    bombs = int(sqrt(rows * columns * 2))
                else:
                    bombs = int(sqrt(rows * columns * 3))
            elif bombs == "-v" or bombs == "--visible":
                tag = "-v"
                if rows < 10 or columns < 10:
                    bombs = int(sqrt(rows * columns * 2))
                else:
                    bombs = int(sqrt(rows * columns * 3))
            else:
                tag = output
            mines = MineSweeper(rows=rows, columns=columns, bombs=bombs, tag=tag)
            mapped = await mines.map_builder()
            await ctx.send(mapped)
