def openReadFile(fileName):
    """_summary_

    Args:
        fileName (str): File name that you desire to extract the text

    Returns:
        list[str]: all the lines of the file
    """
    file = []
    path = "C:/Users/eduar/Studyspace/extract-from-reverso-ankicards/"
    path = path + fileName
    with open(path, 'r', encoding="utf-8") as reader:
        #O problema ta aqui por que ele ta lendo o arquivo e não esta separando
        #por quebra de linha
        file = reader.readlines()
        pass
    return file


def openWriteFile(content, fileName):
    """_summary_
    It write the content onto the fileName if the file is not create 
    the function will do
    Args:
        content (list): variable with the content to write onto the file
        fileName (string): variable with the name of the file, make sure 
        specify the extension of file, e.g. file.txt,file.json. 
    """
    encoding = 'utf-8'
    path = "C:/Users/eduar/Studyspace/extract-from-reverso-ankicards/"
    path = path + fileName
    with open(path, 'w', encoding=encoding) as writer:
        writer.writelines(content)
        # for item in content:
        #     writer.write(item)
        # pass
    pass
