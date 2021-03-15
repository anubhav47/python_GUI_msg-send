# -*- coding: utf-8 -*-
"""
Created on Sun Feb 21 14:21:49 2021

@author: INDIAN
"""

import requests
import json
from tkinter import *
from tkinter.messagebox import showinfo,showerror
 

def send_msg(number,message):
    url="https://www.fast2sms.com/dev/bulk"
    parameter={
        
        'authorization':'HjakxI36fqW9GO1pPmilFzVYS7DEeM24tbLJQw0CrsXnyBhKogb1T7kRXPcIWCd5Vh9N83UlrjuOnQJo',
        'sender_id':'FSTSMS',
        'message':message,
        'language':'english',
        'route':"p",
        'numbers':number
    
        
        }#dictionary
    response= requests.get(url,parameter)
    dic=response.json()
    print(dic)
    return dic.get('return')
def btn_click():
    num=textnumber.get()
    msg=textmsg.get("1.0",END)
    r=send_msg(num, msg)
    if r==True:
        showinfo("send succesfully","succesfully send")
    else:
        showerror("cannot send","something went wrong")
    #creating GUI
root=Tk()
root.title("send a message")
root.geometry("400x550")
font=("neuzeit",22,"bold")
textnumber=Entry(root,font=font)
textnumber.pack(fill=X,pady=30)

textmsg=Text(root) 
textmsg.pack(fill=X)#means full width
sendbtn=Button(root,text="send sms",command=btn_click)
sendbtn.pack()
root.mainloop()   
    

   