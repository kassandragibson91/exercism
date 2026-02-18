def translate(text):
    text_array = text.split(' ')

    final = []
    
    for word in text_array:
        final.append(translate_word(word))

    return " ".join(final)
        

def translate_word(text):
    VOWELS = {'a', 'e', 'i', 'o', 'u'}
    
    if text[0] in VOWELS or text.startswith('xr') or text.startswith('yt'):
        return text + 'ay'

    suffix = ''

    for char in text:
        if char == 'y' and len(suffix) > 0:
            break
        if char not in VOWELS:
            suffix += char
        elif char == 'u' and suffix[-1] == 'q':
            suffix += char
        else:
            break
    
    return text[len(suffix):] + suffix + 'ay'
    