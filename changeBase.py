#!/usr/bin/env python
# coding: utf-8

# In[32]:


#گرفتن مقادیر ورودی
number=input("Pleace enter a number: ")
#در نظر گرفتن وارد کردن حروف انگلیسی در مقادیر هگزادسیمال
status=1
for w in number:
    if(w=="A" or w=="B" or w=="C" or w=="D" or w=="E" or w=="F"):
        status=0
if(status==1):
    number=int(number)
base=int(input("Enter input base: "))#گرفتن مبنای اولیه
baseTo=int(input("Enter output base: "))#گرفتن مبنای مقصد
#تعریف تابع تبدیل مبنا
def changeBase(num, base, baseTo):
#در صورتی که کاربر به اشتباه مبنای مبدا و مقصد را یکی وارد کند اخطار بده
    if(base==baseTo):
        return -1
    else:
        if(base==2):
#تبدیل مبنای 2 به 10
            if(baseTo==10):
                i=-1
                x=1
                sum=0
                num1=str(num)
                t=len(num1)
                t=-t
                while(i>=t):
                    y=int(num1[i])
                    sum+=y*x
                    x*=2
                    i-=1
                return sum
#تبدیل مبنای 2 به 16
            elif(baseTo==16):
                myList=[]
                i=-1
                x=1
                sum=0
                num1=str(num)
                t=len(num1)
                t=-t
                while(i>=t):
                    y=int(num1[i])
                    sum+=y*x
                    if(-(i)%4==0):
                        if(sum>=10):
                            if(sum==10):
                                sum="A"
                            if(sum==11):
                                sum="B"
                            if(sum==12):
                                sum="C"
                            if(sum==13):
                                sum="D"
                            if(sum==14):
                                sum="E"
                            if(sum==15):
                                sum="F"
                        myList.append(sum)
                        sum=0
                        x=1
                    else:
                        x*=2
                    i-=1
                myList2=[]
                f=len(myList)-1
                while(f>=0):
                    myList2.append(myList[f])
                    f-=1
                s=""
                for r in myList2:
                    s+=str(r)
                return s
#درصورتی که مبنای مقصد 2 یا 10 یا 16 نباشد اخطار بدهد
            else:
                return -1
        elif(base==10):
#تبدیل مبنای 10 به 2
            if(baseTo==2):
                myList=[]
                x=1
                y=0
                while(x<=num):
                    x*=2
                    y+=1
                x/=2
                while(y>0):
                    if(num<x):
                        myList.append(0)
                        x/=2
                    else:
                        myList.append(int(num/x))
                        num-=x
                        x/=2
                    y-=1
                myList2=[]
                f=len(myList)-1
                while(f>=0):
                    myList2.append(myList[f])
                    f-=1
                s=""
                for r in myList2:
                    s+=str(r)
                return s
#تبدیل مبنای 10 به 16
            elif(baseTo==16):
                myList=[]
                k=0
                x=1
                y=0
                while(x<=num):
                    x*=16
                    y+=1
                x/=16
                while(y>0):
                    k=int(num/x)
                    if(k==10):
                        k="A"
                    elif(k==11):
                        k="B"
                    elif(k==12):
                        k="C"
                    elif(k==13):
                        k="D"
                    elif(k==14):
                        k="E"
                    elif(k==15):
                        k="F"
                    myList.append(k)
                    if(num%x!=0):
                        num%=x
                        x/=16
                    y-=1
                s=""
                for r in myList:
                    s+=str(r)
                return s
#درصورتی که مبنای مقصد 2 یا 10 یا 16 نباشد اخطار بدهد
            else:
                return -1
        elif(base==16):
#تبدیل مبنای 16 به 2
            if(baseTo==2):
                myList=[]
                x=""
                i=-1
                num1=str(num)
                t=len(num1)
                t=-t
                while(i>=t):
                    if(num1[i]==0):
                        x="0000"
                    elif(num1[i]=="1"):
                        x="0001"
                    elif(num1[i]=="2"):
                        x="0010"
                    elif(num1[i]=="3"):
                        x="0011"
                    elif(num1[i]=="4"):
                        x="0100"
                    elif(num1[i]=="5"):
                        x="0101"
                    elif(num1[i]=="6"):
                        x="0110"
                    elif(num1[i]=="7"):
                        x="0111"
                    elif(num1[i]=="8"):
                        x="1000"
                    elif(num1[i]=="9"):
                        x="1001"
                    elif(num1[i]=="A"):
                        x="1010"
                    elif(num1[i]=="B"):
                        x="1011"
                    elif(num1[i]=="C"):
                        x="1100"
                    elif(num1[i]=="D"):
                        x="1101"
                    elif(num1[i]=="E"):
                        x="1110"
                    elif(num1[i]=="F"):
                        x="1111"
                    myList.append(x)
                    i-=1
                myList2=[]
                f=len(myList)-1
                while(f>=0):
                    myList2.append(myList[f])
                    f-=1
                s=""
                for r in myList2:
                    s+=str(r)
                return s
#تبدیل مبنای 16 به 10
            elif(baseTo==10):
                i=-1
                x=1
                sum=0
                num=str(num)
                t=len(num)
                t=-t
                while(i>=t):
                    if(num[i]=="A"):
                        sum+=10*x
                    elif(num[i]=="B"):
                        sum+=11*x
                    elif(num[i]=="C"):
                        sum+=12*x
                    elif(num[i]=="D"):
                        sum+=13*x
                    elif(num[i]=="E"):
                        sum+=14*x
                    elif(num[i]=="F"):
                        sum+=15*x
                    else:
                        sum+=int(num[i])*x
                    x*=16
                    i-=1
                return sum
#درصورتی که مبنای مقصد 2 یا 10 یا 16 نباشد اخطار بدهد
            else:
                return -1
#در صورتی که مبنای مبدا 2 یا 10 ویا 16 نباشد اخطار بدهد
        else:
            return -1
#صدا زدن تابع تبدیل مبنا
amir=changeBase(number, base, baseTo)
#نمایش پیغام مناسب در صورت بروز اخطار و نمایش جواب نهایی در صورت عملکرد درست
if(amir!=-1):
    print("The final answer: ", amir)
else:
    print("Please enter a true number for the base ...")
input()
#امیر مهدی محمدی نژاد  مباحث ویژه


# In[ ]:




