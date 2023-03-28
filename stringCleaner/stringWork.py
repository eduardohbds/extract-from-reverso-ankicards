def compare_strings(phrase, audio):
    """_summary_
    Compare if phrase and audio is equivalent 
    Args:
        phrase (string): the phrase in english
        audio (string): audio of the phrase in english

    Returns:
        int: if the phrase and audio is equivalent return 0, else return -1
    """
    audio = phrase.replace(" ", "_")
    xy = 0
    for x, y in zip(phrase, audio):
        if x != " " or y != "_":
            if x != y:
                xy = -1
                break
    return xy


def clean_strings(value):
    trash = ["\\", "/", ":", "*", "?", "\"",
             "<", '>', "\n", ".", "-", "+", "|"]
    var = ""
    # this feat is created, to in the moment of convert to audio
    # dont read the pronunciation
    for item in value:
        if item in trash:
            var = var + ""
        elif item == " ":
            var = var + "_"
        else:
            var = var + item

    print(f"Phrase:{var} Cleaned")
    return var[0:20]
