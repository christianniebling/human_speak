import random

# functions
def breakup_string(input_text):
    ret_list = input_text.split()
    return ret_list

def random_speak(phrase_list, num_speak, max_speak):
    for i in range(num_speak):
        num_phrases = random.randrange(1,max_speak)
        sentance = ""
        for j in range(num_phrases):
            sentance = sentance + random.choice(phrase_list) + " "
        if i % 2 == 0:
            print("Speaker 1: " + sentance)
        else:
            print("Speaker 2: " + sentance)
            
def english_speak(subjects, verbs, adjectives, num_speak):
    # Subject-Verb-Adjective sentances
    subject_list = breakup_string(subjects)
    verb_list = breakup_string(verbs)
    adjective_list = breakup_string(adjectives)
    
    for i in range (num_speak):
        subject = random.choice(subject_list)
        verb = random.choice(verb_list)
        adjective = random.choice(adjective_list)
        sentance = subject + " " + verb + " " + adjective
        
        if i % 2 == 0:
            print("Speaker 1: " + sentance)
        else:
            print("Speaker 2: " + sentance)
        
    
    
# sample text 1
input_text = "ADORE YOU ALL OF ME ALLMY LIFE AT LAST BABY LOVE CRAZY NLUV HAPPY 2GTHR IGOTU BABE I'LLBE THERE I'M YOURS LEAN ONEME ONLY YOU LOVE SHAK LUVME TENDR MY GIRL PER FECT STILL THE 1 SUGAR SUGAR SUMMR LOVIN"

# sample text 2
subjects = "ME YOU BAE CUITE"
objects = ""
verbs = "LOVE HUG SMILE LAUGH"
adjectives = "COOL SWEET YAAAS GOAT"

# sample text 3
phrases = ["BAE", "CUTIE", "LOVE", "HUG ME", "LAUGH", "SWEET", "SMILE", "YAAAS", "CALL ME", "GOAT", "ONLY YOU", "COOL", "MILK"]

# variables
num_speak = 10
max_speak = 6

# run time ;)
my_input = breakup_string(input_text)
random_speak(phrases, num_speak, max_speak)

print("------------- switching modes -------------")

#trying out english_speak
english_speak(subjects, verbs, adjectives, num_speak)
