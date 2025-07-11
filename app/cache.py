cache = {}

def store_result(text: str, result: dict):
    cache[text] = result
    for word in result['top_words']:
        cache[word[0]] = result

def search_term(term: str):
    import re
    for key in cache:
        if re.search(term, key):
            return cache[key]
    return None
