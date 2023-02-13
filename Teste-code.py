# %%
import gtts
def convert_text_to_audio(value, file):
    """_summary_
    From value convert the text into audio and save in .mp3 in the current directory
    Args:
        value (string): the phrase which be convert to audio
        file (string): the name of the file
    """
    # make request to google to get synthesis
    tts = gtts.gTTS(value)
    # save the audio file
    path = "C:/Users/eduar/Studyspace/scrapy/extract-from-reverso-ankicards/audio/"
    tts.save(path+file+"mp3")
    print(f"Convert {value} to audio")


# %%
def openReadFile(fileName):
    """_summary_

    Args:
        fileName (str): File name that you desire to extract the text

    Returns:
        list[str]: all the lines of the file
    """    
    file = []
    path = "C:/Users/eduar/Studyspace/scrapy/extract-from-reverso-ankicards/"
    path = path + fileName
    with open(path, 'r',encoding="utf-8") as reader:
        #O problema ta aqui por que ele ta lendo o arquivo e não esta separando 
        #por quebra de linha
        file = reader.readlines()
        pass
    return file

# %%
fronts = "Perhaps it needs a lighter touch."
backs = "Talvez ele precise de um toque mais leve."
medias = "Perhaps_it_needs_a_lighter_touch"
var = f"[sound:{medias}.mp3]"
var

# %%
import genanki
import datetime
dateTimeNow = datetime.datetime.now()

my_model = genanki.Model(
    1675939036,
    'Basic',
    fields=[
        {'name': 'Question'},
        {'name': 'Answer'},
        {'name': 'MyMedia'},
    ],
    templates=[
        {
            'name': 'Card 1',
            'qfmt': '{{Question}}<br>{{MyMedia}}',
            'afmt': '{{FrontSide}}<hr id="answer">{{Answer}}',
        },
    ])
#Do not change the id, because anki identify the cards by id
my_deck = genanki.Deck(
    2059400110,
    'EnglishCards')
print(f"Deck {my_deck} created")
my_package = genanki.Package(my_deck)
 #assign a list of files of audio
my_package.media_files = medias
#Assigning every phrase in fronts and backs to create a card and add to deck
print(f"adding phrases to {my_deck.name}")
my_note = genanki.Note(
    model=my_model,
    fields=[fronts, backs, f"[sound:{medias}.mp3]"])
my_deck.add_note(my_note)

outputApkg = dateTimeNow.strftime("%f") + ".apkg"
genanki.Package(my_deck).write_to_file(outputApkg)
print(f"File {outputApkg} created")


# %%
trash = ["\\", "/", ":", "*", "?", "\"", "<", '>']
value = "LC/GC Certified vials are tested by LC/UV for residues of chemicals used in processing and packaging vials."
#var = map(lambda num: num+1,trash)
var = ""
for i,item in enumerate(value):
    if item in trash:
        var.__add__(item)
    else:
        var.__add__(item)
var

# %%



