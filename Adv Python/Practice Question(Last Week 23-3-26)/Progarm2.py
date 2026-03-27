# Process a user-entered sentence: count vowels/consonants, reverse it, replace spaces with
# underscores, capitalize words

sentence = input("Enter a sentence: ")

vowels = 0
consonants = 0

vowel_set = "aeiouAEIOU"

for ch in sentence:
    if ch.isalpha():  
        if ch in vowel_set:
            vowels += 1
        else:
            consonants += 1


reversed_sentence = sentence[::-1]

modified_sentence = sentence.replace(" ", "_")

capitalized_sentence = sentence.title()


print("\nVowels:", vowels)
print("Consonants:", consonants)
print("Reversed Sentence:", reversed_sentence)
print("Spaces replaced with underscores:", modified_sentence)
print("Capitalized Sentence:", capitalized_sentence)