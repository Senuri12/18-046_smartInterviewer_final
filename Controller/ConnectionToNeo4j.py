import importlib

from py2neo import Graph
from Controller import vari
graph = Graph("")


def ontologyQuestionGen(id):
  query = "MATCH (j:Java{id:"+ id+"}) RETURN j.topic"
  gen_Question = graph.run(query).evaluate()
  # print(gen_Question)
  return gen_Question


def noofsessions():
  importlib.reload(vari)
  query = "MATCH(a: user{Userid: '"+vari.userId+"'}) - [r: userTOsession]->(n:session) RETURN count(n)"
  gen_Question = graph.run(query).evaluate()
  # print(gen_Question)
  return gen_Question




def mostrecentsession(emails):
    query13 = "MATCH (a: user{email: '" +emails+ "'}) - [r: userTOsession]->(n:session) RETURN n.no ORDER BY n.no DESC LIMIT 1;"
    sessionExist1 = graph.run(query13).evaluate()
    return sessionExist1



def getsessionmarks(no):
  result ={}
  importlib.reload(vari)
  for x in range(0, 20):
     query = "MATCH(a: user{Userid: '" + vari.userId + "'}) - [r: userTOsession]->(n:session{no:'" + no + "'}) RETURN n.question"+str(x+1)
     gen_Question = graph.run(query).evaluate()
     result['q' + str(x + 1)] = str(gen_Question)

  return result


def getsessionmarks1():
  query13 = "MATCH (n:session) RETURN n.no ORDER BY n.no DESC LIMIT 1;"
  sessionExist1 = graph.run(query13).evaluate()

  importlib.reload(vari)
  result ={}
  for x in range(0, 20):
     query = "MATCH(a: user{Userid: '" + vari.userId + "'}) - [r: userTOsession]->(n:session{no:'" + sessionExist1 + "'}) RETURN n.question"+str(x+1)
     gen_Question = graph.run(query).evaluate()
     result['q' + str(x + 1)] = str(gen_Question)

  return result


def login(email):
  session = ""
  query = "MATCH (j:oneUser{email:'" + email + "'}) RETURN j.id"
  useridz = graph.run(query).evaluate()

  if(mostrecentsession(email)==None):
      session = "1"
  else:
      no = int(mostrecentsession(email))+1
      session=str(no)

  open('Controller/vari.py', 'w').close()
  fruits = ["global userId\n", "userId = '" + useridz+ "'\n", "global sessionId\n", "sessionId = '" + session + "'\n"]

  new_file = open("Controller/vari.py", mode="a+", encoding="utf-8")
  new_file.writelines(fruits)
  for line in new_file:
      print(line)

  new_file.close()


  email = str(email)
  query = "MATCH (j:oneUser{email:'"+email+"'}) RETURN j.password"
  gen_Question = graph.run(query).evaluate()
  # print(gen_Question)
  return gen_Question

# ontologyQuestionGen("1")



def register(un,pw,email):
  print("ssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssss")

  useridzz=""
  query13 = "MATCH (n:oneUser) RETURN n.id ORDER BY n.id DESC LIMIT 1"
  useridz = graph.run(query13).evaluate()

  if useridz == None:
      useridzz = "uid001"
  else:
      no = int(useridz[3:])+1
      if len(str(no))==1:
          useridzz ="uid00"+str(no)
      elif len(str(no))==2:
          useridzz ="uid0"+str(no)
      elif len(str(no))==3:
          useridzz ="uid"+str(no)

  query = "MATCH(c: loginUser{Name: 'userdb'}) CREATE(c) - [x: has_users]-> (a: oneUser{id:'"+useridzz+"',username :'"+un+"',email:'"+email+"',password:'"+pw+"'})"
  graph.run(query).evaluate()

  # return ""
  return useridzz


def getValueFromdb(subsection,type):

    if type == 'nested':
        subsection = "" + subsection
        exist = "MATCH(b:subB{Name:'"+subsection+"'})RETURN b.Details"
        validationValue = graph.run(exist).evaluate()
        print(validationValue)
        return validationValue
    else:
        subsection = "" + subsection
        exist = "MATCH(a: language) - [r: has]->(b:sub{Name:'" + subsection + "'})RETURN b.Details"
        validationValue = graph.run(exist).evaluate()
        print(validationValue)
        return validationValue

def cvQuestionGen(db,id):
  query = "MATCH (j:"+db+"{id:"+ id+"}) RETURN j.topic"
  gen_Question = graph.run(query).evaluate()
  # print(gen_Question)
  return gen_Question



def session_Node_Count(db,session):
  # session ="2"
  query = "MATCH (a:"+db+"{session: " +session+ "}) RETURN count(*)"
  gen_count = graph.run(query).evaluate()
  # print(gen_count)
  return  gen_count



def get_node_id(db,session):
  query = "MATCH (a:"+db+"{session: " + session + "}) RETURN a.id"
  gen_count = graph.run(query).evaluate()
  # print(gen_count)
  return gen_count



def technical_question_keyword(table,id):
  val = "1"
  query = "MATCH(a:language{Name:'"+table+"'}) - [r: has]->(b:sub{id:'"+id+"'})RETURN b.Name"
  gen_Question = graph.run(query).evaluate()
  # print(gen_Question)
  return gen_Question

def getTechNodeCount(db):
  query = "MATCH(a:language{Name:'"+db+"'}) - [r: has]->(b:sub{})RETURN count(*)"
  gen_count = graph.run(query).evaluate()
  # print(gen_count)
  print("inside the function")
  return gen_count

def getProjTwoAva(uid):
    print(uid)

    query = "MATCH (a:CV{id:5})-[r1:projects]->(b:project{topic:'project two'})-[r2:projects_details]->(c:project_d{uid:'"+uid+"'}) RETURN b.pid"
    get_projects =graph.run(query).evaluate()
    return get_projects

def getProjects(uid):
    finalCount = []
    # query = "MATCH (a:"+db+"{id:"+id+"})-[:projects]->(proj) RETURN count(*)"
    # query = "MATCH (a:CV{id:5})-[:projects]->(projects)RETURN count(*)"
    print(uid)
    query = "MATCH (a:CV{id:5})-[r1:projects]->(b:project{topic:'project one'})-[r2:projects_details]->(c:project_d{uid:'"+uid+"'}) RETURN b.pid"
    proOne_id =graph.run(query).evaluate()
    print(proOne_id)
    print("proOne_id")

    proTwoId = getProjTwoAva(uid)
    print(proTwoId)
    print("proTwoId")
    if proOne_id != None:
        finalCount.append(proOne_id)
    if proTwoId !=None:
        finalCount.append(proTwoId)
    print(finalCount)
    print("This is final")

    return finalCount
getProjects("uid002")




# print(getProjTwoCount("uid044401"))
def getMatchingTopics(db,topic):
    query = "MATCH(a:language{Name:'" + db + "'}) - [r: has]->(b:sub{Name:'"+topic+"'}) -[r2:nested_has]->(c:subB) RETURN count(c.Name)>0"
    get_availability = graph.run(query).evaluate()
    print(get_availability)
    return get_availability

def getMatchingNestedTopicId(db,topic):
    query = "MATCH(a:language{Name:'" + db + "'}) - [r: has]->(b:sub{Name:'"+topic+"'}) -[r2:nested_has]->(c:subB) RETURN c.id"
    get_availability = graph.run(query).evaluate()
    return get_availability
# getMatchingNestedTopicId("java","oop")

def getMatchingNestedTopic(db,topic,nesid):
    query = "MATCH(a:language{Name:'" + db + "'}) - [r: has]->(b:sub{Name:'"+topic+"'}) -[r2:nested_has]->(c:subB{id:'"+nesid+"'}) RETURN c.Name"
    get_availability = graph.run(query).evaluate()
    print(get_availability)
    return get_availability


def getMatchingTopicsNonTech(db):

    query = "MATCH(a:language{Name:'" + db + "'}) - [r: has]->(b:sub)RETURN count(b)>0"
    availability = graph.run(query).evaluate()

    return availability


def getMatchingTopicsNonTech1(db):
    query = "MATCH(a:language{Name:'" + db + "'}) - [r: has]->(b:sub)RETURN count(b)>0"
    availability = graph.run(query).evaluate()

    if availability==True:
        qtable = "[0.0, 0.0, 0.0, 0.0, 0.0],[0.0, 0.0, 0.0, 0.0, 0.0],[0.0, 0.0, 0.0, 0.0, 0.0],[0.0, 0.0, 0.0, 0.0, 0.0],[0.0, 0.0, 0.0, 0.0, 0.0]"
        useridz = vari.userId

        query2 = "MATCH(a:language{Name:'" + db + "'})- [r: has]->(b:sub) return b." + useridz + ""
        availability2 = graph.run(query2).evaluate()

        if availability2 == None:
            query1 = "MATCH(a:language{Name:'" + db + "'})- [r: has]->(b:sub) set b." + useridz + "='" + qtable + "'"
            availability1 = graph.run(query1).evaluate()

    return availability

# def cvProjectTech(db,db2,pid,userId):
#   # query = "MATCH (j:"+db+"{pid:'"+ pid+"'}) RETURN j.technologies"
#   query = "MATCH (j:" + db + "{pid:'" + pid + "'}) - [r: projects_details]->(b:" + db2 + "{uid:'" + userId + "'}) RETURN b.technologies"
#   gen_Question = graph.run(query).evaluate()
#   print(gen_Question)
#   return gen_Question
def cvProjectTech(db,topic,userId):
  # query = "MATCH (j:"+db+"{pid:'"+ pid+"'}) RETURN j.technologies"
  query = "MATCH (j:" + db + "{topic:'" + topic + "'}) RETURN j."+ userId + ""
  gen_Question = graph.run(query).evaluate()
  print(gen_Question)
  return gen_Question

#returns the difficulty level list
def getdiffLevelList(userId,db,db2,techno,level):
    query = "MATCH (j:" + db + "{uid:'" + userId + "'}) - [r: level]->(b:" + db2 + "{technology:'" + techno + "'}) RETURN b." + level+""
    gen_list = graph.run(query).evaluate()
    print("my generated list")

    print(gen_list)
    print("my generated list")
    return gen_list
# getdiffLevelList("uid002","user_difficulty","difficulty","python","easy")

def getNestedDiffLevelList(userId,db,db2,db3,techno,level):
    query = "MATCH (j:" + db + "{uid:'" + userId + "'}) - [r: level]->(b:" + db2 + "{technology:'" + techno + "'}) -[r2:nested_level] ->(c:"+db3+") RETURN c." + level+""
    gen_list = graph.run(query).evaluate()
    print(gen_list)
    return gen_list

#generates the session details
def getQuestionMarks(db,db2,userId,sessid,number):
    print(db)
    print(db2)
    print(userId)
    print(sessid)
    print(number)
    query = "MATCH(a: "+db+"{Userid: '" + userId + "'}) - [r: userTOsession]->(b:"+db2+"{no: '"+sessid+"'}) return b."+number+""
    gen_mark = graph.run(query).evaluate()
    print("marks will be printed not to worry")

    print(gen_mark)

    print("marks will be printed not to worry")
    return gen_mark

def sessionMarksStoring(Userid,Session,question,marks):

    newSession = ""

    query = "MATCH(a: user{Userid: '"+Userid+"'}) return a.Userid"
    userExist = graph.run(query).evaluate()

    if (userExist == None):

        query1 = "MATCH(c: root{Name: 'Session'}) CREATE(c) - [x: rootTOuser]-> (a: user{Userid:'"+Userid+"'})"
        graph.run(query1).evaluate()




    if question == "question1":
        query13 = "MATCH (n:session) RETURN n.no ORDER BY n.no DESC LIMIT 1;"
        sessionExist1 = graph.run(query13).evaluate()
        if sessionExist1== None:
            sessionExist1 = 0
        number = int(sessionExist1)+1
        query14 = "MATCH(a: user{Userid: '"+Userid+"'}) CREATE(a) - [r: userTOsession]->(b:session{no: '" + str(number) + "'})"
        graph.run(query14).evaluate()
#############################################################################################think
        open('Controller/vari.py', 'w').close()
        fruits = ["global userId\n", "userId = '" + Userid + "'\n", "global sessionId\n",
                  "sessionId = '" + str(number) + "'\n"]

        new_file = open("Controller/vari.py", mode="a+", encoding="utf-8")
        new_file.writelines(fruits)
        for line in new_file:
            print(line)

        new_file.close()

    # query3 = "MATCH(a: user{Userid: '"+Userid+"'}) - [r: userTOsession]->(b:session{no: '" + Session + "'}) return b.no"
    # sessionExist = graph.run(query3).evaluate()
    #
    # if (sessionExist == None):
    #
    #     query4 = "MATCH(a: user{Userid: '"+Userid+"'}) CREATE(a) - [r: userTOsession]->(b:session{no: '" + Session + "'})"
    #     graph.run(query4).evaluate()

    query3 = "MATCH (n:session) RETURN n.no ORDER BY n.no DESC LIMIT 1;"
    newSession = graph.run(query3).evaluate()


    query5 = "MATCH(a: user{Userid: '" + Userid + "'}) - [r: userTOsession]->(b:session{no: '" + newSession + "',"+question+":'"+marks+"'}) return b.no"
    questionExist = graph.run(query5).evaluate()

    if (questionExist == None):

        query6 = "MATCH(a: user{Userid: '"+Userid+"'}) - [r: userTOsession]->(b:session{no: '" + newSession + "'}) SET b."+question+" = '"+marks+"' RETURN b"
        marking = graph.run(query6).evaluate()

    return questionExist


# Anuruddha part
def createQtable1(languageName, subName):
    uid = vari.userId
    print(uid)
    exist = "MATCH(a:language{Name:'" + languageName + "'}) - [r: has]->(b:sub{Name:'" + subName + "'})RETURN b." + uid + ""
    qtableValue = graph.run(exist).evaluate()
    return qtableValue


#check user exist fro info retrievel
def checkuserinnwadas(uid):
    exist = "MATCH (n:CV{topic:'your strengths'}) RETURN count(n." + uid + ")>0"
    qtableValue = graph.run(exist).evaluate()
    print(qtableValue)
    return qtableValue



# this is to send and update values
def sendQtable(languageName,subName,qTableCreated):
    uid = vari.userId
    query = "Match (n:language{Name:'" + languageName + "'}) - [r: has]->(b:sub{Name:'" + subName + "'}) where b.Name='" + subName + "' SET b." + uid + "='" + qTableCreated + "'  RETURN b." + uid + ""
    qtableValue1 = graph.run(query).evaluate()
    return qtableValue1

#send the node list updated existing category-asked 1 remove krarapu 1
def sendExistingDifficultyList(userid,languageName,difficultyLevel,str_getDiffList3):
    exist = "MATCH(n: user_difficulty{uid: '" + userid + "'}) - [r: level]->(b:difficulty{technology: '" + languageName + "'}) SET b." + difficultyLevel + " ='" + str_getDiffList3 + "' return b." + difficultyLevel + ""
    qtableValue = graph.run(exist).evaluate()
    return qtableValue


 #get the difficulty list that wants to update - new list
def getNewRewardList(userid,languageName,rewardState):
    exist = "MATCH(n: user_difficulty{uid: '" + userid + "'}) - [r: level]->(b:difficulty{technology: '" + languageName + "'}) return b."+rewardState+""
    qtableValue = graph.run(exist).evaluate()
    return qtableValue


#get the easy, medium, hard to list
def getDifficultyList(userid,langName,category):
    exist = "MATCH(n: user_difficulty{uid: '" + userid + "'}) - [r: level]->(b:difficulty{technology: '" + langName + "'}) return b." + category + ""
    qtableValue = graph.run(exist).evaluate()
    print("hello anuruddha")
    print(qtableValue)
    return qtableValue

#set the new value to node
def sendNewDifficultyList(userid,languageName,rewardState,str_getDiffList4):
    exist = "MATCH(n: user_difficulty{uid: '" + userid + "'}) - [r: level]->(b:difficulty{technology: '" + languageName + "'}) SET b." + rewardState + " = '" + str_getDiffList4 + "' return b."+rewardState+""
    qtableValue = graph.run(exist).evaluate()
    return qtableValue


#get hard state to show suggestion
def getHardList(userid,languageName):
    exist = "MATCH(n: user_difficulty{uid: '" + userid + "'}) - [r: level]->(b:difficulty{technology: '" + languageName + "'}) return b.hard"
    qtableValue = graph.run(exist).evaluate()
    return qtableValue




#create a cv
def createNewCv(userid,fname,usage,usschool,usuni,usdob,usemail,ustpno,usweak,usstrengh,usidlcmp,usftech,usproone,ustech1,usprotwo,ustech2):
# def createNewCv(userid, usweak):
    print("hi")
    exist = "MATCH(c: CV{topic: 'yourself'}) CREATE(c) - [x: your_detail]-> (a: yourdet{uid:'" + userid + "',name:'"+fname+"',age:'"+usage+"',school:'"+usschool+"',university:'"+usuni+"', dob:'"+usdob+"',email:'"+usemail+"',telephone:'"+ustpno+"'})"
    createdCvUserDetail = graph.run(exist).evaluate()
    print(createdCvUserDetail)

    exist2 = "MATCH(c: CV{topic: 'your weaknesses'}) SET c."+userid+" = '"+usweak+"' "
    createdCvWeakDetail = graph.run(exist2).evaluate()
    print(createdCvWeakDetail)


    exist3 = "MATCH(c: CV{topic: 'your strengths'}) SET c." + userid + " = '" + usstrengh + "' "
    createdCvStrenDetail = graph.run(exist3).evaluate()
    print(createdCvStrenDetail)


    exist4 = "MATCH(c: CV{topic: 'your ideal company'}) SET c." + userid + " = '" + usidlcmp + "' "
    createdCvIdlCmpDetail = graph.run(exist4).evaluate()
    print(createdCvIdlCmpDetail)


    exist5 = "MATCH(c: CV{topic: 'familiar technologies'}) SET c." + userid + " = '" + usftech + "' "
    createdCvFTechDetail = graph.run(exist5).evaluate()
    print(createdCvFTechDetail)


    exist6 = "MATCH(c: project{pid: 'p1'}) CREATE(c) - [x: projects_details]-> (a: project_d{uid:'" + userid + "',topic:'"+usproone+"',technologies:'"+ustech1+"'})"
    createdCvProOneDetail = graph.run(exist6).evaluate()
    print(createdCvProOneDetail)


    exist6 = "MATCH(c: project{pid: 'p2'}) CREATE(c) - [x: projects_details]-> (a: project_d{uid:'" + userid + "',topic:'" + usprotwo + "',technologies:'" + ustech2 + "'})"
    createdCvProOneDetail = graph.run(exist6).evaluate()
    print(createdCvProOneDetail)

    return 1






def cvQuestionProjectGen(db,db2,pid,user):
  # query = "MATCH (j:"+db+"{pid:'"+ pid+"'}) RETURN j.topic"
  query = "MATCH (j:" + db + "{pid:'" + pid + "'}) - [r: projects_details]->(b:" + db2 + "{uid:'" + user + "'}) RETURN b.topic "
  gen_Question = graph.run(query).evaluate()
  print(gen_Question)
  return gen_Question

def addDifficultyLevelsForSpecificTech(tech,easy,medium,hard):
    # query = "MATCH(u:root{topic:'difficulty levels'})-[r:level]->(b:user_difficulty) CREATE (N: difficulty{technology:"+ tech +",easy:"+ easy +", medium:"+medium+ ",hard:"+hard+"}) MERGE(b)-[r1:level]->(N)"
    query = "MATCH(u:root{topic:'difficulty levels'})-[r:level]->(b:user_difficulty) CREATE (N: difficulty{technology:'"+tech+"',easy:'"+easy+"',medium:'"+medium+"',hard:'"+hard+"'})MERGE(b)-[r1:level]->(N)"
    add_node = graph.run(query).evaluate()
    print(add_node)
    return add_node
# addDifficultyLevelsForSpecificTech("a","","","1")

#retrieve the topics which are available in the db
# def getExistingTechnologies():
#     query = "MATCH(u:root{Name:'technical'})-[r:have]->(b:language) RETURN b.Name"
#     node_list = graph.run(query).evaluate()
#     print(node_list)
#     return node_list
# getExistingTechnologies()
def getExistingTechnologies():
    query = "MATCH(u:root{Name:'technical'})-[r:have]->(b:language) RETURN b.Name"
    node_list = graph.run(query).data()
    mylist = []
    for x in range (0,len(node_list)):
        mylist.append(node_list[x]['b.Name'])
    return mylist
# print(getExistingTechnologies())

def genUserDiffLevel(uid):
    query = "MATCH(J1:root{topic:'difficulty levels'}) CREATE (J2: user_difficulty{uid:'"+uid+"'}) MERGE(J1)-[r1:level]->(J2)"
    node = graph.run(query).evaluate()
    print(node)
    return node

def addDifficultyLevelsForTech(uid,tech,easy,medium,hard):
    print(uid)
    print(tech)
    print(easy)
    print(medium)
    print(hard)
    query = "MATCH(u:root{topic:'difficulty levels'})-[r:level]->(b:user_difficulty{uid:'"+uid+"'}) CREATE (N: difficulty{technology:'"+tech+"',easy:'"+easy+"',medium:'"+medium+"',hard:'"+hard+"'})MERGE(b)-[r1:level]->(N)"
    # query = "MATCH(u:root{topic:'difficulty levels'})-[r:level]->(b:user_difficulty{uid:'"+uid+"'}) CREATE (b)-[:level]->(gg:technology{technology:'"+tech+"',easy:'"+easy+"',medium:'"+medium+"',hard:'"+hard+"'})"

    add_node = graph.run(query).evaluate()
    print(add_node)
    return add_node
# addDifficultyLevelsForTech("uid033","ccc","1,2,5,6,9,15","3,7,10,12,16","4,8,11,13,14")
def addDiffLevelNestedNodesForTech(uid,tech,easy,medium,hard):
    query = "MATCH(u:root{topic:'difficulty levels'})-[r:level]->(b:user_difficulty{uid:'"+uid+"'})-[r2:level]->(c:difficulty{technology:'"+tech+"'}) CREATE (N: difficulty{technology:'"+tech+"',easy:'"+easy+"',medium:'"+medium+"',hard:'"+hard+"'})MERGE(c)-[r5:nested_level]->(N)"
    add_node2 = graph.run(query).evaluate()
    print(add_node2)
    return add_node2
# addDiffLevelNestedNodesForTech("uid080","python","1,2,5,6,9,15","3,7,10,12,16","4,8,11,13,14")

def getLastCreatedUid():
    query13 = "MATCH (n:oneUser) RETURN n.id ORDER BY n.id DESC LIMIT 1"
    useridz = graph.run(query13).evaluate()
    print(useridz)
    return useridz

#----------------ayesh voice-------------------------------

#ayesh voice createVoiceUser
def createVoiceUser(userId):
    voiceNode1 = "Match(m: root{Name: 'VoiceResult'}) CREATE (m) -[c:connectToUser]-> (u: userNode{userId :'" + userId + "'})"
    create_voice_node = graph.run(voiceNode1).evaluate()
    return create_voice_node

#ayesh voice createVoiceUserSession
def createVoiceUserSession(userId,sessionNumber):
    VoiceSessionNum = "Vses" + sessionNumber
    createVoiceUserSession = "MATCH (m:root{Name:'VoiceResult'})-[c:connectToUser]-> (u: userNode{userId :'" + userId + "'})CREATE (u) - [s: connectToSession]->(i:interviewSession{number : '"+VoiceSessionNum+"'})"
    create_voice_ses_node = graph.run(createVoiceUserSession).evaluate()
    return create_voice_ses_node

#ayesh voice getQuestionNumberToSave
def getQuestionNumberToSave(userId,sessionNumber,qnumber):
    queryVoice1 = "MATCH(u: userNode{userId: '" + userId + "'}) - [s: connectToSession]->(i:interviewSession{number: '"+sessionNumber+"'}) return i."+qnumber+""
    generate_qNumber = graph.run(queryVoice1).evaluate()
    return generate_qNumber

#ayesh voice saveVoiceMarks
def saveVoiceMarks(userId,sessionNumber,qnumber, voiceMark):
    VoiceSessionNum = "Vses" + sessionNumber
    saveMarkQuery = "MATCH(u: userNode{userId: '" + userId + "'}) - [s: connectToSession]->(i:interviewSession{number: '" + VoiceSessionNum + "'}) SET i." + qnumber + " = '" + voiceMark + "' RETURN i"
    generate_mark = graph.run(saveMarkQuery).evaluate()
    return generate_mark

#----------------ayesh facial-----------------------------

#ayesh facial createVoiceUser
def createFacialUser(userId):
    facialNode1 = "Match(m: root{Name: 'FacialResult'}) CREATE (m) -[c:connectToUser]-> (u: userNode{userId :'" + userId + "'})"
    create_facial_node = graph.run(facialNode1).evaluate()
    return create_facial_node

#ayesh facial createFacialUserSession
def createFacialUserSession(userId,sessionNumber):
    FacialSessionNum = "Fses" + sessionNumber
    createFacialUserSession = "MATCH (m:root{Name:'FacialResult'})-[c:connectToUser]-> (u: userNode{userId :'" + userId + "'})CREATE (u) - [s: connectToSession]->(i:interviewSession{number : '"+FacialSessionNum+"'})"
    create_Facial_ses_node = graph.run(createFacialUserSession).evaluate()
    return create_Facial_ses_node

#ayesh facial getQuestionNumberToSave
def getQuestionNumberToSaveFacial(userId,sessionNumber,qnumber):
    queryFacia11 = "MATCH(u: userNode{userId: '" + userId + "'}) - [s: connectToSession]->(i:interviewSession{number: '"+sessionNumber+"'}) return i."+qnumber+""
    generate_facial_qNumber = graph.run(queryFacia11).evaluate()
    return generate_facial_qNumber

#ayesh facial saveFacialMarks
def saveFacialMarks(userId,sessionNumber,qnumber, facialMark):
    FacialSessionNum = "Fses" + sessionNumber
    saveFacialMarkQuery = "MATCH(u: userNode{userId: '" + userId + "'}) - [s: connectToSession]->(i:interviewSession{number: '" + FacialSessionNum + "'}) SET i." + qnumber + " = '" + facialMark + "' RETURN i"
    generate_facial_mark = graph.run(saveFacialMarkQuery).evaluate()
    return generate_facial_mark








