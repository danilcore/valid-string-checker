# test_valid_string.py

import is_valid_string as ivs

def test_module():
    print("Тестирование модуля is_valid_string")
    print("is_dog('@noname'): ", ivs.is_dog('@noname'))
    print("is_lower('HyperNick'): ", ivs.is_lower('HyperNick'))
    print("is_number('duckbann2345'): ", ivs.is_number('duckbann2345'))
    print("is_underline('nickname'): ", ivs.is_underline('nickname'))
    
if __name__ == "__main__":
    test_module()
    
