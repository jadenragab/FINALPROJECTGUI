# -*- coding: utf-8 -*-
"""
Created on Sun Oct 16 14:53:03 2022

@author: jaden
"""
#%%
#Import Tkinter
from tkinter import *
from tkinter import ttk
import tkinter as tk

#Import Image
from PIL import Image, ImageTk

#Import Yahoo Finance
import yfinance as yf
#%%
#Create an instance of tkinter frame or window
win= Tk()

#Set the geometry of tkinter frame
win.geometry("1080x720")
#%%
# Variable Placeholder
var = StringVar()
var.set('No Value')
#%%
#Background Image and Path
image1 = Image.open(r"C:\Users\jaden\Downloads\photo.jpg")
background = ImageTk.PhotoImage(image1)
label1 = tk.Label(image=background)
label1.image = background

#Image Position
label1.place(x=0, y=0)
#%%
#Corner Image and Path
image2 = Image.open(r"C:\Users\jaden\Downloads\download.jpg")
cornerimage = ImageTk.PhotoImage(image2)
label2 = tk.Label(image=cornerimage)
label2.image = cornerimage

# Position image
label2.place(x=0, y=0)
#%%
#Header Label
Label(win, text= "Support and Resistance", font= ('Helvetica 17 bold')).pack(pady=30)
entry1 = Entry(win)
entry1.pack()

#Support and Resistance Function
def getRS():  
    #Collect User Input
    ticker= entry1.get()
    
    #Variables
    timeperiod= "40d"
    timeinterval= "15m"
    taps= 4
    
    #Dataframe Data
    data = yf.download(tickers = ticker, period = timeperiod, interval = timeinterval)
    
    #Searching for multiple retests within the dataset
    taps=int(taps)
    data=data.round(2)
    data=data[["High","Low"]]
    high = data['High'].values.tolist()
    low = data['Low'].values.tolist()
    numbers = high + low
    duplicates = [number for number in numbers if numbers.count(number) > taps]
    unique_duplicates = list(set(duplicates))
    unique_duplicates.sort()
    label1 = Label(win, text= str(unique_duplicates))
    
    #If list has values, change var variable to dupliactes
    if len(unique_duplicates) > 1:
        var.set(unique_duplicates)
        
    #If list has no values, change var variable to text
    else:
        var.set("No levels found!")
     
#Button to run getRS function      
ttk.Button(text="Find Support and Resistance", command=getRS).pack()
#%%
#New Window Function
def ticker():
   new= Toplevel(win)
   
   #New Window Size
   new.geometry("750x250")
   
   #New Window Header
   new.title("Tickers")
   
   #New Window Text
   Label(new, text="AAPL" + "\n" + "SPY"+ "\n" + "NVDA" + "\n" + "TSLA"+ "\n" + "AMD" + "\n" + "ETC...", font=('Helvetica 12')).pack(pady=30)

   #Close Function
   def Close():
       new.destroy()   
      
   # Button for closing
   exit_button = Button(new, text="back", command=Close)
   exit_button.pack(pady=20)
   
#Button to run ticker function   
ttk.Button(win, text="Tickers", command=ticker).pack()
#%%
#New Window Function
def information():
   new= Toplevel(win)
   
   #New Window Size
   new.geometry("750x250")
   
   #New Window Text
   new.title("Information")
   
   ##New Window Text
   Label(new, text="This program helps you find support and resistance levels" + "\n" +"on 40d range with 15m candles", font=('Helvetica 15')).pack(pady=30)
  
   #Close Function
   def Close():
       new.destroy()   
      
   # Button for closing
   exit_button = Button(new, text="back", command=Close)
   exit_button.pack(pady=20)
   
#Button to run information function   
ttk.Button(win, text="Info", command=information).pack()
#%%
#Output Box
label1=Label(win,pady=10,font=("arial",15))
label1.pack()

label1.config(textvariable= var)

win.mainloop()