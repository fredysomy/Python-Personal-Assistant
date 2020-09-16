from tkinter import*
from tkinter import messagebox
import time
from datetime import datetime
import requests
from bs4 import BeautifulSoup
import html5lib
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
op=Options()
op.add_argument("headless")
root=Tk()
root.geometry("400x320")
root.resizable(0,0)
root.title("CHATBOT_LOGIN")
root.configure(bg="grey")
user="f"
pasw="h"

def timte():
    time_now=time.strftime('%r:%x')
    timestring.config(text=time_now)
    timestring.after(100,timte)
timestring=Label(root)
timestring.place(x=90,y=100)
timte()


def chatbotmainwindow():

    chatbot=Tk()
    chatbot.geometry("1025x700")
    chatbot.resizable(0,0)
    chatbot.title("CHATBOT")
    qw=Label(chatbot,text="JARVIS V-2.3.4",font="time 32 bold",fg="#FFFFFF",bg="#507075",borderwidth=3.5, relief=GROOVE)
    chatbot.configure(bg="grey")
    qw.place(x=63,y=10)
    def chattime():
        tisme_now=time.strftime('%H:%M:%S')
        tismestring.config(text=tisme_now)
        tismestring.after(100,chattime)
    tismestring=Label(chatbot)
    tismestring.place(x=90,y=100)
    chattime()
    def chat():
        qweqw=str(chat_pad.get())
        qw=qweqw.split()
        if "hi" in qw or "hello" in qw:
            chatpad.configure(text="Hi "+user+ ",its nice seeing you back")
        elif "name" in qw or "greatname" in qw:
            chatpad.configure(text="My name is JARVIS")
        elif "male" in qw or "female" in qw:
	        chatpad.configure(text="Well i am just a computer program dude")
        elif "creator" in qw or "created" in qw or "daddy" in qw:
	        chatpad.configure(text="Well i am written by Fredy,Shahin,Siddarth,Adarsh")
        elif "hate" in qw and "you" in qw:
	        chatpad.configure(text="Well did i do any offence")
        elif "doing" in qw or "job" in qw or "purpose" in qw :
	        chatpad.configure(text="I am a chatbot,programmed to talk to humans")
        elif "favorite" in qw and "food" in qw :
	        chatpad.configure(text="My favorite food is 230 v electricity,yummy")
        elif "do" in qw and "can" in qw:
	        chatpad.configure(text="I can do many things,Talk with you,etc")
        elif "girlfriend" in qw or "boyfriend" in qw:
	        chatpad.configure(text="I AM INSIDE A PC AND IF YOU COME INSIDE I SHALL BE YOUR FRIEND")
        elif "party" in qw and "you" in qw:
	        chatpad.configure(text="I am in the side of the rulling party,hahaha")
        elif "can" in qw and "sing" in qw:
	        chatpad.configure(text="I can play a song for you if you enter"'googlesearch,song'"")
        elif "you" in qw and "married" in qw:
	        chatpad.configure(text="I have a dozen of wives and husbands.. "+'/n'+" are you a fool i am a Program!!!")
        elif "friend" in qw:
	        chatpad.configure(text="My best friend are my creators,Ican be your friend too!!")
        elif "like" in qw and "humans":
	        chatpad.configure(text="Yes, that is why i am talking to you")
        elif "specialities" in qw or "abilities" in qw :
	        chatpad.configure(text="My specialities is,i dont get angry talking with you")
        elif "AI" in qw or "artificial" in qw and "intelligence" in qw:
	        chatpad.configure(text="No i am not that developed,Underdeveloped")
        elif "whatis" in qw:
                eew=" "
                for ee in range(1,len(qw)):
                    eew=eew+" "+qw[ee]
                ww=eew
                try:
                    rootwik=Tk()
                    S = Scrollbar(rootwik)
                    T = Text(rootwik, height=20, width=60)
                    S.pack(side=RIGHT, fill=Y)
                    T.pack(side=LEFT, fill=Y)
                    S.config(command=T.yview)
                    T.config(yscrollcommand=S.set)
                    op=Options()
                    op.add_argument("headless")
                    url="https://www.wikipedia.org/"
                    driver=webdriver.Chrome('E:\cfhcghcg\chromedriver.exe')
                    driver.get(url)
                    driver.minimize_window()

                    driver.find_element_by_id('searchInput').send_keys(ww)

                    button=driver.find_element_by_xpath('/html/body/div[2]/form/fieldset/button')

                    button.click()
                    result=" "
                    for i in range(1,5):
                        z=driver.find_element_by_xpath('/html/body/div[3]/div[3]/div[4]/div/p[i]')
                        result=result+z.text
                    
                    sa=result
                    T.insert(END, sa)
                    driver.quit()
                    rootwik.mainloop()
                    
                except:
                    print("error")
                    driver.quit()
                
    def calculator():
        df=Tk()
        df.title("CALCULATOR")
        df.geometry("290x200")
        df.configure(bg="#575656")
        def fdf():
            qw=eval(ew.get())
            dd.config(text="RESULT="+str(qw))
        ew=Entry(df)
        ew.place(x=60,y=85)
        qwq=Button(df,text="CALCULATE",command=fdf)
        qwq.place(x=95,y=115)
        dd=Label(df,bg="#575656")
        dd.place(x=100,y=150)
        qww=Label(df,text="THIS A SIMPLE CALCULATOR",bg="#575656",fg="white")
        qww.place(x=50,y=10)
        qwsw=Label(df,text="PLEASE ENTER THE EXPRESSION",bg="#575656",fg="white")
        qwsw.place(x=40,y=30)
        dsf=Label(df,text="eg:((54+56)*43)/2",bg="#575656",fg="white")
        dsf.place(x=80,y=50)
        asdd=Label(df,text="simple but powerfull",bg="#575656",fg="red")
        asdd.place(x=0,y=180)
        df.mainloop()
    
    def gogoogle():
        try:
            re=str(query_pad.get())
            urlr="https://www.google.com/"
            driver=webdriver.Chrome('E:\cfhcghcg\chromedriver.exe')
            driver.get(urlr)
            search_bar=driver.find_element_by_name('q')
            search_bar.send_keys(re)
            search_bar.send_keys(Keys.RETURN)
            time.sleep(10)
            driver.quit()

        except:
            driver.quit()
            messagebox.showerror("ERROR","No Internet Connection")

    a=Label(chatbot,text=("Hi "+user),font="time 22 bold",fg="white",bg="grey",)
    a.place(x=160,y=130)

    chat_pad=Entry(chatbot,width=30,)
    chat_pad.place(x=70,y=200)


    enterbutton=Button(chatbot,text="ENTER",fg="black",bg="#575656",pady=0.8,command=chat)
    enterbutton.place(x=260,y=197)

    query=Label(chatbot,text="GOOGLE QUERY",font="times 12 bold",fg="black",bg="grey")
    query.place(x=110,y=380)

    gogquerybutton=Button(chatbot,fg="black",bg="#575656",command=gogoogle,text="GO",pady=0.7, borderwidth=3)
    gogquerybutton.place(x=270,y=405)

    query_pad=Entry(chatbot,width=30)
    query_pad.place(x=75,y=410)



    chatpad=Label(chatbot)
    chatpad.place(x=0,y=120)


    clacbutton=Button(chatbot,text="CALCULATOR",padx=2,pady=3,bg="#575656",fg="black",command=calculator)
    clacbutton.place(x=3,y=525)
    stockfame=LabelFrame(chatbot,text="Stock Market",height=200,width=200,fg="blue")
    stockfame.place(x=700,y=0)
    priceframe=LabelFrame(chatbot,text="Prices",fg="blue")
    priceframe.place(x=700,y=275)
    #the reqiured links for web scrape
    url1="https://in.finance.yahoo.com/quote/%5EBSESN?p=^BSESN"

    url2="https://in.finance.yahoo.com/quote/%5ENSEI?p=^NSEI"

    url3="https://in.finance.yahoo.com/quote/%5EGSPC?p=^GSPC&.tsrc=fin-srch"

    url4="https://in.finance.yahoo.com/quote/INR=X?p=INR=X"

    u2="https://www.goodreturns.in/diesel-price.html"

    u="https://www.goodreturns.in/petrol-price.html"

    u3="https://in.finance.yahoo.com/quote/CL=F?p=CL=F&.tsrc=fin-srch"
    #def stock gets the stock market live prices and so does def pricess
    def stock():
        try:
            r1=requests.get(url1)
            r2=requests.get(url2)
            r3=requests.get(url3)
            r4=requests.get(url4)
            soup1=BeautifulSoup(r1.content,'html5lib')
            soup2=BeautifulSoup(r2.content,'html5lib')
            soup3=BeautifulSoup(r3.content,'html5lib')
            soup4=BeautifulSoup(r4.content,'html5lib')
            a1=soup1.find_all('span')[8].text

            s1=soup1.find_all('span')[9].text

            a2=soup2.find_all('span')[8].text

            s2=soup2.find_all('span')[9].text

            a3=soup3.find_all('span')[8].text

            s3=soup3.find_all('span')[9].text

            a4=soup4.find_all('span')[6].text

            s4=soup4.find_all('span')[7].text
        except:
            eroor.config(text="No internet connection")


        q1.config(text="------BSE------")

        w1.config(text="Price="+a1)
        e1.config(text="Rate Of Change="+s1)

        q2.config(text="------NSE------")

        w2.config(text="Price="+a2)

        e2.config(text="Rate Of Change="+s2)

        q3.config(text="----S&P 500----")

        w3.config(text="Price="+a3)

        e3.config(text="Rate Of Change="+s3)

        q4.config(text="------INR------")

        w4.config(text="Price="+a4)

        e4.config(text="Rate Of Change="+s4)

    q1=Label(stockfame,fg="red")
    q1.pack()
    w1=Label(stockfame)
    w1.pack()
    e1=Label(stockfame)
    e1.pack()
    q2=Label(stockfame,fg="red")
    q2.pack()
    w2=Label(stockfame)
    w2.pack()
    e2=Label(stockfame)
    e2.pack()
    q3=Label(stockfame,fg="red")
    q3.pack()
    w3=Label(stockfame)
    w3.pack()
    e3=Label(stockfame)
    e3.pack()
    q4=Label(stockfame,fg="red")
    q4.pack()
    w4=Label(stockfame)
    w4.pack()
    e4=Label(stockfame)
    e4.pack()
    eroor=Label(stockfame,fg="red",bg="black")
    eroor.pack()
    def pricess():
        w=requests.get(u)
        ss=BeautifulSoup(w.content,'html5lib')
        w2=requests.get(u2)
        ss2=BeautifulSoup(w2.content,'html5lib')
        w3=requests.get(u3)
        ss3=BeautifulSoup(w3.content,'html5lib')

        tri_petrol=ss.find_all('td')[42].text+ss.find_all('td')[43].text

        tri_diesel=ss2.find_all('td')[42].text+ss2.find_all('td')[43].text

        crude2=ss3.find_all('span')[7].text

        crude=ss3.find_all('span')[8].text

        qwee.config(text="------PETROL------",fg="red")
        petrolP.config(text=tri_petrol)
        qwww.config(text="------DIESEL------",fg="red")
        diselP.config(text=tri_diesel)
        crudeoil.config(text="------CRUDE OIL------",fg="red")
        crude_p.config(text="Price="+crude2)

        crude_p2.config(text="Rate of Change="+crude)
    qwee=Label(priceframe)
    qwee.pack()
    petrolP=Label(priceframe)
    petrolP.pack()
    qwww=Label(priceframe)
    qwww.pack()
    diselP=Label(priceframe)
    diselP.pack()
    crudeoil=Label(priceframe)
    crudeoil.pack()
    crude_p=Label(priceframe)
    crude_p.pack()
    crude_p2=Label(priceframe)
    crude_p2.pack()

    sss=Button(chatbot,text="UPDATE",command=lambda:[pricess(),stock()])
    sss.place(x=770,y=450)

    chatbot.mainloop()

def LOGIN():

    rett=str(re.get())
    tett=str(te.get())
    if rett==user and tett==pasw:
        root.destroy()
        chatbotmainwindow()

    else:
        messagebox.showerror("ERROR!","Wrong Username or Password")

def signup():
    signuptk=Tk()
    signuptk.geometry("300x250")
    signuptk.resizable(0,0)
    signuptk.title("SIGNUP")
    sign=Label(signuptk,text="SIGNUP",font="time 18 bold",fg="white",bg="#575656")
    sign.place(x=100,y=0)
    def singupp():
        #usr_entr_val=str(usr_entr.get())
        #pas_entr_val=str(pas_entr.get())
        pass
    usr=Label(signuptk,text="USERNAME:",fg="white",bg="black")
    usr.place(x=0,y=50)

    pas=Label(signuptk,text="PASSWORD:",fg="white",bg="black")
    pas.place(x=0,y=75)

    usr_entr=Entry(signuptk)
    usr_entr.place(x=90,y=50)

    pas_entr=Entry(signuptk)
    pas_entr.place(x=90,y=75)

    entrsgnup=Button(signuptk,text="SIGNUP",bg="black",fg="white",command=singupp,relief=GROOVE,border=3.5)
    entrsgnup.place(x=120,y=190)

    placelabel=Label(signuptk,text="PLACE:",fg="white",bg="black")
    placelabel.place(x=0,y=100)

    statelabel=Label(signuptk,text="STATE:",fg="white",bg="black")
    statelabel.place(x=0,y=125)

    gmaillabel=Label(signuptk,text="GMAIL:",fg="white",bg="black")
    gmaillabel.place(x=0,y=150)

    place_etr=Entry(signuptk)
    place_etr.place(x=90,y=100)

    state_etr=Entry(signuptk)
    state_etr.place(x=90,y=125)

    mail_etr=Entry(signuptk)
    mail_etr.place(x=90,y=150)


    signuptk.mainloop()

def maingraphics():

    q=Label(root,text="LOGIN",font="time 22 ",bg="grey",fg="white",)
    q.pack()
    q.place(x=150,y=130)

    w=Label(root,text="USERNAME:",font="time 12 ",bg="grey",fg="white")
    w.place(x=0,y=170)

    e=Label(root,text="PASSWORD:",font="time 12 ",bg="grey",fg="white")
    e.place(x=0,y=194)


    y=Button(root,text="LOGIN",padx=2,pady=2,command=LOGIN,bg="#575656",fg="black",border=3.5)
    y.place(x=170,y=230)

    u=Label(root,text="JARVIS V-2.3.4",font="time 32 bold",fg="#FFFFFF",bg="#507075",relief="groove",border=3.5)
    u.place(x=40,y=0)

    i=Button(root,text="SIGNUP",padx=2,pady=2,command=signup,bg="#575656",fg="black",borderwidth=3.5)
    i.place(x=166,y=280)

    o=Label(root,text="If No Account,SIGNUP!",font="time 8 ",fg="white",bg="grey")
    o.place(x=134,y=258)

maingraphics()
#the both entrys stay out of the function as the .get() function does not work inside function
re=Entry(root)
re.place(x=120,y=170)


te=Entry(root,show="@")
te.place(x=120,y=194)




root.mainloop()
