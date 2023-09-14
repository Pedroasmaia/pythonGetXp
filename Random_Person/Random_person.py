import requests as r
from tkinter import messagebox, Tk, Label, Entry, Button, font
from PIL import Image, ImageTk
import logging
import wget
import os


def person():
    person = r.get("https://randomuser.me/api/")
    person = person.json()
    person = person["results"]
    person = person[0]
    persona = person["name"]
    name = f'{persona["first"]} {persona["last"]}'
    gender = f'{person["gender"]}'
    country = f'{person["location"]["country"]}'
    picture_person = person["picture"]["large"]
    username = person["login"]["username"]
    password = person["login"]["password"]
    try:
        os.remove("./picture_person.jpeg")
    except FileNotFoundError:
        logging.exception("Como esperado,arquivo não existe")
    wget.download(picture_person, "./picture_person.jpeg")
    return (name, gender, country, "./picture_person.jpeg",username,password)


def show_image(picture):
    image = Image.open(picture)
    photo = ImageTk.PhotoImage(image)
    image_label = Label(image=photo)
    image_label.image = photo
    image_label.grid(column=1, row=2)
def show_info(name, gender, country,username,password):
    person_name = Label(text=f"Name: {name.title()}", font=montserrat, justify='left')
    person_gender = Label(text=f"Gender: {gender.title()}", font=helvetica, justify='left')
    person_country = Label(text=f"Country: {country.title()}", font=helvetica, justify='left')
    person_username = Label(text=f"Username: {username.title()}", font=helvetica, justify='left')
    person_password = Label(text=f"Password: {password.title()}", font=helvetica, justify='left')
    title.grid(column=1, row=0)
    person_name.grid(column=1, row=3)
    person_gender.grid(column=1, row=4)
    person_country.grid(column=1, row=5)
    person_username.grid(column=1, row=6)
    person_password.grid(column=1, row=7)
if __name__ == "__main__":
    name, gender, country, picture,username,password= person()
    window = Tk()
    window.title("Gerando personagem")
    helvetica = font.Font(family="Helvetica", size=16)
    montserrat = font.Font(family="Montserrat", size=16)
    title = Label(text="Gerador de Pessoas Fictícias", font=montserrat, justify='left')
    show_image(picture)
    show_info(name, gender, country,username,password)
    window.mainloop()
