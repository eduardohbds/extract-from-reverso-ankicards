from bs4 import BeautifulSoup
import requests
from fileWork import fileWork
from headersToAccessSite import headers
from requestFromSite import scrapeFromDictionary

##This scrape from reverso Context
def request_from_website(wordSearched):
    """_summary_
    resquest from website Reverso Context the html page with translate
        passed by variable wordSearched 
    
    Args:
        wordSearched (str): _description_

    Returns:
        list: a html web page passed by method prettify() from bs4
    """
    page = requests.get(
        "https://context.reverso.net/traducao/ingles-portugues/"+wordSearched,
        headers=headers.headersReverso, cookies=headers.cookiesReverso)
    soup = BeautifulSoup(page.content, 'html.parser')
    soup.get_text()
    print("Request from website successful")

    return soup


def take_from_website(wordSearched):
    """_summary_
    Search in Reverso Context the translate of a word and save in two files
    front.txt and back.txt
    Args: 
        wordSearched(array[str]): it's a array of words 
    """
    file = request_from_website(wordSearched)
    
    NUMBER_OF_CARDS = 10
    examples_content = file.find(id="examples-content")
    front = examples_content.find_all(attrs={"class": "src ltr"})
    back = examples_content.find_all(attrs={"class": "trg ltr"})
    print("Phrases Scraped from website")

    count = 0
    fronts = []
    backs = []

    for item, item2 in zip(front, back):
        if count == NUMBER_OF_CARDS:
            break
        fronts.append(item.get_text().strip()+"\n")
        backs.append(item2.get_text().strip()+"\n")
        count += 1
    print("Phrases cleaned")

    fileWork.openWriteFile(fronts, "front.txt")
    fileWork.openWriteFile(backs, "back.txt")
    print("Phrases saved for file")
    pass

    """
    tratar as frases retirar tab quebra de linha desnecessaria {check}
    concatenar o primeiro com a tradução do segundo{cheak}
    adicionar o audio em ingles {check}
    criar um arquivo apkg to import to anki {check}
    Mover os arquivos audio para a pasta collection anki {check}
    importar para o anki {check}
    """
