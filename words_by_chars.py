def countCharacters(words, chars):
    char_count = {}
    for char in chars:
        char_count[char] = char_count.get(char, 0) + 1
    
    result = 0
    for word in words:
        word_count = {}
        for char in word:
            word_count[char] = word_count.get(char, 0) + 1
        
        is_good = True
        for char, count in word_count.items():
            if char_count.get(char, 0) < count:
                is_good = False
                break
        
        if is_good:
            result += len(word)
    
    return result
