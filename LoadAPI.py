from xmlbook import *
import urllib
from http.client import HTTPConnection
from http.server import BaseHTTPRequestHandler, HTTPServer
from xml.dom.minidom import parse, parseString
#from GUI import *
regKey = 'NziFFXEldFsoUvMdgCHihUyTTIhdMuveRk8ec9HFjLV8u9iRO9jqaHYZwd2v6JJmF0MAvV1xJdh9BJHqESaApg%3D%3D'
server = "api.seibro.or.kr"
conn = None
def userURIBuilder(server,**user):
    str = "https://" + server + "/openapi/service/CorpSvc/getIssucoCustnoByNm?"
    for key in user.keys():
        str += key + "=" + user[key] + "&"
    return str
def userURIBuilder2(server,**user):
    str = "https://" + server + "/openapi/service/CorpSvc/getIssucoBasicInfo?"
    for key in user.keys():
        str += key + "=" + user[key] + "&"
    return str
def userURIBuilder4(server,**user):
    str = "https://" + server + "/openapi/service/CorpSvc/getSecnIssuInfoStock?"
    for key in user.keys():
        str += key + "=" + user[key] + "&"
    return str
def userURIBuilder3(server,**user):
    str = "https://" + server + "/openapi/service/FnTermSvc/getFinancialTermMeaning?"
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
    conn.request("GET", uri)

    req = conn.getresponse()
    print(req.status)
    if int(req.status) == 200:
        infoData = req.read().decode('utf-8')
        print("Info data downloading complete!")
        return LoadInfoData(infoData)
    else:
        print("OpenAPI request has been failed!! please retry")
        return None

def getInfoFromNum(find_key):
    global server, regKey, conn
    if conn == None:
        connectOpenAPIServer()
    uri = userURIBuilder2(server, issucoCustno=find_key, ServiceKey=regKey)
    conn.request("GET", uri)
    req = conn.getresponse()
    print(req.status)
    if int(req.status) == 200:
        infoData = req.read().decode('utf-8')
        print("Info data downloading complete!")

        return LoadInfoData2(infoData)
    else:
        print("OpenAPI request has been failed!! please retry")
        return None
def getStockFromNum(find_key):
    global server, regKey, conn
    if conn == None:
        connectOpenAPIServer()
    uri = userURIBuilder4(server, issucoCustno=find_key, ServiceKey=regKey)
    conn.request("GET", uri)
    req = conn.getresponse()
    if int(req.status) == 200:
        infoData = req.read().decode('utf-8')
        return LoadInfoData4(infoData)
    else:
        print("OpenAPI request has been failed!! please retry")
        return None

def getInfoFromKey(find_key):
    global server, regKey, conn
    if conn == None:
        connectOpenAPIServer()
    find_key = urllib.parse.quote(find_key)
    uri = userURIBuilder3(server, term=find_key, numOfRows=str(10000), ServiceKey=regKey)
    conn.request("GET", uri)

    req = conn.getresponse()
    print(req.status)
    if int(req.status) == 200:
        infoData = req.read().decode('utf-8')
        print("Info data downloading complete!")

        return LoadInfoData3(infoData)
    else:
        print("OpenAPI request has been failed!! please retry")
        return None
def LoadInfoData(infoData):
    global conn
    parseData = parseString(infoData)
    response = parseData.childNodes
    headerNbody = response[0].childNodes
    body = headerNbody[1].childNodes

    items = body[0].childNodes
    for item in items:
        issucoCustno = item.childNodes[0]
        issucoCustnoData = issucoCustno.childNodes[0].data
        issucoNm = item.childNodes[1]
        issucoNmData = issucoNm.childNodes[0].data
        if item.childNodes.length == 3:
            listNm = item.childNodes[2]
            listNmData = listNm.childNodes[0].data
            print("발행번호: ", issucoCustnoData, "\n기업이름: ", issucoNmData, "listNm", listNmData)
        else:
            print("발행번호: ", issucoCustnoData, "\n기업이름: ", issucoNmData)

    conn.close()

def LoadInfoData2(infoData):
    global conn
    parseData = parseString(infoData)
    response = parseData.childNodes
    headerNbody = response[0].childNodes
    body = headerNbody[1].childNodes
    try:
        item = body[0].childNodes
        for ele in item:
            if ele.localName == 'engCustNm':
                engCustNmData = ele.childNodes[0].data
            if ele.localName == 'ceoNm':
                ceoNmData = ele.childNodes[0].data
            if ele.localName == 'founDt':
                founDtData = ele.childNodes[0].data
            if ele.localName == 'totalStkCnt':
                totalStkCntData = ele.childNodes[0].data
        print("기업명: ",engCustNmData, "\nCeo: ", ceoNmData, "\n설립일: ", founDtData, "\n총 발행 주식 수: ", totalStkCntData)
    except:
        print("해당 발행번호에 대한 정보가 존재하지 않습니다.")
    conn.close()

def LoadInfoData3(infoData):
    global conn
    parseData = parseString(infoData)
    response = parseData.childNodes
    headerNbody = response[0].childNodes
    body = headerNbody[1].childNodes
    items = body[0].childNodes
    dic = {}
    for item in items:
        fnceDictNm = item.childNodes[0]
        fnceDictNmData = fnceDictNm.childNodes[0].data

        ksdFnceDictDescContent = item.childNodes[1]
        ksdFnceDictDescContentData = ksdFnceDictDescContent.childNodes[0].data
        dic[fnceDictNmData] = ksdFnceDictDescContentData
        print("용어명: ", fnceDictNmData, "\n설명: ", ksdFnceDictDescContentData)
    conn.close()
    return dic


def LoadInfoData4(infoData):
    global conn
    parseData = parseString(infoData)
    response = parseData.childNodes
    headerNbody = response[0].childNodes
    body = headerNbody[1].childNodes
    try:
        items = body[0].childNodes
        for item in items:
            caltotMartTpcd = item.childNodes[0]
            caltotMartTpcdData = caltotMartTpcd.childNodes[0].data
            stkKacd = item.childNodes[4]
            stkKacdData = stkKacd.childNodes[0].data
        print("상장구분명: ", caltotMartTpcdData, "\n주식종류명: ", stkKacdData)
    except:
        print("해당 발행번호에 대한 정보가 존재하지 않습니다.")
    conn.close()