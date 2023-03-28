#-*- coding:utf-8 -*- 
import os
import shutil
import datetime

from fileWork import fileWork
from requestFromSite import scrapeFromReverso
from requestFromSite import scrapeFromDictionary
from stringCleaner import stringWork
from ankiWork import ankiWork

NUMBER_OF_CARDS=10
dateTimeNow = datetime.datetime.now()

def move_files():
    """_summary_
    Move the directory audio to anki collection media
    """  
    sourceFolder = r"C:/Users/eduar/Studyspace/extract-from-reverso-ankicards/audio//"
    destinationFolder = r"C:/Users/eduar/AppData/Roaming/Anki2/User 1/collection.media//"
    for item in os.listdir(sourceFolder):
        source = sourceFolder + item
        destination = destinationFolder + item
        if os.path.isfile(source):
            shutil.move(source, destination)
            print('Moved:', item)


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


def init(files):
    #files = ["mischief","love"]
    for item in files:
        """
        ao inves de fazer a busca da frase e colocara para cada frase 
        a pronuncia e adefinição, coloca apenas quando for juntar 
        tudo e fazer o deck  
        """
        # puxa do dicionario a pronuncia e a definição
        pronunciations,definitions = scrapeFromDictionary.take_from_website(item)
        scrapeFromReverso.take_from_website(item)
        var = item
        fronts = fileWork.openReadFile("front.txt")
        backs = fileWork.openReadFile("back.txt")
        media = []
        for item2 in fronts:
            fileName = stringWork.clean_strings(item2)
            ankiWork.convert_text_to_audio(item2, fileName)
            media.append(fileName)
        #junta e manda para ser transformado em cards 
        ankiWork.import_to_anki(fronts, backs, media, var.replace(" ","_"), pronunciations,definitions)
        move_files()
pass
if __name__ == "__main__":

    files = phrases_in_file_to_array()
    init(files)

