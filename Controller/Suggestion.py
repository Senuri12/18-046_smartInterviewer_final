import os
from Controller import ConnectionToNeo4j,vari
import numpy as np
import importlib
from Database.Result import answerValidation,facialResult,voiceResult





#Vikum answer validation

def getAnswerMark():
    total = 0

    importlib.reload(answerValidation)


    total = int(answerValidation.q1)+int(answerValidation.q2)+int(answerValidation.q3)+int(answerValidation.q4)+int(answerValidation.q5)+int(answerValidation.q6)+int(answerValidation.q7)+int(answerValidation.q8)+int(answerValidation.q9)+int(answerValidation.q10)+int(answerValidation.q11)+int(answerValidation.q12)+int(answerValidation.q13)+int(answerValidation.q14)+int(answerValidation.q15)+int(answerValidation.q16)+int(answerValidation.q17)+int(answerValidation.q18)+int(answerValidation.q19)+int(answerValidation.q20)

    print('Total Answer Validation Mark: {}'.format(total))

    answer = float(format(total))/20.0
    print(answer)


    if answer > 20.0:

        return "Answer validation . You answered well. The given answers well matched with our database Try to use key words that implies the asked question area. Try to build up your answering performance. "

    elif answer > 15.0:
        return "Answer validation . You answered well. The given answers well matched with our database Try to use key words that implies the asked question area. Try to build up your answering performance. "


    elif answer > 10.0:
        return "Answer validation . You answered well. The given answers well matched with our database Try to use key words that implies the asked question area. Try to build up your answering performance. "


    else:
        return "Answer validation . You answered well. The given answers well matched with our database Try to use key words that implies the asked question area. Try to build up your answering performance. "


def getFacialMark():
    total = 0
    importlib.reload(facialResult)

    #qq
    total = int(facialResult.q1)+int(facialResult.q2)+int(facialResult.q3)+int(facialResult.q4)+int(facialResult.q5)+int(facialResult.q6)+int(facialResult.q7)+int(facialResult.q8)+int(facialResult.q9)+int(facialResult.q10)+int(facialResult.q11)+int(facialResult.q12)+int(facialResult.q13)+int(facialResult.q14)+int(facialResult.q15)+int(facialResult.q16)+int(facialResult.q17)+int(facialResult.q18)+int(facialResult.q19)+int(facialResult.q20)
    print('Total Facial Mark: {}'.format(total))

    facial = float(format(total))/20.0
    print(facial)


    if facial > 20.0:
        return "Facial recognition . You answered well. The given answers well matched with our database Try to use key words that implies the asked question area. Try to build up your answering performance. "


    elif facial > 15.0:
        return "Facial recognition . You answered well. The given answers well matched with our database Try to use key words that implies the asked question area. Try to build up your answering performance. "


    elif facial > 10.0:
        return "Facial recognition . You answered well. The given answers well matched with our database Try to use key words that implies the asked question area. Try to build up your answering performance. "


    else:
        return "Facial recognition . You answered well. The given answers well matched with our database Try to use key words that implies the asked question area. Try to build up your answering performance. "


def getVoiceMark():
    total = 0
    importlib.reload(voiceResult)

    #qq
    total = int(voiceResult.q1)+int(voiceResult.q2)+int(voiceResult.q3)+int(voiceResult.q4)+int(voiceResult.q5)+int(voiceResult.q6)+int(voiceResult.q7)+int(voiceResult.q8)+int(voiceResult.q9)+int(voiceResult.q10)+int(voiceResult.q11)+int(voiceResult.q12)+int(voiceResult.q13)+int(voiceResult.q14)+int(voiceResult.q15)+int(voiceResult.q16)+int(voiceResult.q17)+int(voiceResult.q18)+int(voiceResult.q19)+int(voiceResult.q20)
    print('Total Voice Mark: {}'.format(total))

    voice = float(format(total))/20.0
    print(voice)


    if voice > 20.0:
        return "Voice recognition . You answered well. The given answers well matched with our database Try to use key words that implies the asked question area. Try to build up your answering performance. "


    elif voice > 15.0:
        return "AVoice recognition . You answered well. The given answers well matched with our database Try to use key words that implies the asked question area. Try to build up your answering performance. "


    elif voice > 10.0:
        return "Voice recognition . You answered well. The given answers well matched with our database Try to use key words that implies the asked question area. Try to build up your answering performance. "


    else:
        return "Voice recognition . You answered well. The given answers well matched with our database Try to use key words that implies the asked question area. Try to build up your answering performance. "



# get the hard state values
def showHardSubjectNames():
    userid = vari.userId
    languageName = "python"
    # print(ConnectionToNeo4j.getHardList(userid, languageName))
    # print(type(ConnectionToNeo4j.getHardList(userid, languageName)))
    #
    ListConvert = (ConnectionToNeo4j.getHardList(userid, languageName))
    print(type(ListConvert))
    test = ListConvert.split()
    print(test)
    # test2 = int(test)
    # print(test2)
    # ListConvert2 = list(map(int, ListConvert))
    # print(ListConvert2)
    # print(' '.join(map(str, ListConvert)))

    # uu = np.ndarray.tolist(ListConvert2)
    # print(uu)
    # print(type(uu))

    # test = [4, 8, 11, 13, 14, 17, 26]

    # print(type(test))
    # print(test[0])
    # print(test[1])
    # print(test[2])
    # print(test[3])
    # print(len(test))

    jj = "You better to focus on this areas -> \n"

    if len(test) >= 1:
        element = 1
        # return ConnectionToNeo4j.showHardList(element)
        aa1 = ConnectionToNeo4j.showHardList(element)

    if len(test) >= 2:
        element = 2
        aa2 = ConnectionToNeo4j.showHardList(element)

    if len(test) >= 3:
        element = 3
        aa3 = ConnectionToNeo4j.showHardList(element)

    if len(test) >= 4:
        element = 4
        aa4 = ConnectionToNeo4j.showHardList(element)

    if len(test) >= 5:
        element = 5
        aa5 = ConnectionToNeo4j.showHardList(element)

    if len(test) >= 6:
        element = 6
        aa6 = ConnectionToNeo4j.showHardList(element)


    return jj,aa1,aa2,aa3,aa4,aa5,aa6



# open('Database/Result/answerValidation.py', 'w').close()
# open('Database/Result/facialResult.py', 'w').close()
# open('Database/Result/voiceResult.py', 'w').close()





# getFacialMark()
# getVoiceMark()
# getAnswerMark()
# showHardSubjectNames()
