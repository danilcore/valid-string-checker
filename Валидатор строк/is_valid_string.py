# is_valid_string

def is_dog(string):
    """ Проверка строки на наличие символа: '@' """
    if string.startswith("@"):
        return True
    else:
        return False

def is_lower(string):
    """ Проверка строки на то, что все её символы в нижнем регистре """
    return string.islower()

def is_number(string):
    """ Проверка строки на наличие чисел """
    return string.isalnum()

def is_underline(string):
    """ Проверка строки на наличие символа нижнего подчеркивания """
    if '_' in string:
        return True
    else:
        return False