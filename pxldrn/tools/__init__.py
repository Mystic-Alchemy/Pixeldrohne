from .minesweeper import Base as MineSweeper
import discord

minesweeper_spielhilfe = discord.Embed(
    title="Minesweeper Spielhilfe",
    description="Dies ist eine kurze Hilfe mit Tipps, wie man Minesweeper spielt. Dies soll keine Anleitung sein wie man "
                "gewinnt. Es soll einen nur auf den richtigen Weg bringen."
)
minesweeper_spielhilfe.add_field(
    name="Tipp 1",
    value="Fange erstmal mit einem zufälligen Feld an, dies erhöht deine Chancen."
)
minesweeper_spielhilfe.add_field(
    name="Tipp 2",
    value="Eine Bombe kann in alle Richtungen liegen, auch diagonal."
)
minesweeper_spielhilfe.add_field(
    name="Tipp 3",
    value="Das Feld wird immer neu und ohne Richtlinien gebaut. Das heißt, die Position einer Bombe sagt nichts über die Position einer"
          " anderen Bombe aus."
)
minesweeper_spielhilfe.add_field(
    name="Beispiel 1",
    value=":one::one::one:\n:one:💣:one:\n:one::one::one:"
)
minesweeper_spielhilfe.add_field(
    name="Beispiel 2",
    value="💣:one:⬛\n:one::two::one:\n⬛:one:💣"
)