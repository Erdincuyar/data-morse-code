"""
This module provides functions to encode text into Morse code.

Functions:
- encode(text): Encodes a given text into Morse code, separating words with a pipe (|) and
  letters with a space.
- encode_word(word): Encodes a single word into Morse code, separating letters with a space.
"""

from morse.mapping import MORSE

def encode_word(word):
    """
    Tek bir kelimeyi Morse koduna çevirir.
    Harfler arasına bir boşluk koyar.
    """
    # Her harfi Morse karşılığına çevirip listeye atıyoruz
    # .upper() kullanıyoruz ki 'h' ile 'H' aynı sonucu versin
    encoded_letters = []
    for letter in word.upper():
        if letter in MORSE:
            encoded_letters.append(MORSE[letter])

    # Listeyi boşlukla birleştiriyoruz: ".... .."
    return " ".join(encoded_letters)

def encode(text):
    """
    Tüm metni Morse koduna çevirir.
    Kelimeler arasına '|' koyar.
    """
    # Metni kelimelere bölüyoruz: ["Hi", "Guys"]
    words = text.split()

    # Her kelimeyi encode_word ile çeviriyoruz: [".... ..", "--. ..- -.-- ..."]
    encoded_list = [encode_word(w) for w in words]

    # Kelimeleri pipe (|) ile birleştiriyoruz: ".... ..|--. ..- -.-- ..."
    return "|".join(encoded_list)

if __name__ == "__main__":
    # Example usage for one word
    EXAMPLE_TEXT = "abc"
    ENCODED_TEXT = encode_word(EXAMPLE_TEXT)
    print(f"Encoded word '{EXAMPLE_TEXT}' to Morse code: '{ENCODED_TEXT}'")

    # Example usage for a sentence
    EXAMPLE_TEXT = "abc ABC"
    ENCODED_TEXT = encode(EXAMPLE_TEXT)
    print(f"Encoded '{EXAMPLE_TEXT}' to Morse code: '{ENCODED_TEXT}'")
