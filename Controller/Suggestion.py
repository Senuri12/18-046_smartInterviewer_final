# import os
# from Controller import ConnectionToNeo4j,vari
#
#
# #Ayesh voice
# # a = 1
# # print(type(a))
# # b = 2
# # print(type(b))
# # c = 3
# #
# # while (type(a) == int and type(b) == int and type(c) == int):
# #
# #
# # print("B")
#
# # f = open("../Database/answerValidation.txt", "a+")
# # aa = 10
# # f.write("\n\r".format(aa))
#
#
# #Vikum answer validation
#
# def getAnswerMark():
#     total = 0
#     with open('../Database/answerValidation.txt', 'r') as inp:
#        for line in inp:
#            try:
#                num = float(line)
#                total += num
#            except ValueError:
#                pass
#
#     print('Total Answer Validation Mark: {}'.format(total))
#
#     answer = float(format(total))/20.0
#     print(answer)
#
#
#     if answer > 20.0:
#         print("Answer validation --. \n")
#         print("You answered well. The given answers well matched with our database \n")
#         print("Try to use key words that implies the asked question area. \n")
#         print("Try to build up your answering performance. \n")
#         print(" \n")
#
#     elif answer > 15.0:
#         print("Answer validation --. \n")
#         print("You answered well. But the given answers not well matched with our database \n")
#         print("Try to use key words that implies the asked question area. \n")
#         print("Try to build up your answering performance. \n")
#         print(" \n")
#
#     elif answer > 10.0:
#         print("Answer validation --. \n")
#         print("You answered in intermediate. The given answers not matched with our database \n")
#         print("Try to use key words that implies the asked question area. \n")
#         print("Try to build up your answering performance. \n")
#         print(" \n")
#
#     else:
#         print("Answer validation --. \n")
#         print("You answered in bad. The given answers not matched with our database \n")
#         print("Try to use key words that implies the asked question area. \n")
#         print("Try to build up your answering performance. \n")
#         print(" \n")
#
# def getFacialMark():
#     total = 0
#     with open('../Database/facialResult.txt', 'r') as inp:
#        for line in inp:
#            try:
#                num = float(line)
#                total += num
#            except ValueError:
#                pass
#
#     print('Total Facial Mark: {}'.format(total))
#
#     facial = float(format(total))/20.0
#     print(facial)
#
#
#     if facial > 20.0:
#         print("Facial Expressions --. \n")
#         print("You are in good facial controlling position. \n")
#         print("You presenting with good happy and normal. \n")
#         print("Try to buildup performance. \n")
#         print(" \n")
#
#     elif facial > 15.0:
#         print("Facial Expressions --. \n")
#         print("You are in intermediate level of presenting controlling. \n")
#         print("You speaking with considerable number of silent parts. \n")
#         print("Try to buildup performance. \n")
#         print(" \n")
#
#     elif facial > 10.0:
#         print("Facial Expressions --. \n")
#         print("You are in considerable facial controlling position. \n")
#         print("You presenting with good. \n")
#         print("Try to buildup performance. \n")
#         print(" \n")
#
#     else:
#         print("Facial Expressions --. \n")
#         print("You are in bad facial controlling position. \n")
#         print("You presenting with bad expressions. \n")
#         print("Try to buildup performance more. \n")
#         print(" \n")
#
# def getVoiceMark():
#     total = 0
#     with open('../Database/voiceResult.txt', 'r') as inp:
#        for line in inp:
#            try:
#                num = float(line)
#                total += num
#            except ValueError:
#                pass
#
#     print('Total Voice Mark: {}'.format(total))
#
#     voice = float(format(total))/20.0
#     print(voice)
#
#
#     if voice > 20.0:
#         print("Voice Expressions --. \n")
#         print("You are in good voice controlling position. \n")
#         print("You speaking with less number of silent parts. \n")
#         print("Try to buildup performance. \n")
#         print(" \n")
#
#     elif voice > 15.0:
#         print("Voice Expressions --. \n")
#         print("You are in intermediate level of speaking controlling. \n")
#         print("You speaking with considerable number of silent parts. \n")
#         print("Try to buildup performance. \n")
#         print(" \n")
#
#     elif voice > 10.0:
#         print("Voice Expressions --. \n")
#         print("You are in considerable voice controlling position. \n")
#         print("You speaking with less number of silent parts. \n")
#         print("Try to buildup performance. \n")
#         print(" \n")
#
#     else:
#         print("Voice Expressions --. \n")
#         print("You are in bad voice controlling position. \n")
#         print("You speaking with majority number of silent parts. \n")
#         print("Try to buildup performance more. \n")
#         print(" \n")
#
#
# getFacialMark()
# getVoiceMark()
# getAnswerMark()
#
# # coments for facial detection
#
#
#
# # comments for voice message
#
#
# #Answer validation section
#
#
#
# #get the hard state values
# userid = vari.userId
# languageName = "python"
# print(ConnectionToNeo4j.getHardList(userid, languageName))
# print(type(ConnectionToNeo4j.getHardList(userid, languageName)))
#
#
#
# # close and clear the file