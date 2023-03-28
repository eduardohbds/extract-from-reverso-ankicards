import gtts
import genanki

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
    path = "C:/Users/eduar/Studyspace/extract-from-reverso-ankicards/audio/"
    tts.save(path+file+".mp3")
    print(f"Convert {value} to audio")


def import_to_anki(fronts, backs, medias, files, pronunciations,definitions):
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
    for front, back, media in zip(fronts, backs, my_package.media_files):
        value1 = front + "\n" + pronunciations
        value2 = definitions + "\n" + back
        my_note = genanki.Note(
            model=my_model,
            fields=[value1, value2, f"[sound:{media}.mp3]"])
        my_deck.add_note(my_note)

    outputApkg = files + ".apkg"
    genanki.Package(my_deck).write_to_file(outputApkg)
    print(f"File {outputApkg} created")
