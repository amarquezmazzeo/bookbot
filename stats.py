def get_text_wc(text):
    words = text.split()
    return len(words)

def get_chars_dict(text):
    result = {}
    for c in text:
        c = c.lower()
        if c in result:
            result[c] += 1
        else:
            result[c] = 1
    return result

def format_char_dict(dict):
    dict_list = []
    for k, v in dict.items():
        dict_list.append({
            "char":k,
            "num":v
        })
    dict_list.sort(reverse=True, key=lambda x: x['num'])
    return dict_list
        