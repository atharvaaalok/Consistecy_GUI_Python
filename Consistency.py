import csv
import datetime
import tkinter as tk
from PIL import Image, ImageTk

# activity is a dictionary it will hold the acitvities that i have done either in the past or are ongoing also it will include the starting date 
# the number of days passed since the starting of the activity the number of days I completed the activity which will be entered each day I 
# complete the activity also each entry will contain an element "status" past/present/future every time i complete some activity i will 
# update the status field there will be three dictionaries based on status the activities will place in their respective fields
# the program will each day ask me for entering the details of the present dictionary# also it will ask me if i have completed a task or if 
# i have something new to place in the future dictionary


class Example(tk.Frame):
    def __init__(self, master, **pargs):
        tk.Frame.__init__(self, master, **pargs)



        self.image = Image.open(IMAGE_NAME)
        self.img_copy= self.image.copy()


        self.background_image = ImageTk.PhotoImage(self.image)

        self.background = tk.Label(self, image=self.background_image)
        self.background.pack()                       #fill='both', expand=True
        self.background.bind('<Configure>', self._resize_image)

    def _resize_image(self,event):

        new_width = event.width
        new_height = event.height

        self.image = self.img_copy.resize((new_width, new_height))

        self.background_image = ImageTk.PhotoImage(self.image)
        self.background.configure(image =  self.background_image)

    


# For moving activities from the present dictionary and moving them to the past
def update_past(past, present):
    for widget in canvas.winfo_children():
        widget.destroy()

    
    keyz = present.keys()
    keys = list(keyz)

    label_past_keys = tk.Label(canvas, text = "Select the entries you want to move from past to present", font = ("Comic Sans MS", 15))
    label_past_keys.place(relx = 0.5, rely = 0, relwidth = 0.8, relheight = 0.1, anchor = 'n')
    list_of_checkboxes = []
    var_list = []
    for i in range(len(keys)):
        var = tk.IntVar()
        var_list.append(var)
        c = tk.Checkbutton(canvas, text = keys[i], variable = var_list[i], font = 40)
        list_of_checkboxes.append(c)
        c.place(relx = 0, rely = 0.1 + i * 0.075)

    submit_choices = tk.Button(canvas, text = "Submit", font = ("Comic Sans MS", 12), command = lambda: set_var_list(var_list, keys, "past"))
    submit_choices.place(relx = 0.6, rely = 0.8, relwidth = 0.2, relheight = 0.1)


def add_to_present(activity_name):
    for widget in canvas.winfo_children():
        widget.destroy()

    global present
    startingDate = datetime.datetime.today()     # This is a date object
    activity_startingDate = str(startingDate.day)
    activity_startingDate += ('/' + str(startingDate.month))
    activity_startingDate += ('/' + str(startingDate.year))
    day_count = 1
    consistency = 10
    total_days_done = 1
    present[activity_name] = [activity_startingDate, day_count, total_days_done,consistency]

    label_next = tk.Label(canvas, text = "Press Next to Continue", font = ("Comic Sans MS", 15))
    label_next.place(relx = 0.5, rely = 0, relwidth = 0.8, relheight = 0.1, anchor = 'n')
    next_button = tk.Button(canvas, text = "Next", font = ("Comic Sans MS", 12), command = close_files)
    next_button.place(relx = 0.8, rely = 0.8, relwidth = 0.15, relheight = 0.1)
    

# For entering new activities or updating activities of the present
def update_present(present, mode):
    for widget in canvas.winfo_children():
        widget.destroy()
    
    

    # Entering new activity in the present
    if mode == "ADD":
        label_present_add = tk.Label(canvas, text = "Enter new activity assuming you have already done it today", font = ("Comic Sans MS", 15))
        label_present_add.place(relx = 0.5, rely = 0, relwidth = 0.8, relheight = 0.1, anchor = 'n') 
        new_entry = tk.Entry(canvas, font = ("Comic Sans MS", 12))
        new_entry.place(relx = 0.1, rely = 0.4, relwidth = 0.8, relheight = 0.2)

        new_entry_button = tk.Button(canvas, text = "Submit", command = lambda: add_to_present(new_entry.get()))
        new_entry_button.place(relx = 0.6, rely = 0.8, relwidth = 0.2, relheight = 0.1)


    # Updating the present
    elif mode == "UPDATE":
        keyz = present.keys()
        keys = list(keyz)

        label_past_keys = tk.Label(canvas, text = "Select the activities you did today", font = ("Comic Sans MS", 15))
        label_past_keys.place(relx = 0.5, rely = 0, relwidth = 0.8, relheight = 0.1, anchor = 'n')
        list_of_checkboxes = []
        var_list = []
        for i in range(len(keys)):
            var = tk.IntVar()
            var_list.append(var)
            c = tk.Checkbutton(canvas, text = keys[i], variable = var_list[i], font = 40)
            list_of_checkboxes.append(c)
            c.place(relx = 0, rely = 0.1 + i * 0.075)
        submit_choices = tk.Button(canvas, text = "Submit", font = ("Comic Sans MS", 12), command = lambda: set_var_list(var_list, keys, "present-update"))
        submit_choices.place(relx = 0.6, rely = 0.8, relwidth = 0.2, relheight = 0.1)

    

def add_to_future(activity_name, activity_period):
    global future
    for widget in canvas.winfo_children():
        widget.destroy()

    future[activity_name] = activity_period



    label_next = tk.Label(canvas, text = "Press Next to Continue", font = ("Comic Sans MS", 15))
    label_next.place(relx = 0.5, rely = 0, relwidth = 0.8, relheight = 0.1, anchor = 'n')
    next_button = tk.Button(canvas, text = "Next", font = ("Comic Sans MS", 12), command = close_files)
    next_button.place(relx = 0.8, rely = 0.8, relwidth = 0.15, relheight = 0.1)



def set_var_list(var_list, keys, list_name):
    for widget in canvas.winfo_children():
        widget.destroy()
    global past, future, present
    if list_name == "past":
        for i in range(len(var_list)):
            if var_list[i].get() == 1:
                activity_details = present[keys[i]]
                past[keys[i]] = activity_details
                del present[keys[i]]
        label_next = tk.Label(canvas, text = "Press Next to Continue", font = ("Comic Sans MS", 15))
        label_next.place(relx = 0.5, rely = 0, relwidth = 0.8, relheight = 0.1, anchor = 'n')
        next_button = tk.Button(canvas, text = "Next", font = ("Comic Sans MS", 12), command = close_files)
        next_button.place(relx = 0.8, rely = 0.8, relwidth = 0.15, relheight = 0.1)
    elif list_name == "future":
        for i in range(len(var_list)):
            if var_list[i].get() == 1:
                activity_name = keys[i]
                del future[activity_name]
        label_next = tk.Label(canvas, text = "Press Next to Continue", font = ("Comic Sans MS", 15))
        label_next.place(relx = 0.5, rely = 0, relwidth = 0.8, relheight = 0.1, anchor = 'n')
        next_button = tk.Button(canvas, text = "Next", font = ("Comic Sans MS", 12), command = close_files)
        next_button.place(relx = 0.8, rely = 0.8, relwidth = 0.15, relheight = 0.1)
    elif list_name == "present-update":
        for i in range(len(var_list)):
            total_days_done = int(present[keys[i]][2])
            if var_list[i].get() == 1:
                total_days_done += 1
            

            date_today = datetime.datetime.today()
            startingDate_DateObj = datetime.datetime.strptime(present[keys[i]][0], "%d/%m/%Y") 
            day_count = date_today - startingDate_DateObj
            consistency = (total_days_done / (day_count.days + 1)) * 10
            present[keys[i]] = [present[keys[i]][0], day_count.days, total_days_done, consistency]
        label_next = tk.Label(canvas, text = "Press Next to Continue", font = ("Comic Sans MS", 15))
        label_next.place(relx = 0.5, rely = 0, relwidth = 0.8, relheight = 0.1, anchor = 'n')
        next_button = tk.Button(canvas, text = "Next", font = ("Comic Sans MS", 12), command = close_files)
        next_button.place(relx = 0.8, rely = 0.8, relwidth = 0.15, relheight = 0.1)


def set_future_update(var, keys):
    global future
    for widget in canvas.winfo_children():
        widget.destroy()

    to_update = var.get()

    entry_name = keys[to_update]

    label_present_add = tk.Label(canvas, text = "Enter the period when you want to do the activity", font = ("Comic Sans MS", 15))
    label_present_add.place(relx = 0.5, rely = 0, relwidth = 0.8, relheight = 0.1, anchor = 'n') 
    new_entry_period = tk.Entry(canvas, font = ("Comic Sans MS", 12))
    new_entry_period.place(relx = 0.1, rely = 0.1, relwidth = 0.8, relheight = 0.1)

    new_entry_button = tk.Button(canvas, text = "Submit", command = lambda: add_to_future(entry_name, new_entry_period.get()))
    new_entry_button.place(relx = 0.6, rely = 0.8, relwidth = 0.2, relheight = 0.1)


# dictionary for updating the future activities
def update_future(future, mode):
    for widget in canvas.winfo_children():
        widget.destroy()

    # Adding new entries to the future
    if mode == "ADD":
        label_present_add = tk.Label(canvas, text = "Enter new activity for the Future", font = ("Comic Sans MS", 15))
        label_present_add.place(relx = 0.5, rely = 0, relwidth = 0.8, relheight = 0.1, anchor = 'n') 
        new_entry_name = tk.Entry(canvas, font = ("Comic Sans MS", 12))
        new_entry_name.place(relx = 0.1, rely = 0.1, relwidth = 0.8, relheight = 0.1)

        label_present_add = tk.Label(canvas, text = "Enter the period when you want to do the activity", font = ("Comic Sans MS", 15))
        label_present_add.place(relx = 0.5, rely = 0.5, relwidth = 0.8, relheight = 0.1, anchor = 'n') 
        new_entry_period = tk.Entry(canvas, font = ("Comic Sans MS", 12))
        new_entry_period.place(relx = 0.1, rely = 0.7, relwidth = 0.8, relheight = 0.1)


        new_entry_button = tk.Button(canvas, text = "Submit", command = lambda: add_to_future(new_entry_name.get(), new_entry_period.get()))
        new_entry_button.place(relx = 0.6, rely = 0.8, relwidth = 0.2, relheight = 0.1)


    # Removing entries from the future
    elif mode == "REMOVE":
        keyz = future.keys()
        keys = list(keyz)

        label_past_keys = tk.Label(canvas, text = "Select the entries you want to remove", font = ("Comic Sans MS", 15))
        label_past_keys.place(relx = 0.5, rely = 0, relwidth = 0.8, relheight = 0.1, anchor = 'n')
        list_of_checkboxes = []
        var_list = []
        for i in range(len(keys)):
            var = tk.IntVar()
            var_list.append(var)
            c = tk.Checkbutton(canvas, text = keys[i], variable = var_list[i], font = 40)
            list_of_checkboxes.append(c)
            c.place(relx = 0, rely = 0.1 + i * 0.075)
        submit_choices = tk.Button(canvas, text = "Submit", font = ("Comic Sans MS", 12), command = lambda: set_var_list(var_list, keys, "future"))
        submit_choices.place(relx = 0.6, rely = 0.8, relwidth = 0.2, relheight = 0.1)


    # Changing the entries of the future
    elif mode == "UPDATE":
        keyz = future.keys()
        keys = list(keyz)

        label_past_keys = tk.Label(canvas, text = "Select the entry to update", font = ("Comic Sans MS", 15))
        label_past_keys.place(relx = 0.5, rely = 0, relwidth = 0.8, relheight = 0.1, anchor = 'n')
        list_of_radiobuttons = []
        var = tk.IntVar()
        for i in range(len(keys)):
            c = tk.Radiobutton(canvas, text = keys[i], variable = var, font = 40, value = i)
            list_of_radiobuttons.append(c)
            c.place(relx = 0, rely = 0.1 + i * 0.075)

        

        submit_choice = tk.Button(canvas, text = "Submit", font = ("Comic Sans MS", 12), command = lambda: set_future_update(var, keys))
        submit_choice.place(relx = 0.6, rely = 0.8, relwidth = 0.2, relheight = 0.1)



def main_button():
    button1 = tk.Button(canvas, text = "Print contents", bg = BUTTON_COLOR, command = lambda: print_dictionaries(0))
    button2 = tk.Button(canvas, text = "Modify a dictionary", bg = BUTTON_COLOR, command = modify_dictionaries)
    button1.place(relx = 0.25, rely = 0.8, relwidth = 0.2, relheight = 0.1)
    button2.place(relx = 0.55, rely = 0.8, relwidth = 0.2, relheight = 0.1)


def print_dictionaries(num):
    global past, present, future
    for widget in canvas.winfo_children():
        widget.destroy()
    if num == 0:
        text = tk.Text(canvas, wrap = 'word', bd = 5, height = 700, width = 800, bg = '#D6EAF8', font = ("Comic Sans MS", 12))
        text.place(relx = 0, rely = 0, relwidth = 1, relheight = 1)
        text.insert(tk.END, "PAST :\n" + str(past) + '\n\n\n\n' + "PRESENT :\n" + str(present) + '\n\n\n\n' + "FUTURE :\n" + str(future))
    elif num == 1:
        text = tk.Text(canvas, wrap = 'word', bd = 5, height = 700, width = 800, bg = '#D6EAF8', font = ("Comic Sans MS", 12))
        text.place(relx = 0, rely = 0, relwidth = 1, relheight = 1)
        text.insert(tk.END, "PAST :\n" + str(past))
    elif num == 2:
        text = tk.Text(canvas, wrap = 'word', bd = 5, height = 700, width = 800, bg = '#D6EAF8',font = ("Comic Sans MS", 12))
        text.place(relx = 0, rely = 0, relwidth = 1, relheight = 1)
        text.insert(tk.END, "PRESENT :\n" + str(present))
    elif num == 3:
        text = tk.Text(canvas, wrap = 'word', bd = 5, height = 700, width = 800, bg = '#D6EAF8',font = ("Comic Sans MS", 12))
        text.place(relx = 0, rely = 0, relwidth = 1, relheight = 1)
        text.insert(tk.END, "FUTURE :\n" + str(future))

    next_button = tk.Button(canvas, text = "Next", font = ("Comic Sans MS", 12), command = BOSS)
    next_button.place(relx = 0.8, rely = 0.8, relwidth = 0.15, relheight = 0.1)
    
    
    bool = True


def modify_dictionaries():
    global past, present, future
    for widget in canvas.winfo_children():
        widget.destroy()

    e = Example(canvas)
    e.pack()

    # DISPLAY DIFFERENT IMAGE HERE IN THE BACKGROUND
    button_past = tk.Button(canvas, text = 'Past', bg = BUTTON_COLOR, command = modify_past)
    button_present = tk.Button(canvas, text = 'Present', bg = BUTTON_COLOR, command = modify_present)
    button_future = tk.Button(canvas, text = 'Future', bg = BUTTON_COLOR, command = modify_future)
    label_choose_dict = tk.Label(canvas, text = "Enter the dictionary you want to modify :", justify = 'left', font = ("Comic Sans MS", 15), bg = '#27AE60')
    label_choose_dict.place(relx = 0.5, rely = 0.1, relwidth = 0.5, relheight = 0.12, anchor = 'n')
    button_past.place(relx = 0.1, rely = 0.8, relwidth = 0.2, relheight = 0.1)
    button_present.place(relx = 0.4, rely = 0.8, relwidth = 0.2, relheight = 0.1)
    button_future.place(relx = 0.7, rely = 0.8, relwidth = 0.2, relheight = 0.1)


def modify_past():
    for widget in canvas.winfo_children():
        widget.destroy()

    e = Example(canvas)
    e.pack()
    

    button_past_1 = tk.Button(canvas, text = "Print contents of PAST", bg = BUTTON_COLOR, command = lambda: print_dictionaries(1))
    button_past_2 = tk.Button(canvas, text = "Move entry from PAST to PRESENT", bg = BUTTON_COLOR, command = lambda: update_past(past, present))
    button_past_1.place(relx = 0.25, rely = 0.8, relwidth = 0.2, relheight = 0.1)
    button_past_2.place(relx = 0.55, rely = 0.8, relwidth = 0.2, relheight = 0.1)


def modify_present():
    for widget in canvas.winfo_children():
        widget.destroy()

    e = Example(canvas)
    e.pack()
    

    button_present_1 = tk.Button(canvas, text = "Print PRESENT", bg = BUTTON_COLOR, command = lambda: print_dictionaries(2))
    button_present_2 = tk.Button(canvas, text = "Add to PRESENT", bg = BUTTON_COLOR, command = lambda: update_present(present, "ADD"))
    button_present_3 = tk.Button(canvas, text = "Update PRESENT", bg = BUTTON_COLOR, command = lambda: update_present(present, "UPDATE"))
    button_present_4 = tk.Button(canvas, text = "Move entry from PAST to PRESENT", bg = BUTTON_COLOR, command = lambda: update_past(past, present))

    button_present_1.place(relx = 0.12, rely = 0.8, relwidth = 0.15, relheight = 0.1)
    button_present_2.place(relx = 0.32, rely = 0.8, relwidth = 0.15, relheight = 0.1)
    button_present_3.place(relx = 0.52, rely = 0.8, relwidth = 0.15, relheight = 0.1)
    button_present_4.place(relx = 0.72, rely = 0.8, relwidth = 0.15, relheight = 0.1)



def modify_future():
    for widget in canvas.winfo_children():
        widget.destroy()

    e = Example(canvas)
    e.pack()

    button_future_1 = tk.Button(canvas, text = "Print FUTURE", bg = BUTTON_COLOR, command = lambda: print_dictionaries(3))
    button_future_2 = tk.Button(canvas, text = "Add to FUTURE", bg = BUTTON_COLOR, command = lambda: update_future(future, "ADD"))
    button_future_3 = tk.Button(canvas, text = "Update FUTURE", bg = BUTTON_COLOR, command = lambda: update_future(future, "UPDATE"))
    button_future_4 = tk.Button(canvas, text = "Remove activities", bg = BUTTON_COLOR, command = lambda: update_future(future, "REMOVE"))

    button_future_1.place(relx = 0.12, rely = 0.8, relwidth = 0.15, relheight = 0.1)
    button_future_2.place(relx = 0.32, rely = 0.8, relwidth = 0.15, relheight = 0.1)
    button_future_3.place(relx = 0.52, rely = 0.8, relwidth = 0.15, relheight = 0.1)
    button_future_4.place(relx = 0.72, rely = 0.8, relwidth = 0.15, relheight = 0.1)

    
    

# Prompt
def prompt(past, present, future):

    e = Example(canvas)
    e.pack()
    main_button()
 

def close_files():
    for widget in canvas.winfo_children():
        widget.destroy()

    # store the dictionaries in a file

    path_past = "past.csv"
    path_present = "present.csv"
    path_future = "future.csv"


    file_past = open(path_past, 'w', newline = '')
    file_present = open(path_present, 'w', newline = '')
    file_future = open(path_future, 'w', newline = '')


    writer_past = csv.writer(file_past)
    writer_present = csv.writer(file_present)
    writer_future = csv.writer(file_future)


    writer_past.writerow(['Activity', 'StartingDate', 'DayCount', 'TotalDaysDone', 'Consistency'])
    for key, value in past.items():
        writer_past.writerow([key, value[0], value[1], value[2], value[3]])           # how to convert time to string


    writer_present.writerow(['Activity', 'StartingDate', 'DayCount', 'TotalDaysDone', 'Consistency'])
    for key, value in present.items():
        writer_present.writerow([key, value[0], value[1], value[2], value[3]]) 

    writer_future.writerow(['Activity', 'PeriodOfWork'])
    for key, value in future.items():
        writer_future.writerow([key, value])

    file_past.close()
    file_present.close()
    file_future.close()

    BOSS()


def main():
    global past, present, future
    path_past = "past.csv"
    path_present = "present.csv"
    path_future = "future.csv"


    file_past = open(path_past, newline = '')
    file_present = open(path_present, newline = '')
    file_future = open(path_future, newline = '')


    reader_past = csv.reader(file_past)
    header = next(reader_past)
    for row in reader_past:
        activity_name = row[0]
        startingDate = row[1]#datetime.datetime.strptime(row[1], "%d/%m/%Y")
        dayCount = int(row[2])
        totalDaysDone = int(row[3])
        consistency = float(row[4])
        past[activity_name] = [startingDate, dayCount, totalDaysDone, consistency]
    file_past.close()


    reader_present = csv.reader(file_present)
    header = next(reader_present)
    data = []
    for row in reader_present:
        activity_name = row[0]
        startingDate = row[1]#datetime.datetime.strptime(row[1], "%d/%m/%Y")
        dayCount = int(row[2])
        totalDaysDone = int(row[3])
        consistency = float(row[4])
        present[activity_name] = [startingDate, dayCount, totalDaysDone, consistency]
    file_present.close()


    reader_future = csv.reader(file_future)
    header = next(reader_future)
    data = []
    for row in reader_future:
        activity_name = row[0]
        periodOfWork = row[1]
        future[activity_name] = periodOfWork
    file_future.close()




    prompt(past, present, future)






IMAGE_NAME = 'dna-woods.png'
HEIGHT = 700
WIDTH = 800
SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080
posX = int((SCREEN_WIDTH / 2) - (WIDTH / 2))
posY = int((SCREEN_HEIGHT / 2) - (HEIGHT / 2)) - 80

root = tk.Tk()
geometry_string = f'{WIDTH}x{HEIGHT}+{posX}+{posY}'
root.geometry(geometry_string)

canvas = tk.Canvas(root)              #  height = HEIGHT, width = WIDTH
canvas.pack()




bool = False
BUTTON_COLOR = '#27AE60'



past = {}
present = {}
future = {}


def BOSS():
    for widget in canvas.winfo_children():
        widget.destroy()
    #close_files()
    main()
    root.mainloop()
    for widget in canvas.winfo_children():
        widget.destroy()
    label_again = tk.Label(canvas, text = "Do you want to make any other entries ?", font = ("Comic Sans MS", 12))
    button_again_Yes = tk.Button(canvas, text = "YES", command = BOSS)
    #button_again_No = tk.Button(canvas, text = "NO, EXIT", command = )




if __name__ == '__main__':
    BOSS()