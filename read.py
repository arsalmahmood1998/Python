import ReadVocab

vocab=ReadVocab.readVocab("Grammer.txt")
try:
    file=open("Random.txt","r")
    for line in file:
        for word in line:
            print(vocab[word]["P"], end = vocab[word]["E"])
except FileNotFoundError:
    print("Text File not found")
except KeyError:
    print("Vocab file is Empty")
