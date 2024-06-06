import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.image import Image
from kivy.uix.floatlayout import FloatLayout
import math

countopp=0
decimal=0
click =0

#Builder function to use the file
Builder.load_file("Calculator.kv")

Window.size = (300,500)
todo = 0

#Operation perform as per todo button
def nothing(self):
    global countopp
    global num1
    global num2
    global ans
    global decimal
    global todo
    global click
    if decimal==0:
        num1 = int(self.ids.calc_input.text)
    elif decimal==1:
        num1 = float(self.ids.calc_input.text)
    if click==1:
        self.ids.sign.text = str(num1)+"+"
    elif click==2:
        self.ids.sign.text = str(num1)+"-"
    elif click==3:
        self.ids.sign.text = str(num1)+"X"
    elif click==4:
        self.ids.sign.text = str(num1)+"÷"
    self.ids.calc_input.text ="0"

def add(self):
    global countopp
    global num1
    global num2
    global ans
    global decimal
    global todo
    if decimal==0:
        if countopp == 0:
            num1 = int(self.ids.calc_input.text)
        else:
            num2 = int(self.ids.calc_input.text)
            ans = num1+num2
            num1 = ans
    elif decimal==1:
        if countopp == 0:
            num1 = float(self.ids.calc_input.text)
        else:
            num2 = float(self.ids.calc_input.text)
            ans = num1+num2
            num1 = ans
def minus(self):
    global countopp
    global num1
    global num2
    global ans
    global decimal
    global todo
    if decimal ==0:
        if countopp == 0:
            num1 = int(self.ids.calc_input.text)
        else:
            num2 = int(self.ids.calc_input.text)
            ans = num1-num2
            num1 = ans
    elif decimal ==1:
        if countopp == 0:
            num1 = float(self.ids.calc_input.text)
        else:
            num2 = float(self.ids.calc_input.text)
            ans = num1-num2
            num1 = ans
def multiply(self):
    global countopp
    global num1
    global num2
    global ans
    global decimal
    global todo
    if decimal ==0:
        if countopp == 0:
            num1 = int(self.ids.calc_input.text)
        else:
            num2 = int(self.ids.calc_input.text)
            ans = num1*num2
            num1 = ans
    elif decimal ==1:
        if countopp == 0:
            num1 = float(self.ids.calc_input.text)
        else:
            num2 = float(self.ids.calc_input.text)
            ans = num1*num2
            num1 = ans
def divide(self):
    global countopp
    global num1
    global num2
    global ans
    global decimal
    global todo
    if decimal ==0:
        if countopp == 0:
            num1 = int(self.ids.calc_input.text)
            self.ids.calc_input.text ="0"
        else:
            num2 = int(self.ids.calc_input.text)
            if num2 !=0:
                ans = num1/num2
                num1 = ans
                self.ids.calc_input.text ="0"
            else:
                self.ids.calc_input.text ="Undefined"
    elif decimal ==1:
        if countopp == 0:
            num1 = float(self.ids.calc_input.text)
            self.ids.calc_input.text ="0"
        else:
            num2 = float(self.ids.calc_input.text)
            if num2 !=0:
                ans = num1/num2
                num1 = ans
                self.ids.calc_input.text ="0"
            else:
                self.ids.calc_input.text ="Undefined"

def inverse(self):
    global countopp
    global num1
    global num2
    global ans
    global decimal
    global todo
    global click
    if click==1:
        self.ids.sign.text = str(num1)+"+"
    elif click==2:
        self.ids.sign.text = str(num1)+"-"
    elif click==3:
        self.ids.sign.text = str(num1)+"X"
    elif click==4:
        self.ids.sign.text = str(num1)+"÷"
    self.ids.calc_input.text ="0"

def square(self):
    global countopp
    global num1
    global num2
    global ans
    global decimal
    global todo
    global click
    if click==1:
        self.ids.sign.text = str(num1)+"+"
    elif click==2:
        self.ids.sign.text = str(num1)+"-"
    elif click==3:
        self.ids.sign.text = str(num1)+"X"
    elif click==4:
        self.ids.sign.text = str(num1)+"÷"
    self.ids.calc_input.text ="0"

def root(self):
    global countopp
    global num1
    global num2
    global ans
    global decimal
    global todo
    global click
    if click==1:
        self.ids.sign.text = str(num1)+"+"
    elif click==2:
        self.ids.sign.text = str(num1)+"-"
    elif click==3:
        self.ids.sign.text = str(num1)+"X"
    elif click==4:
        self.ids.sign.text = str(num1)+"÷"
    self.ids.calc_input.text ="0"

def signchange(self):
    global countopp
    global num1
    global num2
    global ans
    global decimal
    global todo
    global click
    if click==1:
        self.ids.sign.text = str(num1)+"+"
    elif click==2:
        self.ids.sign.text = str(num1)+"-"
    elif click==3:
        self.ids.sign.text = str(num1)+"X"
    elif click==4:
        self.ids.sign.text = str(num1)+"÷"
    self.ids.calc_input.text ="0"

class Myload(Widget):
    #Number Buttons
    def press0(self):
        global decimal
        number = self.ids.calc_input.text
        if decimal ==0:
            number = int(number)
            self.ids.calc_input.text=str(number*10)
        elif decimal ==1:
            self.ids.calc_input.text=str(number)+"0"
    def press1(self):
        global decimal
        number = self.ids.calc_input.text
        if decimal==0:
            number = int(number)
            self.ids.calc_input.text= str(number*10+1)
        elif decimal ==1:
            self.ids.calc_input.text=str(number)+"1"
    def press2(self):
        global decimal
        number = self.ids.calc_input.text
        if decimal==0:
            number = int(number)
            self.ids.calc_input.text= str(number*10+2)
        elif decimal ==1:
            self.ids.calc_input.text=str(number)+"2"
    def press3(self):
        global decimal
        number = self.ids.calc_input.text
        if decimal ==0:
            number = int(number)
            self.ids.calc_input.text= str(number*10+3)
        elif decimal ==1:
            self.ids.calc_input.text=str(number)+"3"
    def press4(self):
        global decimal
        number = self.ids.calc_input.text
        if decimal ==0:
            number = int(number)
            self.ids.calc_input.text= str(number*10+4)
        elif decimal ==1:
            self.ids.calc_input.text=str(number)+"4"
    def press5(self):
        global decimal
        number = self.ids.calc_input.text
        if decimal ==0:
            number = int(number)
            self.ids.calc_input.text= str(number*10+5)
        elif decimal ==1:
            self.ids.calc_input.text=str(number)+"5"
    def press6(self):
        global decimal
        number = self.ids.calc_input.text
        if decimal ==0:
            number = int(number)
            self.ids.calc_input.text= str(number*10+6)
        elif decimal ==1:
            self.ids.calc_input.text=str(number)+"6"
    def press7(self):
        global decimal
        number = self.ids.calc_input.text
        if decimal ==0:
            number = int(number)
            self.ids.calc_input.text= str(number*10+7)
        elif decimal ==1:
            self.ids.calc_input.text=str(number)+"7"
    def press8(self):
        global decimal
        number = self.ids.calc_input.text
        if decimal ==0:
            number = int(number)
            self.ids.calc_input.text= str(number*10+8)
        elif decimal ==1:
            self.ids.calc_input.text=str(number)+"8"
    def press9(self):
        global decimal
        number = self.ids.calc_input.text
        if decimal ==0:
            number = int(number)
            self.ids.calc_input.text= str(number*10+9)
        elif decimal ==1:
            self.ids.calc_input.text=str(number)+"9"
    
    #Operation Buttons
    def pressdivide(self):
        global countopp
        global num1
        global num2
        global ans
        global decimal
        global todo
        global click
        click=4
        if todo ==0:
            nothing(self)
        elif todo==1:
            add(self)
        elif todo ==2:
            minus(self)
        elif todo ==3:
            multiply(self)
        elif todo==4:
            divide(self)
        elif todo==6:
            inverse(self)
        elif todo==7:
            square(self)
        elif todo==8:
            root(self)
        elif todo==9:
            signchange(self)
        todo = 4
        self.ids.calc_input.text ="0"
        if countopp!=0:
            self.ids.sign.text=self.ids.sign.text +str(num2)+ "÷"
        decimal =0
        countopp+=1
    def pressX(self):
        global countopp
        global num1
        global num2
        global ans
        global decimal
        global todo
        global click
        click=3
        if todo ==0:
            nothing(self)
        elif todo==1:
            add(self)
        elif todo ==2:
            minus(self)
        elif todo ==3:
            multiply(self)
        elif todo==4:
            divide(self)
        elif todo==6:
            inverse(self)
        elif todo==7:
            square(self)
        elif todo==8:
            root(self)
        elif todo==9:
            signchange(self)
        todo = 3
        self.ids.calc_input.text ="0"
        if countopp!=0:
            self.ids.sign.text=self.ids.sign.text +str(num2)+ "X"
        decimal = 0
        countopp+=1
    def pressminus(self):
        global countopp
        global num1
        global num2
        global ans
        global decimal
        global todo
        global click
        click=2
        if todo ==0:
            nothing(self)
        elif todo==1:
            add(self)
        elif todo ==2:
            minus(self)
        elif todo ==3:
            multiply(self)
        elif todo==4:
            divide(self)
        elif todo==6:
            inverse(self)
        elif todo==7:
            square(self)
        elif todo==8:
            root(self)
        elif todo==9:
            signchange(self)
        todo = 2
        self.ids.calc_input.text ="0"
        if countopp!=0:
            self.ids.sign.text=self.ids.sign.text +str(num2)+ "-"
        countopp+=1
        decimal =0
    def pressadd(self):
        global countopp
        global num1
        global num2
        global ans
        global decimal
        global todo
        global click
        click=1
        if todo ==0:
            nothing(self)
        elif todo==1:
            add(self)
        elif todo ==2:
            minus(self)
        elif todo ==3:
            multiply(self)
        elif todo==4:
            divide(self)
        elif todo==6:
            inverse(self)
        elif todo==7:
            square(self)
        elif todo==8:
            root(self)
        elif todo==9:
            signchange(self)
        self.ids.calc_input.text ="0"
        if countopp!=0:
            self.ids.sign.text=self.ids.sign.text +str(num2)+ "+"
        todo = 1
        countopp+=1
        decimal = 0
    def pressequal(self):
        global countopp
        global num1
        global num2
        global ans
        global decimal
        global todo
        self.ids.sign.text="Ans"
        if decimal ==0:
            if todo==1:
                num2 = int(self.ids.calc_input.text)
                ans = num1+num2
            elif todo==2:
                num2 = int(self.ids.calc_input.text)
                ans = num1-num2
            elif todo==3:
                num2 = int(self.ids.calc_input.text)
                ans = num1*num2
            elif todo==4:
                num2 = int(self.ids.calc_input.text)
                ans = num1/num2
            elif todo==5:
                num2  =int(self.ids.calc_input.text)
                ans = num1*num2
            ans = str(ans)
            if "." in ans:
                ans  =round(float(ans),4)
            self.ids.calc_input.text = str(ans)
        elif decimal ==1:
            if todo==1:
                num2 = float(self.ids.calc_input.text)
                ans = num1+num2
            elif todo==2:
                num2 = float(self.ids.calc_input.text)
                ans = num1-num2
            elif todo==3:
                num2 = float(self.ids.calc_input.text)
                ans = num1*num2
            elif todo==4:
                num2 = float(self.ids.calc_input.text)
                ans = num1/num2
            elif todo==5:
                num2  =float(self.ids.calc_input.text)
                ans = num1*num2
            ans = str(ans)
            if "." in ans:
                ans  =round(float(ans),4)
            self.ids.calc_input.text =str(ans)
    
    #Special Functions
    def presspercent(self):
        global countopp
        global num1
        global num2
        global ans
        global decimal
        global todo
        self.ids.sign.text="%"
        todo = 5
        if decimal==0:
            if countopp == 0:
                num1 = int(self.ids.calc_input.text)/100
            else:
                num2 = int(self.ids.calc_input.text)
                ans = num2 *num1
                num1 = ans
        elif decimal==1:
            if countopp == 0:
                num1 = float(self.ids.calc_input.text)/100
            else:
                num2 = float(self.ids.calc_input.text)
                ans = num1*num2
                num1 = ans
        self.ids.calc_input.text ="0"
        countopp+=1
        decimal = 0
    def press1byx(self):
        global countopp
        global num1
        global num2
        global ans
        global decimal
        global todo
        todo =6
        if decimal==0:
            num1 = int(self.ids.calc_input.text)
            ans = 1/num1
        elif decimal==1:
            num1 = float(self.ids.calc_input.text)
            ans = 1/num1
        ans = str(ans)
        if "." in ans:
            ans = round(float(ans),4)
            num1 =float(ans)
        else:
            num1 = int(ans)
        self.ids.calc_input.text = str(ans)

    def presssquare(self):
        global countopp
        global num1
        global num2
        global ans
        global decimal
        global todo
        todo =7
        if decimal==0:
            num1 = int(self.ids.calc_input.text)
            ans = num1*num1
        elif decimal==1:
            num1 = float(self.ids.calc_input.text)
            ans = num1*num1
        ans = str(ans)
        if "." in ans:
            ans = round(float(ans),4)
            num1=float(ans)
        else:
            num1 = int(ans)
        self.ids.calc_input.text = str(ans)

    def pressrootx(self):
        global countopp
        global num1
        global num2
        global ans
        global decimal
        global todo
        todo =8
        if decimal==0:
            num1 = int(self.ids.calc_input.text)
            ans = math.sqrt(num1)
        elif decimal==1:
            num1 = float(self.ids.calc_input.text)
            ans = math.sqrt(num1)
        ans = str(ans)
        if "." in ans:
            ans = round(float(ans),4)
            num1 =float(ans)
        else:
            num1 = int(ans)
        self.ids.calc_input.text = str(ans)
    
    def presssignchange(self):
        global countopp
        global num1
        global num2
        global ans
        global decimal
        global todo
        todo =9
        if decimal==0:
            num1 = int(self.ids.calc_input.text)
            ans = num1*(-1)
        elif decimal==1:
            num1 = float(self.ids.calc_input.text)
            ans = num1*(-1)
        ans = str(ans)
        if "." in ans:
            ans = round(float(ans),4)
            num1 =float(ans)
        else:
            num1 = int(ans)
        self.ids.calc_input.text = str(ans)

    #dot Opertion
    def pressdot(self):
        global decimal
        number = self.ids.calc_input.text
        number = int(number)
        self.ids.calc_input.text= str(number)+"."
        decimal = 1

    #Clear Operation
    def pressCE(self):
        global countopp
        global num1
        global num2
        global ans
        global decimal
        global todo
        countopp = 0
        num1 =0 
        num2 = 0
        ans = 0
        decimal =0
        todo = 0
        self.ids.calc_input.text = "0"
        self.ids.sign.text = ""
    def pressC(self):
        global countopp
        global num1
        global num2
        global ans
        global decimal
        global todo
        self.ids.calc_input.text = "0"
     
    #Backspace Operation
    def pressback(self):
        global countopp
        global num1
        global num2
        global ans
        global decimal
        global todo
        number = self.ids.calc_input.text
        number = number[:-1]
        self.ids.calc_input.text = str(number)

#Main window loop
class CalculatorApp(App):
    def build(self):
    
        return Myload()

if __name__=="__main__":
    CalculatorApp().run()