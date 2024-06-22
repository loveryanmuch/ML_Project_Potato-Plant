def url_encode(text):
    encoded_text = []
    for char in text.strip():
        if char == ' ':
            encoded_text.append('%20')
        else:
            encoded_text.append(char)
    return ''.join(encoded_text)

