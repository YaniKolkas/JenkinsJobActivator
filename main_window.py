import Tkinter as Tk

index_insert =Tk.INSERT
index_end = Tk.END

def create_gui(def_job_url, def_token):
    master = Tk.Tk()

    master.title('Remote Job activator')
    Tk.Label(master, text="Job URL:").grid(row=0, sticky=Tk.W)
    Tk.Label(master, text="Activation Token:").grid(row=1, sticky=Tk.W)
    Tk.Label(master, text="PARAM:").grid(row=2, sticky=Tk.W )

    entry_url = Tk.Entry(master)
    token = Tk.Entry(master)
    job_param = Tk.Entry(master)
    text_output = Tk.Text(master)
    button = Tk.Button(master, text='CreateBranches!')

    entry_url.grid(row=0, column=1, sticky=Tk.W)
    token.grid(row=1, column=1, sticky=Tk.W)
    job_param.grid(row=2, column=1, sticky=Tk.W)
    text_output.grid(row=3, column=0, columnspan=3)
    button.grid(row=0, column=2, rowspan=3)

    entry_url.insert(0, def_job_url)
    token.insert(0, def_token)

    return entry_url, token, job_param,  text_output, button


def star_gui():
    Tk.mainloop( )