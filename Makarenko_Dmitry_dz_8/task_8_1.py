import re

def email_parse(email: str) ->dict:
    try:
        RE_EMAIL = re.compile(r'[a-zA-Z0-9_.-]+@[a-zA-Z0-9]+(?:\.[a-zA-Z0-9]+)+$')
        assert RE_EMAIL.match(email)
    except AssertionError:
        raise ValueError(f'wrong email: {email}')
    list = re.split(r'@', email)
    result = {'username': list[0], 'domain': list[1]}
    return result


print(email_parse('hodas.work@gmail.com'))
