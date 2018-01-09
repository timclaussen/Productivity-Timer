#Timer GUI

import time
from tkinter import *

class Application(Frame):
    """GUI application with 3 seperate timer buttons"""
    def __init__(self, master):
        """Initialize the frame"""
        super(Application, self).__init__(master)
        self.grid()
#        self.columnconfigure()
        self.bttn1_time = 0
        self.bttn2_time = 0
        self.bttn3_time = 0
        self.total_1 = 0
        self.total_2 = 0
        self.total_3 = 0
        self.yt = StringVar() #tkinter variables for the time labels
        self.vg = StringVar()
        self.pd = StringVar()
        self.create_widgets()
    def create_widgets(self):
        """Create 3 buttons and labels"""
        self.lbl = Label(self, text = "Time (minutes) Spent on Computer")
        self.lbl.grid()
        self.lbl_1 = self.labeler(1, 1, "YouTube Time") #self is implicit first arg
        self.lbl_2 = self.labeler(1, 4, "Video Game Time") 
        self.lbl_3 = self.labeler(1, 7, "Productive") 
        self.lbl_4 = self.var_labeler(3, 1, ("YT: " + str(self.total_1)), self.yt) #col 0 for clear button
        self.lbl_5 = self.var_labeler(3, 4, ("VG: " + str(self.total_2)), self.vg) 
        self.lbl_6 = self.var_labeler(3, 7, ("PD: " + str(self.total_3)), self.pd)
        #self.last_lbl = self.labeler(4, 1, "last label")
        # make buttons, update count command, and put in grid
        # make buttons under the labels
        self.bttn1 =  Button(self, text = "YT start", \
                             command=lambda: self.update_bttn(1, self.lbl_4))
        #need lambda to not call function, but establish relation
        self.bttn1.grid(row = 2, column = 1, sticky = W) 
        self.bttn2 =  Button(self, text = "VG start", \
                             command=lambda: self.update_bttn(2, self.lbl_5))
        self.bttn2.grid(row = 2, column = 4, sticky = W)
        self.bttn3 =  Button(self, text = "PD start", \
                             command=lambda: self.update_bttn(3, self.lbl_6))
        self.bttn3.grid(row = 2, column = 7, sticky = W)
        self.bttn_clear =  Button(self, text = "Clear Times Not Working Yet") # button to clear times
        #command = self.update_bttn_clear
        self.bttn_clear.grid(row = 3, column = 0, sticky = W)
    def labeler(self, row_num, col_num, in_text):
        """refactored from create widgets to reduce lines creating labels"""
        self.lbl = Label(self, text = in_text)
        self.lbl.grid(row = row_num, column = col_num, columnspan=3, sticky = W)
        # sticky W means west (left justified)
        return self.lbl
    def var_labeler(self, row_num, col_num, in_text, text_var):
        """refactored from create widgets to reduce lines creating labels that can change"""
        text_var.set(in_text)
        self.lbl = Label(self, textvariable = text_var)
        self.lbl.grid(row = row_num, column = col_num, columnspan=3, sticky = W)
        # sticky W means west (left justified)
        return self.lbl
    def update_bttn(self, bttn_num, lbl):
        """Button event handler"""      
        if(bttn_num == 1): #button 1 update
            if(self.bttn1_time == 0): #start timer
                self.bttn1_time = int(time.time())
                self.bttn1["text"] = "YT stop"
            else: #stop timer and add to total
                self.total_1 =+ (int(time.time()) - self.bttn1_time)/60
                self.bttn1_time = 0 #reinitialize start timer
                self.bttn1["text"] = "YT start" #reset button text
                self.yt.set("YT: " + str(self.total_1)) #show total on respective label 
              # raise RuntimeError('Button press recognized as yt stop')
              
        elif(bttn_num == 2): #button 2 update
            if(self.bttn2_time == 0): #start timer
                self.bttn2_time = int(time.time())
                self.bttn2["text"] = "VG stop"
            else: #stop timer and add to total
                self.total_2 =+ (int(time.time()) - self.bttn2_time)/60
                self.bttn2_time = 0 #reinitialize start timer
                self.bttn2["text"] = "VG start"
                self.vg.set("VG: " + str(self.total_2)) 
                #raise RuntimeError('Button press recognized as VG stop')
                
        elif(bttn_num == 3): #button 3 update
            if(self.bttn3_time == 0): #start timer
                self.bttn3_time = int(time.time())
                self.bttn3["text"] = "PD stop"
            else: #stop timer and add to total
                self.total_3 =+ (int(time.time()) - self.bttn3_time)/60
                self.bttn3_time = 0 #reinitialize start timer
                self.bttn3["text"] = "PD start"
                self.pd.set("PD: " + str(self.total_3)) 
                #raise RuntimeError('Button press recognized as PD stop')
        else:
            raise RuntimeError('Button press not recognized')
        #if() to check if bttn time != 0 so last time not overwritten
            #start timer (according to bttn number)
            #update button txt to "stop"
        #else total (lbl 4-6) = bttn_time - time.time()
            #update button to start
            #update label on total



#create a root window
root = Tk()
root.title("Computer Timer")
root.geometry("700x600")

#create a frame in the window to hold other widgets
app = Application(root)

#enter root event loop
root.mainloop()

