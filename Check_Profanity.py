import re

"""
# profanity_words.txt is a text file containing racial slurs having one word per line

# Assumptions :

    # All racial words are of same rank i.e each word is equally disrespectful
    # Profanity of a tweet is divided in 4 levels
        - Extreme = Profanity words more than 5
        - Moderate = Profanity words in range [3-5]
        - Mild/Low = Profanity words in range [1-2]
        - Zero = Profanity words is equal to 0

"""
def check_profanity(tweet):
    with open('profanity_words.txt', 'r') as file:
        profanity_words = file.read().splitlines()
    words = re.findall(r'\b\w+\b', tweet)
    profanity_count = sum(1 for word in words if word.lower() in profanity_words)
    return profanity_count

tweet = "This is an example tweet with some bad words."
profanity_count = check_profanity(tweet)


if profanity_count > 5:
    print("This tweet contains {} instances of profanity. Profanity level is Extreme".format(profanity_count))

elif 2<profanity_count<=5:
    print("This tweet contains {} instances of profanity. Profanity level is Moderate".format(profanity_count))

elif 1<=profanity_count<=2:
    print("This tweet contains {} instances of profanity. Profanity level is Mild".format(profanity_count))
else:
    print("This tweet does not contain any instances of profanity. Profanity level is Zero")
