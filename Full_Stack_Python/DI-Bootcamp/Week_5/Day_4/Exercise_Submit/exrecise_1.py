# with open(filename) as f
from random import choice

def get_words_from_file(filename):
    with open(filename) as f:
    # f = open(filename, 'r')
        word_list = f.readlines()
        
    # wordPerLine = [wordPerLine.replace("\n", "")]
        word_list = [word.replace("\n", "") for word in word_list]
        # f.close()
        return word_list
    


listOfWords = get_words_from_file("sowpods.txt")
# print(listOfWords)
print(choice(listOfWords))

def get_random_sentence(length):
    sentenceInAList = []
    for i in range(length):
        randomWord = choice(listOfWords).lower()
        sentenceInAList.append(randomWord)
        print(sentenceInAList)
    sentence = (" ".join(sentenceInAList))
    return sentence

get_random_sentence(4)

def main():
    '''
    collect amount of words defined by a user and combine it to a senence.
    '''
    userNumber = int(input("Please select a number Between 2-20: "))
    if 2 <= userNumber <= 20:
        userSentence = get_random_sentence(userNumber)
        return userSentence
    else:
        print("the range is incorret")
        



main()


    
     
