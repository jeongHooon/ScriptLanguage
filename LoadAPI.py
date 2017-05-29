from xmlbook import *
import urllib
from http.client import HTTPConnection
from http.server import BaseHTTPRequestHandler, HTTPServer
from xml.dom.minidom import parse, parseString

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
    find_key = urllib.parse.quote(find_key)
    uri = userURIBuilder(server, issucoNm=find_key, numOfRows=str(10000), ServiceKey=regKey)
    # uri = userURIBuilder(server, key=regKey, query='%20', display="1", start="1", target="book_adv", d_isbn=isbn)
    conn.request("GET", uri)

    req = conn.getresponse()
    print(req.status)
    if int(req.status) == 200:
        infoData = req.read().decode('utf-8')
        print("Info data downloading complete!")
        #return extractInfoData(infoData)
        return LoadInfoData(infoData)
    else:
        print("OpenAPI request has been failed!! please retry")
        return None

def extractInfoData(infoData):
    from xml.etree import ElementTree
    tree = ElementTree.fromstring(infoData)
    print(infoData)
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
def LoadInfoData(infoData):
    parseData = parseString(infoData)
    response = parseData.childNodes
    headerNbody = response[0].childNodes
    body = headerNbody[1].childNodes
    items = body[0].childNodes
    pass
