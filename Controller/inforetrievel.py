import urllib.request
import urllib.request
import lxml.html
import re
import random
import bs4 as bs
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
from urllib.request import Request, urlopen
import importlib
from py2neo import Graph
from Controller import vari
graph = Graph("http://neo4j:Sepalika1993@127.0.0.1:7474/db/data")



def inforetrievel(technology):

    mylist = []
    mylist1 = []
    connection = urllib.request.urlopen('https://www.tutorialspoint.com/'+technology)

    dom = lxml.html.fromstring(connection.read())
    for link in dom.xpath('//a/@href'): # select the url in href for all a tags(links)
        link_list = str(link)
        result = re.search('/'+technology+'/',link_list)
        if result != None:
            mylist.append(link_list)

    # for c in range(0, len(mylist)):
    #     print(mylist[c])

    number = 0

    for x in range(4):
        mylist1.append(random.randint(1,10)*2,)

    open('test.txt', 'w').close()

    if(len(mylist)>1):
        query = "match(n: root{Name: 'technical'}) create(n) - [: have]->(l:language{Name:'" + technology + "'})"
        graph.run(query).evaluate()

    aa = 0

    for c in range(0, len(mylist)):



        uClient = uReq('https://www.tutorialspoint.com'+mylist[c])
        page_html = uClient.read()
        uClient.close()
        page_soup = soup(page_html, "html.parser")
        title = page_soup.title.string
        paragraph = page_soup.p.string
        number = 1
        if paragraph !=None:
            if paragraph!="" or title!="" or len(paragraph)>3:
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
                print(aa)
                uid = vari.userId
                qtable = "[0.0, 0.0, 0.0, 0.0, 0.0],[0.0, 0.0, 0.0, 0.0, 0.0],[0.0, 0.0, 0.0, 0.0, 0.0],[0.0, 0.0, 0.0, 0.0, 0.0],[0.0, 0.0, 0.0, 0.0, 0.0]"
                query = "match(l:language{Name:'"+technology+"'}) create (l)-[:has]->(x:sub{id:'"+str(aa)+"',Details:'"+str(paragraph)+"',Name:'"+str(title)+"'," + uid + ":'"+qtable+"'}) return x"
                print(graph.run(query).evaluate())

    return number