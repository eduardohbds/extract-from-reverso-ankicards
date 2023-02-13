#-*- coding:utf-8 -*- 
import gtts
import requests
from bs4 import BeautifulSoup
import os
import shutil
import genanki
import datetime
NUMBER_OF_CARDS=10
dateTimeNow = datetime.datetime.now()

headers = {
    'authority': 'context.reverso.net',
    'cache-control': 'max-age=0',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'sec-gpc': '1',
    'sec-fetch-site': 'same-site',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-user': '?1',
    'sec-fetch-dest': 'document',
    'referer': 'https://www.reverso.net/',
    'accept-language': 'en-US,en;q=0.9',
    'cookie': 'CTXTNODEID=bstweb12; experiment_context_Et4k3pePD=0; reverso.net.apps-promo=4; reverso.net.apps-promo-display=1; experiment_context_4rUk3pePA=1; _pbjs_userid_consent_data=6683316680106290; _ramjsShID=87b71bb4-0817-49d6-95d2-3d3f4e96c4cd; context.lastpair=en-pt; floatingpopup_counter=0; history_entry=levantar%20qualquer%20um]#[mischievous; history_pair=pt-en]#[en-pt; reverso.net.dir=eng-fra; reverso.net.LanguageInterface=pt; didomi_token=eyJ1c2VyX2lkIjoiMTc0MzY4NjMtYjMzNy02NTRjLThkZjItZTk4NzZlOGZkM2Y2IiwiY3JlYXRlZCI6IjIwMjItMDMtMDlUMTk6MjA6NTUuMjQ0WiIsInVwZGF0ZWQiOiIyMDIyLTAzLTA5VDE5OjIwOjU1LjI0NFoiLCJ2ZXJzaW9uIjpudWxsfQ==; JSESSIONID=TQnYO-gYID0txylu4x5zKetB.bst-web12',
}

cookies = {
    "CTXTNODEID": "bstweb12",
    "experiment_context_Et4k3pePD": "0",
    "reverso.net.apps-promo": "4",
    "reverso.net.apps-promo-display": "1",
    "experiment_context_4rUk3pePA": "1",
    "_pbjs_userid_consent_data": "6683316680106290",
    "_ramjsShID": "87b71bb4-0817-49d6-95d2-3d3f4e96c4cd",
    "context.lastpair": "en-pt",
    "floatingpopup_counter": "0",
    "history_entry": "levantar%20qualquer%20um]#[mischievous",
    "history_pair": "pt-en]#[en-pt",
    "reverso.net.dir": "eng-fra",
    "reverso.net.LanguageInterface": "pt",
    "didomi_token": "eyJ1c2VyX2lkIjoiMTc0MzY4NjMtYjMzNy02NTRjLThkZjItZTk4NzZlOGZkM2Y2IiwiY3JlYXRlZCI6IjIwMjItMDMtMDlUMTk6MjA6NTUuMjQ0WiIsInVwZGF0ZWQiOiIyMDIyLTAzLTA5VDE5OjIwOjU1LjI0NFoiLCJ2ZXJzaW9uIjpudWxsfQ==",
    "JSESSIONID": "TQnYO-gYID0txylu4x5zKetB.bst-web12",
}

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

def openWriteFile(content,fileName):
    """_summary_
    It write the content onto the fileName if the file is not create 
    the function will do
    Args:
        content (list): variable with the content to write onto the file
        fileName (string): variable with the name of the file, make sure 
        specify the extension of file, e.g. file.txt,file.json. 
    """    
    encoding = 'utf-8'
    path = "C:/Users/eduar/Studyspace/scrapy/extract-from-reverso-ankicards/"
    path = path + fileName
    with open(path, 'w', encoding=encoding) as writer:
        writer.writelines(content)
        # for item in content:
        #     writer.write(item)
        # pass
    pass

def request_from_website(listaDePalavras):
    """_summary_
    resquest from website Reverso Context the html page with translate
        passed by variable listaDePalavras 
    
    Args:
        listaDePalavras (str): _description_

    Returns:
        list: a html web page passed by method prettify() from bs4
    """    
    page = requests.get(
    "https://context.reverso.net/traducao/ingles-portugues/"+listaDePalavras,
    headers=headers,cookies=cookies)
    soup = BeautifulSoup(page.content, 'html.parser')
    soup.get_text()
    print("Request from website successful")
    return soup

def take_from_website(lista_de_palavras):
    """_summary_
    Search in Reverso Context the translate of a word and save in two files
    front.txt and back.txt
    """    
    file = request_from_website(lista_de_palavras)

    #examples_content = file.find(class__="wide-container")
    examples_content = file.find(id="examples-content")
    #subtitles = examples_content.find(attrs={"id":"OPENSUBTITLES-2012.EN-PT_2670996"})
    front = examples_content.find_all(attrs={"class":"src ltr"})
    back = examples_content.find_all(attrs={"class":"trg ltr"})
    print("Phrases Scraped from website")
    count = 0
    fronts = []
    backs = [] 
    for item,item2 in zip(front,back):
        if count == NUMBER_OF_CARDS:
             break
        fronts.append(item.get_text().strip() + "\n") 
        backs.append(item2.get_text().strip() + "\n")
        count +=1
        
    # for item in back:
    #      if item != "\n":
    #          backs=item.get_text().strip()

    print("Phrases cleaned")
    """
    tratar as frases retirar tab quebra de linha desnecessaria {check}
    concatenar o primeiro com a tradução do segundo{cheak}
    adicionar o audio em ingles {check}
    criar um arquivo apkg to import to anki {check}
    Mover os arquivos audio para a pasta collection anki {check}
    importar para o anki {check}
    """    

    openWriteFile(fronts,"front.txt")
    openWriteFile(backs,"back.txt")
    print("Phrases saved for file")
    pass

def convert_text_to_audio(value,file):
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
    tts.save(path+file+".mp3")
    print(f"Convert {value} to audio")

def import_to_anki(fronts,backs,medias,files):
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
        # xy=compare_strings(front,media)
        # if xy==-1:
        #     print(f"{front} and {media} is not equivalent")
        my_note = genanki.Note(
        model=my_model,
        fields=[front, back, f"[sound:{media}.mp3]"])
        my_deck.add_note(my_note)

    outputApkg = files + ".apkg"
    genanki.Package(my_deck).write_to_file(outputApkg)
    print(f"File {outputApkg} created")

def compare_strings(phrase,audio):
    """_summary_
    Compare if phrase and audio is equivalent 
    Args:
        phrase (string): the phrase in english
        audio (string): audio of the phrase in english

    Returns:
        int: if the phrase and audio is equivalent return 0, else return -1
    """
    audio = phrase.replace(" ","_")
    xy=0
    for x,y in zip(phrase,audio):
        if x != " " or y != "_":
            if x != y:
                xy=-1
                break
    return xy

def move_files():
    """_summary_
    Move the directory audio to anki collection media
    """  
    sourceFolder = r"C:/Users/eduar/Studyspace/scrapy/extract-from-reverso-ankicards/audio//"
    destinationFolder = r"C:/Users/eduar/AppData/Roaming/Anki2/User 1/collection.media//"
    for item in os.listdir(sourceFolder):
        source = sourceFolder + item
        destination = destinationFolder + item
        if os.path.isfile(source):
            shutil.move(source, destination)
            print('Moved:', item)

def clean_strings(value):
    trash = ["\\", "/", ":", "*", "?", "\"", "<", '>', "\n",".","-","+","|"]
    var = ""
    for i, item in enumerate(value):
        if item in trash:
            var = var + ""
        elif item == " ":
            var = var + "_"
        else:
            var = var + item
    print(f"Phrase:{var} Cleaned")
    return var

def init(files):
    for item in files:
        take_from_website(item)
        var = item
        fronts = openReadFile("front.txt")
        backs = openReadFile("back.txt")
        media = []
        for item2 in fronts:
            fileName = clean_strings(item2)
            convert_text_to_audio(item2, fileName)
            media.append(fileName)
        import_to_anki(fronts, backs, media, var.replace(" ","_"))
        move_files()
pass

def phrases_in_file_to_array():
    with open('myfile.txt', 'r+') as file:
        # Read the contents of the file
        contents = file.read()
        # Perform some action on the contents of the file
        print(contents)
        contentsReturn = contents.split()
        # Move the file pointer to the beginning of the file
        file.seek(0)
        # Overwrite the file with an empty string
        file.write('')
        # Truncate the file to zero length
        file.truncate()
        return contentsReturn

   
if __name__ == "__main__":

    files = phrases_in_file_to_array()

    init(files)


    # front = openReadFile("front.txt")
    # back = openReadFile("back.txt")
    # for value,value2 in zip(front, back):
    #     value = value.strip()
    #     value2 = value2.strip()
    # openWriteFile(front,"front.txt")
    # openWriteFile(back,"back.txt")
