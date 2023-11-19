import pyodbc
import os

# Substitua as informações de conexão com as suas configurações
server = 'localhost'
database = 'alexander'
username = os.getenv("Username  ")
password = os.getenv("Password")

connection_str = f'DRIVER={{SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}'

try:
    connection = pyodbc.connect(connection_str)
except Exception as e:
    print(f'Falha ao se conectar no banco: {e}')

def all_books():
    cursor = connection.cursor()
    cursor.execute(f"SELECT * FROM books")
    response = cursor.fetchall()
    print('Livros do Autor')
    print('ID | Nome | Autor')
    print('-----------------------------------')
    for a in response:
        print(f' {a[0]} | {a[1]} | {a[2]} ')

def register_book():
    cursor = connection.cursor()
    while True:
        print('Insira o nome do livro:')
        name = input()
        if len(name) <= 255:
            break
        else:
            print('O nome é muito grande')
    while True:
        print('Insira o nome do autor:')
        author = input()
        if len(author) <= 50:
            break
        else:
            print('O nome é muito grande')
    try:  
        cursor.execute(
        f"INSERT INTO books (name,author) VALUES ('{name.title()}','{author.title()}')")
        connection.commit()
    except Exception as e:
        print(f'Falha eo registrar livro: {e}')
    finally:
        cursor.close()


def search_author(author_name):
    cursor = connection.cursor()
    cursor.execute(f"SELECT * FROM books WHERE author = '{author_name.title()}'")
    response = cursor.fetchall()
    print('Livros do Autor')
    print('ID | Nome')
    print('---------')
    for a in response:
        print(f' {a[0]} | {a[1]} ')
    return a
    

def remove_book():
    author_name = input('Nome do Autor do livro que quer remover: ')
    search_author(author_name)
    cursor = connection.cursor()
    i = int(input('Insira o id do livro que pretende apagar: '))
    cursor.execute(f"DELETE FROM books WHERE book_id = {i};")
    connection.commit()

print('------------------------------\n 1- Registrar Livro \n 2- Pesquisar Por Autor\n 3- Remover Livro\n 4- Sair\n 5- Ver Todos Os Livros\n------------------------------')
choice = int(input('Escolha sua opção: '))
while True:
    if choice == 1:
        register_book()
        break
    elif choice == 2:
        author_name = input('Nome do Autor: ')
        search_author(author_name)
        break
    elif choice == 3:
        remove_book()
        break
    elif choice == 4:
        break
    elif choice == 5:
        all_books()
        break
connection.close()
