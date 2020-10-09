import random
print("H A N G M A N")
response = input('Type "play" to play the game, "exit" to quit:')
while response != "exit":
    if response != "play":
        response = input('Type "play" to play the game, "exit" to quit:')
        continue

    possible_words = ["florida", "love", "college", "amazing"]
    random.shuffle(possible_words)
    word = "-" * len(possible_words[0])
    counter = 0
    live_count = 0
    guessed_letters = []

    while live_count < 8:
        print("")
        print(word)
        letter = input("Input a letter: ")

        if len(letter) != 1:
            print("You should input a single letter")
            continue
        if not letter.islower() or not letter.isalpha():
            print("It is not an ASCII lowercase letter")
            continue
        if letter in set(guessed_letters):
            print("You already typed this letter")
            continue
        else:
            guessed_letters.append(letter)
        if letter in set(possible_words[0]):
            for char in possible_words[0]:
                if letter == char:
                    word = word[:counter] + letter + word[counter+1:]
                counter += 1
            counter = 0
        else:
            print("No such letter in the word")
            live_count += 1
        if word == possible_words[0]:
            print("You guessed the word!\nYou survived!")
            break

    if live_count == 8:
        print("You are hanged!")

    response = input('\nType "play" to play the game, "exit" to quit:')
