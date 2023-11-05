import tkinter as tk
from tkinter.filedialog import asksaveasfilename, askopenfilename
from tkinter import messagebox
from tkinter import filedialog

class TextEditor:
    def __init__(self, master):
        self.master = master
        master.title("Bloc-notes")

        self.textarea = tk.Text(master, font=("Helvetica", 12))
        self.textarea.pack(fill="both", expand=True)

        menubar = tk.Menu(master)
        filemenu = tk.Menu(menubar, tearoff=0)
        filemenu.add_command(label="Nouveau", command=self.new_file)
        filemenu.add_command(label="Ouvrir", command=self.open_file)
        filemenu.add_command(label="Enregistrer", command=self.save_file)
        filemenu.add_command(label="Enregistrer sous", command=self.save_file_as)
        filemenu.add_separator()
        filemenu.add_command(label="Mise en page", command=self.page_setup)
        filemenu.add_command(label="Imprimer", command=self.print_file)
        filemenu.add_separator()
        filemenu.add_command(label="Quitter", command=self.quit_app)
        menubar.add_cascade(label="Fichier", menu=filemenu)

        master.config(menu=menubar)

        self.current_file = None

    def new_file(self):
        self.textarea.delete(1.0, tk.END)
        self.current_file = None

    def open_file(self):
        file_path = askopenfilename(filetypes=[("Fichier texte", "*.txt"), ("Tous les fichiers", "*.*")])
        if not file_path:
            return
        self.textarea.delete(1.0, tk.END)
        with open(file_path, "r") as input_file:
            text = input_file.read()
            self.textarea.insert(tk.END, text)
        self.current_file = file_path

    def save_file(self):
        if self.current_file:
            text = self.textarea.get(1.0, tk.END)
            with open(self.current_file, "w") as output_file:
                output_file.write(text)
        else:
            self.save_file_as()

    def save_file_as(self):
        file_path = asksaveasfilename(defaultextension=".txt", filetypes=[("Fichier texte", "*.txt"), ("Tous les fichiers", "*.*")])
        if not file_path:
            return
        with open(file_path, "w") as output_file:
            text = self.textarea.get(1.0, tk.END)
            output_file.write(text)
        self.current_file = file_path

    def page_setup(self):
        self.master.update()
        self.master.page_setup()

    def print_file(self):
        self.master.update()
        self.master.printout()

    def quit_app(self):
        if messagebox.askyesno("Quitter", "Voulez-vous vraiment quitter ?"):
            self.master.destroy()

root = tk.Tk()
app = TextEditor(root)
root.mainloop()
