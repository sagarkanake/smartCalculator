from datetime import *
responses=["Welcome to smart calculator ","My name is Munna ","Thanks",
           "Sorry, this is beyond my ability"]

class User:
    def __init__(self,uid,name,age=0):
        self.id=uid;
        self.name=name;
        self.age=0;
        
def extract_numbers_from_text(text):
    l=[];
    for t in text.split(' '):
        try:
            l.append(float(t));
        except ValueError:
            pass;
    return(l)


def extract_operator(word):
    l=list(word)
    for op in l:
        if op == "+":
            return op
        
        if op == "-":
            return op
        
        if op == "*":
            return op
        
        if op == "/":
            return op
        if op == ",":
            return op


def lcm(a,b):
    L=a if a>b else b
    while L<=a*b:
        if L%a==0 and L%b==0:
            return L;
        L+=1;
        
def hcf(a,b):
    H=a if a<b else b
    while H>=1:
        if a%H==0 and b%H==0:
            return H;
        H-=1
        
def add(a,b):
    return a+b;
def sub(a,b):
    return a-b;
def multiply(a,b):
    return a*b;
def division(a,b):
    return a/b;
def end():
    print(responses[2])
    input("Press any key to exit ")
    exit()
def myname():
    import random
    print(responses[1])
    name=input("And Yours : ")
    v=validateUser(name)
    if v == 0:
        print("")
        uid=random.randint(0,22)
        u=User(uid,name)
        saveUser(u)
        s=viewUser()
        for e in s:
          print("Your Name is : ",e.name,"\nAnd Your id is : ",e.id)
    else:
        print("Hello Welcome Back Sir");
       
    #uid=random.randint(0,22)
    #u=User(uid,name)
    #saveUser(u)
    #s=viewUser()
    #for e in s:
       #print("Your Name is : ",e.name," And Your id is : ",e.id)
       
def validateUser(name):
    import pickle
    try:
     f=open('UserData.obj','rb')
     l=[]
     l+=[pickle.load(f)]
     for data in l:
        if data.name==name:
           return name;
        else:
            return 0
    except:
       return 0

    f.close()
def saveUser(u):
    import pickle
    try:
     f=open('UserData.obj','wb')
     pickle.dump(u,f)
    except:
        return
    f.close()
def viewUser():
    import pickle;
    f=open('UserData.obj','rb')
    s=[]
    s+=[pickle.load(f)]
    f.close()
    return s
def find():
    name=input("Tell me your name :")
    r=uid(name)
    if r==0:
        print("You Don't Have id ")
    else:
        print("your id is ",r)
def uid(name):
    import pickle
    try:
      f=open('UserData.obj','rb')
      l=[]
      l+=[pickle.load(f)]
      for data in l:
        if data.name==name:
           return(data.id);      
    except EOFError:
        return 0
 
    finally:  
      f.close()
def nav():
    print("Bhava maza nav MUNNA ahe \nAni mi Smart Calculator ahe ")
    
def sorry():
    print(responses[3]);
def do():
    print("I am Just Helping you Sir ")
def age():
    print("I am 20 years old ")
def pm():
    print("Indias Prime Minister is Narendra Modi")
def time():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print("Current Time : ",current_time)
def date():
    from datetime import date
    today = date.today()
    d3 = today.strftime("%b %d,%Y")
    print("Today's date is : ",d3)
    
operations={"PLUS":add,"+":add,"-":sub,"*":multiply,"/":division,"ADD":add,"ADDITION":add,"SUM":add,"SUMATION":add,"SUB":sub,"SUBTRACTION":sub,"DIFFERENCE":sub,"SUBTRACT":sub,"MUL":multiply,"MULT":multiply,"MULTIPLICATION":multiply,"INTO":multiply,"PRODUCT":multiply,"MULTIPLY":multiply,
            "DIVISION":division,"DIVIDE":division,"LCM":lcm,"HCF":hcf}
commands={"ID":find,"NAME":myname,"NAV":nav,"NAM":myname,"END":end,"EXIT":end,"CLOSE":end,"DOING":do,"UMRA":age,"AGE":age,"PRIME":pm,"PM":pm,"PRIME-MINSTER":pm,"TIME":time,"DATE":date}


    
    
    
