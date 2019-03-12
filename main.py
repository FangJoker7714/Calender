import tkinter as tk

class mycalendar(tk.Frame):
    def __init__(self,master=None,cnf={},**kw):
        import datetime
        tk.Frame.__init__(self,master,cnf,**kw)
        now = datetime.datetime.now()
        self.year = now.year
        self.month = now.month

        frame_top = tk.Frame(self)
        frame_top.pack(pady=5)

        self.previous_month = tk.Label(frame_top, text = "<", font = ("",18))
        self.previous_month.pack(side = "left", padx = 10)
        self.previous_month.bind("<1>", self.change_month)
        self.current_year = tk.Label(frame_top, text = self.year , font = ("",18))
        self.current_year.pack(side = "left")
        self.current_month = tk.Label(frame_top, text = self.month, font = ("",18))
        self.current_month.pack(side = "left")
        self.next_month = tk.Label(frame_top, text = ">", font = ("",22))
        self.next_month.pack(side = "left", padx = 10)
        self.next_month.bind("<1>", self.change_month)

        frame_week = tk.Frame(self)
        frame_week.pack()
        label_san = d_label(frame_week, text = "Sun", fg = "red")
        label_san.grid(column=0, row=0)
        label_mon = d_label(frame_week, text = "Mon")
        label_mon.grid(column=1, row=0)
        label_tue = d_label(frame_week, text = "Tue")
        label_tue.grid(column=2, row=0)
        label_wed = d_label(frame_week, text = "Wed")
        label_wed.grid(column=3, row=0)
        label_thu = d_label(frame_week, text = "Thu")
        label_thu.grid(column=4, row=0)
        label_fri = d_label(frame_week, text = "Fri", fg = "gold")
        label_fri.grid(column=5, row=0)
        label_sat = d_label(frame_week, text = "Sat", fg = "blue")
        label_sat.grid(column=6, row=0)

        self.frame_calendar = tk.Frame(self)
        self.frame_calendar.pack()
        self.create_calendar(self.year,self.month)

    def create_calendar(self,year,month):
        try:
            for key,item in self.day.items():
                item.destroy()
        except:
            pass
        import calendar
        cal = calendar.Calendar()
        days = cal.monthdayscalendar(year,month)
        self.day = {}

        for i in range(0,42):
            c = i - (7 * int(i/7))
            r = int(i/7)
            try:
                if days[r][c] != 0:
                    self.day[i] = d_label(self.frame_calendar,text = days[r][c])
                    self.day[i].grid(column=c,row=r)
            except:
                break

    def change_month(self,event):
        if event.widget["text"] == "<":
            self.month -= 1
        else:
            self.month += 1

        if self.month == 0:
            self.year -= 1
            self.month = 12
        elif self.month == 13:
            self.year += 1
            self.month =1

        self.current_year["text"] = self.year
        self.current_month["text"] = self.month
        self.create_calendar(self.year,self.month)

class d_label(tk.Label):
    def __init__(self, master=None, cnf={}, **kw):
        tk.Label.__init__(self,master,cnf,**kw)
        self.configure(font=("",18) ,height=2, width=4)

root = tk.Tk()
root.title("Calemdar App")
mycal = mycalendar(root)
mycal.pack()
root.mainloop()
