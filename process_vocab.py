import re
from pykakasi import kakasi

def parse_line(line):
    """
    Parses a line to extract Kanji, Hiragana, and English.
    The format is assumed to be 'Kanji Hiragana English' or ' Hiragana English'.
    """
    line = line.strip()
    parts = re.split(r'\s+', line, maxsplit=2)
    
    if len(parts) == 3:
        # Case with Kanji, Hiragana, English
        kanji, hiragana, english = parts
        # Sometimes the first part is hiragana if there is no kanji
        # A simple check could be if the first two parts are the same
        if kanji == hiragana:
            kanji = ''
        # Or if the first part contains no kanji characters
        elif not any('\u4e00' <= char <= '\u9fff' for char in kanji):
             english = hiragana + ' ' + english
             hiragana = kanji
             kanji = ''

    elif len(parts) == 2:
        # Case with Hiragana, English (no Kanji)
        kanji = ''
        hiragana, english = parts
    else:
        return None, None, None

    return kanji, hiragana, english

def to_romaji(text):
    """Converts Japanese text to Romaji."""
    kks = kakasi()
    result = kks.convert(text)
    return ' '.join([item['hepburn'] for item in result])

def main():
    """
    Main function to process the vocabulary list and generate output files.
    """
    try:
        with open('c:/Users/hoang/Desktop/japanese/vocab/vocaList.txt', 'r', encoding='utf-8') as f:
            lines = f.readlines()
    except FileNotFoundError:
        print("Error: vocaList.txt not found.")
        return

    # Skip header lines
    lines = lines[3:]

    full_version_content = []
    hiragana_only_content = []

    for line in lines:
        if not line.strip():
            continue

        kanji, hiragana, english = parse_line(line)

        if hiragana and english:
            romaji = to_romaji(hiragana)
            
            # Version 1: Full
            # Hiragana, Kanji, English, Romaji
            full_version_content.append(hiragana)
            full_version_content.append(kanji if kanji else hiragana)
            full_version_content.append(english)
            full_version_content.append(romaji)
            full_version_content.append('') # Blank line

            # Version 2: Hiragana-only
            hiragana_only_content.append(hiragana)

    # Write Version 1
    with open('c:/Users/hoang/Desktop/japanese/jlpt_n5_full.txt', 'w', encoding='utf-8') as f:
        f.write('\n'.join(full_version_content))

    # Write Version 2
    with open('c:/Users/hoang/Desktop/japanese/jlpt_n5_hiragana_only.txt', 'w', encoding='utf-8') as f:
        f.write('\n'.join(hiragana_only_content))

    print("Successfully generated jlpt_n5_full.txt and jlpt_n5_hiragana_only.txt")

if __name__ == "__main__":
    main()
