from Controller import infowhat
import lxml.html
import lxml.html
import re
import random
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
from urllib.request import Request, urlopen
import importlib
from py2neo import Graph
from Controller import vari
graph = Graph("http://neo4j:Sepalika1993@127.0.0.1:7474/db/data")

def inforetrievel(technology):
    print(technology)
    mylist = []
    mylist1 = []
    number = []
    aa = 0
    try:


        url3 = Request('https://www.tutorialspoint.com/'+technology, headers={'User-Agent': 'Mozilla/5.0'})
        connection = urlopen(url3).read()
        dom = lxml.html.fromstring(connection)




        for link in dom.xpath('//a/@href'):  # select the url in href for all a tags(links)
            link_list = str(link)

            result = re.search('/' + technology + '/', link_list)
            if result != None:
                mylist.append(link_list)

        if len(mylist) != 0:
            #
            # # for c in range(0, len(mylist)):
            # #     print(mylist[c])

            number.append(technology)
            for x in range(4):
                mylist1.append(random.randint(1,10)*2,)

            open('test.txt', 'w').close()


            if(len(mylist)>1):

                query = "match(n: root{Name: 'technical'}) create(n) - [: have]->(l:language{Name:'" + technology + "'})"
                graph.run(query).evaluate()



            for c in range(0, len(mylist)):


                    uClient = uReq('https://www.tutorialspoint.com'+mylist[c])
                    page_html = uClient.read()
                    uClient.close()
                    page_soup = soup(page_html, "html.parser")
                    title = page_soup.title.string
                    paragraph = page_soup.p.string
                    # number = technology

                    if paragraph !=None:
                        if paragraph!="" or title!="" or len(paragraph)>3 or "Copyright 2018. All Rights Reserved." not in paragraph:
                            # print(mylist[c])
                            # print(page_soup.title)
                            # print(page_soup.p)
                            title = title.replace("'", "")
                            paragraph = paragraph.replace("'", "")

                            title = title.replace('"', '')
                            paragraph = paragraph.replace('"', '')

                            title = title.replace('\\', '')
                            paragraph = paragraph.replace('\\', '')

                            aa= aa +1
                            print(title)
                            print(len(paragraph))
                            print("count me"+str(aa))
                            print(paragraph)

                            #anurudda ewwa wadak ne
                            # uid = vari.userId
                            # qtable = "[0.0, 0.0, 0.0, 0.0, 0.0],[0.0, 0.0, 0.0, 0.0, 0.0],[0.0, 0.0, 0.0, 0.0, 0.0],[0.0, 0.0, 0.0, 0.0, 0.0],[0.0, 0.0, 0.0, 0.0, 0.0]"

                            # query = "match(l:language{Name:'" + technology + "'}) create (l)-[:has]->(x:sub{id:'" + str(
                            #     aa) + "',Details:'" + str(paragraph) + "',Name:'" + str(
                            #     title) + "', '" + uid + "'= '" + qtable + "'}) return x"

                            query = "MATCH(n: oneUser) RETURN n.id"
                            node_list = graph.run(query).data()
                            mylist12 = []
                            for x in range(0, len(node_list)):
                                mylist12.append(node_list[x]['n.id'])
                                print(mylist12)

                            valu = ""
                            for y in range(0, len(mylist12)):
                                qtable = "[0.0, 0.0, 0.0, 0.0, 0.0],[0.0, 0.0, 0.0, 0.0, 0.0],[0.0, 0.0, 0.0, 0.0, 0.0],[0.0, 0.0, 0.0, 0.0, 0.0],[0.0, 0.0, 0.0, 0.0, 0.0]"
                                print(mylist12[y])

                                cvas = str(mylist12[y]) + ":'" + str(qtable) + "'"
                                if y == 0:
                                    valu = valu + cvas
                                else:
                                    valu = valu + "," + cvas

                            query = "match(l:language{Name:'"+technology+"'}) create (l)-[:has]->(x:sub{id:'"+str(aa)+"',Details:'"+str(paragraph)+"',Name:'"+str(title)+"',"+valu+"}) return x"
                            print(graph.run(query).evaluate())



        else:
            print("ethulta gya" + str(len(number)))
            number.append("0")
            # number.append("0")

    except:
        pass


    if len(number)==0:

        number.append("0")
<<<<<<< HEAD
        number.append("0")



        aa= aa +1
        print(title)
        print(len(paragraph))
        print(aa)
        uid = vari.userId
        qtable = "[0.0, 0.0, 0.0, 0.0, 0.0],[0.0, 0.0, 0.0, 0.0, 0.0],[0.0, 0.0, 0.0, 0.0, 0.0],[0.0, 0.0, 0.0, 0.0, 0.0],[0.0, 0.0, 0.0, 0.0, 0.0]"
        query = "match(l:language{Name:'"+technology+"'}) create (l)-[:has]->(x:sub{id:'"+str(aa)+"',Details:'"+str(paragraph)+"',Name:'"+str(title)+"'," + uid + ":'"+qtable+"'}) return x"
        print(graph.run(query).evaluate())

=======
        # number.append("0")
>>>>>>> 19a3a8b2b49ad3ff3091bd95655d7cac9ff47634

    number.append(aa)
    print("testinghhhh"+str(number))
    return number