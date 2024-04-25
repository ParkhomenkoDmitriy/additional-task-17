def remove_vowels(input_text):
    vowels = "aeiouAEIOUаеиоуыэюяАЕИОУЫЭЮЯіІїЇ"
    for vowel in vowels:
        input_text = input_text.replace(vowel, '')
    return input_text


text = input("Введите текс латиницей или кириллицей: ")

print(f'исходный текст: {text}')
print(f'текст без гласных: {remove_vowels(text)}')
