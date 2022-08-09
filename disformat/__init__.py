from base64 import b64decode as decode
import re

def load_tokens(file):
    tokens = []
    for line in [x.strip() for x in open(file, errors="ignore").readlines() if x.strip()]:
        for regex in (r"[\w-]{24}\.[\w-]{6}\.[\w-]{38}", r"mfa\.[\w-]{84}"):
            for token in re.findall(regex, line):
                tokens.append(token)
    return tokens

def load_ids(file):
    ids = []
    for line in [x.strip() for x in open(file, errors="ignore").readlines() if x.strip()]:
        for id in re.findall(r"[0-9]{18,19}", line):
            ids.append(id)
    return ids

def youngest_ids(list, save=False, add_note=True):
    if save:
        ordered = [f'{i}\n' for i in sorted(list, reverse=True)]
        with open(save, 'w') as file:
            if add_note:
                file.write('-'*100+'\n'+' '*16+'ids sorted from youngest to oldest. https://github.com/haze-1337\n'+'-'*100+'\n\n')
            file.writelines(ordered)
    return sorted(list, reverse=True)

def oldest_ids(list, save=False, add_note=True):
    if save:
        ordered = [f'{i}\n' for i in sorted(list, reverse=False)]
        with open(save, 'w') as file:
            if add_note:
                file.write('-'*100+'\n'+' '*16+'ids sorted from oldest to youngest. https://github.com/haze-1337\n'+'-'*100+'\n\n')
            file.writelines(ordered)
    return sorted(list, reverse=False)

def youngest_tokens(list, save=False, add_note=True):
    if save:
        ordered = [f'{i}\n' for i in sorted(dict(zip(list, [str(decode(token.split('.')[0]), 'utf-8') for token in list])), reverse=True)]
        with open(save, 'w') as file:
            if add_note:
                file.write('-'*100+'\n'+' '*16+'tokens sorted from youngest to oldest. https://github.com/haze-1337\n'+'-'*100+'\n\n')
            file.writelines(ordered)
    return sorted(dict(zip(list, [str(decode(token.split('.')[0]), 'utf-8') for token in list])), reverse=True)

def oldest_tokens(list, save=False, add_note=True):
    if save:
        ordered = [f'{i}\n' for i in sorted(dict(zip(list, [str(decode(token.split('.')[0]), 'utf-8') for token in list])), reverse=False)]
        with open(save, 'w') as file:
            if add_note:
                file.write('-'*100+'\n'+' '*16+'tokens sorted from oldest to youngest. https://github.com/haze-1337\n'+'-'*100+'\n\n')
            file.writelines(ordered)
    return sorted(dict(zip(list, [str(decode(token.split('.')[0]), 'utf-8') for token in list])), reverse=False)
