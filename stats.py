def count_words(text):
    words = text.split()
    return(f"Found {len(words)} total words")

def count_characters(text):
    characters = dict()

    for word in text.split():

        word = word.lower()

        for character in word:
            if character not in characters:
                characters[character] = 1
            else:
                characters[character] += 1
    return characters  

def sorted_dict(d):
    return dict(sorted(d.items(), key=lambda item: item[1], reverse=True))