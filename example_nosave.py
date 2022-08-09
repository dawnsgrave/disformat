import disformat

tokens = disformat.load_tokens('tokens.txt')
ids = disformat.load_ids('ids.txt')

print(disformat.oldest_tokens(tokens))
print(disformat.oldest_ids(ids))