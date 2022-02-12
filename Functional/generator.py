import random
USER_LETTERS = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y',
                     'z','0','1','2','3','4','5','6','7','8','9','0','A','B','C','D','E','F','G','H','I','J','K','L','M',
                     'N','O','P','Q','R','S','T','U','V','W','X','Y','Z', "_"]
PASSWORD_LETTERS = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y',
                     'z','0','1','2','3','4','5','6','7','8','9','0','A','B','C','D','E','F','G','H','I','J','K','L','M',
                     'N','O','P','Q','R','S','T','U','V','W','X','Y','Z','!','@','#','$','%','&','*']
NAMES = ["Marcin", "Tomasz", "Michal", "Witold", "Piotr", "Zygfryd", "Zygmunt", "Grzegorz", "Maciej", "Karol", "Jakub",
         "Oskar"]
LASTNAMES = ["Ostrowicz", "Marcinkiewicz", "Marcinowski", "Otopowicz", "Hala", "Wrona", "Nowak", "Czubak", "Ochman",
             "Czajka", "Pies", "Kot","Myszka", "Roman", "Kaszuba", "Sala", "Rogala"]

def user_generator(char_number = 12):
    """generate userName based on site requirements"""
    user = ""
    for i in range(char_number):
        i = random.randrange(len(USER_LETTERS) - 1)
        user += USER_LETTERS[i]
    return user

def password_generator(char_number = 20):
    """generate password based on site requirements"""
    password = ""
    for i in range(char_number):
        i = random.randrange(len(PASSWORD_LETTERS) - 1)
        password += PASSWORD_LETTERS[i]
    return password

def name_generator():
    """generate random name from list"""
    name = NAMES[random.randrange(len(NAMES)) - 1]
    return name

def last_name_generator():
    """generate random name from list"""
    last_name = LASTNAMES[random.randrange(len(NAMES)) - 1]
    return last_name

