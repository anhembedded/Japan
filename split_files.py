import os

def split_file(input_filename, output_prefix, lines_per_chunk, base_dir):
    """
    Splits a file into multiple parts.
    """
    try:
        with open(os.path.join(base_dir, input_filename), 'r', encoding='utf-8') as f:
            lines = f.readlines()
    except FileNotFoundError:
        print(f"Error: {input_filename} not found.")
        return

    chunk_number = 1
    for i in range(0, len(lines), lines_per_chunk):
        chunk = lines[i:i + lines_per_chunk]
        output_filename = os.path.join(base_dir, f"{output_prefix}_part_{chunk_number}.txt")
        with open(output_filename, 'w', encoding='utf-8') as f:
            f.writelines(chunk)
        print(f"Created {output_filename}")
        chunk_number += 1

def main():
    """
    Main function to split the vocabulary files.
    """
    base_dir = 'c:/Users/hoang/Desktop/japanese'
    
    # Split the full version file
    # Each entry is 5 lines (hiragana, kanji, english, romaji, blank)
    # So, 100 words = 500 lines
    split_file('jlpt_n5_full.txt', 'jlpt_n5_full', 500, base_dir)

    # Split the hiragana-only file
    # Each entry is 1 line
    # So, 100 words = 100 lines
    split_file('jlpt_n5_hiragana_only.txt', 'jlpt_n5_hiragana_only', 100, base_dir)

if __name__ == "__main__":
    main()
