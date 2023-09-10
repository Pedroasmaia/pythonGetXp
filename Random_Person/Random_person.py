import requests as r
from tkinter import messagebox, Tk, Label, Entry, Button
import logging
import wget


def new_person():
    person = r.get("https://randomuser.me/api/")
    person = person.json()
    person = person["results"]
    person = person[0]
    picture_person = person["picture"]["medium"]
    persona = (person["name"])
    print(f"{person['name']}")
    wget.download(picture_person, "./picture_person.jpeg")
    return persona

def apply_person():
    name = new_person()
    title_person_name = Label(text=f"Nome: {name}")
    title_person_name.grid(column=2, row=0)

if __name__ == "__main__":
    windows = Tk()
    logging.info("Iniciando Aplicação")
    windows.title("Novo personagem")
    title_person_name = Label(text="Gere um Novo Personagem")
    title_person_name.grid(column=2, row=0)
    new_person_button = Button(
        text="Criar novo personagem", width=36, command=apply_person
    )

    new_person_button.grid(row=1, column=2,)
windows.mainloop()
