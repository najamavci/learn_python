from zoneinfo import available_timezones


def average_words(strings):
    found = [] #found will store the words that meet a certain condition.
    for item in strings:
        if 4 < len(item) < 8: #The condition checks if the word is longer than 4 letters but shorter than 8 letters.
            found.append(item)
    return found #If the word meets the length condition, it is added to the found list.

#average_words(["sup", "how's", "it", "going", "reflecting", "on", "programs", "and", "coding"])
#This function should return a new list of items. We may print the output as an improvement and assign the result within a variable
words=average_words(["sup", "how's", "it", "going", "reflecting", "on", "programs", "and", "coding"])
print(words)

#output: ["how's", 'going', 'coding']

