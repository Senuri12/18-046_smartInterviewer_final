import importlib

from Controller import NonTechnicalQuestions, ConnectionToNeo4j, TechnicalQuestionCreators, NestedQuestionCreator,SpeachToText,CreateReward
from Controller import DifficultyLevelSelector,vari,QuesType,AyeshSilenceDetection
import requests,math,random
from gingerit.gingerit import GingerIt

from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
table_name =""
answer_validy = 0

global actual_question
actual_question = ""


def question_gen():
    #difficulty level  generation
    global changed_know_list
    changed_know_list = []

    db2 = "user"
    db3 = "session"

    global diff_level
    diff_level = "easy"

    session_db = "session"
    importlib.reload(vari)
    userId = vari.userId
    sessionId = vari.sessionId
    question_number = NonTechnicalQuestions.question_number

    global qprinted
    qprinted = 0

    global taking_list
    taking_list= []

    global prev1_ans_result
    prev1_ans_result= 0.2

    global prev2_ans_result
    prev2_ans_result= 0.2

    global prev1_que_count
    # prev1_que_count = 5
    prev1_que_count = 6


    global prev2_que_count
    # prev2_que_count = 6
    prev2_que_count = 7

    global user_diff
    user_diff = "user_difficulty"

    global db_diff
    db_diff = "difficulty"
    global different_change_list
    different_change_list= "False"



    q_list = []
    lang = 'en'
    tech_keywords = NonTechnicalQuestions.technology_list
    print(tech_keywords)
    print("hey")
    global nested_question_ccount
    nested_question_ccount = 2
    global final_itteration_value



    #decide the count of questions that should be generated from one technology
    splitted_table_list = (tech_keywords.split(','))
    # splitted_table_list.append("java")

    print(splitted_table_list)
    print("list is printed")
    splitted_table_list_length = len(splitted_table_list)
    stable_splitted_table_list_length = len(splitted_table_list)
    print("length")
    print(splitted_table_list_length)

    split_list_length = stable_splitted_table_list_length
    itteration_val = int(11 / split_list_length)
    itteration_value = math.floor(itteration_val)

    final_itteration_value = itteration_value


    # get the nested value count after filling technologies
    rem_nested_count = 11 - (split_list_length * itteration_value)
    nested_question_ccount = nested_question_ccount + rem_nested_count
    print(nested_question_ccount)
    print("this is theeeeeeeeeeeeeeerem_nested_count")

    print("itt")
    print(itteration_value)


#selects a keyword from technology list
    while splitted_table_list_length >=1:


        random_table = random.choice(splitted_table_list)
        print(random_table)


        splitted_table_list_length = splitted_table_list_length-1
        print("length")
        print(splitted_table_list_length)
        splitted_table_list.remove(random_table)
        print(splitted_table_list)

        technical_node_count = ConnectionToNeo4j.getTechNodeCount(random_table)
        print(technical_node_count)
        q_list = []
        for id in range(1, technical_node_count + 1):
            q_list.append(id)
        print(q_list)

#generate questions according to question count
        # for itt in range(itteration_value):
        while itteration_value>0:
            print(itteration_value)
            print("my itteration")
            print(itteration_value)
            itteration_value = itteration_value-1


            p1_qno = str(prev1_que_count)
            p1_send_question = "question"+p1_qno
            print(p1_qno)

            p2_qno = str(prev2_que_count)
            p2_send_question = "question"+p2_qno
            print(p1_qno)
            print("this is prev one")
            print(prev1_que_count)
            print("this is prev")
            print(prev2_que_count)

            print("nooooooooooooooooooooooooooo")

            if  prev1_que_count != 6 and prev2_que_count != 7 and prev1_que_count == 7 and question_number < 20:

                prev1_ans_result = 0.2
                prev2_ans_result = ConnectionToNeo4j.getQuestionMarks(db2,db3,userId,sessionId,p2_send_question)
                prev2_ans_result = float(prev2_ans_result)
                print("javaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
                print(prev1_que_count)
                print(prev2_que_count)

                print("javaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
                print("this is prev marksssssssssssss")
                print(prev1_ans_result)
                print(p1_send_question)
                print(question_number)
                print("this is prev marksssssssssssss")

                print("this is prev marksssssssssssss")
                print(prev2_ans_result)
                print(p2_send_question)
                print(question_number)
                print("this is prev marksssssssssssss")

            elif prev1_que_count != 6 and prev2_que_count != 7 and question_number < 20 :

                prev1_ans_result = ConnectionToNeo4j.getQuestionMarks(db2,db3,userId,sessionId,p1_send_question)
                prev2_ans_result = ConnectionToNeo4j.getQuestionMarks(db2,db3,userId,sessionId,p2_send_question)

                prev1_ans_result = float(prev1_ans_result)
                prev2_ans_result = float(prev2_ans_result)
                print("javaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
                print(prev1_que_count)
                print(prev2_que_count)

                print("javaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
                print("this is prev marksssssssssssss")
                print(prev1_ans_result)
                print(p1_send_question)
                print(question_number)
                print("this is prev marksssssssssssss")

                print("this is prev marksssssssssssss")
                print(prev2_ans_result)
                print(p2_send_question)
                print(question_number)
                print("this is prev marksssssssssssss")

            if prev1_que_count != 6 and prev2_que_count != 7 and prev1_que_count == 7 and question_number < 20:

                prev1_ans_result = 0.2
                prev2_ans_result = ConnectionToNeo4j.getQuestionMarks(db2, db3, userId, sessionId, p2_send_question)
                prev2_ans_result = float(prev2_ans_result)
                print("javaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
                print(prev1_que_count)
                print(prev2_que_count)

                print("javaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
                print("this is prev marksssssssssssss")
                print(prev1_ans_result)
                print(p1_send_question)
                print(question_number)
                print("this is prev marksssssssssssss")

                print("this is prev marksssssssssssss")
                print(prev2_ans_result)
                print(p2_send_question)
                print(question_number)
                print("this is prev marksssssssssssss")

            elif prev1_que_count != 6 and prev2_que_count != 7 and question_number < 20 :

                prev1_ans_result = ConnectionToNeo4j.getQuestionMarks(db2, db3, userId, sessionId, p1_send_question)
                prev2_ans_result = ConnectionToNeo4j.getQuestionMarks(db2, db3, userId, sessionId, p2_send_question)

                prev1_ans_result = float(prev1_ans_result)
                prev2_ans_result = float(prev2_ans_result)
                print("javaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
                print(prev1_que_count)
                print(prev2_que_count)

                print("javaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
                print("this is prev marksssssssssssss")
                print(prev1_ans_result)
                print(p1_send_question)
                print(question_number)
                print("this is prev marksssssssssssss")

                print("this is prev marksssssssssssss")
                print(prev2_ans_result)
                print(p2_send_question)
                print(question_number)
                print("this is prev marksssssssssssss")

            # difficulty level  selection
            if prev1_ans_result >= 0.5 and prev2_ans_result >= 0.5 and QuesType.qTypeChange == 'change':
                diff_level = DifficultyLevelSelector.increase_difficulty_level(diff_level)
            elif prev1_ans_result < 0.5 and prev2_ans_result < 0.5 and QuesType.qTypeChange == 'change':
                diff_level = DifficultyLevelSelector.decrease_difficulty_level(diff_level)
            print(diff_level)

            if prev1_ans_result >= 0.5 and prev2_ans_result >= 0.5 and QuesType.qTypeChange == 'continueSame':
                diff_level = DifficultyLevelSelector.increase_difficulty_level(diff_level)

            print(diff_level)

            # get the list of nodes according to the difficulty level
            taking_list = DifficultyLevelSelector.adding_diff_level_val_list(userId, user_diff,db_diff, random_table, diff_level)
            print(taking_list)
            print(taking_list)
            print("hi i am the taking list")

            # comparing two lists to get the nodes that are in the q_list
            changed_know_list = set(q_list) & set(taking_list)
            print("i know it is hereeeeeeeeeeeeeeeeeeeeeeeeeeeeee")
            print(changed_know_list)

            changed_know_list = list(changed_know_list)
            # changed_know_list = None

            if not changed_know_list:
                changed_know_list = q_list
                different_change_list = "True"

            print(changed_know_list)
            print(changed_know_list)
            print("changed_know_list")

            random_que = random.choice(changed_know_list)
            print(random_que)

            random_que_string = str(random_que)
            print(random_que_string)

            #changes the difficulty level if there are no nodes availabble for the exisisting difficulties
            if different_change_list == "True":
                diff_level = DifficultyLevelSelector.change_difficulty_level(random_que_string,random_table)
                print("diffffffffff")
                print(diff_level)
                print("difffffffffffffffffff")

            technical_question = ConnectionToNeo4j.technical_question_keyword(random_table,random_que_string)
            print("qu")
            print(technical_question)
            changed_know_list = []
            q_list.remove(random_que)
            print(q_list)
            print(changed_know_list)
            question_number = question_number+1


            actual_question = TechnicalQuestionCreators.gen_Question(technical_question,question_number,"nonnested")
            AyeshSilenceDetection.silence_detect1(question_number)

            parser = GingerIt()

            #creates the difficulty levels
            CreateReward.rewardForQuestion(random_table,random_que_string,random_que,diff_level)

             # TextToSpeechConverter.text_to_speech(actual_question,lang)
            qprinted = qprinted+1;
            print("qprint")
            print(qprinted)
            print("qprint")


            prev1_que_count = prev1_que_count+1
            prev2_que_count = prev2_que_count+1

            # answer_validity = test.test()
            # answer_validity = input()

            # while (answer_validity == "null"):
                # print(vik_test_codes.question(question_number))

                # answer_validity = test.test()
                #answer_validity = input()

            # if itt>1 and nested_question_ccount>0:

            #generates nested questions if keyword are available
            if itteration_value > 1 and nested_question_ccount > 0:

                filtered_words_string =SpeachToText.validation(technical_question, "technical","nonested","question"+str(question_number))
                nested = NestedQuestionCreator.keywordSelector(random_table,filtered_words_string[1].lstrip(),"2",diff_level)
                if nested != 0:
                    print("nested keyword value")
                    print(nested)
                    question_number = question_number + 1

                    actual_question = TechnicalQuestionCreators.gen_Question(nested,question_number,"nested")
                    AyeshSilenceDetection.silence_detect1(question_number)

                    # TextToSpeechConverter.text_to_speech(actual_question, lang)
                    print(actual_question)

                    qprinted = qprinted + 1;
                    print("qprint")
                    print(qprinted)
                    print("qprint")

                    prev1_que_count = prev1_que_count + 1
                    prev2_que_count = prev2_que_count + 1

                    nested_question_ccount = nested_question_ccount - 1
                    print(nested)

                else:
                    print("when ignores")
                print("true")

            else:
                print("false")

            #gets the correct question number for a sesson if no nested questions
            # if itt == itteration_value-1 and splitted_table_list_length == 1 and nested_question_ccount>0 :
            if  itteration_value == 1 and splitted_table_list_length == 0 and nested_question_ccount > 0:
                itteration_value = itteration_value + 1

                # itteration_value = itteration_value + nested_question_ccount
                nested_question_ccount = nested_question_ccount - 1
                print("it is trueeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee")




            # if prev1_que_count == 7 and question_number<20:
            #get the result of the previous two questions




        itteration_value = final_itteration_value











