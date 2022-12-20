from pprint import pprint

import httplib2
import apiclient.discovery
from oauth2client.service_account import ServiceAccountCredentials

# Файл с токеном google-sheets
CREDENTIALS_FILE = "creds.json"

# ID Google Sheets документа
sheet_id = "1S3PmZ6MaZV2Hv190VecpFzeNn8Jp4VY85b9G9GSPK-4"


# Авторизуемся и получаем service — экземпляр доступа к API
def get_service():
    scopes = ["https://www.googleapis.com/auth/spreadsheets"]
    creds_service = ServiceAccountCredentials.from_json_keyfile_name(CREDENTIALS_FILE, scopes).authorize(
        httplib2.Http())
    return apiclient.discovery.build("sheets", "v4", http=creds_service)


# Пример чтения файла
resp = get_service().spreadsheets().values().batchGet(
    spreadsheetId=sheet_id,
    ranges=["Лист1"],
    majorDimension="ROWS"
).execute()
pprint(resp)

# Пример записи в файл
# values = service.spreadsheets().values().batchUpdate(
#     spreadsheetId=spreadsheet_id,
#     body={
#         "valueInputOption": "USER_ENTERED",
#         "data": [
#             {"range": "B3:C4",
#              "majorDimension": "ROWS",
#              "values": [["This is B3", "This is C3"], ["This is B4", "This is C4"]]},
#             {"range": "D5:E6",
#              "majorDimension": "COLUMNS",
#              "values": [["This is D5", "This is D6"], ["This is E5", "=5+5"]]}
#         ]
#     }
# ).execute()
