
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