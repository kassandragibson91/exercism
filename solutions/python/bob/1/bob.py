def response(hey_bob):
    if not hey_bob.strip():
        return "Fine. Be that way!"
    
    if hey_bob.isupper() and hey_bob[-1] == '?':
        return "Calm down, I know what I'm doing!"
    
    if hey_bob.strip().endswith('?'):
        return "Sure."

    if hey_bob.isupper():
        return "Whoa, chill out!"

    return "Whatever."
