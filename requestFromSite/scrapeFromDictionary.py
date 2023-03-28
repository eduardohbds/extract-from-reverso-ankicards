##This scrape from reverso Context
from bs4 import BeautifulSoup
import requests
from headersToAccessSite import headers

##This scrape from reverso Context
def request_from_website(wordToBeSearched):
    """_summary_
    resquest from website Reverso Context the html page with translate
        passed by variable wordToBeSearched 
    
    Args:
        wordToBeSearched (str): _description_
        
    Returns:
        list: a html web page passed by method prettify() from bs4
    """
    website = "https://dictionary.cambridge.org/pt/dicionario/ingles-portugues/"
    page = requests.get(
        website+wordToBeSearched,
        headers=headers.headersDictionary, cookies=headers.cookiesDictionary)
    soup = BeautifulSoup(page.content, 'html.parser')
    print("####################################################################################")
    print("Request from website successful")
    return soup


def take_from_website(wordToBeSearched):
    """_summary_
    Search in Reverso Context the translate of a word and save in two files
    front.txt and back.txt
    Args:
        wordToBeSearched (str): _description_
        
    Returns:
        list,list: prior is a list of pronunciations later is a list of 
        class grammar of the word and the definition 
    """
    response = request_from_website(wordToBeSearched)
    
    pronunciations = response.findAll(attrs={"class": "ipa dipa"})


    pronunciations_language = ["UK", "US"]
    definitions = response.findAll(attrs={"class": "def ddef_d db"})
    definitions_translated = response.findAll(
        attrs={"class": "trans-block dtrans-block"})
    class_grammar_words = response.findAll(attrs={"class": "pos dpos"})

    value = "pronunciation: "
    def_defTranslated_classfication = "definition: " +"\n"

    for pronunciation, pronunciation_language in zip(pronunciations, pronunciations_language):
        print(pronunciation_language+pronunciation.get_text())
        value+=(pronunciation_language+pronunciation.get_text()) + " "

    for definition, grammar_word in zip(definitions, class_grammar_words):
        print(grammar_word.get_text() + ":" + definition.get_text())
        def_defTranslated_classfication+=(grammar_word.get_text() + ":" + definition.get_text()) + "\n"

    for definition_translated in definitions_translated:
        print(definition_translated.get_text().strip())
        def_defTranslated_classfication += (definition_translated.get_text().strip())
    #isso é um delimitador usado para saber ate quando parar quando estiver lendo
    #def_defTranslated_classfication = def_defTranslated_classfication + '\n' +'pause_here' + '\n'

    return value,def_defTranslated_classfication
    

"""
minha ideia é colocar uma palvra no final do vetor de value e value2
para que quando for fazer leitura ele ir ate um certo ponto 
e que quando for ler o arquivo para traduzir para o audio tbm va 
ate certo ponto 
então tenho q modificar o passa para a função que traduz para o audio e aquela 
que le os arquivos
Once we had a disease decimated us.
UKˈdes.ɪ.meɪtUSˈdes.ə.meɪtUKˈdes.ɪ.meɪt 
Uma vez já tivemos uma grande missão, mas a doença nos dizimou.
verb:to kill a large number of something, or to reduce something severely
verb:(of disease, battle etc) to reduce greatly in number
verb:to kill a large number of something, or to reduce something severelydizimar
verb:to kill a large number of something, or to reduce something severely
verb:(of disease, battle etc) to reduce greatly in number
verb:to kill a large number of something, or to reduce something severely
pause_here

hereby
eyelid
batted
clenched
mole
shroud
flutter
croak
slight
"""
