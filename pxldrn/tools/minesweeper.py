import discord, typing


class Base:
    def __init__(self, rows, columns, seed: typing.Optional[int] = None):
        self.rows = rows
        self.column = columns
        self.seed = seed

    async def map_builder(self):
        count = self.rows * self.column * 5
        if count >= 2000:
            return "Sorry, the board you want is too large."
        else:
            row = []
            for a in range(self.rows):
                col = []
                for i in range(self.column):
                    col.append("||⬛||")
                col.append("\n")
                col = "".join(col)
                row.append(col)
            mapped = "".join(row)
            return mapped
