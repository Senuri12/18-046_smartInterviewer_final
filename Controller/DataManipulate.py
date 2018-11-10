from py2neo import Graph
from py2neo import Node, Relationship
from Controller import vari


graph = Graph()

# vikum = Node("User", Id="U0002", name="nidarshana Vikram",age="24", School="studied School", AL="mathematics", university="Sri Lanka Institute Information Technology", weaknesses="laziness", Strengths="creativity", qualification="software engineering", project="Hotel Management System", technology="Java", GPA="3.5")
# graph.create(vikum)

# graph.delete_all()

# print(ConnectionToNeo4j.sessionMarksStoring('UID001','1','question2','0.8'))

# query = "MATCH(n: oneUser) RETURN n.id"
# node_list = graph.run(query).data()
# mylist = []
# for x in range(0, len(node_list)):
#     mylist.append(node_list[x]['n.id'])
# valu=""
# for y in range(0,len(mylist)):
#     qtable = "[0.0, 0.0, 0.0, 0.0, 0.0],[0.0, 0.0, 0.0, 0.0, 0.0],[0.0, 0.0, 0.0, 0.0, 0.0],[0.0, 0.0, 0.0, 0.0, 0.0],[0.0, 0.0, 0.0, 0.0, 0.0]"
#     mylist[y]
#     cvas = str(mylist[y])+":'"+str(qtable)+"'"
#     if y==0:
#         valu = valu+cvas
#     else:
#         valu = valu+","+cvas
#
# print(valu)


# def getMatchingTopicsNonTech1(db):
#     qtable = "[0.0, 0.0, 0.0, 0.0, 0.0],[0.0, 0.0, 0.0, 0.0, 0.0],[0.0, 0.0, 0.0, 0.0, 0.0],[0.0, 0.0, 0.0, 0.0, 0.0],[0.0, 0.0, 0.0, 0.0, 0.0]"
#     useridz = vari.userId
#
#     query2 = "MATCH(a:language{Name:'" + db + "'}) return a." + useridz +""
#     availability2 = graph.run(query2).evaluate()
#
#
#     if availability2 == None:
#         query1 = "MATCH(a:language{Name:'" + db + "'}) set a." + useridz + "='" + qtable + "'"
#         availability1 = graph.run(query1).evaluate()
#
#
#
#
# getMatchingTopicsNonTech1("csharp")



# def checkuserinnwadas(uid):
#     exist = "MATCH (n:CV{topic:'your strengths'}) RETURN count(n."+uid+")>0"
#     qtableValue = graph.run(exist).evaluate()
#     print(qtableValue)
#     return qtableValue
#
#
# checkuserinnwadas("uid00sad1")


query = "MATCH(n: oneUser) RETURN n.id"
node_list = graph.run(query).data()
mylist = []
for x in range(0, len(node_list)):
    mylist.append(node_list[x]['n.id'])

print(mylist)