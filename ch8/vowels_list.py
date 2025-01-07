vowels = ['a', 'e', 'i', 'o', 'u']  # Define vowels inside the function

def is_vowel(letter):
    # Checks if the input letter is a vowel
    return letter.lower() in vowels  # Make the check case-insensitive


def main():
    # Prompt the user to enter text
    text = input('Enter text: ').strip()  # Remove extra spaces

    # Count vowels in the input
    vowel_counts = {vowel: 0 for vowel in vowels}  # Initialize count for each vowel
    for char in text:
        if is_vowel(char):
            vowel_counts[char.lower()] += 1

    print('Vowel counts:')
    for vowel, count in vowel_counts.items():
        print(f'{vowel}: {count}')
    print(f'Total vowels: {sum(vowel_counts.values())}')


if __name__ == '__main__':
    main()
