import random

phrases = ["BAE", "CUTIE", "LOVE", "HUG ME", "LAUGH", "SWEET", "SMILE", "YAAAS", "CALL ME", "GOAT", "ONLY YOU", "COOL"]
num_speak = 8
max_speak = 8

for i in range(num_speak):
    num_phrases = random.randrange(1,max_speak)
    sentance = ""
    for j in range(num_phrases):
        sentance = sentance + random.choice(phrases) + " "
    if i % 2 == 0:
        print("Speaker 1: " + sentance)
    else:
        print("Speaker 2: " + sentance)