# import bs4 as bs
# from urllib.request import urlopen as uReq
# from bs4  import  BeautifulSoup as soup
#
# word ='cplusplus'
# if word == 'cplusplus':
#     word2 = ''
# search_url  = 'https://www.tutorialspoint.com/csharp/csharp_encapsulation.htm'
# # search_url2  = 'https://www.tutorialspoint.com/'+word+'/cpp_overview.htm'
# # search_url3 = 'https://www.tutorialspoint.com/cplusplus/cpp_environment_setup.htm'
#
# uClient = uReq(search_url)
# page_html = uClient.read()
# uClient.close()
# page_soup = soup(page_html,"html.parser")
# print(search_url)
# print(page_soup.title.string)
# print(page_soup.p)
# print("hhfhvbyhfvhuu")
# # print(page_soup.find_all('p'))
# # for divTag in page_soup.find("div",{"role":"note"}):
# #     print(divTag.string)
# #
# # for divTag in page_soup.find_all('p'):
# #     abc =  divTag.string
# #     cd = str(abc)
# #     cd = cd.replace('None','')
# #     cd = cd.replace('−', '')
# #     sep = '©'
# #     cd = cd.split(sep,1)[0]
# #     print(cd)
#
#
# import urllib.request
# import lxml.html
# connection = urllib.request.urlopen('https://www.tutorialspoint.com/csharp')
#
#
# import re
#
#
# dom =  lxml.html.fromstring(connection.read())
#
# mylist = []
#
# for link in dom.xpath('//a/@href'): # select the url in href for all a tags(links)
#     link_list = str(link)
#     result = re.search('/csharp/',link_list)
#     if result != None:
#         mylist.append(link_list)
#
# for c in range(0, len(mylist)):
#     print(mylist[c])
#     # print(link_list)
#
# # import bs4 as bs
# # import urllib.request
# # source = urllib.request.urlopen('https://en.wikipedia.org/wiki/Apple').read()
# # print(source)
# # soup = bs.BeautifulSoup(source,'lxml')
# # print(soup.encode("utf-8"))
# # # print(soup.find_all('div').encode("utf-8"))
from Controller import vari,TechnicalQuestions,NonTechnicalQuestions,questionSaver_testing,ConnectionToNeo4j

usftech = "java,python,abc"
techsAvailable = ""
infoRetList = ""
finalFamiliarTechList = ""
techWord_list = usftech.split(',')
for techWord in techWord_list:
    availability_node = ConnectionToNeo4j.getMatchingTopicsNonTech(techWord)
    print(techWord)
    print(availability_node)
    if availability_node == True:
        print("available")
        techsAvailable = techsAvailable + "," + techWord
        print(techsAvailable)
    else:
        print("not available")
        infoRet = "0"
        if infoRet != "0":
            print(infoRetList)
            infoRetList = infoRetList + "," + infoRet
            print(infoRetList)
finalFamiliarTechList = techsAvailable + "," + infoRetList
print(finalFamiliarTechList)
if finalFamiliarTechList[0] == ',':
    print("in")
    finalFamiliarTechList = finalFamiliarTechList[1:]
    print(finalFamiliarTechList)
stringLength = len(finalFamiliarTechList)-1
if finalFamiliarTechList[stringLength] == ',':
    print("hahaa")
    finalFamiliarTechList = finalFamiliarTechList[:stringLength]

print(len(finalFamiliarTechList))
print(finalFamiliarTechList)
