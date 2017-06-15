from tkinter import *
from LoadAPI import *

window = Tk()
window.geometry("730x250")

def process():
    global dic
    text = str(inputText.get())
    if state == Search.CustNo:
        getInfoDataFromname(text)
    elif state == Search.BasicInfo:
        getInfoFromNum(text)
    elif state == Search.StockIn:
        getStockFromNum(text)
    elif state == Search.FinancialMean:
        dic = getInfoFromKey(text)
        insertList()
def select():
    global searchList1
    global searchList2
    global dic
    searchList2.delete(0,)
    searchList2.insert(END,dic[searchList1.get(searchList1.curselection()[0])])
    searchList2.yview_scroll ( 3, PAGES )

class Search(enum.Enum):
    CustNo = 0
    BasicInfo = 1
    FinancialMean = 2
    StockIn = 3
state = Search.CustNo

def IssucoCustno():
    global check
    global searchList1
    global searchList2
    global state
    searchList1.destroy()
    searchList2.destroy()
    searchList1 = Listbox(window, width=20)
    searchList1.place(x=110, y=50)
    searchList2 = Listbox(window, width=20)
    searchList2.place(x=420, y=50)
    state = Search.CustNo


def IssucoBasicInfo():
    global check
    global searchList1
    global searchList2
    global state
    searchList1.destroy()
    searchList2.destroy()
    searchList1 = Listbox(window, width=61)
    searchList1.place(x=110, y=50)
    state = Search.BasicInfo


def FinancialTermMeaning():
    global check
    global searchList1
    global searchList2
    global state
    searchList1.destroy()
    searchList2.destroy()
    searchList1 = Listbox(window, width=30)
    searchList1.place(x=110, y=50)
    searchList2 = Listbox(window, width=20)
    searchList2.place(x=420, y=50)
    state = Search.FinancialMean
def insertList():
    global dic
    global searchList1
    global searchList2

    for d in dic.keys():
        searchList1.insert(END,d);



def StockInfo():
    global check
    global searchList1
    global searchList2
    global state
    searchList1.destroy()
    searchList2.destroy()
    searchList1 = Listbox(window, width=30)
    searchList1.place(x=110, y=50)
    searchList2 = Listbox(window, width=20)
    searchList2.place(x=420, y=50)
    state = Search.StockIn
def send_mail():
    import smtplib
    from email.mime.base import MIMEBase
    from email.mime.text import MIMEText

    # global value
    host = "smtp.gmail.com"  # Gmail STMP 서버 주소.
    port = "587"
    htmlFileName = "book.xml"

    senderAddr = "pkekzm6239@gmail.com" # 보내는 사람 email 주소.
    recipientAddr = "pkekzm6239@naver.com"  # 받는 사람 email 주소.

    msg = MIMEBase("multipart", "alternative")
    msg['Subject'] = "Test email in Python 3.5"
    msg['From'] = senderAddr
    msg['To'] = recipientAddr
    htmlFD = open(htmlFileName, 'rb')
    HtmlPart = MIMEText(htmlFD.read(), 'html', _charset='UTF-8')
    htmlFD.close()

    # 만들었던 mime을 MIMEBase에 첨부 시킨다.
    msg.attach(HtmlPart)

    # 메일을 발송한다.
    s = smtplib.SMTP(host, port)
    # s.set_debuglevel(1)        # 디버깅이 필요할 경우 주석을 푼다.
    s.ehlo()
    s.starttls()
    s.ehlo()
    s.login("pkekzm6239@gmail.com","vosalxld!0625")
    s.sendmail(senderAddr, [recipientAddr], msg.as_string())
    s.close()


def start():
    global check
    global searchList1
    global searchList2
    global inputText
    searchList1 = Listbox(window, width=42)
    searchList1.place(x=110, y=50)
    searchList2 = Listbox(window, width=42)
    searchList2.place(x=420, y=50)
    button1 = Button(window, text="발행정보\n조회", font = 20,cursor="hand2",command = IssucoCustno)
    button1.place(x=10,y=10)
    button2 = Button(window, text="기업정보\n조회", font = 20,cursor="hand2", command = IssucoBasicInfo)
    button2.place(x=10,y=70)
    button3 = Button(window, text="주식정보\n조회", font = 20,cursor="hand2", command = StockInfo)
    button3.place(x=10,y=130)
    button4 = Button(window, text="금융용어\n조회", font = 20,cursor="hand2", command = FinancialTermMeaning)
    button4.place(x=10,y=190)
    #button5 = Button(window, text="aaa", font=20, cursor="hand2", command=send_mail)
    #button5.place(x=80, y=190)
    buttonS = Button(window, text="Select", font=20, cursor="hand2", command=select)
    buttonS.place(x=380, y=210)
    inputText = Entry(window,width = 50,font = 10)
    inputText.place(x = 110, y = 10)
    button5 = Button(window, text="검색", font=20, cursor="hand2", command=process)
    button5.place(x=670,y=10)
    window.mainloop()

check = False




