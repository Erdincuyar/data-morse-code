from morse.mapping import MORSE

# 1. Sözlüğü ters çevir
DEC_MORSE = {v: k for k, v in MORSE.items()}

# 2. Önce kelime çözücü (Küçük parça)
def decode_word(morse_word):
    morse_letters = morse_word.split(" ")
    decoded_letters = [DEC_MORSE[code] for code in morse_letters if code in DEC_MORSE]
    return "".join(decoded_letters)

# 3. Sonra cümle çözücü (Büyük parça)
def decode(morse_text): # <--- BU İSİM DOĞRU MU KONTROL ET
    morse_words = morse_text.split("|")
    decoded_list = [decode_word(w) for w in morse_words]
    return " ".join(decoded_list)

# 4. En son çalıştırma bloğu
if __name__ == "__main__":
    from morse.encoder import encode

    encoded_text = ".... ..|--. ..- -.-- ..."
    print(f"Morse Hali: {encoded_text}")

    # Burada 'decode' fonksiyonunu çağırıyoruz, yukarıdakiyle aynı olmalı
    decoded_result = decode(encoded_text)
    print(f"Geri Çözülmüş: {decoded_result}")
