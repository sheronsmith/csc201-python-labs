# Lab 8: Prints all 10 verses of the song "This Old Man."

def print_verse(number_word: str, second_line: str) -> None:
    # Prints one verse. The number and the second line change each time.
    print('This old man, he played ' + number_word + ',')
    print(second_line)
    print('With a knick-knack paddywhack,')
    print('Give a dog a bone,')
    print('This old man came rolling home.')
    print()


def main(args: list[str]) -> int:
    # Uses the same function 10 times, once for each verse.
    print_verse('one', 'He played knick-knack on my thumb.')
    print_verse('two', 'He played knick-knack on my shoe.')
    print_verse('three', 'He played knick-knack on my knee.')
    print_verse('four', 'He played knick-knack on my door.')
    print_verse('five', 'He played knick-knack on my hive.')
    print_verse('six', 'He played knick-knack on my sticks.')
    print_verse('seven', 'He played knick-knack on my heaven.')
    print_verse('eight', 'He played knick-knack on my gate.')
    print_verse('nine', 'He played knick-knack on my spine.')
    print_verse('ten', 'He played knick-knack once again.')

    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
