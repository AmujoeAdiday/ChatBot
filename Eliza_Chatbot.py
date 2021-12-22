
import re
import random



#this is to use the first time the user inputs the Name
greeting_list = ["Nice to meet you", "Hello", "It is nice to start a conversation with you,"]

#the first response after the user puts the name
initial_Q_list = [
    "How are you today?\n", "Tell me about your day\n", "How do you feel today?\n",
    "How would you like to start our conversation today?\n",
]

#this is the intro of ELiza
intro_list = [
    "I'm Eliza ChatBot, I'm here to consult your relationship matter. \nFirst of all I would like you answers my\
    question as honestly as possible because it is the way I can help you more effectively\n\n",
    "My name is Eliza, today I'm gonna consult you with your issues in a relationship.\nPlease response my questions\
    as accurate as possible if you could so that I can do my best at this.\n\n",
    "You can call me Eliza ChatBot. Today I will be more than happy to consult your issues. \nFeel free to tell me\
    any details you can think of as it might be helpful to allow me to do my best that way\n\n"
]

#this list is used to ask about when the user put the feeling words in
feeling_question_list = ["Can you tell me the reason that you are", "Why do you think that you are",
                         "Can you explain what have caused you to feel", "What make you","How do you feel", "What is the reason to make you feel"]

#this list is to ask the user when they input ...ends with ed
EndsWithEd_question_list = [
    "Could you explain in detail about the @ ?\n", "Can you share more details to the @ ?\n"
    , "How did that @ happen ?\n", "Ohh, Do you mind telling me this @ in more details ?\n"
    , "Why did the @ happen ?\n", "When did that @ occur ?\n", "How could that @ happen ?\n"
]

Fam_Frnd_Q_list = [
    "What could possibly be the cause that your # to do that ?\n", "Hmm, Why did your # do that ?\n",
    "How did your # ending up being like that ?\n", "What is your opinion that your # has done that ?\n",
]
confused_w_response_question = [
    "I don't totally get what you mean. Can you tell me more please?\n",
    "Can you go to this detail in depth, please?\n",
    "Do you mind going over this matter in much more detail like in a particular situation?\n",
    "Interesting, but can you provide me in more details like describe in terms of people, feelings, thing that had happened?\n",
    "If you can explain in more detail which like relate to people around you or caused you to be like this, or even all related feeling, I would be greatly appreciated.\n"
]


def recognize_name(response):
    # shuffle greeting_list ,intro_list, initial_Q
    random.shuffle(greeting_list)
    random.shuffle(intro_list)
    random.shuffle(initial_Q_list)

    name_ex = r"(my name is|i am|I am|My name is|I'm|i'm|It's|it's|I go by|i go by|You can call me|you can call me)* ([A-Za-z]+).*"
    answer = re.sub(name_ex, r'\2', response)
    return str(greeting_list[0] + " " + answer + "\n" + intro_list[0] + "\n" + initial_Q_list[0])


def detect_feeling(response):
    # source >> https://www.quora.com/How-do-you-match-an-exact-word-with-Regex-Python
    chk = re.compile(r"\b(sad|happy|excited|nervous|happiness|hurt|good|okay|ok|tired|unhappy|depressed|sadness|saddened|bad|joyful|joy|joyfulness)\b")
    answer = re.findall(chk, response)
    if len(answer) > 0:
        random.shuffle(answer)
        return answer[0]
    else:
        return None


def detect_Ed_words(response):
    new_string = re.findall(r"\b(\w+)ed\b", response)
    if len(new_string) > 0:
        random.shuffle(new_string)
        return new_string[0]+"ing"
    else:
        return None



def detect_fam_frnd(response):
    chk = re.compile(r"\b(mom|mother|dad|father|parent|friend|boyfriend|bf|girlfriend|gf|bro|brother|sister|aunt|uncle|son|daugther)\b")
    answer = re.findall(chk, response)
    if len(answer) > 0:
        random.shuffle(answer)
        return answer[0]
    else:
        return None



def formulate_Q_for_fam_frnd(word):
    # shuffle of available question list
    random.shuffle(Fam_Frnd_Q_list)

    new_list = Fam_Frnd_Q_list[0].split()
    index_wd = 0
    for i in range(len(new_list)):
        if new_list[i] == '#':
            index_wd = i

    return Fam_Frnd_Q_list[0].replace(Fam_Frnd_Q_list[0].split()[index_wd], word)


def formulate_Q_for_EdWord(word):
    # shuffle of available question list
    random.shuffle(EndsWithEd_question_list)

    new_list = EndsWithEd_question_list[0].split()
    index_wd = 0
    for i in range(len(new_list)):
        if new_list[i] == '@':
            index_wd = i

    return EndsWithEd_question_list[0].replace(EndsWithEd_question_list[0].split()[index_wd], word)


def formulate_Q_feeling(response):
    # shuffle of available question list
    random.shuffle(feeling_question_list)

    # shuffle the feeling words found
    # random.shuffle(detect_feeling(response))

    return feeling_question_list[0] + " " + detect_feeling(response) + "?\n"




# Start Eliza bot
user_response = input("What is your name?\n")
res = input(recognize_name(user_response))

flag = "bye"

while res != flag:

    #all possibilities
    # G1 >> not match any group
    # 1> [0,0,0]
    # G2 >> match 1 group
    # 2> [1,0,0]
    # 3> [0,1,0]
    # 4> [0,0,1]
    # G3 >> match 2 groups
    # 5>[1,1,0]
    # 6>[1,0,1]
    # 7>[0,1,1]
    # G4>> match 3 groups
    # 8> [1,1,1]


    # G4

    if (detect_feeling(res) != None) and (detect_Ed_words(res) != None) and detect_fam_frnd(res) != None:
        #print("G 1 1 1")
        choice = random.randint(0, 2)
        #print("CHoice ",choice)
        if choice == 0:
            res = input(formulate_Q_feeling(res))

        elif choice == 1:
            res = input(formulate_Q_for_EdWord(detect_Ed_words(res)))

        else:
            res = input(formulate_Q_for_fam_frnd(detect_fam_frnd(res)))


    # G3
    elif detect_feeling(res) != None and detect_Ed_words(res) != None and detect_fam_frnd(res) == None:
        #print("G 1 1 0")
        choice = random.randint(0, 1)
        if choice == 0:
            res = input(formulate_Q_feeling(res))
        else:
            res = input(formulate_Q_for_EdWord(detect_Ed_words(res)))

    elif detect_feeling(res) != None and detect_Ed_words(res) == None and detect_fam_frnd(res) != None:
        #print("G 1 0 1")
        choice = random.randint(0, 1)
        if choice == 0:
            res = input(formulate_Q_feeling(res))
        else:
            res = input(formulate_Q_for_fam_frnd(detect_fam_frnd(res)))

    elif detect_feeling(res) == None and detect_Ed_words(res) != None and detect_fam_frnd(res) != None:
        #print("G 0 1 1")
        choice = random.randint(0, 1)
        if choice == 0:
            res = input(formulate_Q_for_EdWord(detect_Ed_words(res)))
        else:
            res = input(formulate_Q_for_fam_frnd(detect_fam_frnd(res)))


    #G2
    elif detect_feeling(res) != None and detect_Ed_words(res) == None and detect_fam_frnd(res) == None  :
        #print("G 1 0 0")
        res = input(formulate_Q_feeling(res))

    elif detect_feeling(res) == None and detect_Ed_words(res) != None and detect_fam_frnd(res) == None:
        #print("G 0 1 0")
        res = input(formulate_Q_for_EdWord(detect_Ed_words(res)))

    elif detect_feeling(res) == None and detect_Ed_words(res) == None and detect_fam_frnd(res) != None :
        #print("G 0 0 1")
        res = input(formulate_Q_for_fam_frnd(detect_fam_frnd(res)))

    # G1
    else:
    # elif (detect_feeling(res) == None) and ((res) == None) and (detect_Ed_words(res) == None):
        #print("G 0 0 0")
        random.shuffle(confused_w_response_question)

        res = input(confused_w_response_question[0])






