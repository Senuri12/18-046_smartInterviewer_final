import importlib
from flask import Flask, render_template,request
import json
from Controller import questionSaver_testing,ConnectionToNeo4j,inforetrievel,infowhat,MainQuestionGenerator,QuesType, vari,TechnicalQuestions,NonTechnicalQuestions,Suggestion

#test eka wenuwata sarindige py file name eka danna haha1 method eka athuleth change karanna
import test
import userDetails
from threading import Thread
import time



app = Flask(__name__)



global result12
result12 = 'ram'


@app.route('/')
def hello_world():
    open('userDetails.py', 'w').close()
    fruits = ["global results12\n", "results12 = 'no'"]
    new_file = open("userDetails.py", mode="a+", encoding="utf-8")
    new_file.writelines(fruits)
    for line in new_file:
        print(line)

    new_file.close()

    return render_template('index.html')

@app.route('/interview')
def profile():
    open('Controller/QuesType.py', 'w').close()
    fruits = ["global qTypeChange\n", "qTypeChange = 'change'\n"]
    new_file = open("Controller/QuesType.py", mode="a+", encoding="utf-8")
    new_file.writelines(fruits)
    for line in new_file:
        print(line)
    return render_template('bot.html')





@app.route('/suggesionspage')
def suggesionspage():

    return render_template('suggestion.html')



########################################################################

@app.route('/dum')
def haha1():

    time.sleep(5)
    importlib.reload(questionSaver_testing)
    from Controller.questionSaver_testing import gcpq
    result = {"ques": questionSaver_testing.gcpq,"qno" : questionSaver_testing.qno}
    # result = {"ques": gcpq}
    return json.dumps(result)



@app.route('/testsugest')
def testsugest():

    suggestions = {"suggestion1":Suggestion.getAnswerMark(),"suggestion2":Suggestion.getVoiceMark(),"suggestion3":Suggestion.getFacialMark(), "suggestion4":Suggestion.showHardSubjectNames()}
    return json.dumps(suggestions)


@app.route('/trigerquestion')
def get_python_data():

    async_slow_function()
    pythondata = {"haha":"haha"}
    return json.dumps(pythondata)


@app.route('/alertaboutontologycreation')
def inforetrivelontologycreate():


    importlib.reload(infowhat)
    print("sasasasasaslalalallala" + infowhat.valusa)
    pythondata = {"val":infowhat.valusa}
    return json.dumps(pythondata)



def slow_function():
    print("aa")
    MainQuestionGenerator.startsession()


def async_slow_function():
    thr = Thread(target=slow_function)
    thr.start()
    return thr


@app.route('/logindata', methods = ['POST'])
def get_post_javascript_data():
    un = request.form['username']
    pw = request.form['password']


    dbpw = ConnectionToNeo4j.login(un)


    print(un)
    if pw == dbpw:
        open('userDetails.py', 'w').close()
        fruits = ["global results12\n", "results12 = 'yes'"]
        new_file = open("userDetails.py", mode="a+", encoding="utf-8")
        new_file.writelines(fruits)
        for line in new_file:
            print(line)

        new_file.close()

    else:
        open('userDetails.py', 'w').close()
        fruits = ["global results12\n", "results12 = 'no'"]
        new_file = open("userDetails.py", mode="a+", encoding="utf-8")
        new_file.writelines(fruits)
        for line in new_file:
            print(line)

        new_file.close()


@app.route('/getloginresult')
def haha2():

    time.sleep(2)
    importlib.reload(userDetails)
    result = {"joking": userDetails.results12}
    return json.dumps(result)

@app.route('/home')
def login():
    return render_template('home.html')


@app.route('/signup')
def register():
    return render_template('signup.html')


@app.route('/seleaaaaaaa')
def selectionbox():
    no = ConnectionToNeo4j.noofsessions()
    result = {}

    for x in range(0, int(no)):
        result['no'+str(x+1)] = "session"+str(x+1)

    return json.dumps(result)

@app.route('/history')
def history():
    return render_template('history.html')



@app.route('/results')
def results():
    return render_template('results.html')




@app.route('/chart/<a>')
def chart(a):
    print(a[7:])

    val = ConnectionToNeo4j.getsessionmarks(a[7:])


    result = {"no1":"session1","no2":"session2"}

    print(val)
    print(result)


    return json.dumps(val)

@app.route('/chartsa')
def chartsa():

    val = ConnectionToNeo4j.getsessionmarks1()


    return json.dumps(val)



#cv new thingy
@app.route('/dingdong')
def dingdong():
    print("shalalalallala")
    importlib.reload(vari)
    uid = vari.userId
    val = ConnectionToNeo4j.checkuserinnwadas(uid)
    result = {"myca": str(val)}
    return json.dumps(result)



# @app.route('/dum5')
# def haha5():
#
#     result = {"ques": test.question5}
#     return json.dumps(result)
#









@app.route('/cretesaddddas', methods = ['POST'])
def cretesomething():
    open('Controller/infowhat.py', 'w').close()
    fruits = ["global valusa\n", "valusa = 'ra'\n"]
    new_file = open("Controller/infowhat.py", mode="a+", encoding="utf-8")
    new_file.writelines(fruits)
    for line in new_file:
        print(line)

    return ""

@app.route('/setDiff', methods = ['POST'])
def setDifficultyLevelSelector():
    value = str(request.form['dValue'])
    print(value)

    if value == 'change':
        open('Controller/QuesType.py', 'w').close()
        fruits = ["global qTypeChange\n", "qTypeChange = 'change'\n"]
        new_file = open("Controller/QuesType.py", mode="a+", encoding="utf-8")
        new_file.writelines(fruits)
        for line in new_file:
            print(line)
        new_file.close()

    elif value == 'continueSame':
        open('Controller/QuesType.py', 'w').close()
        fruits = ["global qTypeChange\n", "qTypeChange = 'continueSame'\n"]
        new_file = open("Controller/QuesType.py", mode="a+", encoding="utf-8")
        new_file.writelines(fruits)
        for line in new_file:
            print(line)
        new_file.close()

    return ""

@app.route('/cv')
def cv():
    return render_template('cvform.html')

@app.route('/cvdata', methods = ['POST'])
def get_post_cv_javascript_data():
    print("hello ")

    fname = str(request.form['flname'])
    usage = str(request.form['uage'])
    usschool = str(request.form['uschool'])
    usuni = str(request.form['uuni'])
    usdob = str(request.form['udob'])
    usemail = str(request.form['uemail'])
    ustpno = str(request.form['utpno'])
    usweak = str(request.form['uweak'])
    usstrengh = str(request.form['ustrength'])
    usidlcmp = str(request.form['uidcomp'])
    usftech = str(request.form['ufmtech'])
    usproone = str(request.form['uproone'])
    ustech1 = str(request.form['utech1'])
    usprotwo = str(request.form['uprotwo'])
    ustech2 = str(request.form['utech2'])

    techsAvailable = []
    infoRetList = []
    finalFamiliarTechList = []
    techWord_list = usftech.split(',')
    for techWord in techWord_list:
        techWord = techWord.lower()
        availability_node = ConnectionToNeo4j.getMatchingTopicsNonTech1(techWord)
        print(techWord)
        print(availability_node)
        if availability_node == True:
            print("available")
            techsAvailable.append(techWord)
            print(techsAvailable)
        elif availability_node == False:
            print("not available")
            if techWord == "c#":
                techWord = "csharp"
            elif techWord == "c++":
                techWord = "cplusplus"
            elif techWord == "c":
                techWord = "cprogramming"

            infoList = inforetrievel.inforetrievel(techWord)
            infoRet = infoList[0]
            print("returning ")
            print(infoRet)
            print("returning ")

            technicalNodeCnt = infoList[1]
            print("returning ")
            print(technicalNodeCnt)

            if infoRet != "0":
                infoRet = infoRet.lower()
                print(infoRetList)
                infoRetList.append(infoRet)
                print(infoRetList)
                # ##########################################3 new
                #
                # nodeCountValue = int(technicalNodeCnt / 3)
                # print(nodeCountValue)
                # changingNodeCountValue = nodeCountValue
                # remainingValue = technicalNodeCnt - (nodeCountValue * 3)
                # print(remainingValue)
                # easyNodes = ""
                # mediumNodes = ""
                # hardNodes = ""
                #
                # exactCount = technicalNodeCnt
                #
                # while changingNodeCountValue > 0:
                #     easyNodes = easyNodes + "," + str(exactCount)
                #     exactCount = exactCount - 1
                #     changingNodeCountValue = changingNodeCountValue - 1
                # print(easyNodes)
                # easyNodes = easyNodes[1:]
                # print(easyNodes)
                #
                # changingNodeCountValue = nodeCountValue
                #
                # print("nooooooooooooooooooooooooooooooo")
                # while changingNodeCountValue > 0:
                #     mediumNodes = mediumNodes + "," + str(exactCount)
                #     exactCount = exactCount - 1
                #     changingNodeCountValue = changingNodeCountValue - 1
                # print(mediumNodes)
                # mediumNodes = mediumNodes[1:]
                # print(mediumNodes)
                #
                # print("nooooooooooooooooooooooooooooooo")
                #
                # changingNodeCountValue = nodeCountValue + remainingValue
                # print(changingNodeCountValue)
                # while changingNodeCountValue > 0:
                #     hardNodes = hardNodes + "," + str(exactCount)
                #     exactCount = exactCount - 1
                #     changingNodeCountValue = changingNodeCountValue - 1
                # print(hardNodes)
                # hardNodes = hardNodes[1:]
                # print(hardNodes)
                #
                # restResult = ConnectionToNeo4j.addDifficultyLevelsForSpecificTech(infoRet, easyNodes, mediumNodes,hardNodes)

                # ########################################## new

    importlib.reload(infowhat)
    open('Controller/infowhat.py', 'w').close()
    fruits = ["global valusa\n", "valusa = 'fn'\n"]
    new_file = open("Controller/infowhat.py", mode="a+", encoding="utf-8")
    new_file.writelines(fruits)
    for line in new_file:
        print(line)




    finalFamiliarTechList = techsAvailable +infoRetList
    print(finalFamiliarTechList)
    finalFamiliarTech = ','.join(finalFamiliarTechList)
    print(finalFamiliarTech)
    # while finalFamiliarTechList[0] == ',':
    #     print("in")
    #     finalFamiliarTechList = finalFamiliarTechList[1:]
    #     print(finalFamiliarTechList)
    # stringLength = len(finalFamiliarTechList) - 1
    # while finalFamiliarTechList[stringLength] == ',':
    #     print("hahaa")
    #     finalFamiliarTechList = finalFamiliarTechList[:stringLength]
    # print(finalFamiliarTechList)

    importlib.reload(vari)
    uid = vari.userId

    validation = ConnectionToNeo4j.checkuserinnwadas(uid)

    # if validation != True:
        # fresult = ConnectionToNeo4j.createNewCv(uid,fname,usage,usschool,usuni,usdob,usemail,ustpno,usweak,usstrengh,usidlcmp,finalFamiliarTech,usproone,ustech1,usprotwo,ustech2)

    print(fname)
    pythondata = {'val':infoRet}
    return json.dumps(pythondata)



@app.route('/registerdata', methods = ['POST'])
def get_post_javascript_data1():
    print("lalala")

    un = str(request.form['username'])
    pw = str(request.form['password'])
    email = str(request.form['email'])

    regUserId = ConnectionToNeo4j.register(un,pw,email)

    #adding difficulty db
    availableTechnicalNode = ConnectionToNeo4j.getExistingTechnologies()
    print(availableTechnicalNode)
    # regUserId = ConnectionToNeo4j.getLastCreatedUid()
    node = ConnectionToNeo4j.genUserDiffLevel(regUserId)

    # availableTechnicalNodeList = (availableTechnicalNode.split(','))
    for itt in availableTechnicalNode:
        technicalNodeCnt = ConnectionToNeo4j.getTechNodeCount(itt)
        print(technicalNodeCnt)

        nodeCountValue = int(technicalNodeCnt / 3)
        print(nodeCountValue)
        changingNodeCountValue = nodeCountValue
        remainingValue = technicalNodeCnt - (nodeCountValue * 3)
        print(remainingValue)
        easyNodes = ""
        mediumNodes = ""
        hardNodes = ""

        exactCount = technicalNodeCnt

        while changingNodeCountValue > 0:
            easyNodes = easyNodes + "," + str(exactCount)
            exactCount = exactCount - 1
            changingNodeCountValue = changingNodeCountValue - 1
        print(easyNodes)
        easyNodes = easyNodes[1:]
        print(easyNodes)

        changingNodeCountValue = nodeCountValue

        print("nooooooooooooooooooooooooooooooo")
        while changingNodeCountValue > 0:
            mediumNodes = mediumNodes + "," + str(exactCount)
            exactCount = exactCount - 1
            changingNodeCountValue = changingNodeCountValue - 1
        print(mediumNodes)
        mediumNodes = mediumNodes[1:]
        print(mediumNodes)

        print("nooooooooooooooooooooooooooooooo")

        changingNodeCountValue = nodeCountValue + remainingValue
        print(changingNodeCountValue)
        while changingNodeCountValue > 0:
            hardNodes = hardNodes + "," + str(exactCount)
            exactCount = exactCount - 1
            changingNodeCountValue = changingNodeCountValue - 1
        print(hardNodes)
        hardNodes = hardNodes[1:]
        print(hardNodes)
        restResult = ConnectionToNeo4j.addDifficultyLevelsForTech(regUserId, itt, easyNodes, mediumNodes, hardNodes)
        if itt == "python":
            neseasy = "NES_019,NES_018,NES_015,NES_013,NES_008"
            nesMedium = "NES_017,NES_016,NES_014,NES_011"
            nesHard = "NES_012,NES_009,NES_010"
            restResult2 = ConnectionToNeo4j.addDiffLevelNestedNodesForTech(regUserId, itt, neseasy, nesMedium,nesHard)
        if itt == "java":
            neseasy = "NES_001,NES_002"
            nesMedium = "NES_003,NES_005"
            nesHard = "NES_004,NES_006"
            restResult3 = ConnectionToNeo4j.addDiffLevelNestedNodesForTech(regUserId, itt, neseasy, nesMedium,nesHard)







if __name__ == '__main__':
    app.run()
