from tkinter import *
import math
import re

class Main:
    def __init__(self,frame):
        self.frame = frame
        self.lblue = "#c8bfe7"
        self.dgrey = "#7d7d7d"
        self.equation = ""
        self.equa = ""
        Label(self.frame,width=27,font=("Calibri", 24),anchor="e",bg="white",fg=self.dgrey).grid(row=0,columnspan=4)
        Label(self.frame,width=27,font=("Calibri", 24),anchor="e",bg="white",fg=self.dgrey).grid(row=2,columnspan=4)
        vcmd = (self.frame.register(self.validate),'%d','%P')
        self.entry = Entry(self.frame,width=19,font=("Calibri",34),justify=RIGHT,borderwidth=0,validate = "key", validatecommand = vcmd)
        self.entry.insert(0,"0")
        self.entry.grid(row=1,columnspan=4)
        self.Value = self.entry.get()
        
        self.button = Button(self.frame, text="AC",height=2,width=9,bg="#00e000",font=("Calibri",16))
        self.button.bind("<Button-1>",self.Clear)
        self.button.grid(row=4,column=0)
        self.button = Button(self.frame, text="⌫",height=2,width=9,fg="white",bg=self.dgrey,font=("Calibri",16))
        self.button.bind("<Button-1>",self.delete)
        self.button.grid(row=4,column=1)
        self.button = Button(self.frame, text="÷",height=2,width=9,fg="white",bg=self.dgrey,font=("Calibri",16))
        self.button.bind("<Button-1>",self.div)
        self.button.grid(row=4,column=2)
        self.button = Button(self.frame, text="x",height=2,width=9,fg="white",bg=self.dgrey,font=("Calibri",16))
        self.button.bind("<Button-1>",self.mul)
        self.button.grid(row=4,column=3)
        self.button = Button(self.frame, text="-",height=2,width=9,fg="white",bg=self.dgrey,font=("Calibri",16))
        self.button.bind("<Button-1>",self.sub)
        self.button.grid(row=5,column=3)
        self.button = Button(self.frame, text="+",height=2,width=9,fg="white",bg=self.dgrey,font=("Calibri",16))
        self.button.bind("<Button-1>",self.add)
        self.button.grid(row=6,column=3)
        self.button = Button(self.frame, text="=",height=5,width=9,bg="red",fg="white",font=("Calibri",16))
        self.button.bind("<Button-1>",self.calculate)
        self.button.grid(row=7,column=3,rowspan=2)
        self.button = Button(self.frame, text="+/-",height=2,width=9,bg=self.lblue,font=("Calibri",16))
        self.button.bind("<Button-1>",self.sign)
        self.button.grid(row=8,column=0)
        self.button = Button(self.frame, text=".",height=2,width=9,bg=self.lblue,font=("Calibri",16))
        self.button.bind("<Button-1>",self.dot)
        self.button.grid(row=8,column=2)
        self.button = Button(self.frame, text="(",height=2,width=9,fg="white",bg=self.dgrey,font=("Calibri",16))
        self.button.bind("<Button-1>",self.brac1)
        self.button.grid(row=3,column=0)
        self.button = Button(self.frame, text="√",height=2,width=9,fg="white",bg=self.dgrey,font=("Calibri",16))
        self.button.bind("<Button-1>",self.rot)
        self.button.grid(row=3,column=3)
        self.button = Button(self.frame, text="x²",height=2,width=9,fg="white",bg=self.dgrey,font=("Calibri",16))
        self.button.bind("<Button-1>",self.sqr)
        self.button.grid(row=3,column=2)
        self.button = Button(self.frame, text=")",height=2,width=9,fg="white",bg=self.dgrey,font=("Calibri",16))
        self.button.bind("<Button-1>",self.brac2)
        self.button.grid(row=3,column=1)
        self.button = Button(self.frame, text="0",height=2,width=9,bg=self.lblue,font=("Calibri",16))
        self.button.bind("<Button-1>",self.Num0)
        self.button.grid(row=8,column=1)
        self.button = Button(self.frame, text="1",height=2,width=9,bg=self.lblue,font=("Calibri",16))
        self.button.bind("<Button-1>",self.Num1)
        self.button.grid(row=7,column=0)
        self.button = Button(self.frame, text="2",height=2,width=9,bg=self.lblue,font=("Calibri",16))
        self.button.bind("<Button-1>",self.Num2)
        self.button.grid(row=7,column=1)
        self.button = Button(self.frame, text="3",height=2,width=9,bg=self.lblue,font=("Calibri",16))
        self.button.bind("<Button-1>",self.Num3)
        self.button.grid(row=7,column=2)
        self.button = Button(self.frame, text="4",height=2,width=9,bg=self.lblue,font=("Calibri",16))
        self.button.bind("<Button-1>",self.Num4)
        self.button.grid(row=6,column=0)
        self.button = Button(self.frame, text="5",height=2,width=9,bg=self.lblue,font=("Calibri",16))
        self.button.bind("<Button-1>",self.Num5)
        self.button.grid(row=6,column=1)
        self.button = Button(self.frame, text="6",height=2,width=9,bg=self.lblue,font=("Calibri",16))
        self.button.bind("<Button-1>",self.Num6)
        self.button.grid(row=6,column=2)
        self.button = Button(self.frame, text="7",height=2,width=9,bg=self.lblue,font=("Calibri",16))
        self.button.bind("<Button-1>",self.Num7)
        self.button.grid(row=5,column=0)
        self.button = Button(self.frame, text="8",height=2,width=9,bg=self.lblue,font=("Calibri",16))
        self.button.bind("<Button-1>",self.Num8)
        self.button.grid(row=5,column=1)
        self.button = Button(self.frame, text="9",height=2,width=9,bg=self.lblue,font=("Calibri",16))
        self.button.bind("<Button-1>",self.Num9)
        self.button.grid(row=5,column=2)

    def Evaluate(self):
        self.Value = self.entry.get()
        if "√" in self.Value:
            try:
                a = re.search("[0-9]+",self.Value)
                self.Value = self.Value[:a.span()[1]]+"**0.5"+self.Value[a.span()[1]:]
                self.Value = self.Value.replace("√","")
            except:
                pass
        self.Value = self.Value.replace("²","**2")
        self.equation = self.equation.replace("÷","/")
        self.equation = self.equation.replace("x","*")
        self.Value = self.Value.replace("²","**2")
        if "√" in self.equation:
            try:
                a = re.search("√[0-9]+",self.equation)
                if a:
                    self.equation = self.equation[:a.span()[1]]+"**0.5"+self.equation[a.span()[1]:]
                    self.equation = self.equation.replace("√","")
            except:
                pass

        self.eq = self.equation + self.Value
        try:
            self.ans = eval(self.eq)
            Label(self.frame,text="= "+str(self.ans),width=27,font=("Calibri", 24),anchor="e",bg="white",fg=self.dgrey).grid(row=2,columnspan=4)
        except:
            self.ans = ""

    def Clear(self, event):
        self.equation = ""
        self.equa= ""
        Label(self.frame,width=27,font=("Calibri", 24),anchor="e",bg="white",fg=self.dgrey).grid(row=0,columnspan=4)
        Label(self.frame,width=27,font=("Calibri", 24),anchor="e",bg="white",fg=self.dgrey).grid(row=2,columnspan=4)
        self.entry.delete(0, END)
        self.entry.insert(0,"0")
    def delete(self, event):
        self.Value = self.entry.get()
        self.entry.delete(len(self.Value)-1)
        self.Evaluate()
    def div(self,event):
        self.Value = self.entry.get()
        if re.search("[\+\-x÷%]$",self.Value):
            self.entry.delete(len(self.Value)-2,END)
        self.entry.insert(END," ÷")
    def mul(self,event):
        self.Value = self.entry.get()
        if re.search("[\+\-x÷%]$",self.Value):
            self.entry.delete(len(self.Value)-2,END)
        self.entry.insert(END," x")
    def add(self,event):
        self.Value = self.entry.get()
        if re.search("[\+\-x÷%]$",self.Value):
            self.entry.delete(len(self.Value)-2,END)
        self.entry.insert(END," +")
    def sub(self,event):
        self.Value = self.entry.get()
        if re.search("[\+\-x÷%]$",self.Value):
            self.entry.delete(len(self.Value)-2,END)
        self.entry.insert(END," -")
    def calculate(self,event):
        self.Evaluate()
        Label(self.frame,width=27,font=("Calibri", 24),anchor="e",bg="white",fg=self.dgrey).grid(row=0,columnspan=4)
        Label(self.frame,width=27,font=("Calibri", 24),anchor="e",bg="white",fg=self.dgrey).grid(row=2,columnspan=4)
        self.entry.delete(0,END)
        self.equation = ""
        self.equa = ""
        self.entry.insert(0,self.ans)
    def sign(self,event):
        self.Value=self.entry.get()
        if re.search("^-", self.Value):
            self.entry.delete(0,2)
        else:
            self.entry.insert(0,"- ")
        self.Evaluate()
    def dot(self,event):
        self.Value = self.entry.get()
        try:
            if re.search("[0-9]+",self.Value) and "." not in self.Value:
                self.entry.insert(END,".")
        except:
            pass
    def Num0(self,event):
        self.Value = self.entry.get()
        if re.search("[\+\-x÷]$",self.Value) and self.Value.count("(")==self.Value.count(")"):
            self.equa = self.equa + " " + self.Value
            self.equation = self.equation + self.Value
            self.entry.delete(0,END)
            Label(self.frame,text=self.equa,width=27,font=("Calibri", 24),anchor="e",bg="white",fg=self.dgrey).grid(row=0,columnspan=4)
        try:
            if int(re.search("[0-9]+",self.Value).group())!=0 or "." in self.Value:
                self.entry.insert(END,"0")
                self.Evaluate()
        except:
            self.entry.insert(END,"0")
    def Num1(self,event,p):
        self.Value = self.entry.get()
        if re.search("[\+\-x÷]$",self.Value) and self.Value.count("(")==self.Value.count(")"):
            self.equa = self.equa + " " + self.Value
            self.equation = self.equation + self.Value
            self.entry.delete(0,END)
            self.Value = self.entry.get()
            Label(self.frame,text=self.equa,width=27,font=("Calibri", 24),anchor="e",bg="white",fg=self.dgrey).grid(row=0,columnspan=4)
        try:
            if int(re.search("[0-9]+",self.Value).group())==0 and "." not in self.Value:
                self.entry.delete(len(self.Value)-1)
        except:
            pass
        self.entry.insert(END,p)
        self.Evaluate()
    def Num2(self,event):
        self.Value = self.entry.get()
        if re.search("[\+\-x÷]$",self.Value) and self.Value.count("(")==self.Value.count(")"):
            self.equa = self.equa + " " + self.Value
            Label(self.frame,text=self.equa,width=27,font=("Calibri", 24),anchor="e",bg="white",fg=self.dgrey).grid(row=0,columnspan=4)
            self.equation = self.equation + self.Value
            self.entry.delete(0,END)
            self.Value = self.entry.get()
        try:
            if int(re.search("[0-9]+",self.Value).group())==0 and "." not in self.Value:
                self.entry.delete(len(self.Value)-1)
        except:
            pass
        self.entry.insert(END,"2")
        self.Evaluate()
    def Num3(self,event):
        self.Value = self.entry.get()
        if re.search("[\+\-x÷]$",self.Value) and self.Value.count("(")==self.Value.count(")"):
            self.equa = self.equa + " " + self.Value
            Label(self.frame,text=self.equa,width=27,font=("Calibri", 24),anchor="e",bg="white",fg=self.dgrey).grid(row=0,columnspan=4)
            self.equation = self.equation + self.Value
            self.entry.delete(0,END)
            self.Value = self.entry.get()
        try:
            if int(re.search("[0-9]+",self.Value).group())==0 and "." not in self.Value:
                self.entry.delete(len(self.Value)-1)
        except:
            pass
        self.entry.insert(END,"3")
        self.Evaluate()
    def Num4(self,event):
        self.Value = self.entry.get()
        if re.search("[\+\-x÷]$",self.Value) and self.Value.count("(")==self.Value.count(")"):
            self.equa = self.equa + " " + self.Value
            Label(self.frame,text=self.equa,width=27,font=("Calibri", 24),anchor="e",bg="white",fg=self.dgrey).grid(row=0,columnspan=4)
            self.equation = self.equation + self.Value
            self.entry.delete(0,END)
            self.Value = self.entry.get()
        try:
            if int(re.search("[0-9]+",self.Value).group())==0 and "." not in self.Value:
                self.entry.delete(len(self.Value)-1)
        except:
            pass
        self.entry.insert(END,"4")
        self.Evaluate()
    def Num5(self,event):
        self.Value = self.entry.get()
        if re.search("[\+\-x÷]$",self.Value) and self.Value.count("(")==self.Value.count(")"):
            self.equa = self.equa + " " + self.Value
            Label(self.frame,text=self.equa,width=27,font=("Calibri", 24),anchor="e",bg="white",fg=self.dgrey).grid(row=0,columnspan=4)
            self.equation = self.equation + self.Value
            self.entry.delete(0,END)
            self.Value = self.entry.get()
        try:
            if int(re.search("[0-9]+",self.Value).group())==0 and "." not in self.Value:
                self.entry.delete(len(self.Value)-1)
        except:
            pass
        self.entry.insert(END,"5")
        self.Evaluate()
    def Num6(self,event):
        self.Value = self.entry.get()
        if re.search("[\+\-x÷]$",self.Value) and self.Value.count("(")==self.Value.count(")"):
            self.equa = self.equa + " " + self.Value
            Label(self.frame,text=self.equa,width=27,font=("Calibri", 24),anchor="e",bg="white",fg=self.dgrey).grid(row=0,columnspan=4)
            self.equation = self.equation + self.Value
            self.entry.delete(0,END)
            self.Value = self.entry.get()
        try:
            if int(re.search("[0-9]+",self.Value).group())==0 and "." not in self.Value:
                    self.entry.delete(len(self.Value)-1)
        except:
            pass
        self.entry.insert(END,"6")
        self.Evaluate()
    def Num7(self,event):
        self.Value = self.entry.get()
        if re.search("[\+\-x÷]$",self.Value) and self.Value.count("(")==self.Value.count(")"):
            self.equa = self.equa + " " + self.Value
            Label(self.frame,text=self.equa,width=27,font=("Calibri", 24),anchor="e",bg="white",fg=self.dgrey).grid(row=0,columnspan=4)
            self.equation = self.equation + self.Value
            self.entry.delete(0,END)
            self.Value = self.entry.get()
        try:
            if int(re.search("[0-9]+",self.Value).group())==0 and "." not in self.Value:
                self.entry.delete(len(self.Value)-1)
        except:
            pass
        self.entry.insert(END,"7")
        self.Evaluate()
    def Num8(self,event):
        self.Value = self.entry.get()
        if re.search("[\+\-x÷]$",self.Value) and self.Value.count("(")==self.Value.count(")"):
            self.equa = self.equa + " " + self.Value
            Label(self.frame,text=self.equa,width=27,font=("Calibri", 24),anchor="e",bg="white",fg=self.dgrey).grid(row=0,columnspan=4)
            self.equation = self.equation + self.Value
            self.entry.delete(0,END)
            self.Value = self.entry.get()
        try:
            if int(re.search("[0-9]+",self.Value).group())==0 and "." not in self.Value:
                self.entry.delete(len(self.Value)-1)
        except:
            pass
        self.entry.insert(END,"8")
        self.Evaluate()
    def Num9(self,event):
        self.Value = self.entry.get()
        if re.search("[\+\-x÷%]$",self.Value):
            self.equa = self.equa + " " + self.Value
            Label(self.frame,text=self.equa,width=27,font=("Calibri", 24),anchor="e",bg="white",fg=self.dgrey).grid(row=0,columnspan=4)
            self.equation = self.equation + self.Value
            self.entry.delete(0,END)
            self.Value = self.entry.get()
        try:
            if int(re.search("[0-9]+",self.Value).group())==0 and "." not in self.Value:
                self.entry.delete(len(self.Value)-1)
        except:
            pass
        self.entry.insert(END,"9")
        self.Evaluate()
    def rot(self,event):
        try:
            self.Value = self.entry.get()
            sq = math.sqrt(float(self.Value))
            self.entry.delete(0,END)
            self.entry.insert(0,sq)
            self.Evaluate()
        except ValueError:
            Label(self.frame,text="Invalid Value!",font=("Calibri", 24),anchor="e",bg="white",fg="red").grid(row=2,columnspan=4)

    def sqr(self,event):
        try:
            self.Value = self.entry.get()
            sq = math.pow(float(self.Value),2)
            self.entry.delete(0,END)
            self.entry.insert(0,sq)
            self.Evaluate()
        except ValueError:
            Label(self.frame,text="Invalid Value!",width=27,font=("Calibri", 24),anchor="e",bg="white",fg="red").grid(row=2,columnspan=4)
    def brac1(self,event):
        self.Value = self.entry.get()
        if re.search("[\+\-x÷]$",self.Value) and self.Value.count("(")==self.Value.count(")"):
            self.equa = self.equa + " " + self.Value
            Label(self.frame,text=self.equa,width=27,font=("Calibri", 24),anchor="e",bg="white",fg=self.dgrey).grid(row=0,columnspan=4)
            self.equation = self.equation + self.Value
            self.entry.delete(0,END)
            self.entry.insert(0,"(")
            return
        try:
            if int(re.search("[0-9]+",self.Value).group())==0:
                self.entry.delete(0, END)
                self.entry.insert(0,"(")
                return
        except:
            pass
        if not re.search("[0123456789]$",self.Value):
            self.entry.insert(END,"(")
    def brac2(self,event):
        self.Value = self.entry.get()
        if not re.search("\($",self.Value) and self.Value.count("(") > self.Value.count(")"):
            self.entry.insert(END,")")
            self.Evaluate()

    def validate(self, action, value_if_allowed):
        if action != '1':
           return True
        try:
            for v in value_if_allowed:
                if v not in "0123456789.+-√x÷²() ":
                    return False
            else:
                return True
        except ValueError:
           return False

            
root = Tk()
root.title("Calculator")
root.resizable(0,0)
a = Main(root)
root.mainloop()
