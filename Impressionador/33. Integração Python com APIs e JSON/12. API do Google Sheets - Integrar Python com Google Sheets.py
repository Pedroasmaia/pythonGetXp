import os.path
from dotenv import load_dotenv
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from statistics import median

load_dotenv()
api_credentials = os.getenv('secret_key')
# Nivel de acesso que o código tem:
SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]

# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = os.getenv('planilha_id')
SAMPLE_RANGE_NAME = "Página1!A1:C12"

with open('a.json','w') as outfile:
  outfile.write(api_credentials)

def main():
  creds = None
  if os.path.exists("token.json"):
    creds = Credentials.from_authorized_user_file("token.json", SCOPES)
  if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
      creds.refresh(Request())
    else:
      flow = InstalledAppFlow.from_client_secrets_file(
          'a.json', SCOPES
      )
      creds = flow.run_local_server(port=0)
    with open("token.json", "w") as token:
      token.write(creds.to_json())

  try:
    #Cria o serviço
    service = build("sheets", "v4", credentials=creds)
    sheet = service.spreadsheets()

    taxValues = [["Imposto"]]
    #Requisição de pegar informações
    result = (
        sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID, range=SAMPLE_RANGE_NAME)
        .execute()
    )
    for i,linha in enumerate(result['values']):
      if i > 0:
        faturamento = float(linha[1].replace("R$","").replace(".","").replace(",","."))
        tax = faturamento * 0.1
        taxValues.append([tax])
    writing = [["Dezembro"]]
    # Adicionar informação
    adicionar = (
        sheet.values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID, range='Página1!A13', valueInputOption="USER_ENTERED",body={'values':writing})
        .execute()
    )
    # Criando nova coluna
    adicionar = (
        sheet.values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID, range='Página1!C1', valueInputOption="USER_ENTERED",body={'values':taxValues})
        .execute()
    )
  except HttpError as err:
    print(err)

if __name__ == "__main__":
  main()
  os.remove("a.json")