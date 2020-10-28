
def readVocab(path):
    try:
        vocab={}
        grammer=open(path,"r")
        for line in grammer:
            for word in line:
                dataList=line.split(",")
                vocab[dataList[0]]={"P":dataList[1],"E":dataList[2]}
    except FileNotFoundError:
        print("Vocab File not found")
    return vocab
