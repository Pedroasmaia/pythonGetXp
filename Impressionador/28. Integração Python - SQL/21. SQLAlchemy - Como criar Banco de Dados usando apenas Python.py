from sqlalchemy import create_engine, Column, String, Integer, Boolean,ForeignKey
from sqlalchemy.orm import sessionmaker, declarative_base

#Criando banco ou conexão
db = create_engine("sqlite:///meubanco.db")

#Objeto da seção
Session = sessionmaker(bind=db)
#Inicializar a seção
session = Session()

Base = declarative_base()

#Tabelas
class Usuario(Base):
    __tablename__ = "usuarios" #Define o nome da tabela no banco de dados para ref na Coluna FK
    id = Column('id',
                Integer,
                primary_key=True, #Cada tabela tem que ter uma PK, que é o valor unico que identifica aquela linha
                autoincrement=True) # Sempre fazer um +1 quando uma linha nova for criada
    name = Column('name',String)
    email = Column('email',String)
    password = Column('password',String)
    active = Column('active',Boolean)
    #Toda Classe precisa de uma função __init__
    
    def __init__(self,name,email,password,active=True):
        self.name = name
        self.email = email
        self.password = password
        self.active = active

class Livro(Base):
    __tablename__ = "livros"
    
    id = Column('id',
                Integer,
                primary_key=True, #Cada tabela tem que ter uma PK, que é o valor unico que identifica aquela linha
                autoincrement=True) # Sempre fazer um +1 quando uma linha nova for criada
    title = Column('Title',String)
    pages = Column('pages',Integer)
    owner = Column('owner',ForeignKey("usuarios.id"))

    def __init__(self,title,pages,owner):
        self.title = title
        self.pages = pages
        self.owner = owner

Base.metadata.create_all(bind=db)

# Create - Crud
user = Usuario("Pedro","qualquercoisa@email.com","senhafalsa123")
session.add(user)
session.commit()

# Read - cRud
list_users = session.query(Usuario).filter_by(email="qualquercoisa@email.com").first()
print(list_users.email)

book = Livro("Nome do Vento",1000,owner=list_users.email)
session.add(book)
session.commit()

#Update - crud
list_users.name = "Maia"
session.add(list_users)
session.commit()


#delete
session.delete(list_users)
session.commit()