# --coding: utf-8 --

directions = ["north", "south", "east", "west", "down", "up", "left", "right", "back"]
verbs = ["go", "stop", "kill", "eat"]
stops = ["the", "in", "of", "from", "at", "it"]
nouns = ["door", "bear", "princess", "cabinet"]


def convert_number(s):
    try:
        return int(s)
    except ValueError:
        return None


def scan(text):
    words = text.split()
    result = []
    for word in words:
        number = convert_number(word)
        if number:
            kind = ("number",)
            l = [word]
            result.append(kind + tuple(l))
        elif directions.count(word) != 0:
            kind = ("direction",)
            l = [word]
            result.append(kind + tuple(l))
        elif verbs.count(word) != 0:
            kind = ("verb",)
            l = [word]
            result.append(kind + tuple(l))
        elif stops.count(word) != 0:
            kind = ("stop",)
            l = [word]
            result.append(kind + tuple(l))
        elif nouns.count(word) != 0:
            kind = ("noun",)
            l = [word]
            result.append(kind + tuple(l))
        else:
            kind = ("error",)
            l = [word]
            result.append(kind + tuple(l))
    return result
