from tkinter import *
import tkinter.ttk as ttk

def currency_converter():
    #creating instance of tkinter
    currency_converter = Tk()  
    #Set title of our window form  
    currency_converter.title("Menjacnica")
    #Set dimension of form 
    currency_converter.geometry("800x600")
    #Centers the Window
    currency_converter.update_idletasks()
    w = currency_converter.winfo_screenwidth()
    h = currency_converter.winfo_screenheight()
    size = tuple(int(_) for _ in currency_converter.geometry().split('+')[0].split('x'))
    x = w/2 - size[0]/2
    y = h/2 - size[1]/2
    currency_converter.geometry("%dx%d+%d+%d" % (size + (x, y))) 

    currency_converter.rowconfigure(5, weight=1)

    currency_converter.lift()

#    currency_converter.overrideredirect(1) #Remove border
    currency_converter.configure(background='#007789')

    def enter():
        
        UserInput = float(Currency_Input.get().replace(',', '.'))
        Currency_Output.delete(0,END)
        
        if box.get() == "EUR":            
            Currency_Output_Label.config(text="RSD")
            Currency_Output.insert(0,round(UserInput*120,0))
           
        elif box.get() == "RSD":
            Currency_Output_Label.config(text="EUR")
            Currency_Output.insert(0,round(UserInput*0.0084))
           

    def close_currency_converter():
        currency_converter.destroy()

    Headline_Label = Label(currency_converter, text='Menjacnica', bg='#007780', fg='white',font=("Century Gothic",16))
    Headline_Label.grid(row=0,column=0, columnspan=2, padx=3, pady=3, sticky=W)

    Box_Headline_Label = Label(currency_converter, text='Valuta?', bg='#007780', fg='white',font=("Century Gothic",11))
    Box_Headline_Label.grid(row=1,column=0, columnspan=1, padx=5, pady=5, sticky=W)

    box_value = StringVar() 
    box = ttk.Combobox(currency_converter, textvariable=box_value, width=10)
    box['values'] = ('EUR', 'RSD', )
    box.current(0)
    box.grid(row=1,column=1, pady=5, sticky=E)

    Currency_Input = Entry(currency_converter)
    Currency_Input.grid(row=1,column=2, padx=10, pady=5, sticky=W)

    Currency_Input.bind('<Return>',enter)

    Currency_Output_Label = Label(currency_converter, text='', bg='#007780', fg='white',font=("Century Gothic",11))
    Currency_Output_Label.grid(row=2,column=1, padx=5, pady=5, sticky=W)

   

    Currency_Output = Entry(currency_converter)
    Currency_Output.grid(row=2,column=2, padx=10, pady=5, sticky=W)

    

    
    Button(currency_converter,text="Ugasi",command=close_currency_converter).grid(row=6,column=0, sticky=E+S+W, pady=5, padx=5)
    Button(currency_converter,text="Promeni",command=enter).grid(row=6,column=5, sticky=E+S+W, pady=5, padx=5)
    currency_converter.mainloop()

currency_converter()