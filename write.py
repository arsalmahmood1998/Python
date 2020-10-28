import random
import ReadVocab

try:
    length=int(input("Enter length of String: "))
    vocab=ReadVocab.readVocab("Grammer.txt")
    alphabets=list(vocab.keys())
    file=open("Random.txt","a")
    for i in range(length):
        try:
            randomIndex=random.randint(0,len(alphabets)-1)
        except ValueError:
            print("Vocab file is empty")
            exit()
        file.write(alphabets[randomIndex])
except ValueError:
    print("You have entered an invalid number")
except IndexError:
    print("List size is large")
