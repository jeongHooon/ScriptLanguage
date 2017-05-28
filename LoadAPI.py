from xmlbook import *
from http.client import HTTPConnection
from http.server import BaseHTTPRequestHandler, HTTPServer

regKey = 'NziFFXEldFsoUvMdgCHihUyTTIhdMuveRk8ec9HFjLV8u9iRO9jqaHYZwd2v6JJmF0MAvV1xJdh9BJHqESaApg%3D%3D'
server = "api.seibro.or.kr"
conn = None
def userURIBuilder(server,**user):
    str = "https://" + server + "/openapi/service/CorpSvc/getIssucoCustnoByNm?"
    for key in user.keys():
        str += key + "=" + user[key] + "&"
    return str

def connectOpenAPIServer():
    global conn, server
    conn = HTTPConnection(server)

def getInfoDataFromname(find_key):
    global server, regKey, conn
    if conn == None:
        connectOpenAPIServer()
    uri = userURIBuilder(server, issucoNm=find_key, numOfRows=str(1), ServiceKey=str(regKey))
    # uri = userURIBuilder(server, key=regKey, query='%20', display="1", start="1", target="book_adv", d_isbn=isbn)
    conn.request("GET", uri)

    req = conn.getresponse()
    print(req.status)
    if int(req.status) == 200:
        print("Info data downloading complete!")
        return extractInfoData(req.read())
    else:
        print("OpenAPI request has been failed!! please retry")
        return None

def extractInfoData(strXml):
    from xml.etree import ElementTree
    tree = ElementTree.fromstring(strXml)
    print(strXml)
    # Book 엘리먼트를 가져옵니다.
    itemElements = tree.getiterator("response")  # return list type
    print(itemElements)
    for a in itemElements:
        body = a.find("body")
        for b in body:
            items = b.find("items")
            for c in items:
                item = c.find("item")
                for d in item:
                    issucoCustno = d.find("issucoCustno")
                    issucoNm = d.find("issucoNm")
                    listNm = d.find("listNm")

                    return {"issucoCustno":issucoCustno.text,"issucoNm":issucoNm.text,"listNm":listNm.text}