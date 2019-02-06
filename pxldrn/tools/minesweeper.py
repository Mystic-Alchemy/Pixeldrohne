import discord, typing, random


class Base:
    def __init__(self, bombs=None, rows=None, columns=None, tag=None):
        self.rows = rows
        self.columns = columns
        self.bombs = bombs
        self.tag = tag
        self.chars_non_hidden = {"b": "💣", "0": "⬛", "1": ":one:", "2": ":two:", "3": ":three:", "4": ":four:",
                                 "5": ":five:", "6": ":six:", "7": ":seven:", "8": "eight"}
        self.chars = {"b": "||💣||", "0": "||⬛||", "1": "||:one:||", "2": "||:two:||", "3": "||:three:||", "4": "||:four:||",
                      "5": "||:five:||", "6": "||:six:||", "7": "||:seven:||", "8": "||:eight:||"}


    async def map_builder(self):
        b_list = []
        data_map = {}
        r_list = []
        for i in range(self.rows):
            data_map[i] = {}
            for f in range(self.columns):
                data_map[i][f] = "None"
        for i in range(self.bombs):
            x = random.randrange(self.columns)
            y = random.randrange(self.rows-1)
            pair = [y, x]
            while pair in b_list:
                x = random.randrange(self.columns)
                y = random.randrange(self.rows-1)
                pair = [y, x]
            b_list.append(pair)
        for i in b_list:
            data_map[i[0]][i[1]] = "b"
        for i in data_map:
            for f in data_map[i]:
                if data_map[i][f] == "b":
                    pass
                else:
                    value = 0
                    for y in range(-1, 2):
                        for x in range(-1, 2):
                            if x == 0 and y == 0:
                                pass
                            else:
                                check_y = i + y
                                check_x = f + x
                                if check_x < 0 or check_y < 0:
                                    pass
                                elif check_x >= self.columns or check_y >= self.rows:
                                    pass
                                else:
                                    if data_map[check_y][check_x] == "b":
                                        value += 1
                    data_map[i][f] = str(value)
        for i in data_map:
            for f in data_map[i]:
                if self.tag == "-v":
                    r_list.append(self.chars_non_hidden[data_map[i][f]])
                else:
                    r_list.append(self.chars[data_map[i][f]])
            r_list.append("\n")
        r_list = "".join(r_list)
        return r_list
