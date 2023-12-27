from translate import Translator

translate = Translator(to_lang='zh')

with open('test.txt') as text:
    print(translate(text.read()))