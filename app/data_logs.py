from pprint import pprint
import httplib2
import apiclient.discovery
from oauth2client.service_account import ServiceAccountCredentials

# Файл с токеном conf
CREDENTIALS_FILE = "static/creds.json"

# ID Google Sheets документа
sheet_id = "1S3PmZ6MaZV2Hv190VecpFzeNn8Jp4VY85b9G9GSPK-4"


# Авторизуемся и получаем service — экземпляр доступа к API
def get_service():
    scopes = ["https://www.googleapis.com/auth/spreadsheets"]
    creds_service = ServiceAccountCredentials.from_json_keyfile_name(CREDENTIALS_FILE, scopes).authorize(
        httplib2.Http())
    return apiclient.discovery.build("sheets", "v4", http=creds_service)


def reading_logs():
    """Функция возвращает все записи, исходя из указанного диапазона в ranges"""
    resp = get_service().spreadsheets().values().batchGet(
        spreadsheetId=sheet_id,
        ranges=["Лист1"],
        majorDimension="ROWS"
    ).execute()
    pprint(resp)


def creating_logs():
    """Функция для записи логов в динамические ячейки"""
    values = get_service().spreadsheets().values().batchUpdate(
        spreadsheetId=sheet_id,
        body={
            "valueInputOption": "USER_ENTERED",
            "data": [
                {"range": "A1:A1",
                 "majorDimension": "ROWS",
                 "values": [["Test logs"]]}
            ]
        }
    )
    return values.execute()
