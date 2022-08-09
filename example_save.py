import disformat

tokens = disformat.load_tokens('tokens.txt')
ids = disformat.load_ids('ids.txt')

disformat.oldest_tokens(tokens, save='sorted_tokens.txt', add_note=True)
disformat.oldest_ids(ids, save='sorted_ids.txt', add_note=True)
