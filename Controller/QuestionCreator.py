import nltk
import sys
import nltk
import re
import time

import os,glob
from gingerit.gingerit import GingerIt

import nltk
from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenizer
import random,time
from Controller import vik_test_codes
from Controller  import ConnectionToNeo4j,QuestionCreator,NestedQuestionCreator,vari,SpeachToText,AudioRecorder

sys.path.insert(0, '../Database')
from Database import NonTechnicalQuestionDirectory
from nltk.stem import WordNetLemmatizer
from nltk.wsd import lesk
from nltk.corpus import wordnet as wn
a={}
b=[]
train_text = state_union.raw("2005-GWBush.txt")
# keywords ="Object oriented programming"


question = ""

#gets the keyword and creates a non technical question
def gen_Question(keywords,qno):
    print(keywords)
    print("keywors")
    typo = "nonested"
    typo2 = "nontechnical"
    custom_sent_tokenizer = PunktSentenceTokenizer(train_text)
    tokenized = custom_sent_tokenizer.tokenize(keywords)
    try:
        for i in tokenized:
            words = nltk.word_tokenize(i)
            tagged = nltk.pos_tag(words)
            # print(tagged)
            # namedEnt = nltk.ne_chunk(tagged, binary=True)
            # gen_Question(namedEnt)
            # namedEnt.draw()


        key, words = zip(*tagged)
        compare = list(words)
        #print(key)
        print(words)
        a = dict(zip(key, words))
        b= dict(zip(words, key))

        print(a)
        # print("hey")
        print([b for b, v in a.items() if v in NonTechnicalQuestionDirectory.l1])

    except Exception as e:
        print(str(e))


    if compare == NonTechnicalQuestionDirectory.l1:
        question = "What "+ b['NNP']
        # print(question)
    elif compare == NonTechnicalQuestionDirectory.l2:
        question = "Why should we " +b['NN']+" "+ b['PRP']+"?"
        # print(question)
    elif compare ==  NonTechnicalQuestionDirectory.l3:
        question = "What are " + b['PRP$'] + " " + b['NNS'] + "?"
        # print(question)
    elif compare ==  NonTechnicalQuestionDirectory.l4:
        question = "Tell about " + b['PRP'] + "?"
        # print(question)
    elif compare ==  NonTechnicalQuestionDirectory.l5:
        question = "What are your " + b['JJ'] + " " + b['NNS']  + "?"
        # print(question)
    elif compare ==  NonTechnicalQuestionDirectory.l6:
        question = "What is  " + b['PRP$'] + " " + b['JJ'] +" "+b['NN'] + "?"
        # print(question)
    else:
        question = "Explain about your " + keywords+" and its technologies?"
        # print(question)


    parser = GingerIt()
    grammer_corrected_question_list = parser.parse(question)
    question = grammer_corrected_question_list.get("result")
    print(question ,"hiiiiiiiiiiiiiiiiiii")
    print(vik_test_codes.question(question, qno))

    #jjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjj
    voice_record = AudioRecorder.audio_recorder(qno)
    print("error testing question numberrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrr"+str(qno))
    answer_validity = SpeachToText.validation("", typo2, typo, "question" + str(qno))[0]



    if str(qno) == "20" or qno == 20:

        print(
            "jjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhjjjjjjjjjjj")
        open('Controller/questionSaver_testing.py', 'w').close()

        # fruits = ["gcpq = 'end'\n"]

        fruits = ["global gcpq\n", "gcpq = 'end'\n"]
        new_file = open("Controller/questionSaver_testing.py", mode="a+", encoding="utf-8")
        new_file.writelines(fruits)
        for line in new_file:
            print(line)

        new_file.close()

        filelist = glob.glob("Audio/*.wav")
        for file in filelist:
            os.remove(file)
    # if qno == "20" or qno == 20:
    #
    #     filelist = glob.glob("Audio/*.wav")
    #     for file in filelist:
    #         os.remove(file)

    return question

