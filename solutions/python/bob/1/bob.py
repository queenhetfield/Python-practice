def response(hey_bob):
    stripped = hey_bob.strip()
    if stripped == '':
        return "Fine. Be that way!"
    if '?' == stripped[-1]:
        if hey_bob.upper() == hey_bob and any(c.isalpha() for c in hey_bob):
            return "Calm down, I know what I'm doing!"
        return 'Sure.'
    if hey_bob.upper() == hey_bob and any(c.isalpha() for c in hey_bob):
            return 'Whoa, chill out!'
    return "Whatever."
