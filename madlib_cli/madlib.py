from string import Formatter

def welcome():
    """
    A function to write a welcoming message with the instruction
    """
    print("""this game is about to provide certain types of words and to be filled in a hidden text , and it will show you the hilarious result!!!!
    you should provide the word type as described:""")

def input_words(word_types):
    """
    A function to take words 'string' input as required
    """   
    words = []
    for type in word_types:
            word = input(f"please enter {type} >")
            words.append(word)
    return tuple(words)


def read_template(path):
    """
    this function will red the file from the .txt file in path. if the path is not found it will expect and error.
    """
    isNotFound = False
    try:
        f = open(path)
    except FileNotFoundError:
        content = "Error: Sorry the file does not exist!"
        isNotFound = True
             
    else:
        content = f.read()
        f.close()
    finally:
        if(isNotFound):
            raise FileNotFoundError
        return content

def parse_template(content):
    """
    this function will take the text and return the word type in a tuple , and will return a text with the word type replaced with {}
    """
    word_types = []
    for i in Formatter().parse(content):
         if i[1] != None:
             word_types.append(i[1])
    
    for key in word_types:
        content = content.replace("{"+key+"}","{}")

    return  content,tuple(word_types)

def merge(content,args):
    """
    this function will insert the inputs into the text and will return the result
    """
    return content.format(*args)


def wirte_new_file(content):
    """
    this function will write and store the result of the inserted input into the text in a new file
    """
    with open("assets/answers.txt", "w") as f:
            f.write(f"This is the answers:\n{content}")
    

if __name__== "__main__":
    welcome()
    content = read_template("assets/dark_and_stormy_night_template.txt")
    strip_text,word_types=parse_template(content)
    answers = input_words(word_types)
    print(merge(strip_text,answers))
    wirte_new_file(merge(strip_text,answers))
