import importlib
import random,time
from Controller import ConnectionToNeo4j,QuestionCreator,NestedQuestionCreator,vari,AudioRecorder,AyeshSilenceDetection
from Controller import SpeachToText
from gingerit.gingerit import GingerIt
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)



importlib.reload(vari)
# technology_list = []
userid = vari.userId


#gnerates non technical questions
def generate_cv_questions():
    global grammer_corrected_pr0ject_question
    db = "CV"
    db2= "project"
    db3 ="project_d"
    # node_Count = ConnectionToNeo4j.getNodeCount(db)
    lang = 'en'
    q_list = []
    pro_list = []
    count = 1
    session = 0
    typo = "nonested"
    typo2 = "nontechnical"
    answer_validity = 0


    global question_number
    question_number = 0

#generates questions from the three sections
    while count<=3:
        session = session + 1
        print("session")
        print(session)
        session_no_string = str(session)
        session_node_count = ConnectionToNeo4j.session_Node_Count(db,session_no_string)
        print("this is ")
        print(session_node_count)
        node_id = ConnectionToNeo4j.get_node_id(db,session_no_string)

        for id in range(node_id,session_node_count+node_id):
            q_list.append(str(id))
        print(q_list)

        print("node_count")
        print(session_node_count)

        for question_no in range(session_node_count):

            print("question number")
            print(question_no)
            random_que = random.choice(q_list)
            print("random que")
            print(random_que)
            #new pars



            non_technical_question = ConnectionToNeo4j.cvQuestionGen(db,random_que)
            q_list.remove(random_que)
            print(q_list)
            print("jokes"+non_technical_question)

            question_number = question_number + 1

            actual_question = QuestionCreator.gen_Question(non_technical_question,question_number)
            AyeshSilenceDetection.silence_detect1(question_number)

            # print(actual_question)
            # parser = GingerIt()
            # grammer_corrected_question_list = parser.parse(actual_question)
            # grammer_corrected_question = grammer_corrected_question_list.get("result")
            # TextToSpeechConverter.text_to_speech(grammer_corrected_question, lang)

            # print(question_number)
            # print("hiiiiiiiiiiiiiiiiii printing count")
            if random_que == "6":
                global technology_list
                tech = SpeachToText.validation("", typo2,typo,"question"+str(question_number))[1]

                tech = NestedQuestionCreator.keywordSelector("",tech.lstrip(),"1","")

                print(tech)
                print("tech printed")
                technology_list = NestedQuestionCreator.nonTechnicalKeywordSeelector(tech)
                print("hello tech")
                print(technology_list)

            #gets an input to ask questions
            if random_que=="5":
                # voice_record = AudioRecorder.audio_recorder(question_number)
                # answer_validity = SpeachToText.validation("", typo2, typo, "question" + str(question_number))[0]
                project_question = ""
                random_proj_que = ""
                print(vari.userId)
                pro = ConnectionToNeo4j.getProjects(vari.userId)
                print("pro")
                print(pro)
                print("pro")
                if not  pro:
                    random_proj_que = "final year project"
                    print(random_proj_que)
                else:
                    random_proj_que = random.choice(pro)
                    print(random_proj_que)
                print(random_proj_que)

                project_question = ConnectionToNeo4j.cvQuestionProjectGen(db2, db3, random_proj_que, userid)
                question_number = question_number + 1

                print("project question")
                print(project_question)
                print("project question")


                print(" pro length")

                print(len(pro_list))
                print(" pro length")

                actual_project_question = QuestionCreator.gen_Question(project_question,question_number)
                AyeshSilenceDetection.silence_detect1(question_number)



            print("after a while")



        q_list = []
        count = count+1







