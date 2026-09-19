# get the string from the user
def get_string():
    user_str = input("Please enter your desire sentence: ").split()
    return user_str

# finding the longest word
def longest_word(string):
    longest_word = max(string, key=lambda s: len(s))
    return longest_word

# main
def main():
    answer = 'y'
    while answer.lower() == 'y':
        sentence = get_string()
        long_word = longest_word(sentence)
        print(long_word)

        answer = input("Do you want to continue(y/n): ")


if __name__ == "__main__":
    main()