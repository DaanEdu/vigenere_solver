import english_quadgrams
import re

# Display the group information
def group_info():
    return [("0999635", "Daan Kraaijeveld", "INF1I")]


# Encrypt a plaintext into vigenere with the given key
def encrypt_vigenere(plaintext, key):
    plaintext = plaintext.lower().replace(' ', '')
    print([plaintext[i:i+len(key)] for i in range(0, len(plaintext), len(key))])


# Get the quadgram fitness of a given string, lower is better
def quadgram_fitness(text):
    res = 0
    text = re.sub(r'[^A-Za-z]', '', text.lower().replace(' ', ''))

    for index, char in enumerate(text):
        quadgram = text[index:index+4]

        if quadgram in english_quadgrams.quadgram_score:
            res += english_quadgrams.quadgram_score[quadgram]
        else:
            if len(quadgram) > 3:
                res += 23

    return round(res, 7)
    

encrypt_vigenere("A monkey tail is also the name of a plant", "monkey")