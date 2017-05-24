from xmlbook import *
from http.client import HTTPConnection
from http.server import BaseHTTPRequestHandler, HTTPServer

regKey = 'NziFFXEldFsoUvMdgCHihUyTTIhdMuveRk8ec9HFjLV8u9iRO9jqaHYZwd2v6JJmF0MAvV1xJdh9BJHqESaApg%3D%3D'
server = "api.seibro.or.kr"

def userURIBuilder(server,**user):
    str = "https://" + server + "/openapi/service/CorpSvc/getIssucoCustnoByNm?"
    for key in user.keys():
        str += key + "=" + user[key] + "&"
    return str

def connectOpenAPIServer():
    global conn, server
    conn = HTTPConnection(server)

def getBookDataFromISBN(find_key):
    global server, regKey, conn
    if conn == None:
        connectOpenAPIServer()
    uri = userURIBuilder(server, issucoNm=find_key, numOfRows=1, ServiceKey=regKey)
    # uri = userURIBuilder(server, key=regKey, query='%20', display="1", start="1", target="book_adv", d_isbn=isbn)
    conn.request("GET", uri)

    req = conn.getresponse()
    print(req.status)
    if int(req.status) == 200:
        print("Book data downloading complete!")
        return extractBookData(req.read())
    else:
        print("OpenAPI request has been failed!! please retry")
        return None

def extractBookData(strXml):
    from xml.etree import ElementTree
    tree = ElementTree.fromstring(strXml)
    print(strXml)
    # Book 엘리먼트를 가져옵니다.
    itemElements = tree.getiterator("item")  # return list type
    print(itemElements)
    for item in itemElements:
        isbn = item.find("isbn")
        strTitle = item.find("title")
        print (strTitle)
        if len(strTitle.text) > 0 :
           return {"ISBN":isbn.text,"title":strTitle.text}